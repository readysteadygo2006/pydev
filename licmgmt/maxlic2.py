__author__ = 'pgrant'

from copy import deepcopy
import matplotlib.pyplot as plt

dateSet = 0
periodCountTable = {}
periodDeniedCountTable = {}
maxCountTable = {}
maxDeniedCountTable = {}
lastMaxCountTable = {}
lastDate = ""
plotDict = {}
plotDict['xAxis'] = {}
plotList = {}

mapIndex = 0

maxLic = 0
for line in open('/home/pgrant/workarea/python/arm-20140715-095116.log'):
#for line in open('/home/pgrant/workarea/python/pydev/test.log'):
    tokenList = line.split(" ")
    if "TIMESTAMP" in tokenList:
        dateSet = 1
        tokenList[-1] = tokenList[-1][:-1]
        if tokenList[0] == '':
            del tokenList[0]
        if lastDate  != tokenList[-1]:
            lastDate  = tokenList[-1]
            xAxis = plotDict['xAxis']
            xAxis[mapIndex] = tokenList[-1]
 #           print(tokenList[-1], " , ")
            for licName in maxCountTable.keys():
                if licName not in plotDict:
                    plotDict[licName] = {}
            for licName in maxCountTable.keys():
#                print(licName, ", ", maxCountTable[licName], ", ")
                plotDict[licName][mapIndex] = maxCountTable[licName]
#            print("\n")
#            print(tokenList[-1], ", ")
            for licName in maxDeniedCountTable.keys():
                deniedLicName = 'denied' + ':' + licName
                if deniedLicName not in plotDict:
                    plotDict[deniedLicName] = {}
            for licName in maxDeniedCountTable.keys():
                deniedLicName = 'denied' + ':' + licName
#               print(deniedLicName, ", ", maxDeniedCountTable[licName], ", ")
                plotDict[deniedLicName][mapIndex] = maxDeniedCountTable[licName]
            mapIndex = mapIndex + 1
    if dateSet == 1:
        if "OUT:" in tokenList:
            if  "OUT:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3

            licName = tokenList[tokenPos]
            licName = licName[:-1]
            licName = licName[1:]

            if licName in periodDeniedCountTable:
                if licName in maxDeniedCountTable:
                    if periodDeniedCountTable[licName] > maxDeniedCountTable[licName]:
                        maxDeniedCountTable[licName] =  periodDeniedCountTable[licName]
                else:
                    maxDeniedCountTable[licName] =  periodDeniedCountTable[licName]
                periodDeniedCountTable[licName] = 0
            if licName in periodCountTable:
                periodCountTable[licName] =  periodCountTable[licName] + 1
                if periodCountTable[licName] > maxCountTable[licName]:
                    maxCountTable[licName] = periodCountTable[licName]
            else:
                periodCountTable[licName] = 1
                if licName not in maxCountTable:
                    maxCountTable[licName] = 1

        if "IN:" in tokenList:
            if  "IN:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3

            licName = tokenList[tokenPos]
            licName = licName[:-1]
            licName = licName[1:]

            if licName in periodCountTable:
                if periodCountTable[licName] > 0:
                    periodCountTable[licName] = periodCountTable[licName] - 1
                else:
                    periodCountTable[licName] = 0

        if "DENIED:" in tokenList:
            if  "IN:" in tokenList[3]:
                tokenPos = 4
            else:
                tokenPos = 3
            if licName in periodDeniedCountTable:
                periodDeniedCountTable[licName] = periodDeniedCountTable[licName] + 1
            else:
                periodDeniedCountTable[licName] = 1

for licName in plotDict:
    plotList[licName] = []
for indexCount in range(0, mapIndex):
    for licName in plotDict:
        if indexCount in plotDict[licName]:
            plotList[licName].append(plotDict[licName][indexCount])
        else:
            plotList[licName].append(0)

for licName in plotList:
    if licName !=  'xAxis' and 'denied' not in licName:
        plt.plot(plotList[licName], label=licName)

#plt.legend(bbox_to_anchor=(0., 1, 0, 1), loc=2, ncol=2, mode="expand", borderaxespad=0.)
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
#plt.legend(loc='upper center', shadow=True)
plt.show()


