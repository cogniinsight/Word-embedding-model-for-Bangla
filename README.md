

**Word embedding model for Bangla**
-------------------------------

 The model can be found from the following link:
 Link:
 
The corpora for training the model has been collected from different sources, including prothom-alo news corpus, transcriptions of CRBLP speech corpus, Bangla textbook corpus, and wiki dump (wikidump accessed on 20th of July, 2016). It contains 84.25 millions of words, 3.2millions word types, and 7.5 millions of sentences. Please check the paper below for more details. 
 
 Can be used for many Bangla language specific NLP tasks. 
 
The model is trained using gemsim implementation of word2vec. Model training parameters include the following:

    gensim.models.Word2Vec(size=400, window=5, min_count=5, workers=40,seed=1,sample=1e-5,hs=1,negative=5,iter=30)

For tokenization the script `w2vtokenize.py` is used.

 How to use: 

    # Find the top ten most similar words of the word 'প্রধানমন্ত্রী'
    import gensim
    model = gensim.models.Word2Vec.load('palo_book_abp_news_bnwiki_W2V.model', binary=False)
    words=model.most_similar(positive=['প্রধানমন্ত্রী'], negative=[], topn=10)
    
    for w in words:
    	print w[0]
    ##Finding the word vector
    vector = model['প্রধানমন্ত্রী']

 Please cite the following paper if you are using this model:

*Firoj Alam, Shammur Absar Chowdhury and Sheak Rashed Haider Noori, Bidirectional LSTMs - CRFs Networks for Bangla POS Tagging, ICCIT 2016.*
