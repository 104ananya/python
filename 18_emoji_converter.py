message = input(">")
words = message.split(' ')
print(words)

emoji = {
    ":)": "😊",
    "':D": "😃",
    ":(": "☹️",
    "^_^": "😄",
    ":-O": "😮",
    "<3": "️❤️",
}

output = ""
for i in words:
    output += emoji.get(i, i) + " "

print(output)