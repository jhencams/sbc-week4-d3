def custom_tokenize(word):
    prefixes = ["un", "in", "dis", "re", "pre"]
    suffixes = ["ing", "ed", "ly", "s", "ful"]

    for prefix in prefixes:
        if word.startswith(prefix):
            if len(prefix) == 2:
                return [prefix, "##" + word[len(prefix):]]
            elif len(prefix) == 3:
                return [prefix, "###" + word[len(prefix):]]
    
    for suffix in suffixes:
        if word.endswith(suffix):
            if len(suffix) == 2:
                return [suffix, word[:-len(suffix)] + "##"]
            elif len(suffix) == 3:
                return [suffix, word[:-len(suffix)] + "###"]

    return [word]

word = input("Enter a word: ")

tokens = custom_tokenize(word)

print(tokens)
