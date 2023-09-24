message = input()
words = message.split()
encoded_message = ""

for word in words:
    if len(word) < 3 or word.isspace():
        encoded_word = word
    else:
        first_char = chr(ord(word[0]) + 1)
        last_char = chr(ord(word[-1]) - 1)
        middle_chars = str(len(word) - 2)
        encoded_word = first_char + middle_chars + last_char
    encoded_message += encoded_word + " "

print(encoded_message.rstrip())
