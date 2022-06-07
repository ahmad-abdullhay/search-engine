def getDatasetName ():
    with open('configuration.txt') as f:
        contents = f.readlines()
    return contents[0].strip() 


def getDatasetDocumentsPath ():
    with open('configuration.txt') as f:
        contents = f.readlines()
    return contents[1].strip() 

def getDatasetQueriesPath ():
    with open('configuration.txt') as f:
        contents = f.readlines()
    return contents[2].strip() 


def getDatasetResultsPath ():
    with open('configuration.txt') as f:
        contents = f.readlines()
    return contents[3].strip()  