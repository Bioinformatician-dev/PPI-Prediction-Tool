from flask import Flask, request, render_template
from Bio import SeqIO
import numpy as np
from model import predict_interactions  # Importing prediction function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'sequence' not in request.files:
        return "No file uploaded"
    
    file = request.files['sequence']
    sequences = []
    
    # Parse FASTA file
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))
    
    # Call prediction function
    predictions = predict_interactions(sequences)
    
    return render_template('results.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
