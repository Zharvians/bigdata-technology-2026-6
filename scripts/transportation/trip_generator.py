import json, time, random, os
from datetime import datetime

OUTPUT_PATH = "data/serving/transportation"
os.makedirs(OUTPUT_PATH, exist_ok=True)

locations = ["Jakarta", "Balikpapan", "Depok", "Banjarmasin", "Kudus"]
vehicles = ["Car", "Motorbike", "Taxi", "Bus", "Truck"]

i = 1
while True:
    data = {
        "trip_id": f"TRX{i}",
        "vehicle_type": random.choice(vehicles),
        "location": random.choice(locations),
        "distance": random.uniform(1, 20),
        "fare": random.randint(10000, 100000),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(f"{OUTPUT_PATH}/trip_{i}.json", "w") as f:
        json.dump(data, f)

        print("Generated trip:", data)
        i += 1
        time.sleep(3)
