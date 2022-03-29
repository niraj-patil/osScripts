import java.util.Scanner;

class ProducerConsumer{
   
    static Buffer buffer;
    public static void main(String []args){  
        Scanner scan=new Scanner(System.in);
        System.out.print("Enter Buffer Size:");
        int size=scan.nextInt();
        System.out.print("Enter Produce Count:");
        int pCount=scan.nextInt();
        System.out.print("Enter Consume Count:");
        int cCount=scan.nextInt();

        buffer= new Buffer(size);
        Thread producer=new Thread(new Producer(buffer,pCount));
        Thread consumer=new Thread(new Consumer(buffer,cCount));

        consumer.start();
        producer.start();

        scan.close();
    }
}
