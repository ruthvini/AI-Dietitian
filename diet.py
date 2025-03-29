import ollama

def get_diet_plan(health_condition):
    prompt = f"You are a professional dietitian. Based on the following health condition, suggest a personalized diet plan:\n\nHealth Condition: {health_condition}\n\nDiet Plan:"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
