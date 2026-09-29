import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_quiz(topic):
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
Create 5 multiple-choice quiz questions about {topic}.

For each question provide:
1. Question
2. Four options (A, B, C, D)
3. Correct answer

Keep the questions simple and suitable for students.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    quiz = generate_quiz("Python")
    print(quiz)