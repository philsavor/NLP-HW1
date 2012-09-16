import re

class TextManager :
    def __init__(self) :
        self.f = open("in_text")
        self.lines = self.f.readlines()
        self.line_count = 0

    def out(self) :
        line_string = self.lines[self.line_count] 
        if line_string != '\n' : 
             print line_string
        words = re.findall(r'\w+', line_string)
        for word in words :
            print word
        self.line_count += 1
