import openai

# Use the OpenAI API key to initialize the API client
openai.api_key = "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"


def get_answer(question):
    # Define the model and prompt to use
    model_engine = "text-davinci-002"
    prompt = (f"{question}"
             )

    # Use the API client to generate a response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the text of the first response
    message = response["choices"][0]["text"].strip()

    return message

# Example usage
print(get_answer("What is the capital of France?"))
