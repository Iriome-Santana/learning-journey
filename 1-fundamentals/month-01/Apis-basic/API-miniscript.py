import requests

URL = "https://randomuser.me/api/"

response = requests.get(URL)
data = response.json()


name = data["results"][0]["name"]["first"]
last_name = data["results"][0]["name"]["last"]
country = data["results"][0]["location"]["country"]
gender = data["results"][0]["gender"]
email = data["results"][0]["email"]
phone = data["results"][0]["phone"]
age = data["results"][0]["dob"]["age"]

print("This is your new identity")
print(f"Name: {name}")
print(f"Last name: {last_name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Country: {country}")
print(f"Email: {email}")
print(f"Phone: {phone}")


