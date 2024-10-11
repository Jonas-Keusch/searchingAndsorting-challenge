import csv

def load_data(file_path):
    data = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return headers, data

def selection(row):
    n = len(row)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if row[j] < row[min_index]:
                min_index = j
        row[i], row[min_index] = row[min_index], row[i]
    return row

def insertion(row):
    for i in range(1, len(row)):
        key = row[i]
        j = i - 1
        
        while j >= 0 and row[j] > key:
            row[j + 1] = row[j]
            j -= 1
        row[j + 1] = key
    return row

def linear_search(data, student_id):
    for row in data:
        if row[0] == student_id:
            return row
    return None

def binary_search(data, target_score):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][3] == target_score:
            return mid
        elif data[mid][3] < target_score:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def calculate_statistics(data):
    grades = {}
    for row in data:
        grade = row[1]
        reading_score = int(row[3])
        math_score = int(row[4])
        
        if grade not in grades:
            grades[grade] = {'reading_total': 0, 'math_total': 0, 'count': 0, 'pass_reading': 0, 'pass_math': 0}
        
        grades[grade]['reading_total'] += reading_score
        grades[grade]['math_total'] += math_score
        grades[grade]['count'] += 1
        if reading_score >= 70:
            grades[grade]['pass_reading'] += 1
        if math_score >= 70:
            grades[grade]['pass_math'] += 1
    
    for grade, stats in grades.items():
        avg_reading = stats['reading_total'] / stats['count']
        avg_math = stats['math_total'] / stats['count']
        pass_percentage_reading = (stats['pass_reading'] / stats['count']) * 100
        pass_percentage_math = (stats['pass_math'] / stats['count']) * 100
        print(f"Grade: {grade}")
        print(f"  Average Reading Score: {avg_reading:.2f}")
        print(f"  Average Math Score: {avg_math:.2f}")
        print(f"  Percentage Passed Reading: {pass_percentage_reading:.2f}%")
        print(f"  Percentage Passed Math: {pass_percentage_math:.2f}%\n")

headers, data = load_data('Resources/students_complete.csv')

data.sort(key=lambda x: int(x[3]))

student_id = input("Enter Student ID to find their scores: ")
student_scores = linear_search(data, student_id)
if student_scores:
    print(f"Scores for Student ID {student_id}: {student_scores}")
else:
    print("Student ID not found.")

reading_score = int(input("Enter Reading Score to find: "))
index = binary_search(data, reading_score)
if index != -1:
    print(f"Student with Reading Score {reading_score} found at index {index}.")
else:
    print("No student found with that Reading Score.")

calculate_statistics(data)

