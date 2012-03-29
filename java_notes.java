class java_notes {
    public static void main(String[] args) {
        System.out.println("Hello, world");
        
        String name = "Kevin";
        System.out.println(name.length());
        System.out.printf("Math.PI is %.3f\n", Math.PI);
        
        Calculator calc = new Calculator();
        System.out.println(calc.add(5, 6));
        
        String x = "x";
        String y = "xy";
        
        y = String.valueOf(y.charAt(0));
        
        System.out.println(x == y);
        System.out.println(x.equals(y));
        
        Integer i = 5;
        System.out.println(i.getClass());
    }
}

class Calculator {
    public int add(int x, int y) {
        return x + y;
    }
}