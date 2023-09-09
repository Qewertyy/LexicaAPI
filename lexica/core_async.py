import base64
from httpx import AsyncClient as AsyncHttpxClient
from lexica.constants import *


class AsyncClient:
    """
    OpenApi Package for interacting with OpenAPI `api.qewertyy.me`
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
            headers=SESSION_HEADERS,
        )
    
    async def getModels(self) -> dict:
        resp = await self.session.get(f'{self.url}/models')
        return resp.json()
    
    async def __aenter__(self):
        return self

    async def close(self) -> None:
        """Close async session"""
        return await self.session.aclose()
    
    async def palm(self, prompt: str) -> dict:
        """ 
        Get an answer from PaLM 2 for the given prompt
        Example:
        >>> client = Client()
        >>> response = await client.palm("Hello, Who are you?")
        >>> print(response)

        Args:
            prompt (str): Input text for the query.

        Returns:
            dict: Answer from the Open API in the following format:
                {
                    "status": str,
                    "content": str
                }
        """
        params = {
            "model_id": 0,
            "prompt": prompt
        }
        self.session.headers.update({"content-type": "application/json"})
        resp = (await self.session.post(
                f'{self.url}/models',
                params=params,
            )).json()
        if resp['code'] == 0:
            raise Exception(f"API error {resp}")
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
            dict: Answer from the Open API in the following format:
                {
                    "status": str,
                    "content": str
                }
        """
        params = {
            "model_id": 5,
            "prompt": prompt
            ,"context": context if context else ''
        }
        self.session.headers.update({"content-type": "application/json"})
        resp = (await self.session.post(
            f'{self.url}/models',
            params=params,
        )).json()
        if resp['code'] == 0:
            raise Exception(f"API error {resp}")
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
        try:
            b = base64.b64encode(image).decode('utf-8')
            response = await self.session.post(
                f'{self.url}/upscale',
                data={'image_data': b},
                timeout=None
            )
            return response.content
        except Exception as e:
            print(f"Failed to upscale the image: {str(e)}")

    async def generate(self,model_id:int,prompt:str,negative_prompt:str=None,images: int= None) -> dict:
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
            dict: Answer from the Open API in the following format:
                {
                    "message": str,
                    "task_id": int,
                    "request_id": str
                }
        """
        data = {
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt if negative_prompt else '', #optional
            "num_images": images if images else 1,  #optional number of images to generate (default: 1) and max 4
        }
        resp = (await self.session.post(
            f'{self.url}/models/inference',
            data=data
        )).json()
        if resp['code'] == 0:
            raise Exception(f"API error {resp}")
        return resp
    
    async def getImages(self,task_id:int,request_id:str) -> dict:
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
            dict: Answer from the Open API in the following format:
                {
                    "message": str,
                    "img_urls": array,
                }
        """
        data = {
            "task_id": task_id,
            "request_id": request_id
        }
        resp = (await self.session.post(
            f'{self.url}/models/inference/task',
            data=data
        )).json()
        if resp['code'] == 0:
            raise Exception(f"API error {resp}")
        return resp
