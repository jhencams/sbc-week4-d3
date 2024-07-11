sentence_list = []

input_text = input("Enter a paragraph: ")

def process_sentences(input_text):
    current_sentence = ''
    for char in input_text:
        current_sentence += char
        if char in '.!?':
            sentence_list.append(current_sentence)
            current_sentence = ''
    if current_sentence:
        sentence_list.append(current_sentence)

process_sentences(input_text)

print(sentence_list)