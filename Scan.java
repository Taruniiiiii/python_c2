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


