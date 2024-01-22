# Copyright 2024 Qewertyy, MIT License

import asyncio
from lexica import AsyncClient

async def main(model_id:int,prompt:str,negative_prompt:str) -> dict:
    client = AsyncClient()
    resp = await client.generate(model_id,prompt,negative_prompt)
    print(resp)
    task_id = resp['task_id']
    request_id = resp['request_id']
    await asyncio.sleep(30) # sleep for period of time to allow the task to be processed
    response = await client.getImages(task_id,request_id)
    return response

# if status is not "completed" then use this method to get the images

async def getImages(task_id:str,request_id:str) -> dict:
    client = AsyncClient()
    response = await client.getImages(task_id,request_id)
    return response

if __name__ == "__main__":
    asyncio.run(main(2,"1girl, white hair, purple eyes, portrait, realistic, towel,sidelighting, wallpaper",""))
    #print(asyncio.run(getImages("14248074744444933","f884f17b7b78856"))) # task id, request id