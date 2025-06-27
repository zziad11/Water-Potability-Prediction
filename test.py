import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from scipy.stats.mstats import winsorize
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv(r"D:\Water_Data.csv")

print(df.head())
print (df.shape)


Potability_count = df['Potability'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(Potability_count, labels=Potability_count.index, autopct='%.1f%%', colors=plt.cm.Paired(range(len(Potability_count))))
#plt.show() 


plt.figure(figsize=(10, 6))
sns.histplot(df['ph'], bins=30, kde=True, color='blue')
plt.title('Ph')
plt.xlabel('ph')
plt.ylabel('Frequency')



plt.figure(figsize=(10, 6))
sns.histplot(df['Hardness'], bins=30, kde=True, color='blue')
plt.title('Hardness')
plt.xlabel('Hardness')
plt.ylabel('Frequency')
plt.show()
