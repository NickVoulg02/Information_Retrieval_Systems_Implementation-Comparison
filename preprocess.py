import os
import csv

with open("C:/Users/nickv/Documents/information_retrieval/doc_col.tsv", 'wt', newline='', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(["doc_id", "doc"])
    for filename in os.listdir("C:/Users/nickv/Documents/information_retrieval/docs1"):
        with open(os.path.join("C:/Users/nickv/Documents/information_retrieval/docs1", filename), 'r') as f:     # open in readonly mode
            file = f.read().splitlines()
            passage = " "
            passage = passage.join(file)
            id = int(filename)
            tsv_writer.writerow([id, passage])


with open("C:/Users/nickv/Documents/information_retrieval/queries_20.tsv", 'wt', newline='\n', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    with open(os.path.join("C:/Users/nickv/Documents/information_retrieval/", 'Queries_20'), 'r') as f:     # open in readonly mode
            file = f.read().splitlines()
            id=0
            tsv_writer.writerow(["query_id", "query"])
            for x in file: 
                 x = x.upper()
                 tsv_writer.writerow([id, x])
                 id+=1



