#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <stdlib.h>
#include<time.h>
using namespace std;

class Table{
    public:
    float averageSeekTime=0,totalSeekTime=0;
    int* from;
    int* to;
    int* seekTime;
    int size;
        Table(int _size):from(new int[_size]), to(new int[_size]), seekTime(new int[_size])
        { size=_size;};
        void calculateSeekTime(){
            for(int i=0;i<size;i++){
                if(*(from+i)==NULL) continue;
                *(seekTime+i)=abs(*(from+i)-*(to+i));
                totalSeekTime+=*(seekTime+i);
            }
            averageSeekTime=totalSeekTime/size;
        }
        void display(string name){
            cout<<"\n<<"<<name<<">>";
            cout<<"\nFORM\tTO\tSEEKTIME\n";
            cout<<*(from)<<"\t"<<*(to)<<"\t"<<*(seekTime)<<"\n";
            for(int i=1;i<size;i++){
                if(*(from+i)==*(to+i)) continue;
                cout<<*(from+i)<<"\t"<<*(to+i)<<"\t"<<*(seekTime+i)<<"\n";
            }
            cout<<"Total Seek Time:"<<totalSeekTime<<endl;
            cout<<"Average Seek Time:"<<averageSeekTime<<endl;
        }
};

class Disk{
    vector <int> requestQueue;
    int start;
    bool directionMin;
    int diskSize=200;
    public:
    int size;
    Disk(){
        cout<<"1. Randomly Generate Requests(Default)\n2. Manually Enter Request\nEnter Choice:";
        int temp;
        cin>>temp;
        if (temp!=2){
            srand(time(0));
            cout<<"Enter Number of Requests:";
            cin>>size;
            for(int i=0;i<size;i++){
                requestQueue.push_back(rand()%diskSize);
            }
        }else{
            cout<<"Enter Request Queue:";
            while(true){
                int temp;
                cin>>temp;   
                requestQueue.push_back(temp);
                if(cin.get()=='\n')break;    
            }
            size=requestQueue.size();   
        }
        cout<<"1. Towards Minimum(default)\n2. Towards Maximum\nEnter Scanning Direction:";
        cin>>temp;
        directionMin=(temp!=2);
        cout<<"Enter Start Location:";
        cin>>start;  
    }

    int closest(vector<int> &vec, int value) {
        int i,j,_closest;
        bool allNull=true;
        for(i=0;i<size;i++){
            if(vec[i]==NULL) continue;
            if(vec[i]>value) break;
            if(vec[i]!=NULL) allNull=false;
        }      
        if(i==0 || allNull) {
            _closest=vec[i];
            vec[i]=NULL;
            return _closest;
            }
        else{
            for(j=i-1;j>=0;j--){
                if(vec[j]!=NULL) break;
            }
            if(abs(vec[i]-value)>abs(vec[j]-value)){
                _closest=vec[j];
                vec[j]=NULL;
            }
            else{
                _closest=vec[i];
                vec[i]=NULL;
            }
        }
        return _closest;
    }

    bool isVisited(vector <int> &vec,int end, int value){
        for(int i=end;i>=0;i--){
            if(vec[i]==value){return true;}
        }
        return false;
    }
    
    Table fcfs(){
        Table fcfs(size);
        int repeatFlag=0;
        float totalSeekTime=0,averageSeekTime;
        *fcfs.from=start;
        *fcfs.to=requestQueue[0];
        for(int i=1;i<size;i++){
            if(isVisited(requestQueue,i-1,requestQueue[i])||requestQueue[i]==start) {
                *(fcfs.from+i)=NULL;
                *(fcfs.to+i)=requestQueue[i];
                *(fcfs.seekTime+i)=0;
                repeatFlag++;
                continue;
            }
            if(repeatFlag!=0){
                *(fcfs.from+i)=requestQueue[i-1-repeatFlag];
                repeatFlag=0;
            }else{
                *(fcfs.from+i)=requestQueue[i-1];
            }
            *(fcfs.to+i)=requestQueue[i];
        }
        fcfs.calculateSeekTime();
        return fcfs;
    }
    Table sstf(){
        int _closest=start;
        Table sstf(size);
        vector<int> unvisited=requestQueue;
        sort(unvisited.begin(), unvisited.end());

        for(int i=0;i<size;i++){
            *(sstf.from+i)=_closest;
            _closest=closest(unvisited,_closest);
            *(sstf.to+i)=_closest;
        }
        sstf.calculateSeekTime();
        return sstf;
    }
    Table scan(){
        Table scan(size+1);
        vector<int> unvisited=requestQueue;
        int i,turn,k=0;
        sort(unvisited.begin(), unvisited.end());
        for(i=0;i<size;i++){
            if(unvisited[i]>start) break;
        }
        turn=i;
        if(directionMin) {
            if(i==0){
                if(start!=0){
                    *(scan.from+k)=start;
                    *(scan.to+k)=0;
                    k++;
                }  
            }else{
                i--;
                *(scan.from+k)=start;
                *(scan.to+k)=unvisited[i];
                k++;
                while(i>0){
                    *(scan.from+k)=unvisited[i];
                    *(scan.to+k)=unvisited[i-1];
                    k++;
                    i--;
                }
                *(scan.from+k)=unvisited[0];
                *(scan.to+k)=0;
                k++;  
            }
            *(scan.from+k)=0;
            *(scan.to+k)=unvisited[turn];
            k++;
            for(int j=turn;j<size-1;j++){
                *(scan.from+k)=unvisited[j];
                *(scan.to+k)=unvisited[j+1];
                k++;
            }      
        }
        else{
            if(i==size){
                if(start!=diskSize-1){
                    *(scan.from+k)=start;
                    *(scan.to+k)=diskSize-1;
                    k++;
                }  
            }else{
                *(scan.from+k)=start;
                *(scan.to+k)=unvisited[i];
                k++;
                while(i<size-1){
                    *(scan.from+k)=unvisited[i];
                    *(scan.to+k)=unvisited[i+1];
                    k++;
                    i++;
                }
                *(scan.from+k)=unvisited[i];
                *(scan.to+k)=diskSize-1;
                k++;  
            }
            turn--;
            *(scan.from+k)=diskSize-1;
            *(scan.to+k)=unvisited[turn];
            k++;
            for(int j=turn;j>0;j--){
                *(scan.from+k)=unvisited[j];
                *(scan.to+k)=unvisited[j-1];
                k++;
            } 
        }
        scan.calculateSeekTime();
        return scan;
    }
};