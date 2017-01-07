import gensim, logging
import os
import datetime
import warnings
import optparse
import gensim
import aidrtokenize;
import smart_open

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

                
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    
    def __iter__(self):
        for fname in os.listdir(self.dirname):            
            with smart_open.smart_open(os.path.join(self.dirname, fname),"r",encoding='utf-8') as f:
                next(f)
                for line in f:
                    txt=""
                    yield txt
#                    try:
#                        #txt=aidrtokenize.tokenize(line)
#                    except Exception as e:
##                        print e
#                        continue
#                        pass
#                    yield txt

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    a = datetime.datetime.now().replace(microsecond=0)
    parser = optparse.OptionParser()
    parser.add_option('-i', action="store", dest="inputDir")
    parser.add_option('-m', action="store", dest="modelFile")
    options, args = parser.parse_args()
    
    inputDir=options.inputDir
    modelFile=options.modelFile
    base=os.path.basename(modelFile)
    path=os.path.dirname(os.path.abspath(modelFile))
    print (path)
    fname=os.path.splitext(base)[0];
    vocabFile = path+"/"+fname+"_vocab.txt"
    sentences = MySentences(inputDir) # a memory-friendly iterator
    #print sentences
    #print ("sent: "+str(sentences.index))
    model = gensim.models.Word2Vec(size=400, window=5, min_count=2, workers=40,seed=1,sample=1e-5,hs=1,negative=5,iter=30)
    model.build_vocab(sentences)    
    model.train(sentences)
    model.save_word2vec_format(modelFile,vocabFile,binary=False)
    model.save(modelFile)
    
    b = datetime.datetime.now().replace(microsecond=0)
    print "Time taken:"+str((b-a))
