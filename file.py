lower = 1
upper = 250


def prime(lower, upper):
  with open('results.txt', 'w') as file:
    for num in range(lower, upper + 1):
      # all prime numbers are greater than 1
      if num > 1:
        for i in range(2, num):
          if (num % i) == 0:
            break
        else:
          file.write(str(num) + '\n')


prime(lower, upper)
