import os
import nltk
from nltk.corpus import stopwords


#nltk.download('stopwords')
stopping = []
for x in stopwords.words('english'):        # A stop word is a commonly used word that a search engine has been programmed to ignore
    stopping.append(x.upper())


class InvertedIndex:

    def __init__(self):
        self.dictionary = {}                # a dictionary of all the words used in the articles, along with an id
                                            # and a number of total articles they appear in
        self.dic_id = -1                    # used for the token ids in the dictionary
        self.Inv_index = []                 # contains article id and number of occurences of token in said article                                         


    def Tokenization(self, doc):
        words= []
        for x in range(len(doc)):
            if doc[x].isdigit() == False:                                   # removing every number from dictionary
                words.append(doc[x])

        return words


    def Inverted_Index(self, id, doc):
        length=0                                                            # length variable only considers terms that aren't stopwords
        tokenlist = self.Tokenization(doc)                                  # a list of every word in the article
        for x in range(len(tokenlist)):
            if tokenlist[x] not in stopping:                                # checking for stopwords
                length+=1                                                 
                if self.dictionary.get(tokenlist[x]) == None:
                    self.dic_id+=1
                    self.dictionary[tokenlist[x]] = [self.dic_id, 1]
                    self.Inv_index.append([[id , 1]])

                elif self.dictionary.get(tokenlist[x]) != None:
                    token_id = self.dictionary.get(tokenlist[x])[0]
                    if self.Inv_index[token_id][-1][0] == id:               # checking if we're still in the same article by article id
                        temp1 = self.Inv_index[token_id][-1]
                        temp1[1]+=1
                    else:
                        self.dictionary.get(tokenlist[x])[1]+=1
                        self.Inv_index[token_id].append([id , 1])


        return length


def main(inv, file_len, number_of_docs):
    cwd = os.getcwd()                                          # open working directory
    cwd = cwd + "\docs"
    #print(cwd)
    for filename in os.listdir(cwd):
         with open(os.path.join(cwd, filename), 'r') as f:     # open in readonly mode
             file = f.read().splitlines()
             id = int(filename)                                # id depends on filename
             number_of_docs+=1
             file_len[id] = inv.Inverted_Index(id, file)

    return number_of_docs
