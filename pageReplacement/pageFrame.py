from random import randint
from rich.console import Console
from rich.table import Table
from rich import box

class PageReplacer:
    hitCounter=0
    faultCounter=0
    hitFault=[]
    ram=[]
    referenceString=[]
    ramState=[[]]
    frameSize=0
    def initialize(self):
        flag=int(input("Randomly Generate Refrence String?\n\t1: Yes(Default)\t2:No\n\t\tEnter Choice Code:"))
        if(flag==2):
            self.referenceString=input("Enter Refrence String:").split(" ")
            for value in self.referenceString:
                value=int(value)
            self.frameSize=int(input("Enter Number of Frames:"))
        else:
            self.numberOfProcess=int(randint(4,10)) 
            self.referenceString=[randint(1,self.numberOfProcess) for x in range(randint(10,25))]
            self.frameSize=randint(2,4)  
        self.ram=[0]*(self.frameSize)
        self.ramState=[[None for i in range(self.frameSize)] for j in range(len(self.referenceString))]
        print(f"Reference String:{self.referenceString}\nRam:{self.ram}")

    def saveRamState(self,rowNumber):
        for columnNumber in range(len(self.ram)):
            if self.ram[columnNumber]==0:
                self.ramState[rowNumber][columnNumber]=""
            else:
                self.ramState[rowNumber][columnNumber]=str(self.ram[columnNumber])

    def displayOutput(self,_title):
        _table=Table(title=_title,show_header=False,show_footer=True, box=box.ROUNDED)
        for i in range(len(self.referenceString)):
            _table.add_column(footer=self.hitFault[i])
        for row in zip(*self.ramState):
            _table.add_row(*row)
        console=Console()
        console.print(_table)
        print(f"Page Hits\t:{self.hitCounter}")
        print(f"Page Fault\t:{self.faultCounter}")

    def hit(self):
        self.hitFault.append("H")
        self.hitCounter+=1
    def fault(self):
        self.hitFault.append("*")
        self.faultCounter+=1


