# Copyright 2024 Qewertyy, MIT License

import base64, httpx
from lexica.constants import *
from lexica.utils import *
from typing import Union,Dict

class Client:
    """
    Sync Client
    """
    def __init__(
        self: "Client",
    ):
        """
        Initialize the class
        """
        self.url = BASE_URL
        self.session = httpx.Client(
                http2=True
            )
        self.timeout = 60
        self.headers = SESSION_HEADERS
    
    def _request(self : "Client", **kwargs) -> Union[Dict,bytes]:
        self.headers.update(kwargs.get("headers",{}))
        contents = {'json':{},'data':{},'files':{}}
        for i in list(contents):
            if i in kwargs:
                contents[i] = clean_dict(kwargs.get(i))
        response = self.session.request(
                method=kwargs.get('method', 'GET'),
                url=kwargs.get('url'),
                headers=self.headers,
                params=kwargs.get('params'),
                data=contents.get('data'),
                json=contents.get('json'),
                files=contents.get('files'),
                timeout=self.timeout,
            )
        if response.status_code != 200:
            raise Exception(f"API error {response.text}")
        if response.headers.get('content-type') in ['image/png','image/jpeg','image/jpg'] :
            return response.content
        rdata = response.json()
        if rdata['code'] == 0:
            raise Exception(f"API error {response.text}")
        return rdata

    def getModels(self) -> dict:
        resp = self._request(url=f'{self.url}/models')
        return resp
    
    def ChatCompletion(self : "Client", prompt: str,model : dict = languageModels.palm ,*args, **kwargs) -> dict:
        """ 
        Get an answer from LLMs' for the given prompt
        Example:
        >>> client = Client()
        >>> response = client.ChatCompletion("Hello, Who are you?",0)
        >>> print(response)

        Args:
            prompt (str): Input text for the query.
            model (dict): Model dict of the LLM defaults to palm.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": str,
                    "code": int
                }
        """
        params = {
            "prompt": prompt,
            "model_id": model.get('modelId',0),
        }
        resp = self._request(
            url=f'{self.url}/models',
            method='POST',
            params=params,
            json=kwargs.get('json',{}),
            headers={"content-type": "application/json"}
            )
        return resp

    def upscale(self : "Client", image: bytes) -> bytes:
        """ 
        Upscale an image
        Example:
        >>> client = Client()
        >>> response = client.upscale(image)
        >>> with open('upscaled.png', 'wb') as f:
                f.write(response)

        Args:
            image (bytes): Image in bytes.
        Returns:
            bytes: Upscaled image in bytes.
        """
        b = base64.b64encode(image).decode('utf-8')
        content = self._request(
            url=f'{self.url}/upscale',
            method = 'POST',
            json={'image_data': b}
        )
        return content

    def generate(self : "Client",model_id:int,prompt:str,negative_prompt:str="",images: int=1) -> dict:
        """ 
        Generate image from a prompt
        Example:
        >>> client = Client()
        >>> response = client.generate(model_id,prompt,negative_prompt)
        >>> print(response)

        Args:
            prompt (str): Input text for the query.
            negative_prompt (str): Input text for the query.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "task_id": int,
                    "request_id": str
                }
        """
        payload = {
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt, #optional
            "num_images": images,  #optional number of images to generate (default: 1) and max 4
        }
        resp = self._request(
            url=f'{self.url}/models/inference',
            method='POST',
            json=payload,
            headers={"content-type": "application/json"}
        )
        return resp
    
    def getImages(self : "Client",task_id:str,request_id:str) -> dict:
        """ 
        Generate image from a prompt
        Example:
        >>> client = Client()
        >>> response = client.getImages(task_id,request_id)
        >>> print(response)

        Args:
            prompt (str): Input text for the query.
            negative_prompt (str): Input text for the query.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "img_urls": array,
                    "code": int
                }
        """
        payload = {
            "task_id": task_id,
            "request_id": request_id
        }
        resp = self._request(
            url=f'{self.url}/models/inference/task',
            method='POST',
            json=payload,
            headers={"content-type": "application/json"}
        )
        return resp
    
    def ImageReverse(self : "Client", imageUrl: str,engine: str="goole") -> dict:
        """ 
        Reverse search an image
        Example:
        >>> client = Client()
        >>> response = client.ImageReverse(imageUrl)
        >>> print(response)

        Args:
            imageUrl (str): url of the image for reverse search.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": {
                        "bestResults": array,
                        "relatedContent": array, #optional
                        "others": array #optional
                        },
                    "code": int
                }
        """
        resp = self._request(
            url=f'{self.url}/image-reverse/{engine}',
            method='POST',
            params={"img_url": imageUrl}
        )
        return resp
    
    def MediaDownloaders(self : "Client",platform: str,url:str):
        """ 
        Returns with downloadable links for the given social media url
        Example:
        >>> client = Client()
        >>> response = client.MediaDownloaders(platform,url)
        >>> print(response)

        Args:
            platform (str): social media platform name.
            url (str): url of the post.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": {
                        "url": array,
                        "mediaUrls": array,
                        "by": str,
                        "title": str,
                        },
                    "code": int
                }
        """
        resp = self._request(
            url=f'https://api.qewertyy.me/downloaders/{platform}',
            method='POST',
            params={"url": url}
        )
        return resp
    
    def SearchImages(self : "Client",query: str, page: int=0,engine: str="google") -> dict:
        """ 
        Search for images
        Example:
        >>> client = Client()
        >>> response = client.SearchImages(query)
        >>> print(response)

        Args:
            query (str): query to perform the search.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": [],
                    "code": int
                }
        """
        resp = self._request(
            url=f'{self.url}/image-search/{engine}',
            method='POST',
            params={"query": query}
        )
        return resp
    
    def AntiNsfw(self : "Client", imageUrl: str) -> dict:
        """ 
        Check for an image if it is safe for work or not
        Example:
        >>> client = Client()
        >>> response = client.AntiNsfw(imageUrl)
        >>> print(response)

        Args:
            imageUrl (str): url of the image for reverse search.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": {
                        "sfw": bool #true if sfw (safe for work) else false
                        },
                    "code": int
                }
        """
        resp = self._request(
            url=f'{self.url}/anti-nsfw',
            method='POST',
            params={"img_url": imageUrl}
        )
        return resp