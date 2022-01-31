from random import randint

class Process:
    currentExecutionTime=0                #Total Time CPU was under execution
    averageTurnAroundTime=0             
    averageWaitingTime=0
    def __init__(self,id,arrivalTime,burstTime):
        self.id=id						#Uniquely identifies the Process
        self.arrivalTime=arrivalTime	#Time at which process arrived into the system	
        self.burstTime=burstTime		#Amount of Time Required for a Process to complete its execution	
        self.waitingTime=0				#Amount of Time Process was in Ready Queue
        self.turnAroundTime=0			#Amount of Time Process was in the System
        self.executionTime=0			#Time at which Process started its execution
        self.completionTime=0			#Time at which Process completes its execution	
        self.responseTime=None			#Time at which Process entered into Running State for the first time.
        								#WaitTime==ResponseTime in case of Non-Preemptive Algorithms
    
    """
    Display Process Values
    """
    def displayP(self):
        print(f"Process{self.id} \t {self.arrivalTime} \t\t {self.burstTime} \t\t {self.completionTime}  \t\t {self.waitingTime} \t\t {self.responseTime} \t\t {self.turnAroundTime}")            
    
    def displayNP(self):
        print(f"Process{self.id} \t {self.arrivalTime} \t\t {self.burstTime} \t\t {self.executionTime} \t\t {self.completionTime}  \t\t {self.waitingTime} \t\t {self.turnAroundTime}")            
    
    """
    The reset function resets all values except the id, arrivalTime and burstTime.
    This function can be used to pass same start conditions to different algorithms.
    """
    def reset(self):
        Process.currentExecutionTime=0
        Process.averageTurnAroundTime=0
        Process.averageWaitingTime=0
        self.waitingTime=0
        self.turnAroundTime=0
        self.executionTime=0
        self.completionTime=0
        self.responseTime=None
    
    """
    Creates processList
    """
    def createProcess():
        flag=int(input("0-User Input \n1-Random Values\nPlease Enter Your Choice Code:"))==1
        n=int(input("Enter Number of Process:"))
        if flag:
            processList=[Process(i,randint(0,10),randint(1,10))for i in range (n)]
            print("Process Generated\nProcessName \t ArrivalTime \t BurstTime")
            for i in processList:
                print(f"Process{i.id} \t {i.arrivalTime} \t\t {i.burstTime}")
            print("\n\n")
        else:
            processList=[]
            for i in range (n):
                arrivalTime, burstTime=[int(x) for x in input(f"Enter Arrival Time and Burst Time for Process{i}:").split()]
                processList.append(Process(i,arrivalTime,burstTime))
        return processList
    
    """
    Execution Time= Completion Time - Burst Time
    """
    def calculateExecutionTime(processList):
        for process in processList:
            process.executionTime=process.completionTime-process.burstTime
    
    """
    Wait Time= Completion Time - Burst  Time - Arrival Time
    """        
    def calculateWaitTime(processList):
        for process in processList:
            process.waitingTime=process.completionTime-process.burstTime-process.arrivalTime
            Process.averageWaitingTime+=process.waitingTime
        Process.averageWaitingTime/=len(processList)
	
    """
    Turnaround Time= Burst Time + Waiting Time
    """
    def calculateTurnAroundTime(processList):
        for process in processList:
            process.turnAroundTime=process.burstTime+process.waitingTime
            Process.averageTurnAroundTime+=process.turnAroundTime
        Process.averageTurnAroundTime/=len(processList)

    """
    Single Call to all the Calculation Functions
    """
    def calculate(processList):
        Process.calculateWaitTime(processList)
        Process.calculateTurnAroundTime(processList)

    """
    Displays Final Output
    """
    def displayOutputNP(processList):
        print("ProcessName \t ArrivalTime \t BurstTime \t ExecutionTime \t CompletionTime\t WaitingTime\t TurnAroundTime")
        for process in processList:
            process.displayNP()
        print(f"Average Waiting Time\t\t:{Process.averageWaitingTime}")
        print(f"Average Turn-Around Time\t:{Process.averageTurnAroundTime}")   
        print(f"Total Execution Time\t\t:{Process.currentExecutionTime}\n")
    def displayOutputP(processList):
        print("ProcessName \t ArrivalTime \t BurstTime \t CompletionTime\t WaitingTime\t ResponseTime\t TurnAroundTime")
        for process in processList:
            process.displayP()
        print(f"Average Waiting Time\t\t:{Process.averageWaitingTime}")
        print(f"Average Turn-Around Time\t:{Process.averageTurnAroundTime}")   
        print(f"Total Execution Time\t\t:{Process.currentExecutionTime}\n")
