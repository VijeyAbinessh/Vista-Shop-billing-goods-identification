import json

with open("instances_val.json", "r") as f:
    data = json.load(f)

print(data.keys())
