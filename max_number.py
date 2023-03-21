def high_number(numbers):
    max=numbers[0]
    for number in numbers:
        if number>max:
            max=number
            return max


numbers=[879,7564654,65654,654853,6676]
max=high_number(numbers)

print(max)