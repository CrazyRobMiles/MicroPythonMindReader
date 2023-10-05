import select
import sys

class MindReader:
    
    def reset(self):
        self.buffer = ""
        
    def __init__(self):
        self.reset()
        
    def update(self):
        
        while select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            ch = sys.stdin.read(1)
            if ord(ch) == 10:
                # got a linefeed
                if len(self.buffer)>0:
                    print("Executing: ", self.buffer)
                    exec(self.buffer)
                self.reset()
            else:
                self.buffer = self.buffer + ch

m = MindReader()

while True:
    m.update()
    