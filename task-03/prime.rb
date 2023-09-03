def is_prime(num)
    return false if num <= 1

    (2..Math.sqrt(num)).each do |i|
        return false if num % i == 0
    end

    return true
end

puts "Enter any number: "
n = gets.chomp.to_i

(2..n).each do |i|
    if is_prime(i)
        print i, " "
    end
end
