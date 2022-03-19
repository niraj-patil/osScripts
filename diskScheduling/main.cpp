#include <iostream>
#include <vector>
#include "diskSchedulingAlgorithms.h"
using namespace std;

int main(){
    Disk disk;
    Table fcfs=disk.fcfs();
    Table sstf=disk.sstf();
    Table scan=disk.scan();

    fcfs.display("FCFS");
    sstf.display("SSTF");
    scan.display("SCAN");

    cout<<"-----------------"<<endl;
    cout<<"Average Seek Time"<<endl;
    cout<<"-----------------"<<endl;
    cout<<"FCFS\t:"<<fcfs.averageSeekTime<<endl;
    cout<<"SSTF\t:"<<sstf.averageSeekTime<<endl;
    cout<<"SCAN\t:"<<scan.averageSeekTime<<endl;
    cout<<"-----------------"<<endl;
    
    return 0;
}
