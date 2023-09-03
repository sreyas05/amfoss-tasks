defmodule Prime do
  def is_prime(num) when num <= 1, do: false
  def is_prime(num) when num == 2, do: true
  def is_prime(num) do
    is_prime(num, 2)
  end

  defp is_prime(num, divisor) when divisor >= num, do: true
  defp is_prime(num, divisor) when rem(num, divisor) == 0, do: false
  defp is_prime(num, divisor) do
    is_prime(num, divisor + 1)
  end

  def main do
    IO.puts("Enter any number: ")
    n = IO.gets("") |> String.trim() |> String.to_integer()

    for i <- 2..n, is_prime(i) do
      IO.write("#{i} ")
    end
    IO.puts(" ")
  end
end

Prime.main()
