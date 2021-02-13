import morse_code_data as morsecode
import string

word = []


class MorseCode:

    def __init__(self):
        pass

    def get_input(self):
        global word
        word =[]
        user_input = input('Please enter a string to be converted into morse code: ').upper()

        is_true = True
        for letter in user_input:
            if letter in string.punctuation:
                print("This string contains punctuation")

                is_true = False
                mc.get_input()
            else:
                if is_true:
                    word.append(letter)
        return word

    def translate_word(self, word_data):
        output_list = [morsecode.code[letter] for letter in word_data]
        separator = ""
        print(separator.join(output_list))
        print(*word_data, sep=" ")


mc = MorseCode()

is_on = True
while is_on:
    mc.get_input()
    mc.translate_word(word)
    check = input('Continue? (Type anything to continue or Type 0 to stop) ')
    if check.lower() == "0":
        print("Thank you for using this program!")
        is_on = False
    else:
        continue






