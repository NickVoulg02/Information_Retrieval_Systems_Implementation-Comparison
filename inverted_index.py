import os

class InvertedIndex:

    def __init__(self, doc):
        self.doc = doc
        self.dict = []


    def Tokenization(self):
        words= []
        for x in range(len(self.doc)):
            words.append(self.doc[x])
              
        return words
            
    
    def Inverted_Index(self, id):
        Inv_index = {}
        tokenlist = self.Tokenization()
        for x in range(len(tokenlist)):
            if Inv_index.get(tokenlist[x]) == None:
                Inv_index[tokenlist[x]] = [1, [[id,1], [x+1]]]

            else:
                temp1 = Inv_index.get(tokenlist[x])
                temp1[1][0][1]+=1
                temp1[1][1].append(x+1)

        return Inv_index



if __name__ == "__main__":
            filename = "00001"
    #for filename in os.listdir("C:/Users/nickv/Documents/information_retrieval/docs"):
       #with open(os.path.join("C:/Users/nickv/Documents/information_retrieval/docs", filename), 'r') as f: # open in readonly mode
            file = open(filename, 'r').read().splitlines()
            id = int(filename)
            inv = InvertedIndex(file)
            #print(inv.Tokenization())
            inv_index = inv.Inverted_Index(id)
            print(inv_index.get("PSEUDOMONAS"))
    
    #Inv_index[0] = number of articles it appears in
    #Inv_index[1][0] = id of article, number of appearances in specific article
    #Inv_index 
    
    
