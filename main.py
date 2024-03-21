from fastapi import FastAPI
from schema import SymptomQuery, SimilarSymptomsResponse
from services import SymptomService

app = FastAPI()
service = SymptomService("C:\Users\CHAITANYA\Documents\HEALTETHER COMPANY\disease_symptom\Columbia dataset.json")

@app.post("/similar_symptoms", response_model=SimilarSymptomsResponse)
async def get_similar_symptoms(symptom_query: SymptomQuery):
    similar_symptoms = service.get_similar_symptoms(symptom_query.symptom)
    return {"similar_symptoms": similar_symptoms}
