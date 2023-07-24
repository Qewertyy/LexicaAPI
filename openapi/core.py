from openapi.constants import *
from httpx import AsyncClient

class Client:
    """
    OpenApi Package for interacting with OpenAPI `api.qewertyy.me`
    """

    def __init__(
        self,
        url: str = BASE_URL,
    ):
        """
        Initialize the class
        """
        self.url = url,
        self.session = AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
            )
    
    async def palm(self, prompt: str) -> dict:
        """ 
        Get an answer from Palm 2 for the given prompt
        Example:
        >>> client = Client()
        >>> response = client.palm("Hello, Who are you?")
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
            print(self.url)
            resp = await self.session.post(
                f"{self.url[0]}/models",
                params=params,
            )
            return resp.json()
        except Exception as e:
            print(f"Request failed: {e}")