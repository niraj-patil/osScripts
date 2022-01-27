from Process import Process

processList=Process.createProcess()
complete=[]
ready=[]

burstTime={}
for process in processList:
    burstTime.update({process.id:process.burstTime})


print("SJF(Preemptive)")
processList.sort(key=lambda x: x.burstTime)
processList.sort(key=lambda x: x.arrivalTime)
ready.append(processList.pop(0))
Process.totalExecutionTime=ready[0].arrivalTime
while(True):
    
    while(len(processList)>0):
        if processList[0].arrivalTime<=Process.totalExecutionTime:
            ready.append(processList.pop(0))
        else:
            break
    if(len(ready)==0 and len(processList)>0):
        ready.append(processList.pop(0))
        Process.totalExecutionTime=ready[0].arrivalTime
    if(len(ready)==0):
        break
    
    ready.sort(key=lambda x: x.burstTime)
    ready[0].burstTime-=1
    if(ready[0].burstTime==0):
        ready[0].completionTime=Process.totalExecutionTime+1
        complete.append(ready.pop(0))
    
    Process.totalExecutionTime+=1
    
    
    
    
for process in complete:
    process.burstTime=burstTime[process.id]
Process.calculate(complete)
Process.displayOutputP(complete)
