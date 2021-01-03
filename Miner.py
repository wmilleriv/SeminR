import os
import SentenceTree

#import PyPDF2 implement reading from pdf later
TEST_FILE_PATH = "E:/Chinese/Stories/test.txt" #remove all instances of this constant later
TEST_WORD_BANK_PATH = "E:/Chinese/Stories/known.txt"
FULL_STOP =u'。'
COMMA =u'，'
 
#Get the text and add it to a string. Add support for pdfs and seperating Chinese later
def get_text(file_path):
    #check if file is present
    if os.path.isfile(file_path):
        #open text file in read modecd
        text_file = open(file_path, "r", encoding='utf 8')
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()
    
        return data
    return FileNotFoundError

#seperate text into phrases delimited by 。
#seperate known words delimited by ,
def get_delimited_phrases(text, delimiter):
    
    phrase_list = []
    phrase =""
    for character in text:
        if character == delimiter:
            phrase_list.append(phrase)
            phrase=""
        else:
            phrase = phrase + character
    return phrase_list

def assign_readability_score(raw_sentence, known_words):
    readability = 0
    for word in known_words:
        readability = readability + raw_sentence.count(word)
    readability = readability / len(raw_sentence)
    sentence = SentenceTree.Sentence(raw_sentence, readability)

    return sentence



def main():

    root = None
    tree = SentenceTree.Tree()
    a = get_text(TEST_FILE_PATH)
    b = get_delimited_phrases(a, FULL_STOP)
    a = get_text(TEST_WORD_BANK_PATH)
    c = get_delimited_phrases(a, COMMA)

    for phrase in b:
        sentence = assign_readability_score(phrase, c)
        if root == None:
            root = tree.insert(root, sentence)
            print(root)
        else:
            tree.insert(root, sentence)
    
    print(tree.traverseInorder(root))

if __name__ == "__main__":
    main()