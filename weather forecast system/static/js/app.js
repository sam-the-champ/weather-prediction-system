document.getElementById('weatherForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission

    const date = document.getElementById('date').value; // Get date input

    if (date) {
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ date: date }),
        })
        .then(response => {
            // Check if the response status is not OK
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(`HTTP error! Status: ${response.status}, Message: ${err.error || response.statusText}`);
                });
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            // Check if the response contains an error
            if (data.error) {
                document.getElementById('result').innerText = `Error: ${data.error}`;
            } else {
                // Update the result with the predicted values
                document.getElementById('result').innerText = 
                    `Temperature: ${data.Temperature}, Windspeed: ${data.Windspeed}, Precipitation: ${data.Precipitation}, Humidity: ${data.Humidity}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerText = `Error: ${error.message || 'Unable to fetch prediction'}`;
        });
    } else {
        document.getElementById('result').innerText = 'Please enter a valid date.';
    }
});
