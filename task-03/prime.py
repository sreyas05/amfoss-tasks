def isPrime(num):
      
    if num <= 1 :
        return False
  
    for i in range(2, num):
        if num % i == 0:
            return False
  
    return True

def main():
    n = int(input("Enter a number: "))

    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end = " ")

if __name__ == "__main__": 
    main()