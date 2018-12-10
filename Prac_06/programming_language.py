
class ProgrammingLanguage():
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        #Python, Dynamic Typing, Reflection=True, First appeared in 1991
        return ("{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year))
