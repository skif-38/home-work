import json
import random


def input_user() -> dict:
    user = {}
    for value in [ "имя", "фамилию", "возраст", "номер телефона"]:
        user[value] = input(f"Введите {value}:\n>> ")
    return user


def create_random_users(num_of_users: int) -> list:
    users = []
    for _ in range(num_of_users):
        user = {}
        user["name"] = random.choice(["emma", "sophia", "oliver", "liam", "ava", "mia"])
        user["surname"] = random.choice(["johnson", "williams", "brown", "jones", "garcia", "miller"])
        user["age"] = random.randint(18, 36)
        user["phone"] = f"89{random.randint(100000000, 999999999)}"
        users.append(user)
    return users


def dumps_json_to_file(data, file_name: str = "data.json") -> None:
    with open(file_name, "w") as f:
        f.write(json.dumps(data, indent=4))


def loads_json_from_file(file_name: str = "data.json") -> list[dict]:
    with open(file_name, "r") as f:
        return json.loads(f.read())


def main():
    users = create_random_users(10)
    users.append(input_user())
    dumps_json_to_file(users)
    data = loads_json_from_file()
    print(*[key.ljust(10) for key in (data[1]).keys()])
    print(*[" ".join([str(value).ljust(10) for value in user.values()]) for user in data], sep="\n")


if __name__ == "__main__":
    main()