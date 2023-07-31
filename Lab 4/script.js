// script.js
async function predict() {
    const length = parseFloat(document.getElementById('length').value);
    const width = parseFloat(document.getElementById('width').value);

    // Add more variables here if needed

    if (isNaN(length) || isNaN(width)) {
        alert('Please enter valid numerical values for length and width.');
        return;
    }

    const data = {
        Length1: length,
        Width1: width,
        // Add more data properties here if needed
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    const predictionResult = document.getElementById('prediction-result');
    predictionResult.textContent = `Predicted species: ${result.species}`;
}
