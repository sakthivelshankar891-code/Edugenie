import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_learning_path(topic):
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
Create a simple learning path for students who want to learn {topic}.

Include:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Practice activities
5. A small project idea

Keep it simple and easy to understand.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    learning_path = generate_learning_path("Python")

    print(learning_path)
    