word = input("Please enter your word: ")
word = word.lower()  # 1
begin_a = word.startswith("a")  # 2
end_a = word.endswith("a")
contain_e = "e" in word
word_length = len(word)  # 3
if not begin_a and not end_a and contain_e == False:  # 4
    if word_length <= 4:  # 5
        print("The length of the word is short.")
    elif word_length <= 8 and word_length > 4:  # 6
        print("The length of the word is medium.")
    elif word_length > 8:  # 7
        print("The length of the word is long.")
if begin_a:
    print("You entered a word that begins with 'a'.")
elif end_a:
    print("You entered a word that ends with 'a'.")
elif contain_e:  # 8
    print("You entered a word that contatins 'e'.")  # 9
