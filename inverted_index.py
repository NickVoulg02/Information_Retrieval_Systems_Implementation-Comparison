class InvertedIndex:

    def __init__(self, doc):
        self.doc = doc
        self.dict = []


    def Tokenization(self):
        words= []
        for x in range(len(self.doc)):
            words.append(self.doc[x])
              
        return words
            
    
    def Inverted_Index(self):
        Inv_index = {}
        tokenlist = self.Tokenization()
        for x in range(len(tokenlist)):
            if Inv_index.get(tokenlist[x]) == None:
                Inv_index[tokenlist[x]] = 1
                

            else:
                Inv_index[tokenlist[x]]+=1

        return Inv_index



if __name__ == "__main__":
    file = open("00001", 'r').read().splitlines()
    inv = InvertedIndex(file)
    #print(inv.Tokenization())
    print(inv.Inverted_Index())
    
    