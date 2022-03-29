public class Producer implements Runnable{
    Buffer buffer;
    int count;
    Producer(Buffer _buffer,int _count){
        buffer=_buffer;
        count=_count;
    }
    public void run(){
        for(int i=0;i<count;i++){
            buffer.empty.wait_();
            buffer.m.wait_();
            produce(buffer);
            buffer.m.signal();
            buffer.full.signal();
            }
    }
    static void produce(Buffer buffer){  
                buffer.add(1);
            }
    }
    
