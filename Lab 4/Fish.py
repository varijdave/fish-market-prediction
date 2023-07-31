#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# In[10]:



app = Flask(__name__)

# Load and preprocess the data
data = pd.read_csv('fish.csv')
target_variable = 'Species'
X = data.drop(columns=[target_variable])
y = data[target_variable]


# In[11]:


# Encoding the target variable for classification
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


# In[12]:


# Build the ML model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict_species():
    try:
        data = request.json
        length = data['Length1']
        width = data['Width1']

        # Make a prediction
        prediction = model.predict([[length, width]])[0]
        predicted_species = label_encoder.inverse_transform([prediction])[0]

        return jsonify({'species': predicted_species})
    except Exception as e:
        return jsonify({'error': 'Invalid input. Please provide Length1 and Width1 as numerical values.'}), 400

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




