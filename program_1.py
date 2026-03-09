# Initials
# Samuel Renneke, 3/9/2026

def initials_generator(personsName):

    personsInitials = ''
    nameList = personsName.split(' ')
    for name in nameList:
        personsInitials += name[0]

    return personsInitials.strip()

# Example usage
if __name__=="__main__":
    personsName = input('Enter the users full name: first, middle, and last: ')

    initials = initials_generator(personsName)

    print(initials)
