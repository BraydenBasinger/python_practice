
courses = ["bio", 'art', "history"]

for index, course in enumerate(courses):
    print(index, course)

courses_str = ", ".join(courses)

print(courses_str)

# tuples are immuatble

set1 = {1, 3, 4, 5}
set2 = {1, 3, 8, 9}

print(set1.intersection(set2))