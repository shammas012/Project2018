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

def SpeciesAnalysis():
	with open('Data\IrisData.csv') as input:
			#iterate through each line in the file
			setosaTotalSepalLength = 0.00;	setosaTotalSepalWidth = 0.00;	setosaTotalCount = 0
			setosaMinimumSepalLength = 100.00; 	setosaMinimumSepalwidth = 100.00;
			setosaMaxSepalLength = 0.00;	setosaMaxSepalWidth = 0.00
			setosaMinSepalLengthSpecies = ""; setosaMaxSepalLengthSpecies = ""
			setosaMinSepalWidthSpecies = ""; setosaMaxSepalWidthSpecies = ""


			versiTotalSepalLength = 0.00;	versiTotalSepalWidth = 0.00;	versiTotalCount = 0
			versiMinimumSepalLength = 100.00; 	versiMinimumSepalwidth = 100.00;
			versiMaxSepalLength = 0.00;	versiMaxSepalWidth = 0.00
			versiMinSepalLengthSpecies = ""; versiMaxSepalLengthSpecies = ""
			versiMinSepalWidthSpecies = ""; versiMaxSepalWidthSpecies = ""

			virginicaTotalSepalLength = 0.00;	virginicaTotalSepalWidth = 0.00;	virginicaTotalCount = 0
			virginicaMinimumSepalLength = 100.00; 	virginicaMinimumSepalwidth = 100.00;
			virginicaMaxSepalLength = 0.00;	virginicaMaxSepalWidth = 0.00
			virginicaMinSepalLengthSpecies = ""; virginicaMaxSepalLengthSpecies = ""
			virginicaMinSepalWidthSpecies = ""; virginicaMaxSepalWidthSpecies = ""

			setosaTotalPetalLength = 0.00;	setosaTotalPetalWidth = 0.00;	setosaTotalCount = 0
			setosaMinimumPetalLength = 100.00; 	setosaMinimumPetalwidth = 100.00;
			setosaMaxPetalLength = 0.00;	setosaMaxPetalWidth = 0.00
			setosaMinPetalLengthSpecies = ""; setosaMaxPetalLengthSpecies = ""
			setosaMinPetalWidthSpecies = ""; setosaMaxPetalWidthSpecies = ""


			versiTotalPetalLength = 0.00;	versiTotalPetalWidth = 0.00;	versiTotalCount = 0
			versiMinimumPetalLength = 100.00; 	versiMinimumPetalwidth = 100.00;
			versiMaxPetalLength = 0.00;	versiMaxPetalWidth = 0.00
			versiMinPetalLengthSpecies = ""; versiMaxPetalLengthSpecies = ""
			versiMinPetalWidthSpecies = ""; versiMaxPetalWidthSpecies = ""

			virginicaTotalPetalLength = 0.00;	virginicaTotalPetalWidth = 0.00;	virginicaTotalCount = 0
			virginicaMinimumPetalLength = 100.00; 	virginicaMinimumPetalwidth = 100.00;
			virginicaMaxPetalLength = 0.00;	virginicaMaxPetalWidth = 0.00
			virginicaMinPetalLengthSpecies = ""; virginicaMaxPetalLengthSpecies = ""
			virginicaMinPetalWidthSpecies = ""; virginicaMaxPetalWidthSpecies = ""

			for line in input:
			#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
			#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
				currentSepalLength = float('{}'.format(line.split(',')[0]))
				currentSepalWidth = float('{}'.format(line.split(',')[1]))
				currentPetalLength = float('{}'.format(line.split(',')[2]))
				currentPetalWidth = float('{}'.format(line.split(',')[3]))
				currentSpecies = line.split(',')[4].rstrip()
				if currentSpecies == 'Iris-setosa':
					if currentSepalLength < setosaMinimumSepalLength:
						setosaMinSepalLengthSpecies = line.split(',')[4].rstrip()
						setosaMinimumSepalLength = currentSepalLength
					if currentSepalLength > setosaMaxSepalLength:
						setosaMaxSepalLengthSpecies = line.split(',')[4].rstrip()
						setosaMaxSepalLength = currentSepalLength
					if currentSepalWidth < setosaMinimumSepalwidth:
						setosaMinSepalWidthSpecies = line.split(',')[4].rstrip()
						setosaMinimumSepalwidth = currentSepalWidth
					if currentSepalWidth > setosaMaxSepalWidth:
						setosaMaxSepalWidthSpecies = line.split(',')[4].rstrip()
						setosaMaxSepalWidth = currentSepalWidth	
					if currentPetalLength < setosaMinimumPetalLength:
						setosaMinPetalLengthSpecies = line.split(',')[4].rstrip()
						setosaMinimumPetalLength = currentPetalLength
					if currentPetalLength > setosaMaxPetalLength:
						setosaMaxPetalLengthSpecies = line.split(',')[4].rstrip()
						setosaMaxPetalLength = currentPetalLength
					if currentPetalWidth < setosaMinimumPetalwidth:
						setosaMinPetalWidthSpecies = line.split(',')[4].rstrip()
						setosaMinimumPetalwidth = currentPetalWidth
					if currentPetalWidth > setosaMaxPetalWidth:
						setosaMaxPetalWidthSpecies = line.split(',')[4].rstrip()
						setosaMaxPetalWidth = currentPetalWidth
					setosaTotalSepalLength += currentSepalLength
					setosaTotalSepalWidth += currentSepalWidth
					setosaTotalPetalLength += currentPetalLength
					setosaTotalPetalWidth += currentPetalWidth
					setosaTotalCount += 1
				elif currentSpecies == 'Iris-versicolor':
					if currentSepalLength < versiMinimumSepalLength:
						versiMinSepalLengthSpecies = line.split(',')[4].rstrip()
						versiMinimumSepalLength = currentSepalLength
					if currentSepalLength > versiMaxSepalLength:
						versiMaxSepalLengthSpecies = line.split(',')[4].rstrip()
						versiMaxSepalLength = currentSepalLength
					if currentSepalWidth < versiMinimumSepalwidth:
						versiMinSepalWidthSpecies = line.split(',')[4].rstrip()
						versiMinimumSepalwidth = currentSepalWidth
					if currentSepalWidth > versiMaxSepalWidth:
						versiMaxSepalWidthSpecies = line.split(',')[4].rstrip()
						versiMaxSepalWidth = currentSepalWidth
					if currentPetalLength < versiMinimumPetalLength:
						versiMinPetalLengthSpecies = line.split(',')[4].rstrip()
						versiMinimumPetalLength = currentPetalLength
					if currentPetalLength > versiMaxPetalLength:
						versiMaxPetalLengthSpecies = line.split(',')[4].rstrip()
						versiMaxPetalLength = currentPetalLength
					if currentPetalWidth < versiMinimumPetalwidth:
						versiMinPetalWidthSpecies = line.split(',')[4].rstrip()
						versiMinimumPetalwidth = currentPetalWidth
					if currentPetalWidth > versiMaxPetalWidth:
						versiMaxPetalWidthSpecies = line.split(',')[4].rstrip()
						versiMaxPetalWidth = currentPetalWidth
					versiTotalSepalLength += currentSepalLength
					versiTotalSepalWidth += currentSepalWidth
					versiTotalPetalLength += currentPetalLength
					versiTotalPetalWidth += currentPetalWidth
					versiTotalCount += 1
				elif currentSpecies == 'Iris-virginica':					
					if currentSepalLength < virginicaMinimumSepalLength:
						virginicaMinSepalLengthSpecies = line.split(',')[4].rstrip()
						virginicaMinimumSepalLength = currentSepalLength
					if currentSepalLength > virginicaMaxSepalLength:
						virginicaMaxSepalLengthSpecies = line.split(',')[4].rstrip()
						virginicaMaxSepalLength = currentSepalLength
					if currentSepalWidth < virginicaMinimumSepalwidth:
						virginicaMinSepalWidthSpecies = line.split(',')[4].rstrip()
						virginicaMinimumSepalwidth = currentSepalWidth
					if currentSepalWidth > virginicaMaxSepalWidth:
						virginicaMaxSepalWidthSpecies = line.split(',')[4].rstrip()
						virginicaMaxSepalWidth = currentSepalWidth
					if currentPetalLength < virginicaMinimumPetalLength:
						virginicaMinPetalLengthSpecies = line.split(',')[4].rstrip()
						virginicaMinimumPetalLength = currentPetalLength
					if currentPetalLength > virginicaMaxPetalLength:
						virginicaMaxPetalLengthSpecies = line.split(',')[4].rstrip()
						virginicaMaxPetalLength = currentPetalLength
					if currentPetalWidth < virginicaMinimumPetalwidth:
						virginicaMinPetalWidthSpecies = line.split(',')[4].rstrip()
						virginicaMinimumPetalwidth = currentPetalWidth
					if currentPetalWidth > virginicaMaxPetalWidth:
						virginicaMaxPetalWidthSpecies = line.split(',')[4].rstrip()
						virginicaMaxPetalWidth = currentPetalWidth
					virginicaTotalSepalLength += currentSepalLength
					virginicaTotalSepalWidth += currentSepalWidth
					virginicaTotalPetalLength += currentPetalLength
					virginicaTotalPetalWidth += currentPetalWidth
					virginicaTotalCount += 1
			#print('{}  {}  {}'.format(sepalLength,sepalWidth,totalCount))
			#print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))

			print('********************************Iris-Setosa********************************')

			print("minimum Sepal length for species Iris-Setosa is {} cms".format(setosaMinimumSepalLength))
			print("maximum Sepal length for species Iris-Setosa is {} cms".format(setosaMaxSepalLength))
			print("minimum Sepal width for species Iris-Setosa is {} cms".format(setosaMinimumSepalwidth))
			print("maximum Sepal width for species Iris-Setosa is {} cms".format(setosaMaxSepalWidth))
			print("The Arithmetic Mean of Sepal Length for all flowers from Iris-Setosa species is {} ".format(setosaTotalSepalLength/setosaTotalCount))
			print("The Arithmetic Mean of Sepal Width for all flowers from Iris-Setosa species is {}".format(setosaTotalSepalWidth/setosaTotalCount))

			print("minimum Petal length for species Iris-Setosa is {} cms".format(setosaMinimumPetalLength))
			print("maximum Petal length for species Iris-Setosa is {} cms".format(setosaMaxPetalLength))
			print("minimum Petal width for species Iris-Setosa is {} cms".format(setosaMinimumPetalwidth))
			print("maximum Petal width for species Iris-Setosa is {} cms".format(setosaMaxPetalWidth))
			print("The Arithmetic Mean of Petal Length for all flowers from Iris-Setosa species is {}".format(setosaTotalPetalLength/setosaTotalCount))
			print("The Arithmetic Mean of Petal Width for all flowers from Iris-Setosa species is {}".format(setosaTotalPetalWidth/setosaTotalCount))

			print('********************************Iris-Versicolor********************************')

			print("minimum Sepal length for species Iris-Versicolor is {} cms".format(versiMinimumSepalLength))
			print("maximum Sepal length for species Iris-Versicolor is {} cms".format(versiMaxSepalLength))
			print("minimum Sepal width for species Iris-Versicolor is {} cms".format(versiMinimumSepalwidth))
			print("maximum Sepal width for species Iris-Versicolor is {} cms".format(versiMaxSepalWidth))
			print("The Arithmetic Mean of Sepal Length for all flowers from Iris-Versicolor species is {} ".format(versiTotalSepalLength/versiTotalCount))
			print("The Arithmetic Mean of Sepal Width for all flowers from Iris-Versicolor species is {}".format(versiTotalSepalWidth/versiTotalCount))

			print("minimum Petal length for species Iris-Versicolor is {} cms".format(versiMinimumPetalLength))
			print("maximum Petal length for species Iris-Versicolor is {} cms".format(versiMaxPetalLength))
			print("minimum Petal width for species Iris-Versicolor is {} cms".format(versiMinimumPetalwidth))
			print("maximum Petal width for species Iris-Versicolor is {} cms".format(versiMaxPetalWidth))
			print("The Arithmetic Mean of Petal Length for all flowers from Iris-Versicolor species is {} ".format(versiTotalPetalLength/versiTotalCount))
			print("The Arithmetic Mean of Petal Width for all flowers from Iris-Versicolor species is {}".format(versiTotalPetalWidth/versiTotalCount))

			print('********************************Iris-Virginica********************************')

			print("minimum Sepal length for species Iris-virginica is {} cms".format(virginicaMinimumSepalLength))
			print("maximum Sepal length for species Iris-virginica is {} cms".format(virginicaMaxSepalLength))
			print("minimum Sepal width for species Iris-virginica is {} cms".format(virginicaMinimumSepalwidth))
			print("maximum Sepal width for species Iris-virginica is {} cms".format(virginicaMaxSepalWidth))
			print("The Arithmetic Mean of Sepal Length for all flowers from Iris-virginica species is {} ".format(virginicaTotalSepalLength/virginicaTotalCount))
			print("The Arithmetic Mean of Sepal Width for all flowers from Iris-Virginica species is {}".format(virginicaTotalSepalWidth/virginicaTotalCount))

			print("minimum Petal length for species Iris-virginica is {} cms".format(virginicaMinimumPetalLength))
			print("maximum Petal length for species Iris-virginica is {} cms".format(virginicaMaxPetalLength))
			print("minimum Petal width for species Iris-virginica is {} cms".format(virginicaMinimumPetalwidth))
			print("maximum Petal width for species Iris-virginica is {} cms".format(virginicaMaxPetalWidth))
			print("The Arithmetic Mean of Petal Length for all flowers from Iris-virginica species is {} ".format(virginicaTotalPetalLength/virginicaTotalCount))
			print("The Arithmetic Mean of Petal Width for all flowers from Iris-virginica species is {}".format(virginicaTotalPetalWidth/virginicaTotalCount))

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
				minimumSepalwidth = currentSepalWidth
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

def PetalAnalysis():
	with open('Data\IrisData.csv') as input:
		#iterate through each line in the file
		totalPetalLength = 0.00;	totalPetalWidth = 0.00;	totalCount = 0
		minimumPetalLength = 100.00; 	minimumPetalwidth = 100.00;
		maxPetalLength = 0.00;	maxPetalWidth = 0.00
		minPetalLengthSpecies = ""; maxPetalLengthSpecies = ""
		minPetalWidthSpecies = ""; maxPetalWidthSpecies = ""
		for line in input:
		#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
		#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
			currentPetalLength = float('{}'.format(line.split(',')[2]))
			currentPetalWidth = float('{}'.format(line.split(',')[3]))

			if currentPetalLength < minimumPetalLength:
				minPetalLengthSpecies = line.split(',')[4].rstrip()
				minimumPetalLength = currentPetalLength
			if currentPetalLength > maxPetalLength:
				maxPetalLengthSpecies = line.split(',')[4].rstrip()
				maxPetalLength = currentPetalLength
			if currentPetalWidth < minimumPetalwidth:
				minPetalWidthSpecies = line.split(',')[4].rstrip()
				minimumPetalwidth = currentPetalWidth
			if currentPetalWidth > maxPetalWidth:
				maxPetalWidthSpecies = line.split(',')[4].rstrip()
				maxPetalWidth = currentPetalWidth	

			totalPetalLength += currentPetalLength
			totalPetalWidth += currentPetalWidth
			totalCount += 1
			#print('{}  {}  {}'.format(PetalLength,PetalWidth,totalCount))
			#print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
		print("minimum Petal length species is flower : {} with length {} cms".format(minPetalLengthSpecies,minimumPetalLength))
		print("maximum Petal length species is flower : {} with length {} cms".format(maxPetalLengthSpecies,maxPetalLength))
		print("minimum Petal width species is flower : {} with width {} cms".format(minPetalWidthSpecies,minimumPetalwidth))
		print("maximum Petal width species is flower : {} with width {} cms".format(maxPetalWidthSpecies,maxPetalWidth))
		print("The Arithmetic Mean of Petal Length for all flowers from Iris Data Set is {}: ".format(totalPetalLength/totalCount))
		print("The Arithmetic Mean of Petal Width for all flowers from Iris Data Set is {}: ".format(totalPetalWidth/totalCount))

def DisplayOptions():
	print ("1. Press 1 to View the DataSet")
	print ("2. Press 2 to See the Sepal Analysis")
	print ("3. Press 3 to see the Petal Analysis")
	print ("4. Press 4 to Analyse by species")
	print ("5. Press 5 to exit the application")
	#print "Please choose from an option above:"
	#print "Please choose from an option above:"
DisplayOptions()
# userInput = int(input("Please choose from the options above:"))
userInput = 4
while userInput != 5:
	if userInput > 0 and userInput <= 4:
		if userInput == 1:
			DisplayDataSet()
		elif userInput == 2:
			SepalAnalysis()
		elif userInput == 3:
    			PetalAnalysis()
		elif userInput == 4:
    			SpeciesAnalysis()
	
	# elif userInput == 3:
    # 	print("PL")
	# elif userInput == 4:
    # 	print("Mapping")
	# elif userInput == 5:
    # 	print("Exit")
	DisplayOptions()
	userInput = int(input("Please choose from the options above:"))
