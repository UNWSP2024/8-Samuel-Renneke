# Course Info
# Samuel Renneke, 3/16/2026

classes = {}
for i in range (1, 11):
    ID = input("What is the subject of the class you want to add? (ex. COS) ")
    class_type = input("What is the ID and name of the class you want to add? (ex. 2005 Python Programming) ")
    classes.setdefault(ID, []).append(class_type)

while True:
    showing_classes = input("What subject would you like to see classes for? ")
    print(classes[showing_classes])

    breaking = input("Would you like to see more classes (y/n)? ")
    if breaking != "y":
        break
