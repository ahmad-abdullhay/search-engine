


class QueryModel:
  def printQuery(self):
    print('id = '+self.id+'\n')
    print('query = '+self.query+'\n')


  def __init__(self,id,query,title,author):
    self.id = id
    self.query = query
    self.title = title
    self.author = author



def newQuery (content,id):
   
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
        if line.startswith(".B"):
          mode = 'b'
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
        if mode == 'b':
          crossReferences+=line+'\n'
          continue
    return QueryModel(id, abstract,title,author)