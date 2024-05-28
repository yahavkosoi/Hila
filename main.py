import openai

openai.api_key = "0123456789"


def ask_chatgpt(prompt):
    """
    Sends a question to ChatGPT and returns the answer.
    """
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message["content"]


if __name__ == "__main__":
    question = "Write a goodbye letter to a computer science teacher that has taught us for 2 years."
    print(ask_chatgpt(question))




