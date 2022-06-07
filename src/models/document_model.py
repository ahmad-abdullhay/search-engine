import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'controllers'))
import config as c
class DocumentModel:
  def printDocument(self):
    print('id = '+self.id+'\n')
    print('title = '+self.title+'\n')
    print('author = '+self.author+'\n')
    print('abstract = ')
    print(self.abstract+'\n')
    print('crossReferences = ')
    print(self.crossReferences+'\n')

  def __init__(self,id,title,author,abstract, crossReferences):
    self.id = id
    self.title = title
    self.author = author
    self.abstract = abstract
    self.crossReferences = crossReferences


def newDocument  (content,id):
  if c.getDatasetName() == 'cacm':
    return newCACMDocument (content,id)
  else:
    return newCISIDocument (content,id)

def newCISIDocument (content,id):
    contentArray = content.split("\n")
    mode =''
    title= ''
    author= ''
    abstract= ''
    crossReferences= ''
    currentString = ''
    for line in contentArray:
        if line.startswith(".T"):
          mode = 't'
          continue
        if line.startswith(".A"):
          mode = 'a'
          continue
        if line.startswith(".W"):
          mode = 'w'
          continue
        if line.startswith(".X"):
          mode = 'x'
          continue

        if mode == 't':
          title+=line+'\n'
          continue
        if mode == 'a':
          author+=line+'\n'
          continue
        if mode == 'w':
          abstract+=line+'\n'
          continue
        if mode == 'x':
          crossReferences+=line+'\n'
          continue
    return DocumentModel(id, title, author, abstract, crossReferences)
    
def newCACMDocument (content,id):
   
    contentArray = content.split("\n")
    mode =''
    title= ''
    author= ''
    abstract= ''
    crossReferences= ''
    words = ''
    n = ''
    currentString = ''
    for line in contentArray:
        if line.startswith(".T"):
          mode = 't'
          continue
        if line.startswith(".B"):
          mode = 'B'
          continue
        if line.startswith(".A"):
          mode = 'a'
          continue
        if line.startswith(".N"):
          mode = 'n'
          continue
        if line.startswith(".X"):
          mode = 'x'
          continue
        if line.startswith(".W"):
          mode = 'w'
          continue
        if mode == 't':
          title+=line+'\n'
          continue
        if mode == 'b':
          n+=line+'\n'
          continue
        if mode == 'a':
          author+=line+'\n'
          continue
        if mode == 'n':
          abstract+=line+'\n'
          continue
        if mode == 'x':
          crossReferences+=line+'\n'
          continue
        if mode == 'w':
          words+=line+'\n'
          continue
    return DocumentModel(id, title, author, words,crossReferences)

    