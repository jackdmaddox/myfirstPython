person = input("What is your name? ")
subject = input("What is your favorite subject? ")

def fix_name(person):
    person = person.upper()
    return person

def fix_subject(subject):
    subject = subject.lower()
    return subject

def make_madlib(person, subject):
    fixed_name = fix_name(person)
    fixed_subject = fix_subject(subject)
    return print ("Your name is %s and your favorite subject is %s" % (fixed_name, fixed_subject))

make_madlib(person, subject)