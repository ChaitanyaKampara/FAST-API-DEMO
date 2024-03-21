from repository import SymptomRepository

class SymptomService:
    def __init__(self, dataset_path):
        self.repository = SymptomRepository(dataset_path)
    
    def get_similar_symptoms(self, symptom: str):
        return self.repository.get_similar_symptoms(symptom)
