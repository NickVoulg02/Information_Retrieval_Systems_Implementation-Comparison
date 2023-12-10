import os
import csv

with open("C:/Users/nickv/Documents/information_retrieval/output.tsv", 'wt', newline='', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for filename in os.listdir("C:/Users/nickv/Documents/information_retrieval/docs1"):
        with open(os.path.join("C:/Users/nickv/Documents/information_retrieval/docs1", filename), 'r') as f:     # open in readonly mode
            file = f.read().splitlines()
            passage = " "
            passage = passage.join(file)
            id = int(filename)
            tsv_writer.writerow([id, passage])





