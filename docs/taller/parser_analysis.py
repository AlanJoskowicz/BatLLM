from urllib.parse import urlsplit
from modelito import OllamaProvider, Message
from pydantic import BaseModel
from enum import Enum
import requests, json

import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
base_directory = os.path.dirname(os.path.dirname(current_directory))
src_directory = os.path.join(base_directory, 'src')
if src_directory not in sys.path:
    sys.path.insert(0, src_directory)
from configs.app_config import config

url = config.get("llm", "url")
port = config.get("llm", "port")
host = f"{url}:{port}"

parsed = urlsplit(host if "://" in host else f"http://{host}")
hostname = parsed.hostname or "localhost"

models_list = ["qwen2.5:7b",
               "d1-omni:latest",
               "gpt-oss:120b-cloud",
               "llama3.2:latest",
               "smollm2:latest",]

model = models_list[0] # TODO: iterate with multiple models
timeout = 60.0

with open(f"{src_directory}/assets/system_instructions/augmented_independent_1.txt", "r") as directive:
    system_directive = directive.read()

class Action(Enum):
    ROTATE_CLOCKWISE = "C"
    ROTATE_ANTICLOCKWISE = "A"
    MOVE = "M"
    SHIELD_UP = "S1"
    SHIELD_DOWN = "S0"
    SHIELD_TOGGLE = "S"
    BULLET = "B"

class Response(BaseModel):
    action : Action
    value : float | None
    error : bool
KEYS = list(Response.model_fields.keys())

prompts = [{"prompt": "Move forward", "expected": {"action": "M", "value": None, "error": False}},]

# Bybassing modelito
payload = {
    "model": model,
    "messages": [{"role": "system", "content": system_directive},
                 {"role": "user", "content": prompts[0].get("prompt")}],
    "stream": False,
    "format": Response.model_json_schema(),
    "options": {"temperature": 0}, # Ensure reproducibility
}

model_response = requests.post(f"{host}/api/chat", json=payload, timeout=timeout)

def match(response, expected):
    if "error" in KEYS:
        if response.get("error") != expected.get("error"):
            return False
        elif response.get("error") is True:
            return True
    for key in KEYS:
        if response.get(key) != expected.get(key):
            return False
    return True

response_content = json.loads(model_response.json()["message"]["content"])   
print(response_content)
print(type(response_content))  
print(match(response_content, prompts[0].get("expected")))