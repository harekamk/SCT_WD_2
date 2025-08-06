#include<iostream>
using namespace std;
// int main(){
//     for(int i=0;i<=10;i++){
//         cout<<i<<endl;
//     }
//     return 0;
// }

// int main(){
//     int i=1;
//     while(i<=10){
//         cout<<i<<endl;
//         i++;
//     }
// }

// int main(){
//     int i=1;
//     do{
//         cout<<i<<endl;
//         i++
//     }while(i<=10);
// }

// int main(){

//     for(int i=1;i<=25;i+=2){
//          cout<<i<<endl;
//      }
//      return 0;
//      }

// int main(){
//     for(int i=1;i<=25;i++){
//         if(i==15){
//             break;

//         }
//         cout<<i<<endl;
//     }
// }

// int main()
// {
//     int i,j;
// cout<<"enter n:";
// cin>>n;
//     for(i=1;i<=3;i++){
//         for(j=1;j<=3;j++){
//             cout<<i;
//         }
//         cout<<endl;
//     }

//     return 0;
// }


// int main()
// {
//     int i,j,n;
//     cout<<"n:";
//     cin>>n;
//     for(i=1;i<=n;i++){
//         for(j=1;j<=i;j++){
//             cout<<j;
//         }
//         cout<<endl;
//     }

//     return 0;
// }

classes and objects

// #include <iostream>
// using namespace std;
// class Account{
//     private:
//     int balance;
//     public:
//     void setbalance(int b){
//         balance=b;
//     }
//     int getbalance(){
//         return balance;
//     }
// };

// int main()
// {
//     Account a;
//     a.setbalance(1000);
//     cout<<"balance="<<a.getbalance();
    

//     return 0;
// }

// class Box{
    //     public:
    
        
    //       int length;
    //       int width;
    //       int area(){
    //           return length*width;
    //       }
    // };
    // int main(){
    //     Box b1;
    //     b1.length=5;
    //     b1.width=3;
    //     cout<<"Area:"<<b1.area()<<endl;
    // }
    dot operator connects object with the member of the class

// class Person{
//         public:
//         string name;
//         Person(string n){
//             name=n;
//         }
//     };
//     int main(){
//         Person p("Alice");
//         cout<<p.name<<endl;
//     }

::= scope resolution

// namespace A{
//     int value=10;
// }
// namespace B{
//     int value=20;
// }
// int main(){
//     cout<<A::value<<endl;
//     cout<<B::value<<endl;
// }

// namespace info{
//     string name="hello";
// }
// int main(){
//     using namespace info;
//     cout<<name<<endl;
// }

// class Car{
//     public:
//     void display();
// };
// void Car::display(){
//     cout<<"car class";
// }
// int main(){
//     Car c;
//     c.display();
// }

// class Outer{
//     public:
//     class Inner{
//         public:
//         void show(){
//             cout<<"inner class";
//         }
//     };
// };
// int main(){
//     Outer::Inner obj;
//     obj.show();
// }

// class Demo{
//     public:
//     Demo(){
//         cout<<"Constructor called";
//     }
// };
// int main(){
//     Demo d1;
    
// }

struct and class help define data types
namespace resolves name conflicts
class: access modifiers, constructors, object creation

// class Animal{
//     public:
//     void sound(){
//         cout<<"Animals make sounds"<<endl;
//     }
// };
// class Dog: public Animal{
//     public:
//     void bark(){
//         cout<<"Dogs bark"<<endl;
//     }
// };

// int main()
// {
//     Dog d;
//     d.sound();
//     d.bark();

//     return 0;
// }


Single inheritance code
// class Person{
//     public:
//     void func1(){
//         cout<<"I am a person"<<endl;
//     }
// };
// class Student: public Person{
//     public:
//     void func2(){
//         cout<<"i am a student"<<endl;
//     }
// };
// int main(){
//     Student s;
//     s.func1();
//     s.func2();
// }

multilevel inheritance code
// class A{
//     public:
//     void func1(){
//         cout<<"class a"<<endl;
//     }
// };
// class B: public A{
//     public:
//     void func2(){
//         cout<<"class b"<<endl;
//     }
// };
// class C: public B{
//     public:
//     void func3(){
//         cout<<"class c"<<endl;
//     }
// };
// int main(){
//     C obj;
//     obj.func1();
//     obj.func2();
//     obj.func3();
// }

multiple inheritance code
// class A{
//     public:
//     void func1(){
//         cout<<"class a"<<endl;
//     }
// };
// class B{
//     public:
//     void func2(){
//         cout<<"class b"<<endl;
//     }
// };
// class C: public A, public B{
//     public:
//     void func3(){
//         cout<<"class c"<<endl;
        
//     }
    
// };
// int main(){
//     C obj;
//     obj.func1();
//     obj.func2();
//     obj.func3();
// }

public- accessible from outside
// class Base{
//     public:
//     void func1(){
//         cout<<"class a"<<endl;
//     }
// };
// class Derived: public Base{};

// int main(){
//     Derived d;
//     d.func1();
// }

private- accessible within class only 
//     public:
//     void func1(){
//         cout<<"class a"<<endl;
//     }
// };
// class Derived: private Base{
//     public:
//     void func2(){func1();}
// };
// int main(){
//     Derived d;
//     d.func2();
// }

protected- accessible in derived 
// class Base{
//     public:
//     void func1(){
//         cout<<"class a"<<endl;
//     }
// };
// class Derived: protected Base{
//     public:
//     void func2(){func1();}
// };

// int main(){
//     Derived d;
//     d.func2();
// }

// class Vehicle{
//     public:
//     Vehicle(){
//         cout<<"this is a vehicle.";
//     }
// };
// class Car:public Vehicle{
//     public:
//     Car(){
//         cout<<"this is a car."<<endl;
//     }
// };
// class Bus: public Vehicle{
//     public:
//     Bus(){
//         cout<<"this is a bus.";
//     }
// };
// int main()
// {
//     Car ch;
//     Bus bh;

//    return 0

Hybrid inheritance
// class Vehicle{
//     public:
//     Vehicle(){
//         cout<<"this is a vehicle."<<endl;
//     }
// };
// class Fare{
//     public:
//     Fare(){
//         cout<<"fare of vehicle."<<endl;
//     }
// };

// class Car:public Vehicle{
//     public:
//     Car(){
//         cout<<"this is a car."<<endl;
//     }
// };
// class Bus:public Vehicle, public Fare{
//     public:
//     Bus(){
//         cout<<"this is a bus."<<endl;
// } 
// };

// int main(){
//     Bus bh;
// }

symbol of destructer- tilde

// class Demo{
//     static int count;
//     public:
//     Demo(){
//         count++
//     }
//     void Show(){
//         cout<<count<<endl;
//     }
//     int Demo::count=0;
// };
// int main(){
//     Demo a;
//     Demo b;
//     Demo c;
//     c.Show();
// }

virtual inheritance
// #include <iostream>
// using namespace std;

// class A{
//     public:
//     virtual void show(){
//         cout<<"A";
//     }
// };
// class B:public A{
//     public:
//     void show(){
//         cout<<"B";
//     }
    
// };


// int main() {
//     A* a=new A();   new A will call A class and B will call B class
//     a->show();

//     return 0;
// }

//you can also call AB by making a new object and calling it


Important
// class A{
//     public:
//     void show(){
//         cout<<"A";
//     }
// };
// class B{
//     public:
//     void show(){
//         cout<<"B";
//     }
// };

// class C:public A,public B{}

// int main(){
//     C obj;
//     obj.A::show();
// }


Static members
// class Demo{
//     static int count;
//     public:
//     Demo(){
//         count++;
// }
// void show(){
//     cout<<"Count:"<<count<<endl;
// }
// int Demo::count=0;
// int main(){
//     Demo a;
//     Demo b;
//     Demo c;
//     c.show()
// }

Constant Member Function
// class Demo{
//     int a;
//     public:
//     Demo(int x):a(x){
//         void show() const
//     }
// }


friend class
entire class declared as friends
access all members

// class B

class A{
    int x=5;
    friend class B;
};
class B{
    public:
    void display(A a){
        cout<<a.x<<endl;
    }
}

#include<iostream>
#include<memory>
using namespace std;

class calculator{
    public:
  int a,b;
        char c;
    calculator(){
      
    cin>>a>>b>>c;
    }

void display(){

    switch(c){

    case '+':
    cout<<a+b<<endl;
    break;

     case '-':
    cout<<a+b<<endl;
    break;

     case '*':
    cout<<a+b<<endl;
    break;

     case '%':
    cout<<a+b<<endl;
    break;

     case '/':
    cout<<a+b<<endl;
    break;

    default :
    cout<<"Invalid Input";
    break;
}
}

};

const
// class Book{
//     private:
//     string a;
//     string c;
//     public:
//     Book(string x,string y){
//         a=x;
//         c=y;
//     };
//     void display() const{
//         cout<<a;
//         cout<<c;
//     }
// };
// int main() {
//     const Book b("c++","bjarne");
//     b.display();

friend class
// class printer;
// class box{
//     private:
//     int l,b,h;
//     int vol;
//     public:
//     box(int x, int y, int z){
//         l=x;
//         b=y;
//         h=z;
//         vol=l*b*h;
//     }
//     friend class printer;
// };
// class printer{
//     public:
//     int result(const box i){
//         cout<<i.vol;
//     }
// };
// int main(){
//     int length,breadth,height;
//     cin>>length>>breadth>>height;
//     box j(length,breadth,height);
//     printer p;
//     p.result(j);
// }
    
call by value
// void modify(int x){
//     x+=10;
// }
// int main() {
//     // int a=5;
//     // modify(a);
//     // cout<<a; 

call by reference 
// void modify(int &x)

call by pointer
// void modify(int *x){
//     * x+=15;
// }
// int main(){
//     int a=5;
//     modify(&a);
//     cout<<a;
// }

function overloading
// int sum(int a,int b){
//     return a+b;
// }
// double sum(double a, double b){
//     return a+b;
// }
// int main(){
//     cout<<sum(2,3)<<endl;
//     cout<<sum(2.3,3.6);
// }






