import math
import numpy
from numpy.linalg import norm
import pandas as pd
import vector_space_model
import matplotlib.pyplot as plt


def query_vec_calc(query, inv):
    query_tokens = query.upper().split()

    query_dic = {}
    for x in query_tokens:
        id = inv.dictionary.get(x)                      
        if id != None:                               # query word exists in inverted index dictionary
            if id[0] not in query_dic:
                query_dic[id[0]] = 1                 # word id has been added to query dictionary
                #print(x)
            elif id[0] in query_dic:
                query_dic[id[0]] += 1                # number of occurences inside of query 

    #print(query_dic)

    query_list = []
    for token in inv.dictionary.items():
        id = token[1][0]                                            # token id

        if id in query_dic:
            # print(id)
            term_freq = query_dic.get(id)                           # token occurences inside of query
            x1 = math.log10((term_freq / len(query_tokens)) + 1)
            # print(x1)
            x2 = vector_space_model.idf_values[id]
            # print(x2)
            query_list.append(x1 * x2)
        elif id not in query_dic:
            query_list.append(0)

    return query_list


def cosine_similarity(vector_space, query_vec):
    # cosine similarity between document and query vectors
    result = []
    for column in vector_space:
        doc_vec = vector_space.loc[:, column]
        c1 = numpy.dot(doc_vec, query_vec)
        c2 = (norm(doc_vec, 2) * norm(query_vec, 2))
        cosine = (c1 / c2)
        if cosine>0:
            result.append([column,cosine.item()])
            # print (cosine)
            # print(column)
    return result

if __name__ == "__main__":
    vector_space = pd.read_csv("vector_space2.csv", index_col=0)

    #opening query and relevant answers list
    f = open("Queries_20", "r")
    file = f.read().splitlines()
    queries =[]
    for line in file:
        queries.append(line)                        # queries list includes every line from Queries_20
    
    f.close()

    f = open("Relevant_20", "r")
    file = f.read().splitlines()
    relevant_docs = []
    for line in file:
        line=line.split()
        list = []
        for num in line:
            num = int(num)
            list.append('doc'+str(num))
        relevant_docs.append(list)                  # relevant_docs list includes every line from Relevant_20


    # creating query dictionary and vectors
    query_vec = pd.DataFrame()
    for query in queries:
        query_list = query_vec_calc(query, vector_space_model.inv)
        query_name = str(queries.index(query))
        #print(query_name)
        query_vec[query_name] = query_list
    
    #print(query_vec)
    
    
    #Mean Average Precision
    avg_pr_list = []
    length = len(query_vec.columns[0:])

    for i in range(length):
        retrieved_docs = cosine_similarity(vector_space, query_vec.iloc[:,i])       #first column
        retrieved_docs.sort(key=lambda ret:ret[1], reverse=True)
        retrieved_docs_filtered = retrieved_docs[:100]
        # for x in range(len(retrieved_docs_filtered)):
        #     print(retrieved_docs_filtered[x][0])

        precision_at_k = []
        true_positives = 0
        
        for doc in retrieved_docs_filtered:
            if(doc[0] in relevant_docs[i]):
                true_positives+=1
                precision_at_k.append(true_positives/(retrieved_docs_filtered.index(doc)+1))   
        
        #print(precision_at_k)
    
        average_precision = 0
        for x in range(len(precision_at_k)):
                average_precision += precision_at_k[x]

        average_precision = average_precision/len(relevant_docs[i])
        print(average_precision)

        avg_pr_list.append(average_precision)

    mean_average_precision = sum(avg_pr_list)/length
    print("Mean Average Precision:" + str(mean_average_precision))
    plt.xticks(numpy.arange(len(avg_pr_list)), numpy.arange(1, len(avg_pr_list)+1))
    ypoints = numpy.array(avg_pr_list)
    plt.xlabel("Query ID")
    plt.ylabel("Average Precision for VSM")
    plt.plot(ypoints)
    plt.show()
    

   

    # #Mean Reciprocal Rank
    # mean_rep_rank = 0
    # length = len(query_vec.columns[0:])
    # list=[]
    # for i in range(length):
    
    #     retrieved_docs = cosine_similarity(vector_space, query_vec.iloc[:,i])       #first column
    #     retrieved_docs.sort(key=lambda ret:ret[1], reverse=True)
    #     #retrieved_docs_filtered = retrieved_docs[:250]
    #     #print(retrieved_docs_filtered)

    #     for doc in retrieved_docs:
    #         if(doc[0] in relevant_docs[i]):
    #             value = retrieved_docs.index(doc)+1
    #             #print(value)
    #             break
    #     mean_rep_rank += 1/value
    #     list.append(mean_rep_rank)
        
    # mean_rep_rank = mean_rep_rank/length
    # print("Mean Reciprocal Rank:" + str(mean_rep_rank))
