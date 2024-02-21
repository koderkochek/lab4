from datetime import datetime
import fastapi
from typing import List, Dict
from fastapi import Depends, HTTPException
from models import CreateNote, NoteInfo, ReadNoteText, ListOfNotes
from functions import get_tokens, verification, get_note, write_note, save_note, write_id, get_id

api_router = fastapi.APIRouter()

@api_router.post("/notes", response_model=CreateNote)
def create_note(text: str, token: str = Depends(verification)):
    oldID = get_id()
    newID = str(oldID)
    notes = get_note()
    timeNow = datetime.now().isoformat()
    notes[newID] = {"text": text, "created_at": timeNow, "updated_at": timeNow}
    oldID += 1
    write_id(oldID)
    write_note(notes)
    return CreateNote(id=newID)

@api_router.get("/", response_model = ReadNoteText)
def read_note(id: str, token: str = Depends(verification)):
    note = get_note()
    current_note = note[id]
    return ReadNoteText(id=id, text=current_note["text"])

@api_router.post("/notes/{id}/info", response_model=NoteInfo)
def get_info(id: str, token: str = Depends(verification)):
    note = get_note()
    note_id = note[id]
    return NoteInfo(created_at=note_id["created_at"], updated_at=note_id["updated_at"])

@api_router.post("/", response_model=ReadNoteText)
def edit_text(id: str, text: str, token: str = Depends(verification)):
    note = get_note()
    current_note = note[id]
    current_note["text"] = text
    write_note(note)
    return ReadNoteText(id = id, text = current_note["text"])

@api_router.delete("/notes/{id}/delete", response_model=ReadNoteText)
def delete_note(id: str, token: str = Depends(verification)):
    note = get_note()
    current_note = note[id]
    note.pop(id)
    save_note(note)
    return ReadNoteText(id = id, text = current_note["text"])

@api_router.get("/list", response_model=ListOfNotes)
def list_of_notes(token: str = Depends(verification)):
    note = get_note()
    keys_list = list(note.keys())
    dict_ids = {}
    for i in range(len(keys_list)):
        dict_ids[i] = keys_list[i]
    return ListOfNotes(counters=dict_ids)
