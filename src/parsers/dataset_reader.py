import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'models'))
import document_model as dm;
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'controllers'))
import config as c
def read_all ():
    datasetPath = c.getDatasetDocumentsPath()
    docList = []
    f = open(datasetPath)
    docI = ""
    docContent = None
    for a_line in f.readlines():
        if a_line.startswith(".I"):
            if not docContent is None:
                doc =dm.newDocument(docContent, docI)
                docList.append(doc)
            docI = a_line.split(" ")[1].strip()
            docContent = ''
        else:
            docContent += a_line
    doc =dm.newDocument(docContent, docI)
    docList.append(doc)
    return docList


 