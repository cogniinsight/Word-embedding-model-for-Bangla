

# Word embedding (word2vec) model for Bangla
-------------------------------
For many NLP tasks, we need linguistic resources (e.g. linguistically motivated features, dictionary) in order to design fundamental tools such as *parts-of-speech tagger*, *named entity recognizer*. Such resources are scarce and at the same time digital content, such as text, are growing very fast, can also partially be available. The idea is utilizes the source and design model can be useful in many Bangla language specific NLP tasks.

In order to design the [word embedding model](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiknYmBt6_RAhUCuxQKHa84ArsQFggiMAE&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWord_embedding&usg=AFQjCNEfLh8jgy4D59NSHg0p0saR50y5LA&sig2=haVtPU6KTAvFh-kyNrFsQA), one needs to have a large collection of text. For example, [google-embedding model (GoogleNews-vectors-negative300.bin.gz)](https://code.google.com/archive/p/word2vec/) contains 100 billion words. For Bangla, publicly available text data is not very large. One way is to collect is scrap the text data from the wab.
For this task, we have used several sources including prothom-alo news corpus, transcriptions of CRBLP speech corpus, Bangla textbook corpus, and wiki dump (wikidump accessed on 20th of July, 2016). It contains 84.25 millions of words, 3.2 millions word types, and 7.5 millions of sentences. Please check the paper below for more details.

Due to the license limitation, we can not publicly release this dataset.

## Prerequisites
* Python 2.7
* Gensim (Tested on 1.0.1)

## Data preparation for word2vec model training
Since data sources is different, therefore it is necessary to clean the data first (e.g., removing html tags). We are not including that step here.
Once data is cleaned, the follwing tool can be used to prepare the data for training word embedding model. It basically split the text into sentences and writes to a text file and also multiple files. The sentense delimeter include "?" and "\u0964" characters.
It also annotate all numbers into DIGIT tag.

Please check the Readme in **DataProcessor** module in order to run it. Here is an example,
```java
java -classpath dist/DataProcessor.jar dataprocessor.DataProcessor -i bn_data_files_list.txt -d bn_data_preprocessed/ -o bn_data_preprocessed.txt
```

## Model training parameter
For training the model there are many tools available. We have explored [word2vec](https://code.google.com/archive/p/word2vec/) and [gensim](https://radimrehurek.com/gensim/models/word2vec.html) implementation.

[word2vec](https://code.google.com/archive/p/word2vec/) implementation:
```bash
./word2vec -train bn_data_preprocessed.txt -output bn_w2v_model.txt -cbow 0 -size 300 -window 5 -negative 5 -hs 1 -sample 1e-4 -threads 40 -binary 0 -iter 15 -min-count 3 -save-vocab bn_w2v_model_vocab.txt
```

[gensim](https://radimrehurek.com/gensim/models/word2vec.html) implementation of word2vec. Model training parameters include the following:
```python
gensim.models.Word2Vec(size=300, window=5, min_count=3, workers=40,seed=1,cbow=0,sample=1e-4,hs=1,negative=5,iter=15)
```

## How to use:
**Find the top ten most similar words of the word 'প্রধানমন্ত্রী'**
```python
import gensim
model = gensim.models.Word2Vec.load('bn_w2v_model.bin')
words=model.most_similar(positive=['প্রধানমন্ত্রী'], negative=[], topn=10)

for w in words:
  print w[0]
# The most similar top ten words that we are getting are reasonable, as shown below.
মনমোহন
প্রধানমন্ত্রীর
হাসিনা
রাষ্ট্রপতি
হাসিনার
প্রধানমন্ত্রীকে
শান্তিপথে
বিদেশমন্ত্রী
মনমোহনের
এসডিএফের
#Finding the word vector
vector = model['প্রধানমন্ত্রী']
```
The trained model using [word2vec](https://code.google.com/archive/p/word2vec/) can be found [binary here](https://drive.google.com/file/d/0Bxa1keXJ_v7CMmNwdWlEUVJOdlU/view?usp=sharing) and [text version](https://drive.google.com/open?id=0Bxa1keXJ_v7CMmNwdWlEUVJOdlU).

The vocab size of the model is **436126** with 300-dimensional vectors.

Please cite the following paper if you are using this model:

*Firoj Alam, Shammur Absar Chowdhury and Sheak Rashed Haider Noori, Bidirectional LSTMs - CRFs Networks for Bangla POS Tagging, ICCIT 2016.*

```bib
@inproceedings{alam2016bidirectional,
  title={Bidirectional LSTMs—CRFs networks for bangla POS tagging},
  author={Alam, Firoj and Chowdhury, Shammur Absar and Noori, Sheak Rashed Haider},
  booktitle={19th International Conference on Computer and Information Technology (ICCIT), 2016},
  pages={377--382},
  year={2016},
  organization={IEEE}
}
```
