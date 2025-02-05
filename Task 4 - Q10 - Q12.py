def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence

def check_list(word_string, word):
    found="No"
    word_list = split_sentence(word_string)
    for x in word_list:
        if x == word:
            found = "Yes"
            break
    return found
            
    
def reverse_sentence(word_string):
    reverse_list=[]
    word_list = split_sentence(word_string)
    for i in range(len(word_list)-1,-1,-1):
        reverse_list += [word_list[i]]
    return reverse_list


def output_list(new_list):
    string = ""
    for i in new_list:
        string = string + i
        string = string + " "
    return string

#main
word_string = input("Enter a sentence:")
word = input("Enter the word to search in the sentence:")
print(output_list((split_sentence(word_string))))
print(output_list(reverse_sentence(word_string)))
print(check_list(word_string, word))





      
