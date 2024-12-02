from os import listdir, path
from subprocess import call

#######################################################################################
# MIT License
#
# Copyright (c) 2024 E1480
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#######################################################################################


# ================================
# | Program by: 1480
# ================================



# Settings
folder = "./applets/"


class Main:
    def __init__(self):
        self.path = folder
        self.Dict = {}
        self.Dir = {}
        self.data = listdir(self.path) 

        self._createList()
   
    def _createList(self):
        self.Dict = {}
        self.Dir = {}
        ID = 1
        
        for i in self.data:
            if path.isfile(self.path+i):
               self.Dict[ID] = i
            ID += 1

        ID = 1

    def List(self):
        return self.Dict

    def get(self):
        return self.data
   



def GetFiles(Dict):
    print("\tID:\tFILE:")
    ID = 1
    for i in Dict:
        print("\t",ID,"|\t",Dict[i])
        ID += 1
    ID = 0

def Run(UserIn, Dict):

    Dir = folder
    name, extension = str(Dict[UserIn]).split('.')
    print("From \""+Dict[UserIn]+"\":\n")

    # Add more languages here
    match extension:
         case "py":
             call(['python',Dir+Dict[UserIn]])
         case "c" | "cpp" | "c++":
            if path.isdir(Dir+'output'):
               outDir = Dir+'output'
            else:
                try:
                    call(['mkdir', Dir+'output'])
                    print("Created a file \""+Dir+"output\"")
                except:
                    pass
            
            call(['gcc', Dir+Dict[UserIn],'-o',Dir+"output/"+name])
            call([Dir+"output/"+name])
            
         case _:
             pass

    print("\n",name,"End...")
    GetFiles(Dict)

if __name__ == "__main__":
    app = Main()
    Dict = app.List()
    GetFiles(Dict)
    while True:
        print("type q to exit")
        print("Select using the ID")
        userIn = input(":: ").lower()
        # Exit commands because I'm lazy.
        match userIn:
            case "x":
                break
            case "q":
                break
            case "ff":
                break
            case "exit":
                break
     
        if userIn == "file":
            GetFiles(Dict)


        try:
            Run(int(userIn), Dict)
        except:
            pass
