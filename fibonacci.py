#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_input():
  input = 0
  while (True):
    input = input("Enter a positive integer: ")
    if input.isdigit():
      if int(input) > 0:
        return int(input)
      else:
        print("Enter a valid integer!")
    else:
      print("Enter a valid integer!")

def generate_fibonacci(terms):
  num1 = 1
  num2 = 0
  tmp = 0
  sequence = [terms]
  for i in range(terms):
    sequence[i] = num1
    tmp = num1
    num1 += num2
    num2 = tmp
  return sequence

def print_sequence(sequence):
  for i in range(sequence.length() - 1):
    print("{sequence[i]}, ")
  print("{sequence[i]}")

user_input = get_input()
sequence = generate_fibonacci()
print_sequence(sequence)
