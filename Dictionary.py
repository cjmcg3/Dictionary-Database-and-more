# Your names: Connor McGarry
#
#
#
#

# no other modules allowed
import random,time,sys


class Dictionary:

    '''The constructor takes the name of a dictionary,
        with N/A as the default name for an empty dictionary
        If name is unacceptable, end the code execution'''
    def __init__(self,name='N/A'):
        random.seed(8) 
        self.__name = name
        self.__index = 0
        try:  # checks if the input has a filename attached to it 
            self.__words = list(open(str(self.__name)).read().split()) # creates a list the of words in the filename dictionary 
            print('Load', name)
        except:  # if no filename but no user input, create empty list. End code in cases of user misinput 
            if name == 'N/A':
                self.__words = [] 
            else:
                print('File',name, 'does not exist!')
                sys.exit(0)


    '''Returns the name of the dictionary'''
    def get_name(self):
        return self.__name         


    '''if the dictionary is a file, return the length of said file
        otherwise, return the length of the unnamed dictionary list'''
    def get_size(self):
        try:
            f = open(str(self.__name), 'r')
            return (len(f.readlines()))  # return number of lines in file, in this case equals number of words
        except:
            return len(self.__words)


    '''gets a random sample of words from the requested dictionary'''
    def get_random_list(self,num_words):
        temp = []
        for i in range(num_words):
            random_word = random.choice(self.__words)  # each word is a random choice from dictionary
            temp.append(random_word)
        return temp


    '''returns steps taken to perform sorting'''
    def get_steps(self):
        return self.__steps

            
    '''inserts words from input dictionary to 'unsorted' dictionary '''
    def insert(self, words):
        for w in words.splitlines():  # splitlines puts the dictionary words into a list for appending, otherwise reads letter by letter
            self.__words.append(w)


    '''Handles printing words onscreen, and also conditionally displaying the score of scrabble words for app5'''
    def display(self, score = False):
        if not score:
            for word in self.__words:
                    print(word)  # prints words from the dictionary by default
        if score:  # if there is a score to be returned
            disp_num = []   # score list
            disp_word = []  # word list
            for num in self.__score:
                disp_num.append(num)
            for word in self.__words:
                disp_word.append(word)
            for i in range(len(self.__words)):
                print(disp_word[i],disp_num[i]) # prints the contents of the two lists side by side


    '''randomly shuffles a given list of words and returns time taken'''
    def shuffle(self):
        t1 = time.perf_counter() #capture time
        n=self.get_size()   # gets the length of the list/dictionary
        for out in range(n-1,0,-1): #outer loop (from n-1 to 1)
            index=random.randint(0,out)  # randomly selected index
            self.__words[out],self.__words[index]=self.__words[index],self.__words[out]  # swapping word locations
        t2 = time.perf_counter() #capture time
        return t2-t1

    
    '''returns the index of a word in a given dictionary'''
    def get_index(self):
        return self.__index


    '''Searches through open dictionary for a given word'''
    def lsearch(self,word):
        for x in self.__words:
            if word == self.__words[self.__index]:
                return True
                break
            else:
                self.__index += 1  # move up the indexes in the list until found
            if self.__index >= len(self.__words):
                self.__index = -1  # if its not in the list return -1
                return False
                break


    '''Binary search for a word in current dictionary
        If word is not found, return the index where it should be'''
    def bsearch(self,word):
        self.__steps = 0  # track steps taken, increses every step
        lower=0 
        upper = len(self.__words)-1 
        while lower <= upper:
            middle = lower + (upper - lower)//2 # sets index of middle of the dictionary
            midpoint = self.__words[middle]  # sets the middle word
            if midpoint == self.__words[middle]:
                self.__steps += 1
                self.__index = middle
                return True
                break
            elif midpoint > word:
                self.__steps += 1
                upper = middle - 1  # cuts off upper half of list
            elif midpoint < word:
                self.__steps += 1
                lower = middle + 1 # cuts off bottom half of list
            break
        self.__index = lower  # returns intended location of the word
        return False


    def selection_sort(self):    #provided to you
        """Perfom selection sort, must return the time it takes to sort the list of words
        Remark: Routine works 'in-place'"""
        t1 = time.perf_counter() #capture time
        n=self.get_size()
        for out in range(n-1):        #outer loop
            #find minimum between out+1 and n-1
            imin=out
            for i in range(out+1,n):  #inner loop
                if self.__words[i]<self.__words[imin]: 
                    imin=i #update  minimum index
            #swap (3 step here)
            temp=self.__words[imin]
            self.__words[imin]=self.__words[out]
            self.__words[out]=temp
        t2 = time.perf_counter() #capture time
        return t2-t1


    '''Insertion sort. Takes key words and shifts/swaps with neighboring items 
        according to size comparison, and repeat process
        returns time taken'''
    def insertion_sort(self):
        t1 = time.perf_counter()
        n=len(self.__words)  
        for out in range(1,n): #outer loop 
            temp=self.__words[out] # make a key word
            i=out
            while i>0 and self.__words[i-1]>temp: # if the smaller item is in higher locaton than larger
                self.__words[i]=self.__words[i-1] #swap key
                i=i-1
            self.__words[i]=temp #insertion and restart process
        t2 = time.perf_counter()
        return t2-t1


    '''Uses custom binary search to find the index of a word which
        is then used for insertion sort'''
    def enhanced_insertion_sort(self): 
        def binarySearch(word, lower, upper):  # create a binary search that accepts upper and lower bounds
            if lower > upper:
                return lower   # returns nonetype if coded like bsearch, so there cannot be a while loop, thus different format than previous
            mid = (lower + upper)//2
            middle = self.__words[mid]
            if middle < word:
                return binarySearch(word, mid+1, upper) # another way of cutting off bottom half of the list
            elif middle > word:
                return binarySearch(word, lower, mid-1) # another way of cutting off top half of the list
            else:
                return mid
        t1 = time.perf_counter()
        n = len(self.__words)   
        for word in range(1,n):   # practically regular insertion sort, but just calling new binary search funti
            temp = self.__words[word] 
            key = binarySearch(temp, 0, word-1)  # find the word in the dictionary
            for i in range(word, key, -1):  # insertion sort
                self.__words[i] = self.__words[i-1]
            self.__words[key] = temp       
        t2 = time.perf_counter()
        return t2-t1    




    '''Writes sorted dictionary into a new file'''
    def save(self, name):
        f = open(name, 'w')  # opens a new file
        for word in self.__words:
            f.write(word + '\n')  # writes words line by line
            for lines in name:
                lines.strip()!=''  # fixes some formatting issues
        f.close()
        print('Save', name)


    '''Compares words in a message to words in the corrosponding dictionary and place parenthesis around 
        incorrectly spelled words'''
    def spell_check(self, txt_name):
        temp = []
        punc = '''"!()-[]{};:"\,<>./?@#$%^&*_~"'''  # punctuation needed to ignore in text
        try:
            message = (open(txt_name).read())
        except:
            print('File',txt_name,'does not exist!')
            sys.exit(0)
        new_message = str(message)
        for word in new_message.split():
            if word not in temp:  # make sure that the same word isnt being put in parenthesis more than once ex...(((this)))
                temp.append(word)
        for word in temp:
            if (word.lower().rstrip(punc).lstrip(punc)) not in self.__words: # same concept
            #if not self.bsearch(word.lower().rstrip(punc).lstrip(punc)):  # if not found after stripping punctuation
                new_message = new_message.replace(word, str('('+word+')')) # replace the word with the same word with parenthesis around it
        print(new_message)    


    '''Returns a list of anagrams that exist in the given dictionary. Uses static method sort_word() to get a word and then 
        compares it to words in the initiated dictionary, and appends all correct anagrams  '''
    def anagram(self,word):
        anagrams = []
        scramble = str(self.sort_word(word))  # returns sorted word
        for x in self.__words:
            if len(word) == len(x):  # looks in the dictionary for all words the same length as the sorted word
                comparison = self.sort_word(x)  # sort the 'same length' words in the dictionary
                if comparison == scramble: # if the sorted words match 
                    anagrams.append(x)  # then append to the list
        return anagrams


    '''Asigns point values to letters in words. Changes the self.__score values which are returned in display()'''
    def compute_score_scrabble(self):
        self.__score = [] 
        one = ['e','a','i','o','n','r','t','l','s','u']
        two = ['d','g']
        three = ['b','c','m','p']
        four = ['f','h','v','w','y']
        five = ['k']
        eight = ['j','x']
        ten = ['q','z']

        letters = []  # temp list for letters in each word 
        for word in self.__words:
            score = 0 # reset the score each loop
            letters = list(word)  # splits each word into letters
            for letter in letters:
                if letter in one: 
                    score += 1
                if letter in two:
                    score += 2
                if letter in three:
                    score += 3
                if letter in four:
                    score += 4
                if letter in five:
                    score += 5      
                if letter in eight:
                    score += 8
                if letter in ten:
                    score += 10
            self.__score.append(score)  # appends total score of the word to list


    '''Uses an insertion sort to sort the anagrams and their scores while keeping them matching'''
    def score_sort(self):
        n=len(self.__score) 
        for out in range(1,n): #outer loop 
            temp = self.__score[out] # stores score for sorting
            temp2 = self.__words[out] # stores word for sorting
            i=out
            while i>0 and self.__score[i-1]>temp: # finctons the same as regular insertion sort, just sorting more things
                self.__score[i]=self.__score[i-1]
                self.__words[i]=self.__words[i-1] 
                i=i-1
            self.__score[i]=temp
            self.__words[i]=temp2 


    '''Finds all of the possible words given number of letters and legnth of code'''
    def crack_lock(self, lock):
        possibilities = Dictionary()
        temp = []
        # lock is a list of lists
        # c = options for each letter ^ length of code
        # need to generate 6 times by project requirements
        for i in range(6*len(lock[0])**len(lock)):  # generate 6*c locking combinations
            word = ''
            for combos in lock:
                trial = random.choice(combos)  # random letter from 1st rangeof options, 2nd, ect..
                word = word+trial # takes the random letters and combines them 
            #search = self.bsearch(word) # searches for the comnbined word 
            #if search == True:
            if word in self.__words: ######################################
                if word not in temp:  # if the word isnt in the list of combinations already
                    temp.append(word)
                    possibilities.insert(word)  # need to use insert????

        return possibilities  # need to return an instance of Dictionary, not a regular list, so how do i not use insert
        


    @staticmethod  # provided to you
    def get_word_combination(word, combs=['']):
        """ return a list that contains all the letter combinations (all length) of the input 'word' """
        if len(word) == 0:
            return combs
        head, tail = word[0], word[1:]
        combs = combs + list(map(lambda x: x+head, combs))
        return Dictionary.get_word_combination(tail, combs)

    

    @staticmethod
    def sort_word(word):  # to complete TAE AS EXAMPLE
        scramble = list(word)  # [t, a, e]
        n = len(scramble)
        for out in range(n-1):        #outer loop
        #find minimum between out+1 and n-1
            imin=out
            for i in range(out+1,n):  #inner loop
                if scramble[i]<scramble[imin]: 
                    imin=i #update  minimum index
                    
        #swap (3 step here)
            temp=scramble[imin]
            scramble[imin]=scramble[out]
            scramble[out]=temp
        
        return ''.join(scramble)  # returns ['aet']


    """ must return a string with letters included in 'word' that are now sorted"""





    

    
########################################################################
########################################################################


def main():

    ### step-1 test constructor
    name=input("Enter dictionary name (from file 'name'.txt): ")    
    dict1=Dictionary(name+".txt")

    ### step-2 test get_name, get_size, get_random_list        
    print('Name first dictionary:',dict1.get_name())   
    print('Size first dictionary:',dict1.get_size()) 
    print("Five random words:",end=" ")
    rlist=dict1.get_random_list(5) # 5 means the number of random words we want
    for w in rlist: print(w,end=" ")
    print("\n")

    ### step-3 test constructor again
    dict2=Dictionary()
    print('Name second dictionary:',dict2.get_name())
    
    ### step-4 test insert and display
    for w in rlist: dict2.insert(w)
    print('Display second dictionary:')
    dict2.display()

    ### step-5 test shuffle 
    t=dict2.shuffle()
    print('\nSecond dictionary shuffled in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()

    ### step-6 test linear search
    word="morning"
    print("\nLinear search for the word '%s' in second dictionary"%word)
    status=dict2.lsearch(word)
    print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))

    ### sort second using selection sort (provided to you)
    t=dict2.selection_sort()
    print('\nSecond dictionary sorted in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()


    ### step-7 test binary search (find it)
    word="morning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))

    # binary search (did no find it)
    word="ning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("'%s' is not found so it must be inserted at index %s"%(word,dict2.get_index()))
    

    


## call the main function if this file is directly executed
if __name__=="__main__":
    main()
