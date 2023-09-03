isPrime :: Int -> Bool
isPrime num
    | num <= 1   = False
    | otherwise  = all (\x -> num `mod` x /= 0) [2..num-1]

findPrimes :: Int -> [Int]
findPrimes n = [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStrLn "Enter any number: "
    input <- getLine
    let n = read input :: Int
    let primes = findPrimes n
    putStrLn (show primes)
