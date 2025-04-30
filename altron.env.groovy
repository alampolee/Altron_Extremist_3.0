# --- Azure AI Inference Service (using GitHub Token) ---
# Follow instructions: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# Ensure the token has access to the Azure AI Inference service if applicable, or use Azure OpenAI keys below.
GITHUB_TOKEN="YOUR_GITHUB_PAT_TOKEN"
AZURE_AI_INFERENCE_ENDPOINT="https://models.inference.ai.azure.com"
AZURE_AI_INFERENCE_MODEL_ID="gpt-4o-mini" # Or gpt-4o, etc.

# --- OR Azure OpenAI Service ---
# AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT" # e.g., https://your-resource-name.openai.azure.com/
# AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
# AZURE_OPENAI_DEPLOYMENT_NAME="YOUR_AZURE_OPENAI_DEPLOYMENT_NAME" # e.g., gpt-4o
# AZURE_OPENAI_API_VERSION="2024-05-01-preview" # Or latest appropriate version

# --- Optional: API Keys for External Plugins ---
# SERPAPI_API_KEY="YOUR_SERPAPI_KEY" # Example if using a web search plugin
# DCP_API_ENDPOINT="YOUR_DCP_API_ENDPOINT"
# DCP_API_KEY="YOUR_DCP_API_KEY"
# DRONE_API_ENDPOINT="YOUR_DRONE_API_ENDPOINT"
# DRONE_API_KEY="YOUR_DRONE_API_KEY"