class java_notes {
    public static void main(String[] args) {
        System.out.println("Hello, world");
        
        String name = "Kevin";
        System.out.println(name.length());
        System.out.printf("Math.PI is %.3f\n", Math.PI);
        
        Calculator calc = new Calculator();
        System.out.println(calc.add(5, 6));
    }
}

class Calculator {
    public int add(int x, int y) {
        return x + y;
    }
}