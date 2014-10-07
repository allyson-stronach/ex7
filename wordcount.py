word_file = open("twain.txt")

def main(word_file):

    word_count = {}

    for line in word_file:
        
        alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        #line = line.rstrip(to fill with something)
        #strip file by space
        line = line.rstrip(" ")
        line_words = line.split()

        for i in range(len(line_words)):
            #count = 0
            word = line_words[i]
            for char in word:
                print word, char

                if char not in alph:
                    print "%s is baaaad" % char
                    new_word = word.replace(char, "")
                    line_words[i] = new_word
                    #char = word.replace(word[count], "")#DELETE the THING
                    #count += 1
                




        
        print line_words

        #count how many times each space-seperated word occurs in word_file
        # for word in single_word:
        #     #assign variables for dictionary keys and values
        #     #write a loop that gets and adds new values in the file to the dictionary
        #     word_count[word] = word_count.get(word, 0) + 1

    #print counts to the screen using a dictionary
    #print(word_count)

# Some words are counted separately due to punctuation. Remove punctuation so that they appear as the same word in the output.
if __name__ == "__main__":
    main(word_file)

