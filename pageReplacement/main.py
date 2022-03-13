
from pageFrame import PageReplacer
from pageReplacementAlgorithms import *
from rich.console import Console
from rich.table import Table
_pageReplacer=PageReplacer()
_pageReplacer.initialize()

_table=Table(title="Select Algorithm")
_table.add_column(header="Choice Code")
_table.add_column(header="Algorithm")
_table.add_row("1","FIFO(Default)")
_table.add_row("2","LRU")
_table.add_row("3","Optimal")
Console().print(_table)
code=int(input("Enter Choice Code:"))
if(code==2):
    object=LRU()
elif(code==3):
    object=Optimial()
else:
    object=FIFO()
object.replace(_pageReplacer)
_pageReplacer.displayOutput(object.NAME)