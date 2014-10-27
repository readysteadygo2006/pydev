__author__ = 'pgrant'

__author__ = 'pgrant'
from copy import deepcopy

dateSet = 0
periodCountTable = {}
periodDeniedCountTable = {}
maxCountTable = {}
maxDeniedCountTable = {}
lastMaxCountTable = {}
lastDate = ""

maxLic = 0
for line in open('/home/pgrant/workarea/python/arm-20140715-095116.log'):
    tokenList = line.split(" ")
    if "TIMESTAMP" in tokenList:
        dateSet = 1
        if tokenList[0] == '':
            del tokenList[0]
        if lastDate  != tokenList[-1]:
            lastDate  = tokenList[-1]
            print("\n")
            print(tokenList[-1], " , ", tokenList[0], ", ")
            for licName in maxCountTable.keys():
                print(licName, ", ", maxCountTable[licName], ", ")
            print("\n")
            print(tokenList[-1], " , ", tokenList[0], ", ")
            for licName in maxDeniedCountTable.keys():
                print(licName, ", ", maxDeniedCountTable[licName], ", ")
    if dateSet == 1:
        if "OUT:" in tokenList:
            if  "OUT:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3

            if tokenList[tokenPos] in periodDeniedCountTable:
                if tokenList[tokenPos] in maxDeniedCountTable:
                    if periodDeniedCountTable[tokenList[tokenPos]] > maxDeniedCountTable[tokenList[tokenPos]]:
                        maxDeniedCountTable[tokenList[tokenPos]] =  periodDeniedCountTable[tokenList[tokenPos]]
                else:
                    maxDeniedCountTable[tokenList[tokenPos]] =  periodDeniedCountTable[tokenList[tokenPos]]
                periodDeniedCountTable[tokenList[tokenPos]] = 0
            if tokenList[tokenPos] in periodCountTable:
                periodCountTable[tokenList[tokenPos]] =  periodCountTable[tokenList[tokenPos]] + 1
                if periodCountTable[tokenList[tokenPos]] > maxCountTable[tokenList[tokenPos]]:
                    maxCountTable[tokenList[tokenPos]] = periodCountTable[tokenList[tokenPos]]
            else:
                periodCountTable[tokenList[tokenPos]] = 1
                if tokenList[tokenPos] not in maxCountTable:
                    maxCountTable[tokenList[tokenPos]] = 1

        if "IN:" in tokenList:
            if  "IN:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3
            if tokenList[tokenPos] in periodCountTable:
                if periodCountTable[tokenList[tokenPos]] > 0:
                    periodCountTable[tokenList[tokenPos]] = periodCountTable[tokenList[tokenPos]] - 1
                else:
                    periodCountTable[tokenList[tokenPos]] = 0

        if "DENIED:" in tokenList:
            if  "IN:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3
            if tokenList[tokenPos] in periodDeniedCountTable:
                periodDeniedCountTable[tokenList[tokenPos]] = periodDeniedCountTable[tokenList[tokenPos]] + 1
            else:
                periodDeniedCountTable[tokenList[tokenPos]] = 1



