#!/usr/bin/python -B

import text_manager

class Agent:
   """
   Agent is the class used to receive a put-in text,
   and recongnize the "absolute date" from the content
   of the text, and return the final result text,which only
   contain the "absolute date".
   """
   month = ('January','February','March','April','May','June', \
            'July','August','September','October','November','December',\
            'Jan','Feb','Mar','Apr','May','Aug','Sept','Oct','Nov','Dec')
   day = ('1st','2nd','3rd','4th','5th','6th','7th','8th','9th', \
          '10th','11st','12nd','13rd','14th','15th','16th','17th','18th','19th', \
          '20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th', \
          '30th','31st','1','2','3','4','5','6','7','8','9', \
          '10','11','12','13','14','15','16','17','18','19', \
          '20','21','22','23','24','25','26','27','28','29', \
          '30','31')
   #format: *
   holiday_oneword = ('Halloween','Thanksgiving','Christmas')
   #format: * Day
   holiday_twoword = ('Groundhog','Presidents','Earth','Arbor','Memorial',\
                      'Flag','Independence','Labor','Patriot','Christmas',\
                      'Constitution','Columbus','Mole','Veterans','Patriots')
   #format: * * Day
   holiday_pair_words = {'Valentine':'s','National':'Doctors','April':'Fools',\
                        'Mother':'s' , 'Armed':'Forces' , 'Father':'s',\
                        'Children':'s', 'All':'Saints'}                    
   #format: * *
   holiday_twoword_no_Day = {'Fat':'Tuesday','Ash':'Wednesday','Vernal':'Equinox',\
                             'Palm':'Sunday','Good':'Friday','Easter':'Sunday',\
                             'Pentecost':'Sunday','Summer':'Solstice',\
                             'Rosh':'Hashanah','Autumnal':'equinox','Yom':'Kippur',\
                             'Simchat':'Torah','Winter':'Solstice','Marathon':'Monday'} 
   #format: * * * Day
   holiday_pair_one = {'New':'Year','St':'Patrick','Pearl':'Harbor'}
   holiday_pair_two = {'Year':'s'  ,'Patrick':'s' ,'Harbor':'Remembrance'}

   def __init__(self):
       """
       used to do some initial things.
       """
       self.__current_state = 0 
       self.__final_states = {3,6,8,9,11,14,16,20}
       self.__current_word = None
       self.__buffer_words = [] 
       self.__text_manager = None
       self.__des_file = None
   
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
       #set the destination file name
       self.__des_file = open(des_file_name,"wb")

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
       #used to judge if the state have changed
       temp_state = self.__current_state
       while 1:
            #state 0
            if self.__current_state == 0 :
                if self.__current_word in self.month :
                    self.__current_state = 1
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word == "the" or self.__current_word == "The":
                    self.__current_state = 2 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.day :
                    self.__current_state = 7 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.holiday_oneword:
                    self.__current_state = 9 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.holiday_twoword:
                    self.__current_state = 10 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.holiday_pair_words.keys():
                    self.__current_state = 12 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.holiday_twoword_no_Day.keys():
                    self.__current_state = 15 
                    self.__buffer_words.append(self.__current_word)
                elif self.__current_word in self.holiday_pair_one.keys():
                    self.__current_state = 17 
                    self.__buffer_words.append(self.__current_word)
            #state 1
            elif self.__current_state == 1 :
                if self.__current_word in self.day :
                    self.__current_state = 3 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 2 
            elif self.__current_state == 2 :
                if self.__current_word in self.day :
                    self.__current_state = 4 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 4 
            elif self.__current_state == 4 :
                if self.__current_word == 'of' :
                    self.__current_state = 5 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 5 
            elif self.__current_state == 5 :
                if self.__current_word in self.month :
                    self.__current_state = 6 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 7 
            elif self.__current_state == 7 :
                if self.__current_word in self.month :
                    self.__current_state = 8 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 10 
            elif self.__current_state == 10 :
                if self.__current_word == 'Day' :
                    self.__current_state = 11 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 12 
            elif self.__current_state == 12 :
                if self.__current_word == self.holiday_pair_words.get(self.__buffer_words[0]) :
                    self.__current_state = 13 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 13 
            elif self.__current_state == 13 :
                if self.__current_word == 'Day' :
                    self.__current_state = 14 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 15 
            elif self.__current_state == 15 :
                if self.__current_word == self.holiday_twoword_no_Day.get(self.__buffer_words[0]) :
                    self.__current_state = 16 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 17 
            elif self.__current_state == 17 :
                if self.__current_word == self.holiday_pair_one.get(self.__buffer_words[0]) :
                    self.__current_state = 18 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 18 
            elif self.__current_state == 18 :
                if self.__current_word == self.holiday_pair_two.get(self.__buffer_words[1]) :
                    self.__current_state = 19 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #state 19 
            elif self.__current_state == 19 :
                if self.__current_word == 'Day' :
                    self.__current_state = 20 
                    self.__buffer_words.append(self.__current_word)
                else:
                     self.__current_state = 0
                     self.__buffer_words = []
                     continue
            #final states  
            if self.__current_state in self.__final_states:
                for word in self.__buffer_words:
                    #deal with the situation like "Mother's Day"
                    if word == 's':
                        self.__des_file.write('\'s')
                    else:
                        self.__des_file.write(word)
                    self.__des_file.write(' ')
                self.__des_file.write('\n')
                #initialize the state and buffer
                self.__current_state = 0
                self.__buffer_words = [] 
            break

if __name__ == '__main__':
    agent = Agent()
    input_file_name = raw_input( "Please put in the file's name:")
    agent.set_file(input_file_name)
    agent.parse_file("out.txt")
    print "The result has been saved in out.txt"
