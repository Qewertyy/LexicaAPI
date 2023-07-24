# Copyright 2023 Qewertyy, MIT License
from setuptools import setup

setup(
    name="openapi",
    version="0.0.2",
    author="Qewertyy",
    author_email="Qewertyy.irl@gmail.com",
    description="The python package for api.qewertyy.me",
    url="https://github.com/Qewertyy/Open-API",
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "aiohttp",
        "httpx[http2]",
        "asyncio"
    ],
    keywords="Python, API, Bard, Google Bard, Large Language Model, Chatbot API, Google API, Chatbot, Image Generations, Latent Diffusion, State of Art",
    classifiers=[
        "API",
    ]
)
