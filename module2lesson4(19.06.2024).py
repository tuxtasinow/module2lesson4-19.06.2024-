numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(len(numbers)):
  for j in range(2, numbers[i]):
    if numbers[i] % j == 0:
      not_primes.append(numbers[i])
      break
  else:
    primes.append(numbers[i])

primes.remove(1)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')