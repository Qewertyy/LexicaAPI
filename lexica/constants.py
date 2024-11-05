# Copyright 2024 Qewertyy, MIT License

import re, os
from dataclasses import dataclass
from typing import Literal

BASE_URL = "https://lexica.qewertyy.dev"
ALTERNATE_URL = "https://api.qewertyy.dev"

dirpath = os.path.dirname(os.path.abspath(__file__))
with open(dirpath + "/__init__.py") as f:
    match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
if not match:
    raise RuntimeError("__init__.py doesn't contain __version__")
version = match.groups()[0]

SESSION_HEADERS = {
    "Host": "lexica.qewertyy.dev",
    "User-Agent": f"Lexica/{version}",
}


class languageModels(object):
    gemma = {"modelId": 1, "name": "Gemma"}
    bard = {"modelId": 20, "name": "Bard"}
    mistral = {"modelId": 21, "name": "LLAMA 2"}
    llama = {"modelId": 18, "name": "LLAMA"}
    gpt = {"modelId": 5, "name": "ChatGPT"}
    gemini = {"modelId": 23, "name": "Gemini-Pro"}
    geminiVision = {"modelId": 24, "name": "Gemini-Pro-Vision"}
    openhermes = {"modelId": 27, "name": "OpenHermes"}


@dataclass
class Messages:
    content: str
    role: Literal["assistant", "user"]
