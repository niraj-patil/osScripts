#include <iostream>
#include <vector>
#include "diskSchedulingAlgorithms.h"
using namespace std;

int main(){
    Disk disk;
    Table fcfs=disk.fcfs();
    Table sstf=disk.sstf();

    fcfs.display("FCFS");
    sstf.display("SSTF");
    
    cout<<"Average Seek Time"<<endl;
    cout<<"-----------------"<<endl;
    cout<<"FCFS\t:"<<fcfs.averageSeekTime<<endl;
    cout<<"SSTF\t:"<<sstf.averageSeekTime<<endl;
    cout<<"-----------------"<<endl;
    
    return 0;
}
