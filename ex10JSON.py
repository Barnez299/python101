import json

with open('users.txt') as f:
    data = json.load(f)
    # data = json.dumps(data, indent=2) uncomment this to see JSON format printed

# print(type(data))

for user in data['users']:
   print(f"Name: {user['name']} --> Email: {user['email']}")

# for user in data['users']:
#     print(user indent=2)