word_list = []

def process_words(input_text):
    current_word = ''
    for char in input_text:
        if char == ',':
            if current_word:
                word_list.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word:
        word_list.append(current_word)

input_text = input("Enter a sentence: ")
process_words(input_text)

print(word_list)
