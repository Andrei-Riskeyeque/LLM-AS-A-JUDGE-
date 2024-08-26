import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_KEY')
DEFAULT_MODEL = "gpt-4"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_KEY environment variable is not set")