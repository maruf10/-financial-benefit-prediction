import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline
from pandas.plotting import scatter_matrix
data = pd.read_csv(r"C:\Users\maruf\Downloads\New folder\bank-additional\bank-additional\bank-additional-full.csv")
data.head()
data = pd.read_csv(r"C:\Users\maruf\Downloads\New folder\bank-additional\bank-additional\bank-additional-full.csv", sep=';')
data.head()
data_dict = data.T.to_dict().values()
vec = DictVectorizer()
signal_array = vec.fit_transform(data_dict).toarray()
feature_names = vec.get_feature_names()
df = pd.DataFrame(signal_array,columns=feature_names)
df.head()
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

X = signal_array[:,:-2]
X = np.hstack((X[:,:14],X[:,15:]))
y = signal_array[:,-1]
# Build a forest and compute the feature importances
forest = RandomForestClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %s (%f)" % (f + 1, feature_names[indices[f]], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()
ax = sns.regplot(x="age", y="y=yes", order=3, data=df, truncate=True)
ax = sns.regplot(x="campaign", y="y=yes", order=1, data=df, truncate=True)
df.loc[(df['campaign'] >15) & (df['y=yes']==1)]
ax = sns.regplot(x="emp.var.rate", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="nr.employed", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="age", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="duration", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="contact=telephone", y="y=yes", order=1, data=df,truncate=True)
ax = sns.regplot(x="cons.conf.idx", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="poutcome=nonexistent", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="education=unknown", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="euribor3m", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="housing=unknown", y="y=yes", order=1, data=df, truncate=True)
ax = sns.regplot(x="housing=yes", y="y=yes", order=1, data=df, truncate=True)
sum(df['y=yes'])/sum(df['campaign'])
print ("Nth Call \t Efficiency")
for i in range(1,30):
    goo = sum(df.loc[df['campaign']==i]['y=yes']) / float(df.loc[df['campaign'] >= i].shape[0])
    print (str((i))+" \t\t "+str(goo))
print("For age upto 30")
print ("Nth Call \t Efficiency")
for i in range(1,30):
    num = float(df[(df['age'] <= 30) & (df['campaign']==i) & (df['y=yes']==1)].shape[0])
    den = 1+float(df[(df['age'] <= 30) & (df['campaign'] >= i)].shape[0])
    print (str((i))+" \t\t "+str(num/den))
print("For age between 30-40")
print("Nth Call \t Efficiency")
for i in range(1,30):
    num = float(df[(df['age'] <= 40) & (df['age'] > 30) & (df['campaign']==i) & (df['y=yes']==1)].shape[0])
    den = 1+float(df[(df['age'] <= 40) & (df['age'] > 30) & (df['campaign'] >= i)].shape[0])
    print (str((i))+" \t\t "+str(num/den))
print("For age between 40-50")
print("Nth Call \t Efficiency")
for i in range(1,30):
    num = float(df[(df['age'] <= 50) & (df['age'] > 40) & (df['campaign']==i) & (df['y=yes']==1)].shape[0])
    den = 1+float(df[(df['age'] <= 50) & (df['age'] > 40) & (df['campaign'] >= i)].shape[0])
    print (str((i))+" \t\t "+str(num/den))
print("For age between 50-60")
print("Nth Call \t Efficiency")
for i in range(1,30):
    num = float(df[(df['age'] <= 60) & (df['age'] > 50) & (df['campaign']==i) & (df['y=yes']==1)].shape[0])
    den = 1+float(df[(df['age'] <= 60) & (df['age'] > 50) & (df['campaign'] >= i)].shape[0])
    print (str((i))+" \t\t "+str(num/den))
print("For age above 60")
print("Nth Call \t Efficiency")
for i in range(1,30):
    num = float(df[(df['age'] > 60) & (df['campaign']==i) & (df['y=yes']==1)].shape[0])
    den = float(df[(df['age'] > 60) & (df['campaign'] >= i)].shape[0])+1
    print (str((i))+" \t\t "+str(num/den))
total_calls = sum(df['campaign'])
print(total_calls)
extra_calls = sum(df[df['campaign']>6]['campaign']) - 6*df[df['campaign']>6].shape[0]
print(extra_calls)
reduction=100*extra_calls/total_calls
print(reduction)
total_sales=float(df[df['y=yes']==1].shape[0])
print(total_sales)
less_costly_sales=float(df[(df['campaign'] <= 6) & (df['y=yes']==1)].shape[0])
print(less_costly_sales)
sales_percent=100*less_costly_sales/total_sales
print(sales_percent)
                 
