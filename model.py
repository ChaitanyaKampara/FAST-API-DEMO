from pydantic import BaseModel
from typing import List, Optional

class Symptom(BaseModel):
    name: str
    associated_symptoms: Optional[List[str]] = []
