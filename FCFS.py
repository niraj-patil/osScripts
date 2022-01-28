from Process import Process


"""
Creating processList
"""
processList=Process.createProcess()
print("FCFS")
"""
Reseting the Process's Attribute to Start Conditions
Uncomment when exporting the Program to a Function
This function will reset the changes made by other functions on the passed process list
"""
#for process in processList:
#    process.reset()

"""
Sorting Process List According to Arrival Time
"""
processList.sort(key=lambda x: x.arrivalTime)
"""
Running the loop for all the process in the processList
"""
for process in processList:
        """
        if: Next process to arrive hasn't arrived yet(at currentExecutionTme)
            example:last process completed execution at 7
                but the next process arrived at 10
                Soo, the process will start its execution from 10 itself
        else:The process will start execution at currentExecutionTime
        """
        if process.arrivalTime>Process.currentExecutionTime:
            process.executionTime=process.arrivalTime
        else:
            process.executionTime=Process.currentExecutionTime
        """
        Updating CurrentExecutionTime as Process will occupy the CPU from ExecutionTime till its done with Execution
        And Updating the Completion Time to Current Execution Time
        """
        Process.currentExecutionTime=process.executionTime+process.burstTime
        process.completionTime=Process.currentExecutionTime
"""
Calculate Wait Time, Turn Around Time and Average Timings
"""
Process.calculate(processList)
"""
Non-Preemptive Algorithm: Wait Time == Response Time
"""
for process in processList:
    process.responseTime=process.waitingTime
"""
Display Output
"""
Process.displayOutputNP(processList)


