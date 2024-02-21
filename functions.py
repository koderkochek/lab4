from fastapi import Depends, HTTPException
import json
from typing import Dict, List

def get_tokens():
    try:
        with open("tokens.json", "r", encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []

def verification(token: str, tokens: List[str] = Depends(get_tokens)):
    if token not in tokens:
        raise HTTPException(status_code=401, detail="Incorrect token")

def write_id(id: int):
    with open("id.txt", "w") as f:
        f.write(str(id))

def get_id():
    with open("id.txt", "r") as f:
        return int(f.read())

def write_note(text: str):
    with open("notes.json", "w") as f:
        json.dump(text, f)

def get_note():
    try:
        with open("notes.json", "r", encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {}

def save_note(notes: Dict[str, dict]):
    with open("notes.json", "w") as f:
        json.dump(notes, f)
