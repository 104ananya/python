message = input(">")
words = message.split(' ')
print(words)

emoji = {
    ":)": "đ",
    "':D": "đ",
    ":(": "âšī¸",
    "^_^": "đ",
    ":-O": "đŽ",
    "<3": "ī¸â¤ī¸",
}

output = ""
for i in words:
    output += emoji.get(i, i) + " "

print(output)