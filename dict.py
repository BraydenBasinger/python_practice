
dictionary = {"name": "brayden", "random": "tehe", "other": "blah"}
dictionary["name"] = "bob"

popped_var = dictionary.pop("random")

print(dictionary.get("name"))
print(popped_var)

for key, value in dictionary.items():
    print(key, value)