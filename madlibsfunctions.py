def madlibsfunction():
    celebAction = input('Enter a verb...').lower()

    celebrity = input('Please enter the name of a celebrity...').title()

    gender = input('is that a he, she or they?').lower()

    animal = input('Please enter a type of animal...').lower()

    animalVerb = input('What is the animal doing...').lower()

    numberOfAnimals = int(input('How many of them are there?'))

    print ("%s " "%s " "are" " %s" " %s " "while %s %ss" % (numberOfAnimals, animal, animalVerb, celebrity, gender, celebAction))

madlibsfunction()
