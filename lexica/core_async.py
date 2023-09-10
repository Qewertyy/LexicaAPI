import base64
from typing import Union, Dict
from httpx import AsyncClient as AsyncHttpxClient
from lexica.constants import *
from lexica.utils import *

class AsyncClient:
    """
    Async Client
    """

    def __init__(
        self
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
    
    async def _request(self, **kwargs) -> Union[Dict,bytes]:
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
    
    async def palm(self, prompt: str,model_id:int=0) -> dict:
        """ 
        Get an answer from PaLM 2 for the given prompt
        Example:
        >>> client = Client()
        >>> response = await client.palm("Hello, Who are you?")
        >>> print(response)

        Args:
            prompt (str): Input text for the query.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "message": str,
                    "content": str,
                    "code": int
                }
        """
        params = {
            "model_id": model_id,
            "prompt": prompt
        }
        resp = await self._request(
            url=f'{self.url}/models',
            method='POST',
            params=params,
            headers = {"content-type": "application/json"}
        )
        return resp

    async def gpt(self, prompt: str,context: str = False) -> dict:
        """ 
        Get an answer from GPT-3.5-Turbo for the given prompt
        Example:
        >>> client = Client()
        >>> response = await client.gpt("Hello, Who are you?")
        >>> print(response)

        Args:
            prompt (str): Input text for the query.

        Returns:
            dict: Answer from the API in the following format:
                {
                    "status": str,
                    "content": str,
                    "code": int
                }
        """
        params = {
            "model_id": 5,
            "prompt": prompt,
            "context": context if context else ''
        }
        resp = await self._request(
            url=f'{self.url}/models',
            method='POST',
            params=params,
            headers = {"content-type": "application/json"}
        )
        return resp

    async def upscale(self, image: bytes) -> bytes:
        """ 
        Upscale an image
        Example:
        >>> client = Client()
        >>> response = await client.upscale(image)
        >>> with open('upscaled.png', 'wb') as f:
                f.write(response)

        Args:
            image (bytes): Image in bytes.
        Returns:
            bytes: Upscaled image in bytes.
        """
        b = base64.b64encode(image).decode('utf-8')
        content = await self._request(
            url=f'{self.url}/upscale',
            method='POST',
            json={'image_data': b}
        )
        return content
    
    async def generate(self,model_id:int,prompt:str,negative_prompt:str="",images: int= 1) -> dict:
        """ 
        Generate image from a prompt
        Example:
        >>> client = Client()
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
    
    async def getImages(self,task_id:str,request_id:str) -> dict:
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