# Copyright 2024 Qewertyy, MIT License

import time
from lexica import Client

def main(model_id:int,prompt:str,negative_prompt:str) -> dict:
    client = Client()
    resp = client.generate(model_id,prompt,negative_prompt)
    print(resp)
    task_id = resp['task_id']
    request_id = resp['request_id']
    time.sleep(60) # sleep for period of time to allow the task to be processed
    response = client.getImages(task_id,request_id)
    return response


if __name__ == "__main__":
    print(main(2,"1girl, white hair, purple eyes, portrait, realistic, towel, (onsen), sidelighting, wallpaper","nsfw"))