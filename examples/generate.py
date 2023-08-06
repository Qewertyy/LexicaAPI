import time
from openapi import Client

def main(model_id:int,prompt:str,negative_prompt:str) -> dict:
    client = Client()
    resp = client.generate(model_id,prompt,negative_prompt)
    print(resp)
    task_id = resp['task_id']
    request_id = resp['request_id']
    time.sleep(30) # sleep for period of time to allow the task to be processed
    response = client.getImages(task_id,request_id)
    return response

# is status is not "completed" then use this

def getImages(task_id:str,request_id:str) -> dict:
    client = Client()
    response = client.getImages(task_id,request_id)
    return response

if __name__ == "__main__":
    print(main(2,"1girl, white hair, purple eyes, portrait, realistic, towel, (onsen), sidelighting, wallpaper,nsfw",""))
    #print(getImages("task id here","request id here"))