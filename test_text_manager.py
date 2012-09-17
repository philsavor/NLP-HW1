#!/usr/bin/python -B

import text_manager
tm = text_manager.TextManager()
print tm.get_next_word()
tm.set_file("in_text")
print tm.get_next_word()
while 1:
    word = tm.get_next_word()
    print word
    if word == None:
         break 
