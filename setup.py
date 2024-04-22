# Copyright 2023 Qewertyy, MIT License

from setuptools import setup,find_packages
import re

def get_version():
    filename = "lexica/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version

def get_long_description():
    with open("README.md", encoding="UTF-8") as f:
        long_description = f.read()
        return long_description

setup(
    name="lexica-api",
    version=get_version(),
    author="Qewertyy",
    author_email="Qewertyy.irl@gmail.com",
    description="The python package for api.qewertyy.dev",
    url="https://github.com/Qewertyy/LexicaAPI",
    python_requires=">=3.8",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "httpx[http2]"
    ],
    keywords="Python, API, Bard, Google Bard, Large Language Model, Chatbot API, Google API, Chatbot, Image Generations, Latent Diffusion, State of Art, Image Reverse Search, Reverse Image Search",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
