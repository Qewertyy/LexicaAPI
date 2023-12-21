from lexica import Client
from lexica.constants import languageModels

def main(prompt: str) -> dict:
    client = Client()
    response = client.ChatCompletion(prompt,languageModels.gemini)
    return response

if __name__ == "__main__":
    print(main("hello, who are you?"))