#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num)
{
    if (num <= 1)
        return false;

    for (int i = 2; i < num; i++)
        if (num % i == 0)
            return false;

    return true;
}

int main()
{
    int n;
    printf("Enter any number: ");
    scanf("%i", &n);

    for (int i = 2; i <= n; i++)
        if (isPrime(i))
            printf("%d ", i);

    return 0;
}