import base64
from httpx import AsyncClient
from openapi.constants import *


class Client:
    """
    OpenApi Package for interacting with OpenAPI `api.qewertyy.me`
    """

    def __init__(
        self
    ):
        """
        Initialize the class
        """
        self.url = BASE_URL,
        self.session = AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
        )

    async def palm(self, prompt: str) -> dict:
        """ 
        Get an answer from Palm 2 for the given prompt
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
        try:
            self.session.headers.update({"content-type": "application/json"})
            resp = await self.session.post(
                f'{self.url[0]}/models',
                params=params,
            )
            return resp.json()
        except Exception as e:
            print(f"Request failed: {e}")

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
                f'{self.url[0]}/upscale',
                data={'image_data': b},
                timeout=None
            )
            return response.content
        except Exception as e:
            print(f"Failed to upscale the image: {e}")
