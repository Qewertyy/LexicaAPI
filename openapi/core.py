from openapi.constansts import *
from httpx import AsyncClient

class Client:
    """
    OpenApi Package for interacting with OpenAPI `api.qewertyy.me`
    """

    def __init__(
        self,
        self.url = BASE_URL,
        self.timeout = 30,
    ):
        """
        Initialize the client instance
        """
    self.session = AsyncClient(
            http2=True,
            headers=SESSION_HEADERS
        )
    
    async def palm(self, prompt: str) -> dict:
        """
        Get an answer from Palm 2 for the given prompt
        Example:
        >>> client = Client()
        >>> response = client.palm("Hello, Who are you?")
        >>> print(response['content'])

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
            "prompt":prompt
        }
        try:
            resp = await self.session.post(
                f"{self.url}/models",
                params=params,
                timeout=self.timeout
            )
        except Exception as e:
            print(f"Request failed: {e}")