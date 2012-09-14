class TextManager :
    def __init__(self) :
        self.f = open("in_text")

    def out(self) :
        lines = self.f.readlines()
        print(lines) 

