import json

f = open('data.json')
data = json.load(f)

quotes = data["quotes"]
events = data["events"]

print(quotes)
print(events)
