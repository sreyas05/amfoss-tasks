package main

import "fmt"

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }

    for i := 2; i < num; i++ {
        if num%i == 0 {
            return false
        }
    }

    return true
}

func main() {
    var n int
    fmt.Print("Enter any number: ")
    fmt.Scan(&n)

    for i := 2; i <= n; i++ {
        if isPrime(i) {
            fmt.Printf("%d ", i)
        }
    }
}
