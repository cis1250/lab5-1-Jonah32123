#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_input():
  user_input = 0
  while (True):
    user_input = input("Enter a positive integer: ")
    if user_input.isdigit():
      if int(user_input) > 0:
        return int(user_input)
      else:
        print("Enter a valid integer!")
    else:
      print("Enter a valid integer!")

def generate_fibonacci(terms):
  num1 = 1
  num2 = 0
  tmp = 0
  sequence = []
  for i in range(terms):
    sequence.append(num1)
    tmp = num1
    num1 += num2
    num2 = tmp
  return sequence

def print_sequence(sequence):
  for i in range(len(sequence) - 1):
    print(f"{sequence[i]}, ", end="")
  print(f"{sequence[-1]}")

terms = get_input()
sequence = generate_fibonacci(terms)
print_sequence(sequence)
