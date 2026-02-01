import os
from dotenv import load_dotenv
from google import genai # Importación de la nueva librería google-genai

load_dotenv()

# iniciamos nuestra variable con gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_simple_tasks(description):
    try:
        # medelo de gemini
        model_id = "gemini-2.5-flash" 
        
        prompt = f"""Desglosa la siguiente tarea en una lista de 3 a 5 subtareas simples:
        Tarea: {description}
        Responde solo la lista con guiones."""

        # llamamos al modelo
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        
        if not response.text:
            return ["Error: El modelo no devolvió texto."]

        # Procesamos la respuesta
        subtasks = [line.strip("- ").strip()
                     for line in response.text.split("\n") 
                     if "-" in line]
        
        return subtasks

    except Exception as e:
        print(f"Error con el nuevo SDK: {e}")
        return [f"Error de conexión: {str(e)}"]

# Ejemplo de uso
# print(create_simple_tasks_gemini("Pintar la sala de la casa"))