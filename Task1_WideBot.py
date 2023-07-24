class SpellChecker:
    def __init__(self, dictionary_file):
        self.dictionary = set()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):

        """
        function to Load a dictionary file into a set it takes
        The path to the file containing the dictionary.

        Time complexity: O(n)
        Space complexity: O(n)

        """
        # Initialize an empty set to store the words in the dictionary
        with open(dictionary_file, 'r') as f:
            for line in f:
                # Strip whitespace and add the word to the dictionary
                word = line.strip()
                self.dictionary.add(word)

    def check_spelling(self, word):

        """
        Check if a given word is present in the dictionary , it takes
        the word you want to check and return True if the word is in the dictionary, False otherwise.

        Time complexity: O(1)
        Space complexity: O(1)

        """
        if word in self.dictionary:
            return True
        else:
            return False

    def find_nearest_words(self, word):
        """
        Find the nearest four words to a given word if this word is not in the dictionary ,it takes
        the word and return a list with the nearst 2 words before and
        after this word in lexicographic order.

        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        # Convert the dictionary set to a list and append the new list
        sorted_words = list(self.dictionary)
        sorted_words.append(word)
        # Sort the words in the dictionary and find the index of the given word
        sorted_words = sorted(sorted_words)
        Index = sorted_words.index(word)

        # Initialize an empty list to store the nearest four words
        nearest_4_words = []
        # Append words from index before our word to the index after it.
        nearest_4_words.append(sorted_words[Index-2:Index+3])
        # Remove our word from the list to prevent it from appearing in the output
        nearest_4_words = [[x for x in inner_list if x != word] for inner_list in nearest_4_words]
        return nearest_4_words

    def add_word(self, word):
        """
        Add a new word to the loaded dictionary, it takes the word to add to the dictionary.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.dictionary.add(word)

    def run(self):
        # Enter a loop to make  user to enter a word
        while True:
            word = input('Please enter a word or type exit to end the run: ').lower()

            """ 
                If the word is 'exit', break out of the loop and exit the program
                Otherwise, if th word is exist then tell the user that 
                otherwise find the nearest four words to the given word and print them to the 
                console and also add this word to the dictionary
           
               Time complexity: O(n log n)
               Space complexity: O(n)
            """
            if word == 'exit':
                break

            else:
                flag = self.check_spelling(word)
                if flag:
                    print('Dictionary contains this word.\n')
                else:
                    print('Dictionary does not contain this word,The nearest four words are : ',self.find_nearest_words(word))
                    self.add_word(word)
                    print('Note that : This word added to the dictionary.\n')

if __name__ == '__main__':
    # run the program
    spell_checker = SpellChecker('C:/Users/Toshiba/Widebot Tasks/dictionary')
    spell_checker.run()