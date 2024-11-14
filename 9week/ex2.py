import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as font_manager

w=pd.read_csv('moving_keyword.csv',encoding='utf-8')
print(w, end="\n\n")
print(w.head(10),end="\n\n")

w_n = w.iloc[:,1:5]
print(w_n,end="\n\n")
w_cor=w_n.corr(method='pearson')
print(w_cor,end="\n\n")
    
font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
sns.pairplot(w_n)   #산점도 그림

plt.figure(figsize= (10,7))
sns.heatmap(w_cor,annot=True,cmap='Blues')  #산관행절도=heatmap
plt.show()