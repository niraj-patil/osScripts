from Process import Process

"""
Creating processList
"""
processList=Process.createProcess()
complete=[]                             #List of Processes which have completed their execution
ready=[]                                #List of Processes in Ready Queue
flag=False                              #Flag==True : Process is yet to complete its execution
                                        #Flag==False: Process has completed its execution

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
 
print("Round Robin")
"""
Time Quantum:Maximum Time Slice given to a process to execute in one cycle
"""
timeQuantum=int(input("Enter Time Quantum:"))    
"""
Sorting Process List According to Arrival Time
Removing the 0th Element(lowest Arrival Time) from Process List and
Appending it to the Empty Ready List
"""   
processList.sort(key=lambda x: x.arrivalTime)
ready.append(processList.pop(0))
"""
CPU will start actual execution when the first process arrives
"""
Process.currentExecutionTime=ready[0].arrivalTime

while(True):
    """
    Setting Response Time of the Process
    This will be executed just once per process
    As, after first update ResponseTime won't be equal to None(null)
    """
    if ready[0].responseTime==None:
        ready[0].responseTime=Process.currentExecutionTime-ready[0].arrivalTime
    """
    if(burstTime <= timeQuantum):
        The process will complete its execution in the current cycle
        Updating CurrentExecutionTime as Process will occupy the CPU till they complete their Execution
        When completed. Remove the process from Ready list and append it to the completed list
    else(burstTime> timeQuantum):
        The process will occupy the CPU for <timeQuantum> units of time
        Decrementing the burst time by <timeQuantum>
        Since, the process hasn't completed its execution, the flag is set True.
    """
    if ready[0].burstTime<=timeQuantum:
        Process.currentExecutionTime+=ready[0].burstTime
        ready[0].completionTime=Process.currentExecutionTime
        complete.append(ready.pop(0))
    else:
        Process.currentExecutionTime+=timeQuantum
        ready[0].burstTime-=timeQuantum   
        flag=True
    """
    Adding Processes from processList into the ready Queue
        while(there are processes in ready queue)
            (if):   pop the processes which have arrived(arrivalTime<=executionTime) and 
                    append them to the ready queue
            (else): break when no such process exist in processList(processes yet to arrive)      
    """
    while(len(processList)>0):
        if processList[0].arrivalTime<=Process.currentExecutionTime:
            ready.append(processList.pop(0))
        else:
            break
    """
    if  :Flag is True when the Current Process hasn't completed it's execution yet.
         In such a case: Pop the process from the front(current) 
         and append it to the back of the Ready "Queue"
         We need to use a Flag because we first need to append the newly arrived processes.
         Before inserting the old one.
         Resetting the Flag for next Cycle
    """
    if(flag):
        ready.append(ready.pop(0))
        flag=False
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
