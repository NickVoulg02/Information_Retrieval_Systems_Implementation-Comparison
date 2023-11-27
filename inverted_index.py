import os
import nltk
import math
from nltk.corpus import stopwords    


#nltk.download('stopwords')
stopping = []
for x in stopwords.words('english'):        # A stop word is a commonly used word that a search engine has been programmed to ignore
    stopping.append(x.upper())


class InvertedIndex:

    def __init__(self):
        self.dictionary = {}                # a dictionary of all the words used in the articles, along with an id and a number of articles they appear in
        self.dic_id = -1                    # used for the token ids in the dictionary
        self.Inv_index = []                 # contains article id, number of appearance of token in said article, word appearance positions 


    def Tokenization(self, doc):
        words= []
        for x in range(len(doc)):
            words.append(doc[x])
              
        return words
  
    
    def Inverted_Index(self, id, doc):
        tokenlist = self.Tokenization(doc)                              # a list of every word in the article
        for x in range(len(tokenlist)):
            if tokenlist[x] not in stopping:                            # removing stopwords
                if self.dictionary.get(tokenlist[x]) == None:
                    self.dic_id+=1
                    self.dictionary[tokenlist[x]] = [self.dic_id, 1]
                    self.Inv_index.append([[id , 1]])
                    #self.Inv_index.append([[id , 1, [x+1]]])

                elif self.dictionary.get(tokenlist[x]) != None:
                    token_id = self.dictionary.get(tokenlist[x])[0]         
                    if self.Inv_index[token_id][-1][0] == id:               # checking if we're still in the same article by article id
                        temp1 = self.Inv_index[token_id][-1]
                        temp1[1]+=1
                        #temp1[2].append(x+1)
                    else:
                        self.dictionary.get(tokenlist[x])[1]+=1
                        self.Inv_index[token_id].append([id , 1])
                        #self.Inv_index[token_id].append([id , 1, [x+1]])
                     

        return self.Inv_index

def idf_calculation(doc_num, term_dic):
    idf_result = []

    for value in term_dic.items():
         idf_result.append(math.log10((doc_num/value[1][1])+1))

    return idf_result


def main(inv, file_len, number_of_docs):
    for filename in os.listdir("C:/Users/nickv/Documents/information_retrieval/docs"):
         with open(os.path.join("C:/Users/nickv/Documents/information_retrieval/docs", filename), 'r') as f:     # open in readonly mode
             file = f.read().splitlines()
             id = int(filename)                                                                                  # id depends on filename
             file_len[id] = len(file)
             number_of_docs+=1    
             inv.Inverted_Index(id, file) 
    
    return number_of_docs

 
    

































  
    # first document only
    # list1 = []
    # for token in inv.dictionary.items():
    #     detected = 0
    #     id = token[1][0]
    #     term = inv.Inv_index[id]
    #     for i in range(len(term)):
    #         if term[i][0] == 1:
    #                  detected = 1
    #                  #print(term[i])
    #                  x1 = (term[i][1]/file_len.get(1))
    #                  #print(x1)
    #                  x2=idf_values[id]
    #                  #print(x2)
    #                  list1.append(x1*x2)
    #     if detected == 0:
    #         list1.append(0)
    # #print(list)
    # vector_space = pd.DataFrame()
    # x = list(file_len.keys())
    # vector_space[x[0]] =  list1
    # print(vector_space)

    # #print(list)
    # vector_space = pd.DataFrame({"doc1": list})
    # print(vector_space.loc[0:20])
    
    