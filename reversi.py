#code for Assignment #1
#CSCI-561 Spring 2017
import numpy

def readFromFile(fname):
	inputArray=[]
	with open(fname) as f:
		inputArray = f.readlines()
	
	inputArray = [x.strip() for x in inputArray]

	currentPlayer = inputArray[0] #we store the player we are supposed to play with in this variable from the inputArray
	inputArray.pop(0) #and then we remove it from the inputArray
	depth = int(inputArray[0]) #we store the depth in this variable from the inputArray & depth changed from Type String to Int
	inputArray.pop(0) #and then we remove it from the inputArray

	arr=["-"]*100
	
	i,j=0,0
	x=11
	while i<=7 and j<=7:
		while j<=7:
			arr[x] = inputArray[i][j]
			x+=1
			j+=1
		x+=2
		j=0
		i+=1
	return currentPlayer,depth,arr, inputArray


def currentPlayerPositions(initArray, currentPlayer): #gives us all the possible current positions of the currentPlayer
	i,arr,x=11,[]*64,0
	while i<89:
		if initArray[i]==currentPlayer:
			arr.append(i)
		i+=1
	return arr

def evalFunctionComputation(initArray, currentPlayer): #will help to get the computation of the evaluation function to us
	evalFunctionArray = numpy.array(([99,-8,8,6,6,8,-8,99],
	[-8,-24,-4,-3,-3,-4,-24,-8],
	[8,-4,7,4,4,7,-4,8],
	[6,-3,4,0,0,4,-3,6],
	[6,-3,4,0,0,4,-3,6],
	[8,-4,7,4,4,7,-4,8],
	[-8,-24,-4,-3,-3,-4,-24,-8],
	[99,-8,8,6,6,8,-8,99]), dtype=int)
	arrX = currentPlayerPositions(initArray, 'X')
	#print arrX #testing
	arrO = currentPlayerPositions(initArray, 'O')
	#print arrO #testing
	sumX, sumO = 0,0
	if not arrX:
		sumX=0
	else:
		length = len(arrX)
		for a in range(0,length):
			j=arrX[a]%10 -1#j component
			i=arrX[a]/10 -1#i component
			sumX+=evalFunctionArray[i][j]
			#print sumX#testing

	if not arrO:
		sumO=0
	else:
		length = len(arrO)
		for a in range(0, length-1):
			j=arrO[a]%10 - 1 #j component
			i=arrO[a]/10 - 1#i component
			sumO+=evalFunctionArray[i][j]
			#print sumO#testing

	#print 'currentPlayer ',currentPlayer#testing

	if currentPlayer=='X':
		return sumX-sumO
	else:
		return sumO-sumX

def outputToFile(outputFileName, inputArray, outputArray):
	with open(outputFileName, 'w+') as file:
		for i in inputArray:
			file.write(str(i)+'\n')
		for i in range(0,len(outputArray)-1):
			file.write(outputArray[i]+'\n')
		file.write(outputArray[len(outputArray)-1])

def convertArray(initArray):
	x,i,resString,inputArray=11,1,'',[]
	while x<89:
		while i<=8:
			resString+=initArray[x]
			x+=1
			i+=1
		inputArray.append(resString)
		x+=2
		i=1
		resString=''
	return inputArray

def nodeName(lastModifiedPosition): #return the name of the current node that we are in.
	a = lastModifiedPosition%10
	b = lastModifiedPosition/10
	a = chr(a+96)
	b = str(b)
	name = a+b
	return name 

def findBracket(initArray, currentPlayerPosition, currentPlayer, opponent):
	arr=[]*10
	for key, value in actions.iteritems():
		bracket = currentPlayerPosition+value
		if initArray[bracket]==opponent:
			while initArray[bracket]==opponent:
				bracket+=value
			if initArray[bracket]!='-':
				arr.append(str(bracket)+','+key)
	return arr



def isValidMovePossible(initArray, currentPlayerPosition, currentPlayer, opponent):
	arr = findBracket(initArray, currentPlayerPosition, currentPlayer, opponent)
	opponentPlayerPositionsArray = currentPlayerPositions(initArray, opponent)
	if not arr and not opponentPlayerPositionsArray:
		return False, []
	return True, arr

def getAlphaBetaValueString(number):
	b = float('inf')
	a = (-1)*float('inf')
	if number==a:
		return '-Infinity'
	elif number==b:
		return 'Infinity'
	else:
		return str(number)

def getOutputString(lastModifiedPosition, currentDepth, value, alpha, beta, outputArray):
	outputString=''
	if lastModifiedPosition==-1:
		name='pass'
	else:
		name=nodeName(lastModifiedPosition)
	if currentDepth==0:
		name='root'
	value = getAlphaBetaValueString(value)
	alphaString = getAlphaBetaValueString(alpha)
	betaString = getAlphaBetaValueString(beta)
	outputString = name+','+str(currentDepth)+','+str(value)+','+alphaString+','+betaString
	print outputString #just a test to see if this is working
	outputArray.append(outputString)

def nextDepthVal(number):
	neginf=(-1)*float('inf')
	posinf = float('inf')
	if number==posinf:
		return neginf
	elif number==neginf:
		return posinf
	else:
		return number

def outputPassed(outputArray):
	length = len(outputArray)-1
	a = outputArray[length].split(',')
	b = outputArray[length-1].split(',')

	if a[0]=='pass' and b[0]=='pass':
		return True
	else:
		return False

def find_move(initArray, outputArray, currentDepth, depth, value, alpha, beta, currentPlayer, opponent, lastModifiedPosition, currentPlayerPositionsArray):

	if currentDepth==depth:
		#currentDepth is equal to the depth
		#print "*leaf node*" #testing
		currValue = evalFunctionComputation(initArray, currentPlayer)
		value = currValue
		getOutputString(lastModifiedPosition, currentDepth, value, alpha, beta, outputArray)
		return value
		#currentDepth is equal to the depth

	else:	
	#current depth is not equal to given depth
		#print currentPlayer, opponent
		if not currentPlayerPositionsArray:
		#that is current player has no tile on the board
			oa = outputArray[len(outputArray)-1].split(',')
			if oa[0]=='pass':
			#if the previous ply was a pass
				#print "*passing - terminal state reached*"#testing
				currValue = evalFunctionComputation(initArray, opponent)
				print '**', currentPlayer, opponent, currValue
				value = currValue
				getOutputString(-1, currentDepth, nextDepthVal(value), alpha, beta, outputArray)
				return value
			#if the previous ply was a pass
			else:
			#if the previous ply was not a pass
				#print '*one pass recorded*'#testing
				getOutputString(-1,currentDepth, nextDepthVal(value), alpha,beta, outputArray)
				opponentPlayerPositionsArray = currentPlayerPositions(initArray, opponent)
				#print currentPlayerPositionsArray
				if not currentPlayerPositionsArray:
					#print '*going here*'#testing
					value = find_move(initArray, outputArray, currentDepth+1, depth, nextDepthVal(value), alpha, beta, opponent, currentPlayer, -1, opponentPlayerPositionsArray)
				else:
					#print '*in the else*'#testing
					for i in opponentPlayerPositionsArray:
					#looping over all the positions occupied by the opponent
						value = find_move(initArray, outputArray, currentDepth+1, depth, nextDepthVal(value), alpha, beta, opponent, currentPlayer, i, opponentPlayerPositionsArray)
						return value
					#looping over all the positions occupied by the opponent

			#if the previous ply was not a pass
		#that is current player has no tile on the board
		else:
		#current player has tiles on the board
			invalidCounter=0
			for i in currentPlayerPositionsArray:
			#looping over all the positions occupied by the current player
				validMoveExists,validMovesArray=isValidMovePossible(initArray, i, currentPlayer, opponent)
				if validMoveExists==False:
				#no valid move exists
					#print 'no valid move'#testing
					invalidCounter+=1
					continue
				#no valid move exists
				else:
				#valid move exists
					#print 'else block'#testing
					for j in validMovesArray:
					#looping over all the valid moves available
						validMovesArrayElements = j.split(',')
						validMovesArrayElements[0] = int(validMovesArrayElements[0])
						getOutputString(validMovesArrayElements[0], currentDepth, nextDepthVal(value), alpha, beta, outputArray)
						initArrayN = initArray
						initArrayN[validMovesArrayElements[0]] = currentPlayer
						iterator = i+actions.get(validMovesArrayElements[1])
						while  initArrayN[iterator]!=currentPlayer:
							initArrayN[iterator]=currentPlayer
							iterator+=actions.get(validMovesArrayElements[1])
						lastModifiedPosition = iterator
						#print opponent
						opponentPlayerPositionsArray = currentPlayerPositions(initArray, opponent)
						#print opponentPlayerPositionsArray
						#print '*outside the loop*'#testing
						if not opponentPlayerPositionsArray:
							value = find_move(initArrayN, outputArray, currentDepth+1, depth, nextDepthVal(value), alpha, beta, opponent, currentPlayer, -1, opponentPlayerPositionsArray)
						else:
							for k in opponentPlayerPositionsArray:
							#print currentPlayer, opponent
								#print '*in the loop*'#testing
								value = find_move(initArrayN, outputArray, currentDepth+1, depth, nextDepthVal(value), alpha, beta, opponent, currentPlayer, lastModifiedPosition, opponentPlayerPositionsArray)
								#print value#testing
								if currentDepth%2==0:
									alpha=value
								else:
									beta=value
								getOutputString(i, currentDepth, value, alpha, beta, outputArray)

						initArrayN = initArray
					#looping over all the valid moves available
				#valid move exists
			#looping over all the positions occupied by the current player
			if invalidCounter==len(currentPlayerPositionsArray):
				opponentPlayerPositionsArray = currentPlayerPositions(initArray, opponent)
				#print 'invalid counter', opponentPlayerPositionsArray#testing
				getOutputString(-1, currentDepth, nextDepthVal(value), alpha, beta, outputArray)
				value = find_move(initArray, outputArray, currentDepth+1, depth, nextDepthVal(value), alpha, beta, opponent, currentPlayer, lastModifiedPosition, opponentPlayerPositionsArray)
				if currentDepth%2==0:
					alpha = value
				else:
					beta = value
				getOutputString(-1, currentDepth, value, alpha, beta, outputArray)
				return value

		#current player has tiles on the board

	#current depth is not equal to given depth
		if currentDepth!=depth or outputPassed(outputArray)==False:
			#print '*end of loop*', value, currentDepth#testing
			if currentDepth%2==0:
				alpha = value
			else:
				beta = value
			getOutputString(lastModifiedPosition,currentDepth, value, alpha, beta, outputArray)
		return value #returns the value to main

def main():
	global initArray, outputArray
	currentPlayer,depth,initArray,inputArray = readFromFile('input.txt')

	if currentPlayer=='X':
		opponent='O'
	else:
		opponent='X'
	
	global actions
	actions = {'Up':-10, 'Down':10, 'Left':-1, 'Right':1, 'UpLeft':-9, 'UpRight':9, 'DownRight':11, 'DownLeft':-11}

	outputArray=['Node,Depth,Value,Alpha,Beta', 'root,0,-Infinity,-Infinity,Infinity']
	alpha = (-1)*float('inf')
	beta = float('inf')
	value=alpha
	#print value, alpha, beta
	currentPlayerPositionsArray = currentPlayerPositions(initArray, currentPlayer)
	#logic
	#find_move(initArray, outputArray, currentDepth, depth, value, alpha, beta, currentPlayer, opponent, lastModifiedPosition, currentPlayerPositionsArray, passCounter)
	lastModifiedPosition=currentPlayerPositionsArray[0]
	#print value, alpha,beta, lastModifiedPosition
	value = find_move(initArray, outputArray, 1, depth, value, alpha, beta, currentPlayer, opponent, lastModifiedPosition, currentPlayerPositionsArray)
	getOutputString(0,0,value,value,beta, outputArray)

	#print value
	#logic
	inputArray = convertArray(initArray)
	outputToFile('output.txt', inputArray, outputArray) #we will have to modify the input array to match the new version with the move for the current player.

main()
