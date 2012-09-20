NLP-HW1
=======

[OVERVIEW]
This programm is to recognize all "absolute" dates, including the following
format:
1.Month Day:  
  March 15, Mar 15th, 15 March 
2.the Day of Month:
  the 15th of March
3.Holiday:
  Christmas, Thanksgiving
4.Word Day:
  Labor Day, Memorial Day
5.Word Word Day:
  Armed Forces Day
6.Word Word:
  Fat Tuesday
7.Word Word Word Day:
  Pearl Harbor Remembrance Day  
 
The algorithm is based on the theory of automata.
Programming language is python and the platform is Linux.

[FILES]
README.txt
agent.py (the main file, containing the algorithm)
text_manager.py (used to parse file and provide word one by one)

[HOW TO USE]
1../agent.py
2.input text file's name such as input.txt
(this text file shold be put into the same directory as agent.py)
3.view the result in file out.txt
