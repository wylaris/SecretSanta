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
    print("> Making a random list for {}".format(list))


def main():
    print("> Welcome to the Secret Santa Generator")
    stateChanger = input("> Do you want people to be paired or with different people?: ")
    people = input("> Please enter in the people you want to add.  Separate people with a ; : ")
    peopleList = people.split(';')
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
        differentPeople(list)
    print("> Goodbye and Merry Christmas!")


main()
