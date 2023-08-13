from openapi import Client

def main(prompt: str) -> dict:
    client = Client()
    response = client.gpt(prompt)
    return response

if __name__ == "__main__":
    print(main("hello, who are you?"))