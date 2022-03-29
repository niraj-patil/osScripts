public class Buffer{
	Integer [] buffer;
	Semaphore m=new Semaphore(1),full=new Semaphore(0),empty;
	int front=-1,end=-1;
	Buffer(int size){
		buffer = new Integer[size];
		empty=new Semaphore(size);
	}
	public void add(int data){
		if ((front == 0 && end == buffer.length-1) || (front == end+1))  
		{  
			System.out.println("Buffer Overflow");  
			return;  
		} 
		if (front == -1)  
            {  
                front = 0;  
                end = 0;  
            }  
		else  
		{  
			if (end == buffer.length - 1)  
				end = 0;  
			else  
				end = end + 1;  
		}  
        buffer[end] = data ; 
		System.out.println("Data Produced");  
	}
	public void remove(){
		if (front == -1)  
            {  
                System.out.println("Queue Underflow");  
                return ;  
            }  
            System.out.println("Data Consumed");  
            if (front == end)  
            {  
                front = -1;  
                end = -1;  
            }  
            else  
            {  
                if (front == buffer.length - 1)  
                    front = 0;  
                else  
                    front = front + 1;  
            }  
	}

	public void display(){
		int temp=front;
		if (front == -1)  
		{  
			System.out.println("Queue is empty");  
			return;
		}  
		System.out.print("Buffer Elements:");
		if (front <= end)  
		{  
			while (front <= end)  
			{  
				System.out.print(buffer[front]+" ");
				front++;  
			}
		}  
		else  
		{  
			while (front <= buffer.length - 1)  
			{  
				System.out.print(buffer[front]+" ");  
				front++;  
			}  
			front = 0;  
			while (front <= end)  
			{  
				System.out.print(buffer[front]+" ");  
				front++;  
			}  
			
		}  
		System.out.println();
		front=temp;
	}

}