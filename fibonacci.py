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
  i = 1
  j = 0
  tmp = 0
  sequence = ""
  for i in range(terms):
    sequence = sequence + "{i} "
    tmp = i
    i = i + j
    j = tmp

def print_sequence(sequence):
  print("{sequence}")
