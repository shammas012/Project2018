# Author: Mohamed Shammas Mohamed Ali Manaf 
# Date : 2018-04-08
# Description : Analyse the Iris Data Set.
#References : https://stackoverflow.com/questions/1025379/decimal-alignment-formatting-in-python
#			  https://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-trailing-newline-in-python
#
def DisplayDataSet():
	with open('Data\IrisData.csv') as input:
			#iterate through each line in the file
		for line in input:
			#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
			#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
			print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))

def LengthAnalysis():
	with open('Data\IrisData.csv') as input:
	#iterate through each line in the file
		sepalLength = 0.00
		petalLength = 0.00
		#totalCount = 0.00, minimumSepalLength = 0.00, minimumPetalLength = 0.00
		for line in input:
			#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
			#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
			sepalLength += float('{}'.format(line.split(',')[0]))
			petalLength += float('{}'.format(line.split(',')[2]))
			totalCount += 1
			print('{}  {}  {}'.format(sepalLength,petalLength,totalCount))
			print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))

def SepalAnalysis():
	with open('Data\IrisData.csv') as input:
		#iterate through each line in the file
		totalSepalLength = 0.00;	totalSepalWidth = 0.00;	totalCount = 0
		minimumSepalLength = 100.00; 	minimumSepalwidth = 100.00;
		maxSepalLength = 0.00;	maxSepalWidth = 0.00
		minSepalLengthSpecies = ""; maxSepalLengthSpecies = ""
		minSepalWidthSpecies = ""; maxSepalWidthSpecies = ""
		for line in input:
		#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
		#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
			currentSepalLength = float('{}'.format(line.split(',')[0]))
			currentSepalWidth = float('{}'.format(line.split(',')[1]))

			if currentSepalLength < minimumSepalLength:
				minSepalLengthSpecies = line.split(',')[4].rstrip()
				minimumSepalLength = currentSepalLength
			if currentSepalLength > maxSepalLength:
				maxSepalLengthSpecies = line.split(',')[4].rstrip()
				maxSepalLength = currentSepalLength
			if currentSepalWidth < minimumSepalwidth:
				minSepalWidthSpecies = line.split(',')[4].rstrip()
				minimumSepalwidth = currentSepalLength
			if currentSepalWidth > maxSepalWidth:
				maxSepalWidthSpecies = line.split(',')[4].rstrip()
				maxSepalWidth = currentSepalWidth	

			totalSepalLength += currentSepalLength
			totalSepalWidth += currentSepalWidth
			totalCount += 1
			#print('{}  {}  {}'.format(sepalLength,sepalWidth,totalCount))
			#print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
		print("minimum Sepal length species is flower : {} with length {} cms".format(minSepalLengthSpecies,minimumSepalLength))
		print("maximum Sepal length species is flower : {} with length {} cms".format(maxSepalLengthSpecies,maxSepalLength))
		print("minimum Sepal width species is flower : {} with width {} cms".format(minSepalWidthSpecies,minimumSepalwidth))
		print("maximum Sepal width species is flower : {} with width {} cms".format(maxSepalWidthSpecies,maxSepalWidth))
		print("The Arithmetic Mean of Sepal Length for all flowers from Iris Data Set is {}: ".format(totalSepalLength/totalCount))
		print("The Arithmetic Mean of Sepal Width for all flowers from Iris Data Set is {}: ".format(totalSepalWidth/totalCount))


def DisplayOptions():
	print ("1. Press 1 to View the DataSet")
	print ("2. Press 2 to See the Sepal Analysis")
	print ("3. Press 3 to see teh Petal Analysis")
	print ("5. Press 5 to exit the application")
	#print "Please choose from an option above:"
	#print "Please choose from an option above:"
DisplayOptions()
# userInput = int(input("Please choose from the options above:"))
userInput = 2
while userInput != 5:
	if userInput > 0 and userInput <= 4:
		if userInput == 1:
			DisplayDataSet()
		elif userInput == 2:
			SepalAnalysis()
	
	# elif userInput == 3:
    # 	print("PL")
	# elif userInput == 4:
    # 	print("Mapping")
	# elif userInput == 5:
    # 	print("Exit")
	DisplayOptions()
	userInput = int(input("Please choose from the options above:"))
