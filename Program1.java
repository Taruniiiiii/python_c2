package Mod1;
public class Program1
{
    //static variable
    static int x=20;
    static String name1="hello";

    //non-static
    int z;
    String name3="Good"
    public static void main(String[]args)
    {
    //variable declaration
    String name;
    int age;
    //variable initialization

    name="hello";
    age=21;
    System.out.println(age);

    //variable declaration and initialization
    String a ="java";

    //fetching the data
    System.out.println(name);
    System.out.println(age);
    System.out.println(a);

    //duplicate variables are not allowed
    //String name ="tar"

}
System.out.println

package com.taruni;

public class Animal {
	String name;
	int legs;
	String color;
	
	public void eat() {
		System.out.println("all the dogs bark");
	}
	public void sleep() {
		System.out.println("all the dogs sleep");
		
	}


}

class Dogs extends Animal
{
	String breed;
	int age;
	
	public void toBark()
	{
		System.out.println("all the dogs barks");
	}
	
	public void toProtect()
	{
		System.out.println("all the dogs protect");
	}

		
}
class Mains
{
	public static void main(String[] args)
	{
		Dogs d=new Dogs();
		System.out.println(d.age);
		System.out.println(d.name);
		System.out.println(d.color);
		System.out.println(d.breed);
		System.out.println(d.legs);
		
		d.toBark();
		d.toProtect();
		d.sleep();
		d.eat();
	}
}



class Vehicle
{
    String brand;

    public void start()
    {
        System.out.println("Vehicle starts");
    }
}

// Specialized Class
class Car extends Vehicle
{
    int doors;

    public void drive()
    {
        System.out.println("Car is driving");
    }
}

// Specialized Class
class Bike extends Vehicle
{
    public void ride()
    {
        System.out.println("Bike is riding");
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Car c = new Car();
        c.brand = "BMW";

        c.start();
        c.drive();

        Bike b = new Bike();
        b.brand = "Honda";

        b.start();
        b.ride();
    }
}

package src;

public class Father 
{
	public void houseColor()
	{
		System.out.println("the color of the house is yellow");
		
	}

}
class Son extends Father
{
	@Override
	public void houseColor()
	{
		System.out.println("son changed the color to pink");
	}
}
class Drive
{
	public static void main(String[] args)
	{
		Son s=new Son();
		s.houseColor();
		
		Father f=new Son();
		f.houseColor();
	}
	
}

//how to acurie abstact class
package src;

abstract class Demo1 
{
	//a method without the  method body
	abstract public void m1();

}
class Childs extends Demo1
{
	//by overriding we will be providing the implementation in the child class
	@Override
	public void m1()
	{
		System.out.println("here we are giving the implementation");
	}
}
class ChildDriver
{
	public static void main(String[] args)
	{
		Childs c1=new Childs();
		c1.m1();
	}
}

//training


public class int1 
{
	//before java version 8
	//final Variable
	//by default all the variable are public static final
	public static final double pi=3.14;
	int age=22;
	
	//abstract method
	
	public void m1()
	
	//by default the method is abstract
	abstract void m2()
	
	//after java version 8
	
	public static void m3()
	{
		System.out.println("this is a default method");
	}
	//default method (non-static methods prefixed with default kwyword
	
	default void m4()
	{
		System.out.println("thi is a default method");
	}
	

}
class Ch1 implements Int1
{
	public void m1()
	{
		System.out.println("m1() implemented");
	}
	public void m2()
	{
		System.out.println("m2() implemented");
	}
}
class Int1Driver
{
	public static void main(String[] args)
	{
		 //===>> WE CANNOT CREATE CLASS AN OBJECT FOR AN INTERFACE
		 //====>>  WE CANNOT CREATE AN OBJECT FOR AN ABSTRACT CLASS
		//Int1 obj1 = new Int1();

	}
}

//EXCEPTIONS
//NullPointerException
package src;

public class Java1 
{
	public static void main(String[] args) {
		System.out.println("this is start");
		try
		{
			//here we are the risky line of code
			String s=null;
			System.out.println(s.length());
			
		}
		catch(NullPointerException n)
		{
			n.printStackTrace();
		}
		System.out.println("This is end");
	}
}


//ArithmeticException
package src;

public class Java1 
{
	public static void main(String[] args) {
		System.out.println("this is start");
		try
		{
			//here we are the risky line of code
			int a=10;
			int b=20;
			
			System.out.println(a/b);
			
		}
		catch(ArithmeticException e)
		{
			e.printStackTrace();
		}
		System.out.println("This is end");
	}
}
