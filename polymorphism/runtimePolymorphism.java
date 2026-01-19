package polymorphism;


class animal{
    public void sound(){
        System.out.println("Amnimal Sound");
    }
}

class cat extends animal{
    public void sound(){
        System.out.println("Cat Sound");
    }
}

class dog extends animal{
    public void sound(){
        System.out.println("Dog Sound");
    }
}

public class runtimePolymorphism {

    public static void main(String[] args) {
        
        animal og = new animal();
        og.sound();
        og.sound();
        og.sound();
        og = new dog();
        og.sound();
        og.sound();
        og.sound();
        og = new cat();
        og.sound();
        og.sound();
        og.sound();

    }
    
}
