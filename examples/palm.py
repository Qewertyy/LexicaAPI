from lexica import Client

def main(prompt: str) -> dict:
    client = Client()
    response = client.palm(prompt)
    return response

if __name__ == "__main__":
    print(main("hello world"))