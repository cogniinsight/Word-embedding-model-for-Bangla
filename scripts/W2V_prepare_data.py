import gensim, logging
import os
import datetime
import warnings
import optparse
import gensim
import w2vtokenize;
import smart_open
import codecs

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

                
def getdata(dirname,outfile):
    #fopen = open(outfile, "wb","utf8");
    fopen = codecs.open(outfile, "w", "utf-8")
    for fname in os.listdir(dirname):            
        with smart_open.smart_open(os.path.join(dirname, fname),"r",encoding='utf-8') as f:
            next(f)
            for line in f:
                txt=""
                try:
                    st=""                    
                    txt=w2vtokenize.tokenize(line)
                    for w in txt:
                        st=st+" "+w.decode('utf-8')
                    print st
                    fopen.write(st)
                except Exception as e:
                        print e
                        pass
    fopen.close

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    a = datetime.datetime.now().replace(microsecond=0)
    parser = optparse.OptionParser()
    parser.add_option('-i', action="store", dest="inputDir")
    parser.add_option('-o', action="store", dest="outFile")
    options, args = parser.parse_args()
    
    inputDir=options.inputDir
    outFile=options.outFile

    getdata(inputDir,outFile) # a memory-friendly iterator
    
    b = datetime.datetime.now().replace(microsecond=0)
    print "Time taken:"+str((b-a))
