import numpy as np
name = 'SUBJ'
data_dir="/home/juncsu/Code/Data/CapsData/%s/test.tsv" % name
data_dir1="/home/juncsu/Code/Data/Temp/%s/test_results.tsv" % name

with open(file=data_dir,mode="r",encoding="utf-8") as f:
    text=f.readlines()
    y_true=[]
    for i,t in enumerate(text):
        if i == 0:
            continue
        elif t.split("\t")!=0 and t!="\n":
            y_true.append(int(t.split("\t")[1]))
        else:
            pass

with open(file=data_dir1,mode="r",encoding="utf-8") as f:
    result=f.readlines()
    y_pred=[]
    for l in result:
        l=list(map(float,l.split("\t")))
        y_pred.append(np.argmax(l))

assert len(y_true) == len(y_pred)

from sklearn import metrics
# 混淆矩阵
print("Confusion Matrix...")
cm = metrics.confusion_matrix(y_true, y_pred)
from sklearn.metrics import classification_report
#target_names = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
print('-'*23+name+'-'*23)
print(classification_report(y_true, y_pred))#, target_names=target_names))

