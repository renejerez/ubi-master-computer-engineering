package junit;


public class Calculator {
    public int add(int a, int b) {
        return a + b;            
    }

    public int subtract(int a, int b) {
        return a - b;    
    }

    public int multiply(int a, int b) {
        return a * b;    
    }
                    
    public double divide(int a, int b) {

        if(b < 1) return 0.0;
        
        return a / b;
    }

    public boolean isPrime(int number){
        return number %2 ==0;
    }
}
