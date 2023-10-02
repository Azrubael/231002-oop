#!/usr/bin/python3


class Graph:
  LIMIT_Y = [0 ,10]
  data = []

  def set_data(self, data):
    if len(data) > 0:
      self.data = data
       

  def draw(self):

    if len(self.data) != 0:
      output = ""
      minY = self.LIMIT_Y[0]
      maxY = self.LIMIT_Y[1]

      for i in self.data:
        if i >= minY and i <= maxY:
          output = output + str(i) + " "
      
      print(output.strip())
      
      
digits = [10,-5, 100, 20, 0, 80, 45, 2, 5, 7]

graph_1 = Graph()
graph_1.set_data(digits)
graph_1.draw()