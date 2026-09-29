from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "buildbuddy"

client.create_bank(
    bank_id=BANK_ID,
    name="BuildBuddy Project Memory"
)

client.retain(
    bank_id=BANK_ID,
    content="BuildBuddy is a Python project. The developer prefers simple Python code and uses FastAPI for the backend."
)

print("Memory saved successfully!")

result = client.recall(
    bank_id=BANK_ID,
    query="What programming language and backend framework does the developer prefer?"
)

print("\nRecalled memory:")
print(result)