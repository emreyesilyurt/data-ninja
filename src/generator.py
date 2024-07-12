import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI API with your API key from configuration
def generate_data(details):
    print("Generating item data using GPT-4...")
    prompt = f"""
    Create a high-level item data for the following item using the provided details:

    Item Name: {details['name']}
    Item Description: {details['description']}
    Item Specifications: {details['specs']}

    Data:
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    data = response.choices[0].text.strip()
    print("Item data generated successfully.")
    return data
