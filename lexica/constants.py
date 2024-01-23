# Copyright 2024 Qewertyy, MIT License

import re

BASE_URL = "https://lexica.qewertyy.dev"
MISC_URL = "https://api.qewertyy.dev"

def get_version():
    filename = "__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version

SESSION_HEADERS = {
    "Host": "lexica.qewertyy.dev",
    "User-Agent":f"Lexica/{get_version()}"
}


class languageModels(object):
    bard = {"modelId":20,"name":"Bard"}
    palm = {"modelId":0,"name":"PaLM"}
    palm2 = {"modelId":1,"name":"PaLM 2"}
    mistral = {"modelId":21,"name":"LLAMA 2"}
    llama = {"modelId":18,"name":"LLAMA"}
    gpt = {"modelId":5,"name":"ChatGPT"}
    gemini = {"modelId":23,"name":"Gemini-Pro"}
    geminiVision = {"modelId":24,"name":"Gemini-Pro-Vision"}