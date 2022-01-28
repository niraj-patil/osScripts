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
"""
Saving Original Burst Time in a Dictionary
As we are going to overwrite them in the Algorithm
"""
burstTime={}
for process in processList:
    burstTime.update({process.id:process.burstTime})


print("SJF(Preemptive)")
"""
Sorting List such that we get Process with the lowest Arrival Time and Burst Time
"""
processList.sort(key=lambda x: x.burstTime)
processList.sort(key=lambda x: x.arrivalTime)
"""
Removing the 0th Element(lowest Arrival Time and Burst Time) from Process List and
Appending it to the Empty Ready List
"""
ready.append(processList.pop(0))
"""
CPU will start actual execution when the first process arrives
"""
Process.currentExecutionTime=ready[0].arrivalTime

while(True):
    """
    Adding Processes from processList into the ready Queue
    Algorithm:
        while(there are processes in ready queue)
            (if):   pop the processes which have arrived(arrivalTime<=executionTime) and 
                    append them to the ready queue
                    Sorting the ready queue whenever new process is Added
            (else): break when no such process exist in processList(processes yet to arrive)
        end while(no processes in process list)
            
    """
    while(len(processList)>0):
        if processList[0].arrivalTime<=Process.currentExecutionTime:
            ready.append(processList.pop(0))
            ready.sort(key=lambda x: x.burstTime)
        else:
            break
    """
    If the Ready Queue is Empty but there are still Processes yet to arrive
    Update the Ready Queue with the 0th Process(lowest Arrival Time and Burst Time)
    Update the currentExecutionTime to cover the CPU Ideal Time
        example:last process completed execution at 7
                but the next process arrived at 10
                CPU is ideal for 3units. So we update currentExecutionTime from 7 to 10
    """
    if(len(ready)==0 and len(processList)>0):
        ready.append(processList.pop(0))
        Process.currentExecutionTime=ready[0].arrivalTime
    """
    break when ready queue is empty
    this will be hit only if the processList is also empty
    As the earlier blocks checks if there are processes in process queue or not
    """
    if(len(ready)==0):
        break
    
    """
    Setting Response Time of the Process
    This will be executed just once per process
    As, after first update ResponseTime won't be equal to None(null)
    """
    if(ready[0].responseTime==None):
        ready[0].responseTime=Process.currentExecutionTime-ready[0].arrivalTime
    """
    Reducing BurstTime of Process under execution by 1
    """
    ready[0].burstTime-=1
    """
    Checking if process has completed its execution
    if true:    update completionTime and move the process to complete list
    if false:   do nothing
    """
    if(ready[0].burstTime==0):
        ready[0].completionTime=Process.currentExecutionTime+1
        complete.append(ready.pop(0))
    """
    Incrementing Time Counter(Total Execution Time)
    """
    Process.currentExecutionTime+=1
    
    
    
"""
Resetting the BurstTime to original values
"""  
for process in complete:
    process.burstTime=burstTime[process.id]

"""
Resetting Original List
Uncomment when exporting the Program to a Function
This is to make the original list usable by other functions
"""
#processList=complete
"""
Calculate Wait Time, Turn Around Time and Average Timings
"""
Process.calculate(complete)
"""
Display Output
"""
Process.displayOutputP(complete)
