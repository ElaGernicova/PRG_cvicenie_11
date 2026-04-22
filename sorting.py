import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(sequence):
    sequence = sequence[:]
    n = len(sequence)
    for it in range(n):
        min_index = it
        for index in range(it + 1,n):
            if sequence[index] < sequence[min_index]:
                min_index = index
        sequence[it], sequence[min_index] = sequence[min_index], sequence[it]

    return sequence


def bubble_sort(sequence):
    sequence = sequence[:]
    n = len(sequence)
    for it in range(n-1):
        for index in range(n - 1 - it):
            if sequence[index] > sequence[index + 1]:
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index]

    return sequence

def main():
    sequence = random_numbers(20,0,100)
    sorted_sequence = selection_sort(sequence)
    bubble_sequence = bubble_sort(sequence)
    print(sequence)
    print(sorted_sequence)
    print(bubble_sequence)


if __name__ == "__main__":
    main()