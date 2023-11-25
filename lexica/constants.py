BASE_URL = "https://lexica.qewertyy.me"
MISC_URL = "https://api.qewertyy.me"

SESSION_HEADERS = {
    "Host": "lexica.qewertyy.me",
}

class languageModels(object):
    bard = {"modelId":20,"name":"Bard"}
    palm = {"modelId":0,"name":"PaLM"}
    palm2 = {"modelId":1,"name":"PaLM 2"}
    mistral = {"modelId":21,"name":"LLAMA 2"}
    llama = {"modelId":18,"name":"LLAMA"}
    gpt = {"modelId":5,"name":"ChatGPT"}