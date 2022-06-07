


class QueryResultModel:
  def printQueryResult(self):
    print(self.id)
    print(self.result)

  def newResult(self,newresult):
    self.result.append(newresult)

  def isMatch(self,index):

      index = str(index+1)
      return index in self.result

  def __init__(self,id,result):
    self.id = id
    self.result = result

