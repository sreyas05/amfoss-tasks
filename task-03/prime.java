import java.util.Scanner;

class prime 
{
    static boolean isPrime(int n)
    {
        if (n <= 1)
            return false;
  
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;
  
        return true;
    }

    public static void main(String[] args)
    {   
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = input.nextInt();
        for (int i = 2; i <= num; i++) {
            if (isPrime(i))
                System.out.print(i + " ");
        }
    }
}