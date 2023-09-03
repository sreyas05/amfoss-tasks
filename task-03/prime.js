const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Enter a number ", (num) => {
  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) process.stdout.write(i + " ");
  }
  readline.close();
});

const isPrime = (n) => {
  if (n <= 1) return false;

  for (let i = 2; i < n; i++) if (n % i == 0) return false;

  return true;
};
