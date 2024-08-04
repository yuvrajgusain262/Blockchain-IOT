import random
import time
from datetime import datetime
import json

# Function to generate random temperature and humidity data
def generate_data():
    temperature = round(random.uniform(20, 40))
    humidity = round(random.uniform(0, 10))
    return {
        'Temperature': temperature,
        'Humidity': humidity,
        'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# Function to generate and save JSON data periodically
def generate_json():
    data_freq = 10
    data = []
    interval = 5
    for i in range(data_freq):
        data_generated = generate_data()
        data.append(data_generated)
        time.sleep(interval)
    # Save JSON data to file
    with open(r'D:\python\iot blockchain\data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
# Generate JSON data
    generate_json()
