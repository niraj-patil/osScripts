from Process import Process

processList=Process.createProcess()
print("FCFS")
for process in processList:
    process.reset()
processList.sort(key=lambda x: x.arrivalTime)
for process in processList:
        if process.arrivalTime>Process.totalExecutionTime:
            process.executionTime=process.arrivalTime
        else:
            process.executionTime=Process.totalExecutionTime
        Process.totalExecutionTime=process.executionTime+process.burstTime
        process.completionTime=Process.totalExecutionTime
#Calculations and Output
Process.calculate(processList)
for process in processList:
    process.responseTime=process.waitingTime
Process.displayOutputNP(processList)


