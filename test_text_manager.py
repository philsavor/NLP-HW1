#!/usr/bin/python -B

import text_manager
tm = text_manager.TextManager()
while 1:
    word = tm.get_next_word()
    print word
    if word == None:
         break 
