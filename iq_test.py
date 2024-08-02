from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk

questions = [
    # Easy5
    {"question": "Sum of 2 and 5", "options": ["7", "5", "12", "9"], "answer": "7", "point":5},
    {"question": "Square of 4", "options": ["13", "34", "16", "9"], "answer": "16", "point":5},
    {"question": "Average of 2, 4, 6", "options": ["4", "5", "3", "2"], "answer": "4.0", "point":5},
    {"question": "Factorial of 3", "options": ["0", "6", "24", "9"], "answer": "6", "point":5},
    {"question": "Simple interest for P=1000, R=5, T=2", "options": ["250", "1000", "500", "100"], "answer": "100", "point":5},
    # Medium
    {"question": "GCD of 36 and 60", "options": ["7", "0", "12", "9"], "answer": "12","point":10},
    {"question": "Sum of digits of 123", "options": ["18", "5", "2", "6"], "answer": "6","point":10},
    {"question": "Reverse of 1234", "options": ["2431", "1342", "1243", "4321"], "answer": "4321","point":10},
    {"question": "Missing number in [1, 2, 4, 5] (1 to 5)", "options": ["7", "5", "12", "3"], "answer": "3","point":10},
    {"question": "Area of a triangle with base 10 and height 5", "options": ["7", "50", "12", "25.0"], "answer": "25.0","point":10},
    {"question": "Convert 0°C to Fahrenheit", "options": ["32.0", "50", "25", "45"], "answer": "32.0","point":10},
    {"question": "Roots of x^2 - 3x + 2 = 0", "options": ["1.0, 2.0", "2.0, 3.0", "1.5, 2.5", "2.0, 1.0"], "answer": "2.0, 1.0","point":10},
    # Hard
    {"question": "10th Fibonacci number", "options": ["34", "55", "21", "44"], "answer": "55","point":15},
    {"question": "LCS of AGGTAB and GXTXAYB", "options": ["4", "5", "6", "7"], "answer": "4","point":15},
    {"question": "3rd smallest element in [7, 10, 4, 3, 20, 15]", "options": ["7", "4", "3", "10"], "answer": "7","point":15},
    {"question": "Knapsack with weights [1, 2, 3] and values [10, 15, 40] for capacity 6", "options": ["55", "45", "50", "60"], "answer": "55","point":15},
    {"question": "Longest increasing subsequence in [10, 22, 9, 33, 21, 50, 41, 60]", "options": ["4", "5", "6", "7"], "answer": "5","point":15},
    {"question": "Median of [1, 3, 5, 7, 9, 11]", "options": ["5.0", "6.0", "7.0", "8.0"], "answer": "6.0","point":15},
    {"question": "Maximum subarray sum in [2, 3, -2, 4]", "options": ["7", "5", "6", "8"], "answer": "7","point":15},
    {"question": "Binomial coefficient C(5, 2)", "options": ["10", "12", "8", "6"], "answer": "10","point":15},
    {"question": "Minimum path sum in grid [[1,3,1],[1,5,1],[4,2,1]]", "options": ["7", "8", "9", "10"], "answer": "7","point":15},
    {"question": "Count inversions in [2, 3, 8, 6, 1]", "options": ["5", "4", "3", "6"], "answer": "5","point":15},
    # Additional Questions
    {"question": "What is the next number in the sequence 2, 4, 8, 16?", "options": ["32", "20", "30", "40"], "answer": "32","point":15},
    {"question": "What is 5 raised to the power 3?", "options": ["125", "100", "150", "175"], "answer": "125","point":15},
    {"question": "What is the square root of 81?", "options": ["9", "8", "7", "10"], "answer": "9","point":15},
    {"question": "How many degrees are in a right angle?", "options": ["90", "180", "45", "360"], "answer": "90","point":15},
    {"question": "What is the value of π (pi) approximately?", "options": ["3.14", "3.16", "3.12", "3.18"], "answer": "3.14","point":15},
    {"question": "What is the cube root of 27?", "options": ["3", "6", "9", "12"], "answer": "3","point":15},
    {"question": "What is 15% of 200?", "options": ["30", "25", "35", "40"], "answer": "30","point":15},
    {"question": "If a car travels 60 miles per hour, how far will it travel in 2 hours?", "options": ["120 miles", "100 miles", "80 miles", "140 miles"], "answer": "120 miles","point":15},
    {"question": "What is the sum of angles in a triangle?", "options": ["180 degrees", "360 degrees", "90 degrees", "270 degrees"], "answer": "180 degrees","point":15}
]

current_question = 0
total_score = 0

def display_question():
    global current_question
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))
    else:
        show_result()

def check_answer(selected_option):
    global current_question, total_score
    if selected_option == questions[current_question]["answer"]:
        total_score += questions[current_question]["points"]
    current_question += 1
    display_question()

def show_result():
    percentage_score = (total_score / 135) * 100
    messagebox.showinfo("Result", f"Your score is {total_score} out of 135.\nPercentage: {percentage_score:.2f}%")
    root.quit()


root = Tk()
root.title("IQ Test")

root.geometry(r"800x500")
question_label = Label(root, text="", wraplength=400)
question_label.pack(pady=10)

option_buttons = [Button(root, width=40,padx=20 , pady=20) for _ in range(4)]
for button in option_buttons:
    button.pack(pady=5,fill=X)


display_question()

# Importing Images
image = Image.open("ii.png")
bg_image = ImageTk.PhotoImage(image)
canvas = Canvas(root, width=800 , height=500)
canvas.pack()
canvas.create_image(0,0, anchor= "nw", image=bg_image)









text=Label(root,text="WELCOM TO IQQQQ TESTTTT", font="Hevatica 20 bold")
text1=Label(root,text="WELCOM TO IQQQQ TESTTTT", font="Hevatica 20 bold")
text2=Label(root,text="WELCOM TO IQQQQ TESTTTT", font="Hevatica 20 bold")
text.pack(pady=20)
text1.pack(pady=20)
text2.pack(pady=20)


root.mainloop()
