import json

"""This is a dictionary"""
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}

"""And this a JSON"""
person_json = "{'name': 'Iriome', 'country': 'Spain', 'studies': 'Self-taught', 'skills': ['Python']}"

"""Usually use 3 comillas to make more legible"""
person_json = '''{
    "name":"Iriome",
    "country":"Spain",
    "studies":"Self-taught",
    "skills":["Python"]
}'''

"""Convert JSON to dictionary"""
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct["name"])

"""Convert dictionary to JSON"""
person = {
    "name": "Iriome",
    "country": "Spain",
    "studies": "Self-taught",
    "skills": ["Python"]}

person_json = json.dumps(person, indent=2)
print(type(person_json))
#print(person_json)

"""Save a file in JSON"""
with open("C:\\Users\\iriom\\Desktop\\person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)
    
    
with open("C:\\Users\\iriom\\Desktop\\person.json", "r", encoding="utf-8") as f:
    person = json.load(f)
    print(person)
    
    