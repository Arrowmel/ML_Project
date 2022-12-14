import sys
print("Python:{}".format(sys.version))
import scipy
print("Scipy:{}".format(scipy.__version__))
import numpy
print("Numpy:{}".format(numpy.__version__))
import matplotlib
print("Matplotlib:{}".format(matplot.__version__))
import pandas
print("Pandas:{}".format(pandas.__version__))
import sklearn
print("Sklearn:{}".format(sklearn.__version__))
import pandas 
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbours import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

#loading the data
url="http://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=read_csv(url,names=names)
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
pyplot.show()
dataset.hist()
pyplot.show()
scatter_matrix(datasets)
pyplot.show()
array=dataset.values
x=array[:,0:4]
y=array[:,4]
x_train,x_valudation,y_train,y_valudation=train_test_split(x,y,test_size=0,2,random_state=1)

model=[]
models.append(('LR',LogisticRegression(solver='liblinear',multi_class='ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC(gamma='auto')))

results=[]
names[]
for name,model in models:
  kfold=StratiedKFold(n_splits=10,random_state=1)
  cvresults=cross_val_score(model,x_train,Y_train,cv=kfold,scoring='accuracy')
  results.append(cv_results)
  names.append(name)
print('%s:%f(%f)'%(name,cv_results.mean(),cv_results.std()))
pyplot.boxplot(result,labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
model=SVC(gamma='auto')
model.fit(x_train,y_train)
predictions=model.predict(x_validation)
  
#evaluate out prediciton
print(accuracy_score(y_validation,predictions)
print(confusion_matrix(y_validation,predicitions))
print(classification_report(y_validation,predictions))
