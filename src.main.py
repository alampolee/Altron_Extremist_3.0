import asyncio
import os
from dotenv import load_dotenv

from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.function_call_content import FunctionCallContent
from semantic_kernel.contents.function_result_content import FunctionResultContent
from semantic_kernel.contents.utils.author_role import AuthorRole

# Import local modules
from src.agent.kernel_config import create_kernel_with_config
from src.agent.altron_agent import create_altron_agent
from src.plugins.core_functions import CoreFunctionsPlugin
from src.plugins.external_systems import ExternalSystemsPlugin

async def main():
    load_dotenv() # Load environment variables from .env file

    # 1. Create Kernel
    try:
        kernel, service_id = create_kernel_with_config()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return

    # 2. Add Plugins (Tools)
    kernel.add_plugin(CoreFunctionsPlugin(), plugin_name="CoreFunctionsPlugin")
    kernel.add_plugin(ExternalSystemsPlugin(), plugin_name="ExternalSystemsPlugin")
    print("Plugins loaded.")

    # 3. Create Altron Agent
    altron = create_altron_agent(kernel, service_id)
    print("Altron agent created.")

    # 4. Initialize Chat History
    chat_history = ChatHistory()
    # Optional: Add the system prompt to history for explicit context, though it's part of agent instructions
    # chat_history.add_system_message(altron.instructions)

    print("\n--- Altron Initialized ---")
    print("Enter your commands or questions for Altron (type 'quit' to exit).")

    # 5. Interaction Loop (Simulating AR/VR Input)
    while True:
        try:
            user_input = input("User > ")
            if user_input.lower() == 'quit':
                print("Shutting down Altron...")
                break
            if not user_input:
                continue

            chat_history.add_user_message(user_input)

            print("Altron < Thinking...")
            full_response = ""
            function_calls_info = [] # To store info about function calls for display

            # Use invoke_stream for potential real-time feedback
            async for message_content in altron.invoke_stream(chat_history):
                # print(f"DEBUG: Received content type: {type(message_content)}") # Debugging line
                # print(f"DEBUG: Content items: {message_content.items}") # Debugging line

                # Accumulate text content
                if message_content.role == AuthorRole.ASSISTANT and message_content.content:
                     print(message_content.content, end="", flush=True)
                     full_response += message_content.content

                # Process and display function calls and results
                for item in message_content.items:
                    if isinstance(item, FunctionCallContent):
                        func_call_msg = f"\n   [Function Call: {item.name} ({item.arguments})]"
                        print(func_call_msg, flush=True)
                        function_calls_info.append(func_call_msg)
                    elif isinstance(item, FunctionResultContent):
                        func_result_msg = f"\n   [Function Result ({item.name}): {item.result}]"
                        print(func_result_msg, flush=True)
                        function_calls_info.append(func_result_msg)


            print() # Newline after streaming is complete

            # Add the complete assistant message (including text and function info) to history
            # We construct a message that includes the text and represents the function interactions
            # Note: SK handles adding FunctionCallContent/FunctionResultContent internally during invoke,
            # so we just need to add the final textual response from the assistant.
            if full_response:
                 chat_history.add_assistant_message(full_response)
            # If only function calls happened, we might need to add a placeholder or summary message
            # For simplicity, we assume the LLM provides some text response even after function calls.


        except Exception as e:
            print(f"\nAn error occurred: {e}")
            # Optionally, decide whether to continue or break the loop on error
            # break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")