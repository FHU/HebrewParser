import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn import tree
from sklearn import preprocessing
import pandas

class ClassifierTester:
	
	def StratifiedKFoldTest(self, classifier, dataset, labels, k):
		scores = cross_validation.cross_val_score(classifier, dataset, labels, cv=k)
		return scores.mean(), scores.std()*2 

	def LeaveOneOutTest(self, classifier, dataset, labels):
		loo = cross_validation.LeaveOneOut(len(dataset))
		scores = cross_validation.cross_val_score(classifier, dataset, labels, cv=loo)
		return scores.mean(), scores.std()*2

		
if __name__ == '__main__':
	# Load Dataset
	excel = pandas.ExcelFile("final_dataset.xlsx")
	parsedXlsx = excel.parse("data")
	
	leClass = preprocessing.LabelEncoder()
	leClass.fit(['J', 'E', 'D', 'P'])
	parsedXlsx['Classification'] = leClass.transform(parsedXlsx['Classification'])
	
	leGenre = preprocessing.LabelEncoder()
	leGenre.fit(['Genealogy', 'Narrative', 'Covenant', 'Blessing', 'Law'])
	parsedXlsx['Genre'] = leGenre.transform(parsedXlsx['Genre'])
	
	leName = preprocessing.LabelEncoder()
	leName.fit(['Y', 'N'])
	parsedXlsx['hasElohim'] = leName.transform(parsedXlsx['hasElohim'])
	parsedXlsx['hasYHWH'] = leName.transform(parsedXlsx['hasYHWH'])
	
	dataset = parsedXlsx.drop(['Classification'], axis=1).values
	labels = parsedXlsx['Classification'].values
	clf = tree.DecisionTreeClassifier()

	#Stratified K Fold 
	clfTester = ClassifierTester()
	meanAccuracy, stdAccuracy = clfTester.StratifiedKFoldTest(clf, dataset, labels, 10)
	print "10-Fold Crossvalidation"
	print "Accuracy\tStandard Deviation"
	print str(meanAccuracy) +"\t" + str(stdAccuracy)
	print ""
	'''
	#Leave One Out 
	meanAccuracy, stdAccuracy = clfTester.LeaveOneOutTest(clf, dataset, labels)
	print "Leave-One-Out Crossvalidation"
	print "Accuracy\tStandard Deviation"
	print str(meanAccuracy) +"\t" + str(stdAccuracy)
'''
