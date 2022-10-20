#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

print()
print()

string = "Lorem: ipsum dolor sit amet, consectetur adipiscing elit."

text_indentation(string)
print()
print()

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sollicitudin ultrices nisl at tincidunt. Donec tempor dictum libero vitae cursus. Ut feugiat augue vel fringilla fringilla. Quisque viverra dolor tellus, scelerisque varius nisi accumsan eget. Pellentesque consequat ultrices lobortis. Pellentesque turpis diam, congue ac consequat a, dapibus et sem. Nulla sed libero velit. Fusce pellentesque a mi quis hendrerit. Etiam iaculis velit non massa tincidunt,"

text_indentation(string)
print()
print()


string = "Hello Holbie"

text_indentation(string)
print("--")
print("--")


string = "   Hello Holbie   "
text_indentation(string)

print("--")
print("--")



string = "  hello,    fine:  dating??   it's ok,,,,.  bye?"
text_indentation(string)

print("--")
print("--")

string = "1        .2         3.     end:"
text_indentation(string)

print("--")
print("--")

string = "..::??"
text_indentation(string)

print("--")
print("--")

string = "ssssssss, sssssssss. ssssssssssss."
text_indentation(string)


print("--")
print("--")
string = "ssssssss, sssssssss. ssssssssssss.       "
text_indentation(string)


print("--")
print("--")


string = 13
try:
    text_indentation(string)
except Exception as e:
    print(e)

string = float('inf')
try:
    text_indentation(string)
except Exception as e:
    print(e)

string = float('NaN')
try:
    text_indentation(string)
except Exception as e:
    print(e)

string = [1, 2, 3]
try:
    text_indentation(string)
except Exception as e:
    print(e)

string = {"hola", "hola"}

try:
    text_indentation(string)
except Exception as e:
    print(e)

string = 3.5

try:
    text_indentation(string)
except Exception as e:
    print(e)


print("--")
print("--")
string = ""

text_indentation(string)
