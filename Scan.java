"""package src;
class Arithmetic{
    int a=12,b=13;
    System.out.println("addition:"+ (a+b));
    System.out.println((a-b));
    System.out.println((a*b));
    System.out.println((a/b));
    System.out.println((a%b));


}
public static void main(String[] args){
    float f=13.56f;
    int i;
    i=f;
    System.out.println(i);
    System.out.println(f);

}
class Arithmetic {
    public static void main(String[] args) {
        int a = 12;
        int b = 13;

        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));
    }
}
class RelationalOperator {
    public static void main(String[] args) {
        int a=12;
        int b=13;

        System.out.println(a == b);
        System.out.println (a != b);
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a >= b);
        System.out.println(a <= b);
    }
}

class Logic {
    public static void main(String[] args) {
        int a=12;
        int b=13;

        System.out.println(a>=b && a==b);
        System.out.println(a!=b || a<b);
        System.out.println(!(a==b));

    }
}
class Bitwise {
    public static void main(String[] args) {
        int a=12;
        int b=13;

        System.out.println(a&b);
        System.out.println(a|b);
        System.out.println(~a);
        System.out.println(~b);
        

    }
}

package Pack1;
import java.util.Scanner;
public class Scan
{
    public class Scan void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the first number");
        int num1=sc.nextInt();
        System.out.println("enter the second number");
        int num2=sc.nextInt();
        int res=num1+num2;
        
        System.out.println("the res is "+res);
        System.out.println("enter yopr name");
        String name =sc.next();
        System.out.println(name);
        
        System.out.println("enter the sentencce");
        String name2=sc.nextLine();
        System.out.println(name2);
        
        String name2=sc.nextLine();
        System.out.println(name2);
        
    }
}


class inbuilt{
    public static void main(String[] args){
        String a="  taruni Medishetty";
        System.out.println(a.length());
        System.out.println(a.charAt(5));
        System.out.println(a.toUpperCase());
        System.out.println(a.toLowerCase());
        System.out.println(a.trim());
    }
}"""


class conditionals{
    public static void main(String[] args) {
        int a=21;
        int b=12;
        if(a>b){
            System.out.println("a is greater");
        }
    }
}


import java.util.Scanner;

class conditionals{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);//object
        System.out.println("enter your age");
        int age=sc.nextInt();//method
        if(age>=18){
            System.out.println("You are eligible to vote");
        }
        else{
            System.out.println("You are NOT eligible to vote");
        }
            
    }
    
}


class vote{
    public static void main(String[] args) {
        boolean courage=true;
        boolean single=true;
        
        if(courage==true)
        {
            System.out.println("first condition satisfies");
            if(single==true)
            {
                System.out.println("con 2 sat");
            }
        }
        else{
            System.out.println("both con are not satisfied");
        }
    }
}



import java.util.Scanner;

class SwitchExample {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);//obj

        System.out.print("Enter a num: ");
        int choice=sc.nextInt();//method

        switch(choice) {
            case 1:
                System.out.println("money is deposited");
                break;//pause the execution if condiotion is true
            case 2:
                System.out.println("withdraw the money");
                break;
            case 3:
                System.out.println("check balance");
                break;
            case 4:
                System.out.println("exit");
                break;

            default:
                System.out.println("Invalid Choice");
        }

    }
}
//loops
public class stars
{
    public static void main(String[] args)
    {
        for(int i=1;i<=5;i++)
        {
            System.out.println("*");
        }
    }
}

//table
public class table
{
    public static void main(String[] args){
    int i=1;
    while(i<=10){
        System.out.println("5"+"*"+i+"="+ 5*i);
        i++;
    }
}
}
public class Arr1
{
    public static void main(String[] args){
    int [] arr1=new int[5];
    arr1[0]=10;
    arr1[1]=20;
    arr1[2]=30;
    arr1[3]=40;
    arr1[4]=50;
    //arr[5]=60;
    for(int i=0;i< arr1.length;i++){
        System.out.println(arr1[i]);
    }
    
    
    
    
    }
}

//assignment q1
public class Count{
    public static void main(String[] args) {
       int[] arr2={10,20,30,40,50,60};
       System.out.println(arr2.length);
    }
}

//q2 sum
public class Addition{
    public static void main(String[] args) {
       int[] arr2={10,20,30,40,50,60};
       int sum=0;
       for(int i=0;i<arr2.length;i++){
        sum+=arr2[i];
       }
        System.out.println(sum);
       }
    }

//q3 product

public class Multiplication{
    public static void main(String[] args) {
       int[] arr2={10,20,30,40,50,60};
       int product=1;
       for(int i=0;i<arr2.length;i++){
        product*=arr2[i];
       }
        System.out.println(product);
       }
    }

//18th
public class Met1
{
    public static void main(String[] args)
    {
        System.out.println("start");
        //method call sattement
        m1();
        m1();
        m2(10,20);//METHOD CALL M1
        //actual argument is the data or value that is stored informL Argument i.e variable
        System.out.println("end");
    }
    public static void m1()
    {
        System.out.println("this is m1 method");
    }
    //formal argument is the variable declaration
    //we can have n no.of formal arguments
    public static void m2(int a,int b)
    {
        System.out.println(a+b);
    }
}

public class Met1
{
    public static void main(String[] args)
    {
        System.out.println("start");
        //method call sattement
        m1();
        m1();
         //actual argument is the data or value that is stored informL Argument i.e variable
        m2(10,20);
        System.out.println(m4(70,22));
        System.out.println(m3("taruni"));
        String result=m3("java");
        System.out.println(result);
        
        //METHOD CALL M1
       
        System.out.println("end");
    }
    public static void m1()
    {
        System.out.println("this is m1 method");
    }
    //formal argument is the variable declaration
    //we can have n no.of formal arguments
    public static void m2(int a,int b)
    {
        System.out.println(a+b);
    }
    public static String m3(String name1)
    {
        return name;
        //return name2;
        
    }
    public static int m4(int x,int y)
    {
        return x+y;
        System.out.println("hello");
    }
}

//19
class Stat
{
    //static variables
    static int age;
    static String name;
    static double price;
    //single line static initializer
    
    static String name1="java";
    //static method
    public static void main(String[] args)
    {
        System.out.println("this is a static method");
    }
    //multiline static initializer
    static
    {
        System.out.println("this is amultiline static intializer");
        System.out.println("age");
        System.out.println("price");
        System.out.println("name");
        System.out.println("name1");
    }
}


public class Phone
{
    String brand;
    double price;
    String color;
    
}

//stack
package src;
public class stack {
	int top=-1;
	int[] stack=new int[5];
	
	//push
	void push(int data)
	{
		if (top==stack.length-1)
		{
			System.out.println("stack overflow");
		}
		else {
			//move from -1 to 0th index position
			top++;
			stack[top]=data;
			System.out.println(data+"inserted");
		}
	}
void display()
{
    if(top == -1)
    {
        System.out.println("Stack is Empty");
    }
    else
    {
        for(int i = top; i >= 0; i--)
        {
            System.out.println(stack[i]);
        }
    }
}
void peek()
{
	if(top==-1)
	{
		System.out.println("no element in stack");
	}
	System.out.println("top ele is"+stack[top]);
}
void pop()
{
    if(top == -1)
    {
        System.out.println("Stack Underflow");
    }
    else
    {
        //the top most ele is removed
        System.out.println("Removed or popped Element is: " + stack[top]);
        //you have to move one step behind
        top--;
    }
}
public static void main(String[] args)
{
	stack s=new stack();
	s.push(10);
	s.push(20);
	s.push(30);
	s.push(40);
	s.push(50);
	s.peek();
	s.pop();

}
}

//node
package src;

class Node
{
    int data;
    Node next;

    Node(int data)
    {
        this.data = data;
        this.next = null;
    }
}

public class StackLL
{
    Node top = null;

    // Push
    void push(int data)
    {
        Node newNode = new Node(data);

        if(top == null)
        {
            top = newNode;
        }
        else
        {
            newNode.next = top;
            top = newNode;
        }

        System.out.println(data + " inserted");
    }

    // Pop
    void pop()
    {
        if(top == null)
        {
            System.out.println("Stack is Empty");
        }
        else
        {
            System.out.println(top.data + " deleted");
            top = top.next;
        }
    }

    // Peek
    void peek()
    {
        if(top == null)
        {
            System.out.println("Stack is Empty");
        }
        else
        {
            System.out.println("Top Element = " + top.data);
        }
    }

    // Display
    void display()
    {
        if(top == null)
        {
            System.out.println("Stack is Empty");
        }
        else
        {
            Node temp = top;

            while(temp != null)
            {
                System.out.println(temp.data);
                temp = temp.next;
            }
        }
    }

    // Main Method
    public static void main(String[] args)
    {
        StackLL s = new StackLL();

        s.push(10);
        s.push(20);
        s.push(30);

        System.out.println("\nStack Elements:");
        s.display();

        System.out.println();
        s.peek();

        System.out.println();
        s.pop();

        System.out.println("\nStack After Pop:");
        s.display();
    }
}

//hashing
package src;

class Node
{
    int key;
    String value;
    Node next;

    Node(int key, String value)
    {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}

public class HashMapDSA
{
    // Hash Table (Array of Linked Lists)
    Node[] table = new Node[10];

    // Hash Function
    int hashFunction(int key)
    {
        return key % table.length;
    }

    // Insert Operation
    void insert(int key, String value)
    {
        int index = hashFunction(key);

        Node newNode = new Node(key, value);

        // If bucket is empty
        if(table[index] == null)
        {
            table[index] = newNode;
        }
        else
        {
            // Collision occurred
            Node temp = table[index];

            while(temp.next != null)
            {
                temp = temp.next;
            }

            temp.next = newNode;
        }

        System.out.println(key + " inserted successfully.");
    }

    // Display Hash Table
    void display()
    {
        for(int i = 0; i < table.length; i++)
        {
            System.out.print("Bucket " + i + ": ");

            Node temp = table[i];

            while(temp != null)
            {
                System.out.print("(" + temp.key + "," + temp.value + ") -> ");
                temp = temp.next;
            }

            System.out.println("NULL");
        }
    }

    // Search Operation
    void search(int key)
    {
        int index = hashFunction(key);

        Node temp = table[index];

        while(temp != null)
        {
            if(temp.key == key)
            {
                System.out.println("Key Found");
                System.out.println("Value = " + temp.value);
                return;
            }

            temp = temp.next;
        }

        System.out.println("Key Not Found");
    }

    // Main Method
    public static void main(String[] args)
    {
        HashMapDSA obj = new HashMapDSA();

        obj.insert(10, "Taruni");
        obj.insert(20, "Anu");
        obj.insert(30, "Ravi");
        obj.insert(40, "Sai");
        obj.insert(11, "Priya"); // Collision with key 1 if table size changes accordingly

        System.out.println("\nHash Table:");
        obj.display();
        

        System.out.println();
        obj.search(20);
        obj.search(50);
    }
}