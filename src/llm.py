import subprocess
import asyncio
from src.prompt import system_instruction  # Import the system instruction

# Define the model name
MODEL_NAME = "llama3.2:latest"  # Use the model you have available


async def query_ollama_model(prompt):
    # Run the Ollama model and capture the output
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME], input=prompt, text=True, capture_output=True
    )
    return result.stdout.strip()  # Return the output without extra whitespace


# Initialize the messages list with the system instruction
messages = [{"role": "system", "content": system_instruction}]


async def ask_order(messages):
    # Create the conversation string
    conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    # Include the system instruction directly in the prompt
    full_prompt = f"{system_instruction}\n{conversation}"

    # Query the Ollama model
    response = await query_ollama_model(full_prompt)

    return response
