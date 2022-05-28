# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgi import print_arguments


def read_file_content():
    # [assignment] Add your code here
    bg_file = open("./story.txt", "r")
    print(bg_file.read())
    
    return bg_file
    
def count_words(filename):
    file = read_file_content("./story.txt")
    #[assignment] Add your code here
dict = {}
for word in open("./story.txt").read().split() :
		if word in dict :
			dict [word] += 1
		else:
			dict [word] = 1

print (dict)