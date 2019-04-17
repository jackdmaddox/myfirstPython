celebAction = input('Enter a verb...')
celebrity = input('Please enter the name of a celebrity...')
gender = input('is that a he, she or they?')
animal = input('Please enter a type of animal...')
animalVerb = input('What is the animal doing...')
numberOfAnimals = int(input('How many of them are there?'))

def fixCelebAction(celebAction):
    celebAction = celebAction.lower()
    return celebAction

def fixCelebrity(celebrity):
    celebrity = celebrity.title()
    return celebrity

def fixGender(gender):
    gender = gender.lower()
    return gender

def fixAnimal(animal):
    animal = animal.lower()
    return animal

def fixAnimalVerb(animalVerb):
    animalVerb = animalVerb.lower()
    return animalVerb
    

def madlibsfunction(celebAction, celebrity, gender, animal, animalVerb, numberOfAnimals):
    fixedAnimal = fixAnimal(animal)
    fixedAnimalVerb = fixAnimalVerb(animalVerb)
    fixedCelebrity = fixCelebrity(celebrity)
    fixedGender = fixGender(gender)
    fixedCelebAction = fixCelebAction(celebAction)

    return print ("%s " "%s " "are" " %s" " %s " "while %s %ss" % (numberOfAnimals, fixedAnimal, fixedAnimalVerb, fixedCelebrity, fixedGender, fixedCelebAction))


madlibsfunction(celebAction, celebrity, gender, animal, animalVerb, numberOfAnimals)
