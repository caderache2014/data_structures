
#parenthetics function
def addParen(outputList, leftRem, rightRem, s, count):

    if (leftRem < 0 or  rightRem < leftRem):
        return # invalid state
    if (leftRem == 0 and rightRem == 0):
        #no more parens left
        from copy import  deepcopy
        sprime = deepcopy(s)
        outputList.append(sprime)
    else:
        #add a left paren if there are any left parens remaining
        if (leftRem > 0):
            s[count] = '('
            addParen(outputList, leftRem - 1, rightRem, s, count + 1)
        #add right paren if expression is valid
        if (rightRem > leftRem):
            s[count] = ')'
            addParen(outputList, leftRem, rightRem - 1, s, count + 1)



def  generateParen(count):
    #
    s = ['0']*(2*count)
    outputList = []
    addParen(outputList, count, count, s, 0)
    return outputList

def evaluateParenString(parensinput):
    #check if there are an equal number of '(' and ')''
    leftCount = 0
    rightCount = 0
    inputList = list(parensinput)
    for paren in inputList:
        if (paren == '('):
            leftCount = leftCount + 1
        elif (paren == ')'):
            rightCount = rightCount + 1
        else:
            print "Invalid input"
            break
    if (leftCount == rightCount):
        parenList = generateParen(leftCount)
        for permutation in parenList:
            x = "".join(permutation)
            print "permutation %s parensinput %s" % (x, parensinput)
            if (x  == parensinput):
                return 0
        return -1 #we have an imbalance
    else:
        return 1

if __name__ == "__main__":

    test1 = "(()())"
    test2 = ")((())"
    retVal1 = evaluateParenString(test1)
    retVal2 = evaluateParenString(test2)
    print "test1 %s returns %d" % (test1, retVal1)
    print "test2 %s returns %d" % (test2, retVal2)