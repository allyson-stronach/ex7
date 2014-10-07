word_file = open("twain.txt")

def main(word_file):

    word_count = {}

    for line in word_file:
        line = line.rstrip(" ")
        single_word = line.split()
        
        for word in single_word:
            word_count[word] = word_count.get(word, 0) + 1

    print(word_count)

    #count how many times each space-seperated word occurs in word_file

    #strip file by space

    #assign variables for dictionary keys and values
    #write a loop that gets and adds new values in the file to the dictionary

    #print counts to the screen using a dictionary

if __name__ == "__main__":
    main(word_file)

