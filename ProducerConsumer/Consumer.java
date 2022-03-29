public class Consumer implements Runnable{
    Buffer buffer;
    int count;
    Consumer(Buffer _buffer,int _count){
        buffer=_buffer;
        count=_count;
    }
    public void run(){
        for(int i=0;i<count;i++){
            buffer.full.wait_();
            buffer.m.wait_(); 
            consume(buffer);
            buffer.m.signal(); 
            buffer.empty.signal(); 
        }
        }
        static void consume(Buffer buffer){
            buffer.remove();                                                                                
        }
    }
