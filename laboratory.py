class Person:
    def __init__(self, name):

        self.name = name

people = []

people.append(Person("Jeff"))
people.append(Person("Tom"))

def weave(actor, target, attribute):
    actor.attribute = target.attribute