#include <iostream>
#include "diskSchedulingAlgorithms.h"
using namespace std;

int main(){
    Disk disk;
    Table fcfs=disk.fcfs();
    Table sstf=disk.sstf();
    Table scan=disk.scan();
    Table look=disk.look();

    fcfs.display("FCFS");
    sstf.display("SSTF");
    scan.display("SCAN");
    look.display("LOOK");

    cout<<"-----------------"<<endl;
    cout<<"Average Seek Time"<<endl;
    cout<<"-----------------"<<endl;
    cout<<"FCFS\t:"<<fcfs.averageSeekTime<<endl;
    cout<<"SSTF\t:"<<sstf.averageSeekTime<<endl;
    cout<<"SCAN\t:"<<scan.averageSeekTime<<endl;
    cout<<"LOOK\t:"<<look.averageSeekTime<<endl;
    cout<<"-----------------"<<endl;

    return 0;
}
