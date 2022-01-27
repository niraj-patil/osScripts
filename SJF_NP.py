from Process import Process
processList=Process.createProcess()
complete=[]
ready=[]
for process in processList:
    process.reset()
processList.sort(key=lambda x: x.burstTime)
processList.sort(key=lambda x: x.arrivalTime)
ready.append(processList.pop(0))
while(len(ready)!=0):
    if ready[0].arrivalTime>Process.totalExecutionTime:
        ready[0].executionTime=ready[0].arrivalTime
    else:
        ready[0].executionTime=Process.totalExecutionTime
    Process.totalExecutionTime=ready[0].executionTime+ready[0].burstTime
    ready[0].completionTime=Process.totalExecutionTime
    complete.append(ready.pop(0))
    while(len(processList)>0):
        if processList[0].arrivalTime<=Process.totalExecutionTime:
            ready.append(processList.pop(0))
        else:
            break
    if(len(ready)==0 and len(processList)>0):
        ready.append(processList.pop(0))  
    ready.sort(key=lambda x: x.burstTime)
Process.calculate(complete)
for process in complete:
    process.responseTime=process.waitingTime
Process.displayOutput(complete)