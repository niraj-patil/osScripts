from Process import Process
"""
Creating processList
"""
processList=Process.createProcess()
complete=[]                             #List of Processes which have completed their execution
ready=[]                                #List of Processes in Ready Queue
"""
Reseting the Process's Attribute to Start Conditions
Uncomment when exporting the Program to a Function
This function will reset the changes made by other functions on the passed process list
"""
#for process in processList:
#    process.reset()
print("Shortest Job First-Non Preemptive")
"""
Sorting List such that we get Process with the lowest Arrival Time and Burst Time at index:0
"""
processList.sort(key=lambda x: x.burstTime)
processList.sort(key=lambda x: x.arrivalTime)
"""
Removing the 0th Element(lowest Arrival Time and Burst Time) from Process List and
Appending it to the Empty Ready List
"""
ready.append(processList.pop(0))
"""
while(there are processes in ready queue)
"""
while(len(ready)!=0):
    """
        if: Next process to arrive hasn't arrived yet(at currentExecutionTme)
            example:last process completed execution at 7
                but the next process arrived at 10
                Soo, the process will start its execution from 10 itself
        else:The process will start execution at currentExecutionTime
    """
    if ready[0].arrivalTime>Process.currentExecutionTime:
        ready[0].executionTime=ready[0].arrivalTime
    else:
        ready[0].executionTime=Process.currentExecutionTime
    """
        Updating CurrentExecutionTime as Process will occupy the CPU from ExecutionTime till its done with Execution
        And Updating the Completion Time to Current Execution Time
        Further, moving the process from ready list to complete list
    """
    Process.currentExecutionTime=ready[0].executionTime+ready[0].burstTime
    ready[0].completionTime=Process.currentExecutionTime
    complete.append(ready.pop(0))
    
    while(len(processList)>0):
        """
        Adding Processes from processList into the ready Queue
            while(there are processes in ready queue)
                (if):   pop the processes which have arrived(arrivalTime<=executionTime) and 
                        append them to the ready queue
                        Sorting the ready queue whenever new process is Added
                (else): break when no such process exist in processList(processes yet to arrive)
            end while(no processes in process list)      
        """
        if processList[0].arrivalTime<=Process.currentExecutionTime:
            ready.append(processList.pop(0))
            ready.sort(key=lambda x: x.burstTime)
        else:
            break
    """
    If the Ready Queue is Empty but there are still Processes yet to arrive
    Update the Ready Queue with the 0th Process(lowest Arrival Time and Burst Time)
    """
    if(len(ready)==0 and len(processList)>0):
        ready.append(processList.pop(0))
    
"""
Calculate Wait Time, Turn Around Time and Average Timings
"""
Process.calculate(complete)
"""
Non-Preemptive Algorithm: Wait Time == Response Time
"""
for process in processList:
    process.responseTime=process.waitingTime
"""
Display Output
"""
Process.displayOutputNP(complete)