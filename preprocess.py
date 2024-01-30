import os
import csv

cwd = os.getcwd()                                          # open working directory
docs = cwd + "\docs"

with open(cwd+"/doc_col.tsv", 'wt', newline='', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(["doc_id", "doc"])
    for filename in os.listdir(docs):
        with open(os.path.join(docs, filename), 'r') as f:     # open in readonly mode
            file = f.read().splitlines()
            passage = " "
            passage = passage.join(file)
            id = int(filename)
            tsv_writer.writerow([id, passage])


with open(cwd+"/queries_20.tsv", 'wt', newline='\n', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    with open(os.path.join(cwd, 'Queries_20'), 'r') as f:     # open in readonly mode
            file = f.read().splitlines()
            id=0
            for x in file: 
                 x = x.upper()
                 tsv_writer.writerow([id, x])
                 id+=1



