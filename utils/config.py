import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMADB_PATH = os.getenv("CHROMADB_PATH", "./db")
VERSION_DIR = os.getenv("VERSION_DIR", "./versions")

# Additional configs (optional)
DEFAULT_MODEL = "gpt-4"
PROMPT_DIR = os.path.join(os.path.dirname(__file__), "../ai_engine/prompts/")
