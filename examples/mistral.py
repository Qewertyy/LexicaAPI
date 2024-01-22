# Copyright 2024 Qewertyy, MIT License

from lexica import Client,languageModels

def main(prompt: str) -> dict:
    client = Client()
    response = client.ChatCompletion(prompt,languageModels.mistral)
    return response

if __name__ == "__main__":
    print(main("hello, who are you?"))