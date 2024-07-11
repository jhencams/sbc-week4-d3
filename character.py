input_text = input("Enter a sentence: ")

def process_characters(input_text):
    char_list = []
    for char in input_text:
        char_list.append(char)
    return char_list

char_list = process_characters(input_text)

print(char_list)