import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        word_code = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters are valid.")
        generate_phonetic()
    else:
        print(word_code)


generate_phonetic()




