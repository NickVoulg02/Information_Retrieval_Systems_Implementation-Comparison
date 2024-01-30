import math
from warnings import simplefilter
import pandas as pd
import inverted_index

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

def idf_calculation(doc_num, term_dic):
    idf_result = []

    for value in term_dic.items():
        #print(value)                                                   #value[1][1] is the number of documents where the term appears
        idf_result.append(math.log10((doc_num / value[1][1]) + 1))
        

    return idf_result


inv = inverted_index.InvertedIndex()
file_len = {}
number_of_docs = 0


number_of_docs = inverted_index.main(inv, file_len, number_of_docs)

idf_values = idf_calculation(number_of_docs, inv.dictionary)  # calculate idf values for every token (how rare it is)
#print(idf_values)


vector_space = pd.DataFrame()  # vector space consisting of tokens and documents
# filling the vector space
for doc in file_len.items():
    #print(doc)
    list = []
    for token in inv.dictionary.items():
        detected = 0
        id = token[1][0]                                    # document id
        term = inv.Inv_index[id]                            # Inv_index record for the specific token
        for i in range(len(term)):                          # record for every doc the token appears in
            if term[i][0] == doc[0]:                        # checking if it appears in the doc we're currently checking
                # print(token[0])
                # print(doc[1])
                # print(term[i][1])                         # occurences in specific file
                x1 = math.log10((term[i][1] / doc[1])+1)    #logarithmically scaled frequency
                #print(x1)
                x2 = idf_values[id]
                # print(x2)
                list.append(x1 * x2)
                # print(x1*x2)
                detected = 1
        if detected == 0:
            list.append(0)
    doc_name = "doc" + str(doc[0])
    vector_space[doc_name] = list

print(vector_space)
vector_space.to_csv('vector_space2.csv', encoding='utf-8')
