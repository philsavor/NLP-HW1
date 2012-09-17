import text_manager

class Agent:
   """
   Agent is the class used to receive a put-in text,
   and recongnize the "absolute date" from the content
   of the text, and return the final result text,which only
   contain the "absolute date".
   """
   month = ('January','February','March','April','May','Jule', \
            'July','August','September','October','Novermber', \
            'December')
   day = ('1st','2nd','3rd','4th','5th','6th','7th','8th','9th', \
          '10th','11th','12th','13th','14th','15th','16th','17th','18th','19th', \
          '20th','21th','22th','23th','24th','25th','26th','27th','28th','29th', \
          '30th','31th','1','2','3','4','5','6','7','8','9', \
          '10','11','12','13','14','15','16','17','18','19', \
          '20','21','22','23','24','25','26','27','28','29', \
          '30','31')

   def __init__(self):
       """
       used to do some initial things.
       """
       self.__current_state = 0 
       self.__final_states = {3,6}
       self.__current_word = None
       self.__buffer_words = [] 
       self.__text_manager = None
   
   def set_file(self,file_name):
       """
       set file and initialize the __text_manager
       """
       self.__text_manager = text_manager.TextManager() 
       self.__text_manager.set_file(file_name)

   def parse_file(self,des_file_name):
       """
       parse the input file and crate a result file, which path is 
       same as the parameter value. 
       """
       if self.__text_manager == None:
           return "ERROR:no input file!"
       while 1:
           word = self.__text_manager.get_next_word() 
           if word == None: 
               break
           self.__automata(word)

   def __automata(self,word):
       """
       The core class for parsing the text content.It matain a series
       of states,which may change when recieve the right word.When the
       state is one of the final states, put out the phrase representing
       a absolute date.
       """
       self.__current_word = word
       #state 0
       if self.__current_state == 0 :
           if self.__current_word in self.month :
               self.__current_state = 1
               self.__buffer_words.append(self.__current_word)
           elif self.__current_word == "the" :
               self.__current_state = 2 
               self.__buffer_words.append(self.__current_word)
       #state 1
       elif self.__current_state == 1 :
           if self.__current_word in self.day :
               self.__current_state = 3 
               self.__buffer_words.append(self.__current_word)
               #final state 
               print self.__buffer_words
               self.__current_state = 0
               self.__buffer_words = []
           else:
               self.__current_state = 0
               self.__buffer_words = []
       #state 2 
       elif self.__current_state == 2 :
           if self.__current_word in self.day :
               self.__current_state = 4 
               self.__buffer_words.append(self.__current_word)
           else:
               self.__current_state = 0
               self.__buffer_words = []
       #state 4 
       elif self.__current_state == 4 :
           if self.__current_word == 'of' :
               self.__current_state = 5 
               self.__buffer_words.append(self.__current_word)
           else:
               self.__current_state = 0
               self.__buffer_words = []
       #state 5 
       elif self.__current_state == 5 :
           if self.__current_word in self.month :
               self.__current_state = 6 
               self.__buffer_words.append(self.__current_word)
               #final state 
               print self.__buffer_words
               self.__current_state = 0
               self.__buffer_words = []
           else:
               self.__current_state = 0
               self.__buffer_words = []
        
