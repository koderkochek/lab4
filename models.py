from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class CreateNote(BaseModel):
    id: int

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime

class ReadNoteText(BaseModel):
    id: int
    text: str

class ListOfNotes(BaseModel):
    notes: Dict[int, str]
