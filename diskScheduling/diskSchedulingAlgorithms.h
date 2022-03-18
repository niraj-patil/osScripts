#include <iostream>
#include <vector>
#include <bits/stdc++.h>
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
            cout<<"<<"<<name<<">>";
            cout<<"\nFORM\tTO\tSEEKTIME\n";
            for(int i=0;i<size;i++){
                cout<<*(from+i)<<"\t"<<*(to+i)<<"\t"<<*(seekTime+i)<<"\n";
            }
            cout<<"Total Seek Time:"<<totalSeekTime<<endl;
            cout<<"Average Seek Time:"<<averageSeekTime<<endl;
        }
};

class Disk{
    vector <int> requestQueue;
    int start;
    public:
    int size;
    Disk(){
        cout<<"Enter Request Queue:";
        while(true){
            int temp;
            cin>>temp;   
            requestQueue.push_back(temp);
            if(cin.get()=='\n')break;    
        }


        size=requestQueue.size();

        cout<<"Enter Start Location:";
        cin>>start;  
    }

    int closest(vector<int> &vec, int value) {
        int j,temp,_closest,index;
        for(j=0;j<size;j++){
            if(vec[j]==NULL) continue;
            else{
                temp=abs(vec[j]-value);
                _closest=vec[j];
                break;
            }
        }
        for(int i=j+1;i<size-j-1;i++){
            if(vec[i]==NULL) continue;
            if(abs(vec[i]-value)<temp){
                temp=abs(vec[i]-value);
                _closest=vec[i];
                j=i;
            } 
            if(abs(vec[i+1]-value)>=temp) break;
        }      
        vec[j]=NULL;
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
        int _closest;
        Table sstf(size);
        vector<int> unvisited=requestQueue;
        sort(unvisited.begin(), unvisited.end());
        _closest=start;
        for(int i=0;i<size;i++){
            if(isVisited(requestQueue,i-1,requestQueue[i])||requestQueue[i]==start) {
                    *(sstf.from+i)=NULL;
                    *(sstf.to+i)=requestQueue[i];
                    *(sstf.seekTime+i)=0;
                    continue;
                }
           
            *(sstf.from+i)=_closest;
            _closest=closest(unvisited,_closest);
            *(sstf.to+i)=_closest;
            cout<<">"<<_closest<<endl;
        }
        sstf.calculateSeekTime();
        return sstf;
    }
};