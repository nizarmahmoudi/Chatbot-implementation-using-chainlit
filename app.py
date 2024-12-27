import chainlit as cl
from src.llm import ask_order

# Initialize the messages list with a system instruction
messages = [{"role": "system", "content": "You are a helpful assistant."}]


@cl.on_message
async def main(message: cl.Message):
    """
    Main function to handle user messages and respond using the LLM.
    """
    # Append user message to the conversation
    messages.append({"role": "user", "content": message.content})

    # Get response from the Ollama model asynchronously
    response = await ask_order(messages)

    # Append assistant's response to the conversation
    messages.append({"role": "assistant", "content": response})

    # Send the response back to the user
    await cl.Message(content=response).send()
