import random
from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score >= 90:
           return"A"
        elif 80 <=score<= 89:
            return"B"
        elif 70 <=score<= 79:
            return"C"
        elif 60 <=score<= 69:
            return"D"
        elif 50 <= score <= 59:
            return"E"
        else:
            return"F"


    def find(self, score):
        index = 0
        position = []
        searched_data = self.scores
        while index < len(searched_data):
            if searched_data[index] == score:
                position.append(index)
            index += 1
        return position

    def get_sorted(self):
        sequence = self.scores[:]
        n = len(sequence)
        for it in range(n - 1):
            for index in range(n - 1 - it):
                if sequence[index] > sequence[index + 1]:
                    sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
        return sequence

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    for student in range(results.scores()):
        print(f"Student {student}: {results.get_by_index(student)} points - {results.get_grade(student)}")
    print(f"Plny pocet bodov mali studenti: {results.find(100)}")
    print(f"Zoradene vysledky: {results.get_sorted()}")


    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()