from lexica import Client

def main(url: str) -> dict:
    client = Client()
    response = client.MediaDownloaders("instagram",url)
    return response

if __name__ == "__main__":
    print(main("https://www.instagram.com/p/Cz2HsJ5NRDf/"))