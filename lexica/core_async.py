# Copyright 2024 Qewertyy, MIT License

import base64
from typing import Union, Dict,Optional
from httpx import AsyncClient as AsyncHttpxClient
from lexica.constants import *
from lexica.utils import *

class AsyncClient:
    """
    Async Client
    """

    def __init__(
        self: "AsyncClient",
    ):
        """
        Initialize the class
        """
        self.url = BASE_URL
        self.session = AsyncHttpxClient(
            http2=True,
        )
        self.headers = SESSION_HEADERS
        self.timeout = 60
        #self.models = self.getModels()
    
    async def _request(self : "AsyncClient", **kwargs) -> Union[Dict,bytes]:
        self.headers.update(kwargs.get("headers",{}))
        contents = {'json':{},'data':{},'files':{}}
        for i in list(contents):
            if i in kwargs:
                contents[i] = clean_dict(kwargs.get(i))
        response = await self.session.request(
                method=kwargs.get('method', 'GET'),
                url=kwargs.get('url'),
                headers=self.headers,
                content=kwargs.get('content'),
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

    async def getModels(self) -> dict:
        resp = await self._request(url=f'{self.url}/models')
        return resp
    
    async def __aenter__(self):
        return self

    async def close(self) -> None:
        """Close async session"""
        return await self.session.aclose()

    async def ChatCompletion(self : "AsyncClient", prompt: str,model : dict = languageModels.palm2,*args, **kwargs) -> dict:
        """
        Get an answer from LLMs' for the given prompt
        Example:
        >>> client = AsyncClient()
        >>> response = await client.ChatCompletion("Hello, Who are you?")
        >>> print(response)

        Args:
            prompt (str): Input text for the query.
            model (dict): Model dict of the LLM defaults to palm.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "status": str,
                    "content": str,
                    "code": int
                }
        """
        params = {
            "model_id": model.get('modelId',0),
            "prompt": prompt,
        }
        resp = await self._request(
            url=f'{self.url}/models',
            method='POST',
            params=params,
            json=kwargs.get('json',{}),
            headers = {"content-type": "application/json"}
        )
        return resp

    async def upscale(self : "AsyncClient", image: bytes= None, image_url: str= None,format: str = "binary") -> bytes:
        """ 
        Upscale an image
        Example:
        >>> client = AsyncClient()
        >>> response = await client.upscale(image)
        >>> with open('upscaled.png', 'wb') as f:
                f.write(response)

        Args:
            image (bytes): Image in bytes.
        Returns:
            bytes: Upscaled image in bytes.
        """
        payload = {
            "format": format,
        }
        if image and not image_url:
            payload.setdefault('image_data',base64.b64encode(image).decode('utf-8'))
        elif not image and not image_url:
            raise Exception("No image or image_url provided")
        else:
            payload.setdefault('image_url',image_url)
        content = await self._request(
            url=f'{self.url}/upscale',
            method = 'POST',
            json=payload
        )
        return content
    
    async def generate(self : "AsyncClient",model_id:int,prompt:str,negative_prompt:str="",images: int= 1) -> dict:
        """ 
        Generate image from a prompt
        Example:
        >>> client = AsyncClient()
        >>> response = await client.generate(model_id,prompt,negative_prompt)
        >>> print(response)

        Args:
            prompt (str): Input text for the query.
            negative_prompt (str): Input text for the query.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "task_id": int,
                    "request_id": str,
                    "code": int
                }
        """
        payload = {
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt, #optional
            "num_images": images,  #optional number of images to generate (default: 1) and max 4
        }
        resp = await self._request(
            url=f'{self.url}/models/inference',
            method='POST',
            json=payload,
            headers = {"content-type": "application/json"}
        )
        return resp
    
    async def getImages(self : "AsyncClient",task_id:str,request_id:str) -> dict:
        """ 
        Generate image from a prompt
        Example:
        >>> client = AsyncClient()
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
        resp = await self._request(
            url=f'{self.url}/models/inference/task',
            method='POST',
            json=payload,
            headers = {"content-type": "application/json"}
        )
        return resp
    
    async def ImageReverse(self : "AsyncClient", imageUrl: str,engine: str="google") -> dict:
        """ 
        Reverse search an image
        Example:
        >>> client = AsyncClient()
        >>> response = await client.ImageReverse(imageUrl)
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
        resp = await self._request(
            url=f'{self.url}/image-reverse/{engine}',
            method='POST',
            params={'img_url': imageUrl}
        )
        return resp
    
    async def MediaDownloaders(self : "AsyncClient",platform: str,url:str) -> dict:
        """ 
        Downloadable links for the given social media url
        Example:
        >>> client = AsyncClient()
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
        resp = await self._request(
            url=f'{MISC_URL}/downloaders/{platform}',
            method='POST',
            params={'url': url}
        )
        return resp
    
    async def SearchImages(self : "AsyncClient",query: str, page: int=0,engine: str="google") -> dict:
        """ 
        Search for images
        Example:
        >>> client = AsyncClient()
        >>> response = await client.SearchImages(query)
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
        resp = await self._request(
            url=f'{self.url}/image-search/{engine}',
            method='POST',
            params={'query': query,'page':page}
        )
        return resp
    
    async def AntiNsfw(self : "AsyncClient", imageUrl: str, modelId: int = 28) -> dict:
        """ 
        Check for an image if it is safe for work or not
        Example:
        >>> client = AsyncClient()
        >>> response = await client.AntiNsfw(imageUrl)
        >>> print(response)

        Args:
            imageUrl (str): url of the image for anti nsfw.

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
        resp = await self._request(
            url=f'{self.url}/anti-nsfw',
            method='POST',
            params={'img_url': imageUrl,"model_id":modelId}
        )
        return resp