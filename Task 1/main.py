# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filter_dog_owners" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filter_adults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
    {"id": '1', "name": 'John Smith', "age": 20, "hasDog": True},
    {"id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False},
    {"id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True},
    {"id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False},
    {"id": '5', "name": 'Alex John', "age": 25, "hasDog": True},
    {"id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True},
    {"id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True},
    {"id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False},
    {"id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True},
]


def filter_dog_owners(dict):
    has_dog = filter(lambda x: x['hasDog'] == True, dict)
    print(list(has_dog))
    return list(has_dog)


def filter_adults(dict):
    is_adult = filter(lambda x: x['age'] > 18, dict)
    print(list(is_adult))
    return list(is_adult)


filter_dog_owners(users)
filter_adults(users)
