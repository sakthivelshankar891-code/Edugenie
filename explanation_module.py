from transformers import pipeline

# Load the local explanation model
explainer = pipeline(
    "text2text-generation",
    model="MBZUAI/LaMini-Flan-T5-783M"
)


def explain_concept(concept):
    if not concept.strip():
        return "Please enter a concept."

    prompt = f"Explain the concept of {concept} in simple words."

    result = explainer(
        prompt,
        max_length=150,
        do_sample=False
    )

    return result[0]["generated_text"]


if __name__ == "__main__":
    answer = explain_concept("Python")
    print(answer)