import random


def SamePerson(list):
    dictionary = dict()
    print("> Making a paried list for ", list)
    for i in range(0, len(list), 2):
        dictionary[list[i]] = list[i+1]
        print(list[i], "'s secret Santa is ", list[i+1])
        dictionary[list[i+1]] = list[i]
        print(list[i+1], "'s secret Santa is ", list[i])
    save = input("> Do you want this to be saved to a SecretSanta.txt file?: ")
    if save.lower() == "yes":
        file = open("SecretSanta.txt","w")
        for key in dictionary:
            file.write(key + "'s secret Santa is " + dictionary[key] + "\n")
        file.close()
    print(dictionary)


def differentPeople(list):
    dictionary = dict()
    initialList = list[:]
    print("> Making a random list for {}".format(list))
    while len(initialList) != 0:
        dictionary[initialList[0]] = "No one"
        initialList.pop(0)
    while "No one" in dictionary.values():
        index = random.randint(0, (len(list)-1))
        if list[index] not in dictionary.values():
            for key in dictionary:
                if dictionary[key] == "No one" and key != list[index] and (list[index] not in dictionary.values()):
                    dictionary[key] = list[index]
    print(dictionary)
    save = input("> Do you want this to be saved to a SecretSanta.txt file?: ")
    if save.lower() == "yes":
        file = open("SecretSanta.txt", "w")
        for key in dictionary:
            file.write(key + "'s secret Santa is " + dictionary[key] + "\n")
        file.close()

def main():
    print("> Welcome to the Secret Santa Generator")
    stateChanger = input("> Do you want people to be paired or with different people?: ")
    people = input("> Please enter in the people you want to add.  Separate people with a ; : ")
    if people != "":
        peopleList = people.split(';')
        if len(peopleList) > 1:
            if (stateChanger.lower() == "paired") or (stateChanger.lower() == "yes"):
                if len(peopleList) % 2 != 0:
                    change = input(
                        "> This feature is only available for an even number of people.  Would you like to make the list with"
                        " different people?: ")
                    if change.lower() == "yes":
                        differentPeople(peopleList)
                    else:
                        print("> Goodbye and Merry Christmas!")
                        quit()
                else:
                    SamePerson(peopleList)
            else:
                differentPeople(peopleList)
        else:
            print("> You'll have a blue Christmas alone! ")
    print("> Goodbye and Merry Christmas!")


main()
