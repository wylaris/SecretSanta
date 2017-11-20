def SamePerson(list):
    print("> Making a list for {}".format(list))

def differentPeople(list):
    print("> Making a list for {}".format(list))
def main():
    print("> Welcome to the Secret Santa Generator")
    stateChanger = input("> Do you want people to be paired or with different people?: ")
    people = input("> Please enter in the people you want to add.  Separate people with a ; : ")
    peopleList = people.split(';')
    if stateChanger.lower() == "yes":
        if len(peopleList) % 2 != 0:
            change = input("> This feature is only availabile for an even number of people.  Would you like to make the list with"
                  " different people?: ")
            if change.lower() == "yes":
                differentPeople(peopleList)
            else:
                print("> Goodbye and Merry Christmas!")
                quit()
        else:
            SamePerson(peopleList)
    else:
        pass

main()