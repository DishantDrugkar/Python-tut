marks = {
    "Harry" : 100,
    "Dishant" : 89,
    "Rohit" : 23,
    "Virat" : 101
}

print(marks)
# print(marks.get("Harry2")) # Return None
# print(marks["Harry2"]) # Returns an error

marks.update({"Dishant" : 95})
print(marks)