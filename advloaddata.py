import sys
import csv
csv.field_size_limit(2147483647)
from preprocessing import Tokenizer, pad_sequences

# small = True
small = False
if small:
    textdatafolder = 'textdata_small/'
else:
    textdatafolder = 'textdata/'
            
class dataset:
    def __init__(self,filename,line=3):
        self.output = []
        self.content = []
        self.columns=line
        self.loadcsv(filename)
        
    def loadcsv(self, filename):
        reader = csv.reader(open(filename, "rt", encoding = "utf-8-sig"))
        count = 0
        for row in reader:
            if not row:
                continue
            if self.columns==2 and row[0].strip()!='':
                self.output.append(int(row[0].strip())-1)
                self.content.append((row[1]).lower())
            elif self.columns==3 and row[0].strip()!='':
                self.output.append(int(row[0].strip())-1)
                self.content.append((row[1] + " " + row[2]).lower())           
            elif self.columns==4 and row[0].strip()!='':
                self.output.append(int(row[0].strip())-1)
                self.content.append((row[1] + " " + row[2] + " " + row[3]).lower())       
def loaddata(i = 0):
    datanames = ['wikipedia_comments','ag_news','amazon_review_full','amazon_review_polarity','dbpedia','sogou_news','yahoo_answers','yelp_review_full','yelp_review_polarity','enron','blog-authorship-corpus']
    lines = [2,3,3,3,3,3,4,2,2,2,2]
    classes= [2,4,5,2,14,5,10,5,2,2,3]
    # if not 'blog' in datanames[i]:
    trainadd = textdatafolder+datanames[i]+'_csv/train.csv'
    adversarialadd = textdatafolder+datanames[i]+'_csv/adversarial.csv'
    testadd = textdatafolder+datanames[i]+'_csv/test.csv'
    traindata = dataset(trainadd,lines[i])
    adversarialdata = dataset(adversarialadd,lines[i])
    testdata = dataset(testadd,lines[i])
    return (traindata,adversarialdata,testdata,classes[i])
    # else:
    #     data = dataset()
    #     return (traindata,testdata,classes[i])

def loaddatawithtokenize(i = 0, nb_words = 20000, start_char = 1, oov_char=2, index_from=3, withraw = False, datalen = 500):
    (traindata,adversarialdata,testdata,numclass) = loaddata(i)
    rawtrain = traindata.content[:]
    rawadversarial = adversarialdata.content[:]
    rawtest = testdata.content[:]
    tokenizer = Tokenizer(lower=True)
    tokenizer.fit_on_texts(traindata.content + testdata.content)
    adversarialdata.content = tokenizer.texts_to_sequences(adversarialdata.content)
    traindata.content = tokenizer.texts_to_sequences(traindata.content)
    testdata.content  = tokenizer.texts_to_sequences(testdata.content)
    
    if start_char==None:
        adversarialdata.content = [[w + index_from for w in x] for x in adversarialdata.content]
        traindata.content = [[w + index_from for w in x] for x in traindata.content]
        testdata.content = [[w + index_from for w in x] for x in testdata.content]
    else:
        adversarialdata.content = [[start_char]+[w + index_from for w in x] for x in adversarialdata.content]
        traindata.content = [[start_char]+[w + index_from for w in x] for x in traindata.content]
        testdata.content = [[start_char]+[w + index_from for w in x] for x in testdata.content]

    adversarialdata.content = [[w if w < nb_words else oov_char for w in x] for x in adversarialdata.content]
    traindata.content = [[w if w < nb_words else oov_char for w in x] for x in traindata.content]
    testdata.content = [[w if w < nb_words else oov_char for w in x] for x in testdata.content]
    
    adversarialdata.content = pad_sequences(adversarialdata.content, maxlen=datalen)
    traindata.content = pad_sequences(traindata.content, maxlen=datalen)
    testdata.content = pad_sequences(testdata.content, maxlen=datalen)

    if withraw:
        return traindata,adversarialdata,testdata,tokenizer,numclass,rawtrain,rawadversarial,rawtest
    else:
        return traindata,adversarialdata,testdata,tokenizer,numclass
    
if __name__ == "__main__":
    (traindata,adversarialdata,testdata,numclass) = loaddata(9)
    print(len(traindata.output))
    # blogdata('textdata/blog-authorship-corpus_csv/blogtext.csv',2)