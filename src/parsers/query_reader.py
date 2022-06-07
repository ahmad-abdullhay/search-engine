import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'models'))
import query_model as qm;
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'controllers'))
import config as c


def readAllQueries ():
    datasetPath = c.getDatasetQueriesPath()
    queryList = []
    f = open(datasetPath)
    queryI = ""
    queryContent = None

    for a_line in f.readlines():
        if a_line.startswith(".I"):
            if not queryContent is None:
                query = qm.newQuery(queryContent, queryI)
                queryList.append(query)
            queryI = a_line.split(" ")[1].strip()
            queryContent = ''
        else:
            queryContent += a_line
    query = qm.newQuery(queryContent, queryI)
    queryList.append(query)
    return queryList


 