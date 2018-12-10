
from Prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python.reflection)

languageList = []
languageList = [ruby, python, visual_basic]

for element in languageList:
    if element.is_dynamic():
        print(element.name)
