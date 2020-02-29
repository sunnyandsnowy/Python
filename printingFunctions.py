def printModels(unprintedDesigns, completedModels):
	while unprintedDesigns:
		currentDesign = unprintedDesigns.pop()
		print("Printing model: " + currentDesign)
		completedModels.append(currentDesign)
		
def showCompletedModels(completedModels):
	print("\nThe following models have been printed:")
	for completedModel in completedModels:
		print(completedModel)
		
