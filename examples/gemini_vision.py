# Copyright 2024 Qewertyy, MIT License

import base64,mimetypes
from lexica import Client,languageModels

def main(prompt: str,images:list) -> dict:
    client = Client()
    imageInfo = []
    for image in images:
        with open(image,"rb") as imageFile:
            data = base64.b64encode(imageFile.read()).decode("utf-8")
            mime_type,_= mimetypes.guess_type(image)
            imageInfo.append({
                "data": data,
                "mime_type": mime_type
            })
    payload = {
        "images":imageInfo
    }
    response = client.ChatCompletion(prompt,languageModels.geminiVision,json=payload)
    return response

if __name__ == "__main__":
    print(main("what's this?",["./examples/images/image.png"]))