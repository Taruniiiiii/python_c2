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



