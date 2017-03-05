""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import random


def skip_first_part(text):
    """
    Takes the opened file to read as input and takes off the top part.

    """
    for line in text:
        line = line.replace("-"," ")
        line = line.replace("_"," ")
        if line.startswith('*** START'): #place where the Gutenburg Project starts the actual text
            break


def get_word_list(file_name, to_skip_or_not_to_skip):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.


    Takes the boolean 'to_skip_or_not_to_skip' to decide if the text is sent to the function skip_first_part
    to take off the header. This is just in case you are not using a Gutenburg project book

    """
    fin = open(file_name) #opening file
    histogram={} 
    if to_skip_or_not_to_skip == True:  #if I want to skip the header this is set to True
        skip_first_part(fin)
    for line in fin: #runs through lines of book file
        line = line.replace("-"," ") #takes out dashed, underscroes, numbers, whitespaces, and punctuation
        line = line.replace("_"," ")
        to_remove = string.punctuation + string.whitespace + '0123456789' 
        for word in line.split():
            word = word.strip(to_remove) #running through all words in each line 
            if word == 'God' or 'Lord':
                pass
            else:
                word = word.lower()
            histogram[word] = histogram.get(word, 0)+1
    return histogram


def get_top_n_words(filename, n, to_search_word_or_not, word_to_serach, get_random):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring

    takes parameters:
        filename to be opened
        n number of top words
        to_search_word_or_not is a boolean telling to serach a certain word or not
        word_to_search is the word you want to serach, (if serach or not is Flase, word to serach is None)
        get_random is a boolean telling to get a random word or not
    """

    histogram = get_word_list(filename, True)  #calls histogram file
    output = []
    for word,value in histogram.items():  #sorts words into new histogram that has value, word pairs to sort
        output.append((value,word))
    output.sort()
    output.reverse()  #sorting from greatest to least
    final_n_output = []

    if get_random == True:  #possibly sending getrandom funtion to get random words
        random_word = getrandom(histogram)
    else:
        random_word = None

    if to_search_word_or_not == True: #possibly sending getrandom funtion to get random words
        num_of_word = search_for_a_word(histogram, word_to_serach)
    else:
        num_of_word = None

    for i in range(n):
        final_n_output.append(output[i]) #making a final output list

    print(random_word)

    return final_n_output, num_of_word, random_word

def getrandom(hist):
    """
    takes histogram as input and gets a random word from the text
    
    Does NOT adjust for frequency

    """
    word, freq = random.choice(list(hist.items()))
    return word


def search_for_a_word(histogram, word):
    if word in histogram:
        return histogram[word]
    else:
        return 'Word Not Found'


def write_resutls_file(name_for_write_file, filename, top_n_words, to_search_word_or_not = False, word_to_search = None, get_random = False):
    """
    Makes a file in the same directory

    Take parameters:
        name_for_write is what you want to call the new file
        filename is the text you want to analyze
        to_search_word_or_not is a boolean telling to serach a certain word or not
        word_to_search is the word you want to serach, (if serach or not is Flase, word to serach is None)
        get_random is a boolean if you want to get a random word or not

    """
    name = '%s.txt' %name_for_write_file
    textfile = open(name, "w")
    top_n_words = get_top_n_words(filename, top_n_words , to_search_word_or_not, word_to_search, get_random)
    #getting histogram

    #printing into a text file
    if to_search_word_or_not == True:
        textfile.write('\n\n\n\t')
        textfile.write("THE RESULTS OF YOUR SEARCH:")
        textfile.write('The word %s is used %s times' %(word_to_search, str(top_n_words[1]))+ '\n\n')

    if get_random == True:
        textfile.write('\n\t\t')
        textfile.write("YOUR RANDOM WORD IS:  ")
        textfile.write(str(top_n_words[2]) + '\n\n')    

    for i in top_n_words[0]:
        textfile.write('The word:' + ' ' + str(i[1]) + '\n' + '\t' + 'is used' + ' '+ str(i[0]) + ' '+ 'times')
        textfile.write('\n\n')
    textfile.close()



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    write_resutls_file("Bible_Analysis", 'Bible.txt', 30, True, 'love', True)
