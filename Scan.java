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

