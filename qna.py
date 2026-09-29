import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def answer_question(question):
    if not question.strip():
        return "Please enter a question."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return response.text


if __name__ == "__main__":
    answer = answer_question("What is Python?")
    print(answer)