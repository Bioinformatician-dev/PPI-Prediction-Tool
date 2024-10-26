from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Mock model for demonstration purposes
class MockModel:
    def predict(self, features):
        return ['Interaction' if np.random.rand() > 0.5 else 'No Interaction' for _ in features]
    
    def predict_proba(self, features):
        return np.random.rand(len(features), 2)

# Instantiate mock model
model = MockModel()

def predict_interactions(sequences):
    # Example feature extraction (for simplicity, we'll use random features)
    features = np.random.rand(len(sequences), 10)  # Mock feature vector of length 10
    
    predictions = model.predict(features)
    confidence_scores = model.predict_proba(features)
    
    # Combine predictions with confidence scores
    result = []
    for i in range(len(predictions)):
        result.append((sequences[i], predictions[i], confidence_scores[i].max()))
    
    return result
