'''
科学计算实验
'''
class Student():
      def __init__(self,name,score):
            self.name=name
            self.score=score
      def showName(self):
            print(self.name)
      def getScore(self):
            print(self.score)

#a=Student('zhang',90)

class Class():
      def __init__(self):
            self._list=[]
      def addstu(self,people):
            self._list.append(people)
      def removestu(self,people):
            self._list.remove(people)
      def showname(self):
            j=[]
            for i in self._list:
                  k.append(i.name)
            print('学生姓名：'+str(j))
      def maxscore(self):
            k=[]
            for i in self._list:
                  k.append(i.score)
            maxscore=max(k)
            for t in self._list:
                  if t.score == maxscore:
                        print(t.name+' 分数最高，为：'+ste(t.score))

