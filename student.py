class Student:
  def __init__(self,name):
    self.name = name
    self.test_scores = []
    
  def add_test(self,test_score):
    self.test_scores.append(test_score)

  def get_average(self):
    average = 0
    for i in range(len(self.test_scores)):
      average += (self.test_scores[i]/i)
      average = round(average,1)
    return average
    
