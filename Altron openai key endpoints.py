
import os  
import base64
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL", "")  
deployment = os.getenv("DEPLOYMENT_NAME", "Altron_gpt-35-turbo")  
subscription_key = os.getenv("")  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2025-01-01-preview",
)
    
    

#Prepare the chat prompt 
chat_prompt = [
    {
        "role": "user",
        "content": "thanks I'm back to work."
    },
    {
        "role": "assistant",
        "content": "Welcome back! How can I assist you with your work today?"
    }
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt  
    
# Generate the completion  
completion = client.chat.completions.create(  
    model=deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.4,  
    top_p=0.39,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False
)

print(completion.to_json())  
    
