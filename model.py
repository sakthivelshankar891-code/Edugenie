from model import generate_answer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "MBZUAI/LaMini-Flan-T5-248M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_answer(question):
    inputs = tokenizer(
        question,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer
    answer = generate_answer(question)
return {"answer": answer}