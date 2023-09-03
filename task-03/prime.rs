use std::io;

fn is_prime(num: i32) -> bool {
    if num <= 1 {
        return false;
    }

    for i in 2..num {
        if num % i == 0 {
            return false;
        }
    }

    true
}

fn main() {
    let mut input = String::new();
    println!("Enter any number: ");
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: i32 = input.trim().parse().expect("Invalid input");

    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
}
