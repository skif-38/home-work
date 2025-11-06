import json
import random

users = []
for _ in range(4):
    user = {}
    data = random.choice([""])
    user["name"] = random.choice(["emma", "sophia", "oliver", "liam", "ava", "mia"])
    user["surname"] = random.choice(["johnson", "williams", "brown", "jones", "garcia", "miller"])
    user["age"] = random.randint(18, 36)
    user["phone"] = f"89{random.randint(100000000, 999999999)}"
    users.append(user)

print(json.dumps(users))