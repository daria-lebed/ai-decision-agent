import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sample CRM dataset
data = {
    "Lead": ["Acme Corp", "Nova AI", "GrowthLabs", "HyperCRM"],
    "Stage": ["Negotiation", "Discovery", "Lost", "Closed Won"],
    "Value": [25000, 15000, 8000, 42000],
}
df = pd.DataFrame(data)

# Create a prompt for the AI
prompt = f"""
You are an AI RevOps analyst.
Analyze this CRM dataset and suggest the top 2 actions
to increase conversions next week.

Data:
{df.to_markdown()}
"""

# Run analysis
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
)

print("\n--- AI Decision Agent Output ---\n")
print(response.output_text)
