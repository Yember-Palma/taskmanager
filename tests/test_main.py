import builtins
from unittest.mock import MagicMock
import main
from main import main as run_main
import pytest


def _set_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(it))


def test_add_task_calls_add_task_and_exit(monkeypatch):
    tm_instance = MagicMock()
    TaskManagerMock = MagicMock(return_value=tm_instance)
    monkeypatch.setattr(main, "TaskManager", TaskManagerMock)

    _set_inputs(monkeypatch, ["1", "Tarea de prueba", "6"])

    run_main()

    TaskManagerMock.assert_called_once()
    tm_instance.add_task.assert_called_once_with("Tarea de prueba")


def test_add_complex_tasks_success(monkeypatch):
    tm_instance = MagicMock()
    monkeypatch.setattr(main, "TaskManager", MagicMock(return_value=tm_instance))
    monkeypatch.setattr(main, "create_simple_tasks", lambda desc: ["sub1", "sub2"])

    _set_inputs(monkeypatch, ["2", "Tarea compleja", "6"])

    run_main()

    assert tm_instance.add_task.call_count == 2
    tm_instance.add_task.assert_any_call("sub1")
    tm_instance.add_task.assert_any_call("sub2")


def test_add_complex_tasks_error(monkeypatch, capsys):
    tm_instance = MagicMock()
    monkeypatch.setattr(main, "TaskManager", MagicMock(return_value=tm_instance))
    monkeypatch.setattr(main, "create_simple_tasks", lambda desc: ["Error: fallo al generar subtareas"])

    _set_inputs(monkeypatch, ["2", "Tarea compleja con error", "6"])

    run_main()
    captured = capsys.readouterr()

    tm_instance.add_task.assert_not_called()
    assert "Error: fallo al generar subtareas" in captured.out


def test_complete_and_delete_calls_methods(monkeypatch):
    tm_instance = MagicMock()
    monkeypatch.setattr(main, "TaskManager", MagicMock(return_value=tm_instance))

    _set_inputs(monkeypatch, ["4", "10", "5", "20", "6"])

    run_main()

    tm_instance.complete_task.assert_called_once_with(10)
    tm_instance.delete_task.assert_called_once_with(20)


def test_invalid_inputs_print_message(monkeypatch, capsys):
    tm_instance = MagicMock()
    monkeypatch.setattr(main, "TaskManager", MagicMock(return_value=tm_instance))

    _set_inputs(monkeypatch, ["x", "999", "6"])

    run_main()
    captured = capsys.readouterr()

    assert captured.out.count("Opcion no valida. Selecciona otra.") >= 2
