# Copyright 2024 Qewertyy, MIT License

import asyncio
import base64
import mimetypes
from lexica import AsyncClient, languageModels

async def async_main(prompt: str,images: list) -> dict:
    client = AsyncClient()
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
    response = await client.ChatCompletion(prompt,languageModels.geminiVision,json=payload)
    return response

if __name__ == "__main__":
    print(asyncio.run(async_main("whats this?",["./examples/images/image.png"])))