public class Semaphore {
    int semaphore;
    Semaphore(int i){
        semaphore=i;
    }
    public void wait_(){
        while(semaphore<=0);
        semaphore--;
    }
    public void signal(){
        semaphore++;
    }
}
