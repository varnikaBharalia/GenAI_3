from typing import TypedDict

# Defining a TypedDict for a person
class Person(TypedDict):
    name: str
    age: int

# Creating an instance of the TypedDict
new_person: Person = {
    "name" : "Varun",
    "age" : 30
}

print(new_person)