package polymorphism;   

class solution{
    public int add(int a,int b){
        return a + b;
    }

    public float add(float a, float b){
        return a + b;
    }

    public double add(double a, double b){
        return a + b;
    }
}
public class compiletimePolymorphism {

     public static void main(String[] args){

        solution sol = new solution();
        
        System.out.println(sol.add(1, 5));           // int version
        System.out.println(sol.add(3.9, 7.3));       // double version
        System.out.println(sol.add(4.5f, 2.5f));    // float version
     }
}
