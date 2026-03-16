# Word Separator
# Samuel Renneke, 3/9/2026

def word_separator(sentence):

    new_sentence = sentence[0]

    for letter in sentence[1:]:
        if letter.isupper():
            new_sentence += " " + letter.lower()
        else:
            new_sentence += letter

    return new_sentence.strip()

# Example usage
if __name__=="__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)
