import json

class SymptomRepository:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
    
    def get_similar_symptoms(self, symptom: str, num_similar=5):
        with open(self.dataset_path, 'r') as f:
            data = json.load(f)
        if symptom in data:
            return data[symptom]['associated_symptoms'][:num_similar]
        return []
