from random import randint

class Process:
    totalExecutionTime=0
    averageTurnAroundTime=0
    averageWaitingTime=0
    def __init__(self,id,arrivalTime,burstTime):
        self.id=id
        self.arrivalTime=arrivalTime
        self.burstTime=burstTime
        self.waitingTime=0
        self.turnAroundTime=0
        self.executionTime=0
        self.completionTime=0
        self.responseTime=None
    
    def displayP(self):
        print(f"Process{self.id} \t {self.arrivalTime} \t\t {self.burstTime} \t\t {self.completionTime}  \t\t {self.waitingTime} \t\t {self.responseTime} \t\t {self.turnAroundTime}")            
    
    def displayNP(self):
        print(f"Process{self.id} \t {self.arrivalTime} \t\t {self.burstTime} \t\t {self.executionTime} \t\t {self.completionTime}  \t\t {self.waitingTime} \t\t {self.turnAroundTime}")            
    
    def reset(self):
        Process.totalExecutionTime=0
        Process.averageTurnAroundTime=0
        Process.averageWaitingTime=0
        self.waitingTime=0
        self.turnAroundTime=0
        self.executionTime=0
        self.completionTime=0
        self.responseTime=0
    
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
    
    def calculateExecutionTime(processList):
        for process in processList:
            process.executionTime=process.completionTime-process.burstTime
    
    def calculateCompletionTime(processList):
        pass
            
    def calculateWaitTime(processList):
        for process in processList:
            process.waitingTime=process.completionTime-process.burstTime-process.arrivalTime
            Process.averageWaitingTime+=process.waitingTime
        Process.averageWaitingTime/=len(processList)

    def calculateTurnAroundTime(processList):
        for process in processList:
            process.turnAroundTime=process.burstTime+process.waitingTime
            Process.averageTurnAroundTime+=process.turnAroundTime
        Process.averageTurnAroundTime/=len(processList)

    def calculateNP(processList):
        Process.calculateCompletionTime(processList)
        Process.calculateWaitTime(processList)
        Process.calculateTurnAroundTime(processList)
        
    def calculate(processList):
        Process.calculateWaitTime(processList)
        Process.calculateTurnAroundTime(processList)

    def displayOutputNP(processList):
        print("ProcessName \t ArrivalTime \t BurstTime \t ExecutionTime \t CompletionTime\t WaitingTime\t TurnAroundTime")
        for process in processList:
            process.displayNP()
        print(f"Average Waiting Time\t\t:{Process.averageWaitingTime}")
        print(f"Average Turn-Around Time\t:{Process.averageTurnAroundTime}")   
        print(f"Total Execution Time\t\t:{Process.totalExecutionTime}\n")
    def displayOutputP(processList):
        print("ProcessName \t ArrivalTime \t BurstTime \t CompletionTime\t WaitingTime\t ResponseTime\t TurnAroundTime")
        for process in processList:
            process.displayP()
        print(f"Average Waiting Time\t\t:{Process.averageWaitingTime}")
        print(f"Average Turn-Around Time\t:{Process.averageTurnAroundTime}")   
        print(f"Total Execution Time\t\t:{Process.totalExecutionTime}\n")
