import nltk
import numpy as np
import pandas as pd
import math
import re
# =============================================================================
# read document
# =============================================================================
doc1 = open("/home/helmisatria/FALAH/Teks Mining/DataPRTFIDF/1.txt","r")
doc2 = open("/home/helmisatria/FALAH/Teks Mining/DataPRTFIDF/2.txt","r")
doc3 = open("/home/helmisatria/FALAH/Teks Mining/DataPRTFIDF/3.txt","r")
doc4 = open("/home/helmisatria/FALAH/Teks Mining/DataPRTFIDF/4.txt","r")
doc5 = open("/home/helmisatria/FALAH/Teks Mining/DataPRTFIDF/5.txt","r")
lema1 = []
lema2 = []
lema3 = []
lema4 = []
lema5 = []
# =============================================================================
# tokenisasi lowercase dan stopwords
# =============================================================================
for i in doc1 :
    i = re.sub('[--.()/!@#$,"123456789]', '', i) #for delete not string character
    lema1 += (nltk.word_tokenize(i.lower())) #line.lower untuk mengubah bentuk huruf menjadi lowercase
print(sorted(set(lema1),key = str.lower)) #sorted(set(lema),key = str.lower) untuk sorting huruf dari yang paling kecil
#set(lema) untuk menampilkan hanya huruf unik
for j in doc2 :
    j = re.sub('[--.()/!@#$,"123456789]', '', j) #for delete not string character
    lema2 += (nltk.word_tokenize(j.lower())) #line.lower untuk mengubah bentuk huruf menjadi lowercase
print(sorted(set(lema2),key = str.lower)) #sorted(set(lema),key = str.lower) untuk sorting huruf dari yang paling kecil
#set(lema) untuk menampilkan hanya huruf unik
for k in doc3 :
    k = re.sub('[--.()/!@#$,"123456789]', '', k) #for delete not string character
    lema3 += (nltk.word_tokenize(k.lower())) #line.lower untuk mengubah bentuk huruf menjadi lowercase
print(sorted(set(lema3),key = str.lower)) #sorted(set(lema),key = str.lower) untuk sorting huruf dari yang paling kecil
#set(lema) untuk menampilkan hanya huruf unik
for l in doc4 :
    l = re.sub('[--.()/!@#$,"123456789]', '', l) #for delete not string character
    lema4 += (nltk.word_tokenize(l.lower())) #line.lower untuk mengubah bentuk huruf menjadi lowercase
print(sorted(set(lema4),key = str.lower)) #sorted(set(lema),key = str.lower) untuk sorting huruf dari yang paling kecil
#set(lema) untuk menampilkan hanya huruf unik
for m in doc5 :
    m = re.sub('[--.()/!@#$,"123456789]', '', m) #for delete not string character
    lema5 += (nltk.word_tokenize(m.lower())) #line.lower untuk mengubah bentuk huruf menjadi lowercase
print(sorted(set(lema5),key = str.lower)) #sorted(set(lema),key = str.lower) untuk sorting huruf dari yang paling kecil
#set(lema) untuk menampilkan hanya huruf unik
# =============================================================================
# stemming
# =============================================================================
from nltk.stem.porter import PorterStemmer
stemming = PorterStemmer()
stemm1 = []
stemm2 = []
stemm3 = []
stemm4 = []
stemm5 = []
for a in range(len(lema1)) :
    stemm1.append(stemming.stem(lema1[a]))
for b in range(len(lema2)) :
    stemm2.append(stemming.stem(lema2[b]))
for c in range(len(lema3)) :
    stemm3.append(stemming.stem(lema3[c]))
for d in range(len(lema4)) :
    stemm4.append(stemming.stem(lema4[d]))
for e in range(len(lema5)) :
    stemm5.append(stemming.stem(lema5[e]))
allStemm = set(stemm1+stemm2+stemm3+stemm4+stemm5)
allVocabAllDoc = (stemm1+stemm2+stemm3+stemm4+stemm5)


# =============================================================================
# try
# =============================================================================
# =============================================================================
# TF
# =============================================================================
count1 = []
count2 = []
count3 = []
count4 = []
count5 = []
for i, valuez in enumerate(allStemm):
    count1.append(stemm1.count(valuez))
    count2.append(stemm2.count(valuez))
    count3.append(stemm3.count(valuez))
    count4.append(stemm4.count(valuez))
    count5.append(stemm5.count(valuez))
    
tf1 = []
tf2=[]
tf3=[]
tf4=[]
tf5=[]
for i in range(len(count1)):
    tf1.append(count1[i]/len(stemm1))
for i in range(len(count2)):
    tf2.append(count2[i]/len(stemm2))
for i in range(len(count3)):
    tf3.append(count3[i]/len(stemm3))
for i in range(len(count4)):
    tf4.append(count4[i]/len(stemm4))
for i in range(len(count5)):
    tf5.append(count5[i]/len(stemm5))

rows = np.array([
                 tf1, 
                 tf2,
                 tf3,
                 tf4,
                 tf5
                ])
columns = []
indeks = ['1','2', '3','4','5']

df = pd.DataFrame(rows,columns=allStemm, index=indeks)
# =============================================================================
# IDF
# =============================================================================
IDFcountWordAllDoc = []
for i, valuez in enumerate(allStemm):
    IDFcountWordAllDoc.append(np.log(5/allVocabAllDoc.count(valuez)))

z1 = np.vstack(allStemm)
z2 = np.vstack(IDFcountWordAllDoc)

zrowsIDF = np.array([
        z1,
        z2
        ])
    
# =============================================================================
# reshapeRowsIDF = nsp.reshape(rowsIDF, )
# =============================================================================
    
dfidf = pd.DataFrame({ 'Vocab' : np.array(list(allStemm)), 'IDF' : IDFcountWordAllDoc})
# =============================================================================
# xlsx
# =============================================================================
path = 'PR 20Feb Result_1301154577_KARTINI NURFALAH-PR TF IDF.xlsx'
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name="TF")
dfidf.to_excel(writer, sheet_name='IDF')
writer.save()
writer.close()