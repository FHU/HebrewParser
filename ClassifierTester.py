import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

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
	irisDataset = datasets.load_iris()
	dataset = irisDataset.data
	labels = irisDataset.target 
	clf = svm.SVC(kernel='linear', C=1) 

	#Stratified K Fold 
	clfTester = ClassifierTester()
	meanAccuracy, stdAccuracy = clfTester.StratifiedKFoldTest(clf, dataset, labels, 10)
	print "10-Fold Crossvalidation"
	print "Accuracy\tStandard Deviation"
	print str(meanAccuracy) +"\t" + str(stdAccuracy)
	print ""
	
	#Leave One Out 
	meanAccuracy, stdAccuracy = clfTester.LeaveOneOutTest(clf, dataset, labels)
	print "Leave-One-Out Crossvalidation"
	print "Accuracy\tStandard Deviation"
	print str(meanAccuracy) +"\t" + str(stdAccuracy)

