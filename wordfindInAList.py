# '''
# You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random note.

# Your task is to write a function that, given a list of words and a note, finds and returns the word in the list that is scrambled inside the note, if any exists. If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

# Example:  
# words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
# note1 = "ctay"
# find(words, note1) => "cat"   (the letters do not have to be in order)  
  
# note2 = "bcanihjsrrrferet"
# find(words, note2) => "cat"   (the letters do not have to be together)  
  
# note3 = "tbaykkjlga"
# find(words, note3) => "-"     (the letters cannot be reused)  
  
# note4 = "bbbblkkjbaby"
# find(words, note4) => "baby"    
  
# note5 = "dad"
# find(words, note5) => "-"    
  
# note6 = "breadmaking"
# find(words, note6) => "bird"    

# note7 = "dadaa"
# find(words, note7) => "dada"    

# All Test Cases:
# find(words, note1) -> "cat"
# find(words, note2) -> "cat"
# find(words, note3) -> "-"
# find(words, note4) -> "baby"
# find(words, note5) -> "-"
# find(words, note6) -> "bird"
# find(words, note7) -> "dada"
  
# Complexity analysis variables:  
  
# W = number of words in `words`  
# S = maximal length of each word or of the note  
# '''

# # words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
# # note1 = "ctay"
# # note2 = "bcanihjsrrrferet"
# # note3 = "tbaykkjlga"
# # note4 = "bbbblkkjbaby"
# # note5 = "dad"
# # note6 = "breadmaking"
# # note7 = "dadaa"

from collections import Counter
def find(words, note1):
    
    frequencyCountGivenInput = Counter(note1) # 0(n)
        
    for item in words: # 0(m)
        # calculate frequency for the given input word list
        frequencyCountForWords = Counter(item) 
        count = 0

        for char in frequencyCountForWords: # 0(s)
            if frequencyCountGivenInput[char] < frequencyCountForWords[char]:
                break

            if frequencyCountGivenInput[char] >= frequencyCountForWords[char]:
                count += 1

            if count == len(frequencyCountForWords):
                return item
    return "-"

words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay" 
note2 = "bcanihjsrrrferet"
note3 = "tbaykkjlga"
note4 = "bbbblkkjbaby"
note5 = "dad"
note6 = "breadmaking"
note7 = "dadaa"
print(find(words,note1))
print(find(words,note2))
print(find(words,note3))
print(find(words,note4))
print(find(words,note5))
print(find(words,note6))
print(find(words,note7))
    
    
    