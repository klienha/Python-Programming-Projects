#This is an insurance company currently working on an application to keep track of which of their insured members have met their deductible for the
#year. An insured member is eligible for 100% coverage if they have met their deductible of $3000 or higher.
def fullCoverageClearance(dataDict={}):
	boolList = []
	if dataDict == {}:
		return None
	total = 0
	for k in dataDict:
		for j in dataDict[k]:
			for i in dataDict[k][j]:
				total += i
		if total < 3000:
			boolList.append(False)
		else:
			boolList.append(True)
		total = 0
	return boolList


def buildCoverageDictionary(paidList):
	newDict = {}
	for values in paidList:
		deductables = {}
		innerList = []
		for i in range(1, len(values)):
			innerList.append(values[i])
			
		deductables["Paid"] = innerList
		newDict[values[0]] = deductables
	return newDict

def createNewCoverageList(namesList=[], paymentList=[]):
	if len(namesList) == 0 or len(paymentList) == 0:
		return None
	newList = []
	for i in range(len(namesList)):
		innerList = []
		innerList.append(namesList[i])
		for j in range(len(paymentList[i])):
			innerList.append(paymentList[i][j])
		newList.append(innerList)
	return newList

def eligibility(*args):
	clearedList = []
	if len(args) == 2:
		newList = createNewCoverageList(args[0], args[1])
		newDict = buildCoverageDictionary(newList)
		boolList = fullCoverageClearance(newDict)
	if len(args) == 1:
		if type(args[0]) == list:
			newDict = buildCoverageDictionary(args[0])
			boolList = fullCoverageClearance(newDict)
		if type(args[0]) == dict:
			boolList = fullCoverageClearance(args[0])
	
	return boolList
