import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'models'))
import query_result_model as qrm
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'controllers'))
import config as c
def readAllQueriesResult ():
    datasetPath = c.getDatasetResultsPath()
    f = open(datasetPath)
    currentQueryResult = qrm.QueryResultModel(-1, [])
    queryResultList = []
    for a_line in f.readlines():
        queryResultRow = a_line.split()
        id = queryResultRow[0]
        if (id[0] == '0'):
            id = id[1]
        result = queryResultRow[1]
        if (id == currentQueryResult.id):
            currentQueryResult.newResult(result)
        else:
            queryResultList.append(currentQueryResult)
            currentQueryResult = qrm.QueryResultModel(id, [result])
    queryResultList.pop(0)
    return queryResultList
