import math
import numpy
from warnings import simplefilter
from numpy.linalg import norm
import pandas as pd
import inverted_index
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def idf_calculation(doc_num, term_dic):
    idf_result = []

    for value in term_dic.items():
         idf_result.append(math.log10((doc_num/value[1][1])+1))

    return idf_result


def query_vec_calc(query, inv):
    query_tokens = query.upper().split()
    
    query_dic = {}
    for x in query_tokens:
        id = inv.dictionary.get(x)
        if id != None:
            if id[0] not in query_dic:
                query_dic[id[0]] = 1
                print(x)
            elif id[0] in query_dic:
                query_dic[id[0]] += 1

    query_list = []
    for token in inv.dictionary.items():
        id = token[1][0]

        if id in query_dic:
            #print(id)
            term_freq = query_dic.get(id)
            x1 = math.log10((term_freq/len(query_tokens))+1)
            #print(x1)
            x2 = idf_values[id]
            #print(x2)
            query_list.append(x1*x2)
        elif id not in query_dic:
            query_list.append(0)

    return query_list


def cosine_similarity(vector_space, query_vec):
    #cosine similarity between query vector and vector space
    for column in vector_space:
        doc_vec = vector_space.loc[:,column]
        c1 = numpy.dot(doc_vec,query_vec)
        c2 = (norm(doc_vec,2)*norm(query_vec,2))
        cosine = (c1/c2)
        if cosine > 0.1:
            print(column)
            print(cosine)


if __name__ == "__main__":
    inv = inverted_index.InvertedIndex()
    file_len = {}
    number_of_docs=0

    number_of_docs = inverted_index.main(inv,file_len,number_of_docs)

    idf_values = idf_calculation(number_of_docs, inv.dictionary)                               # calculate idf values for every token (how rare it is)
    #print(idf_values)

    vector_space = pd.DataFrame()                                                              # vector space consisting of tokens and documents
    # filling the vector space
    for doc in file_len.items():
        list = []
        for token in inv.dictionary.items():
            detected = 0
            id = token[1][0]
            term = inv.Inv_index[id]
            for i in range(len(term)):
                if term[i][0] == doc[0]:
                    #print(token[0])
                    #print(doc[1])
                    #print(term[i][1])
                    x1 = math.log10((term[i][1]/doc[1])+1)     # logarithmically scaled frequency
                    #print(x1)
                    x2 = idf_values[id]
                    #print(x2)
                    list.append(x1*x2)
                    #print(x1*x2)
                    detected = 1
            if detected == 0:
                list.append(0)
        doc_name = "doc"+str(doc[0])
        vector_space[doc_name] = list 

    #print(vector_space)


    #making a dictionary and token list for our query
    query = "Can one distinguish between the effects of mucus hypersecretion and infection on the submucosal glands of the respiratory tract in CF"
    query_list = query_vec_calc(query, inv)
    query_vec = pd.DataFrame({"query":query_list})

    #print(query_vec)

    #cosine_similarity(vector_space,query_vec)