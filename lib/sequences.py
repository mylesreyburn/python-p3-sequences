#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = [0, 1]
    if length == 0:
        fib_seq.clear()
    if length == 1:
        fib_seq.pop()

    i = 1

    while i <= length:
        
        current_value = fib_seq[len(fib_seq) - 1]
        penultimate_value = fib_seq[len(fib_seq) - 2]
        next_value = current_value + penultimate_value
        fib_seq.append(next_value)
        i += 1

    print(fib_seq[0:length])

print_fibonacci(10)