import pandas as pd
import numpy as np

filepath="quiz1_1.xlsx"
df_science = pd.read_excel(filepath, 'py_science')
df_sense = pd.read_excel(filepath, 'py_sense')
df_opinion = pd.read_excel(filepath, 'py_opinion')
df_mind = pd.read_excel(filepath, 'py_mind')


df_science['Sinif'] = "science"
df_sense['Sinif'] = "sense"
df_opinion['Sinif'] = "opinion"
df_mind['Sinif'] = "mind"

df_science.replace("girmedi",np.nan,inplace=True)
df_sense.replace("girmedi",np.nan,inplace=True)
df_opinion.replace("girmedi",np.nan,inplace=True)
df_mind.replace("girmedi",np.nan,inplace=True)

data_concat = pd.concat([df_science,df_sense,df_mind,df_opinion],axis=0,sort=False)
print(data_concat)
#1.sinava kac kisi girmis
filter1 = data_concat.D.isnull() & data_concat.Y.isnull() & data_concat.B.isnull()
filtered_data = data_concat[filter1]
print(filtered_data.Sinif.count(),"students were not in the exam")

#D,Y ve B olanlar

filter2 = data_concat.D.isnull()  | data_concat.Y.isnull() | data_concat.B.isnull()
filtered_dataDYB = data_concat[filter2]
print("Students with D,Y,B :",data_concat.Sinif.count()-filtered_dataDYB.Sinif.count())
#D ve Y olanlar

filter3=data_concat.D.notnull() &data_concat.Y.notnull() &  data_concat.B.isnull()
filtered_dataDY= data_concat[filter3]
print("Students with only D and Y:",filtered_dataDY.Sinif.count())

#sinif ortalamalari
science_mean = df_science.D.mean()
print("Mean of science class: ", science_mean)
mind_mean = df_mind.D.mean()
print("Mean of mind class: ", mind_mean)
sense_mean = df_sense.D.mean()
print("Mean of sense class: ", sense_mean)
opinion_mean = df_opinion.D.mean()
print("Mean of opinion class: ", opinion_mean)
all_mean = data_concat.D.mean()
print("Mean of all classes: ", all_mean)
#en basarili sinif
allDataframesMeans={"science":science_mean, "mind":mind_mean,"sense":sense_mean,"opinion":opinion_mean}
successfullClass=max(allDataframesMeans, key=allDataframesMeans.get)
print('Most succesfull class is',successfullClass,'and its mean is',allDataframesMeans[successfullClass])

#her sinifin en basarili 3 kisisi

