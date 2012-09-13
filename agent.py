class Agent:
   current_word = ""
   final_state = 4
   def __init__(self, state=0 , buffer_words=""):
       self.state = state
       self.buffer_words = buffer_words
       print("init agent/n")
   def receive_word(self, current_word):
       self.current_word = current_word 
       print("tag1: %s" % (self.current_word))
   def recongnize(self):
       if self.state == 0 :
           if self.current_word == "month" :
               print("month")
               self.state = 1
           elif self.current_word == "the" :
               print("the")
               self.state = 2 
           else :
               print("no right word")
       elif self.state == 1 :
           if self.current_word == "num" :
               self.state = 3
           else :
               self.state = 0
       # judge if reach to final state 
       if self.state == 3 :
           print("final")    
agent = Agent()
agent.receive_word("month")
agent.recongnize()
agent.receive_word("num")
agent.recongnize()          
