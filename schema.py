from pydantic import BaseModel

class SymptomQuery(BaseModel):
    symptom: str

class SimilarSymptomsResponse(BaseModel):
    similar_symptoms: List[str]
