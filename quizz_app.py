import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application - Programming")
        self.root.geometry("520x420")
        self.root.config(bg="#0b1c2d")

        self.questions = [
            {
                "question": "ما هي لغة البرمجة المستخدمة لتطوير صفحات الويب؟",
                "options": ["Python", "HTML", "C++", "Java"],
                "answer": 1
            },
            {
                "question": "ما وظيفة المتغير في البرمجة؟",
                "options": [
                    "تخزين البيانات",
                    "طباعة النصوص",
                    "تنفيذ الحلقات",
                    "إنهاء البرنامج"
                ],
                "answer": 0
            },
            {
                "question": "أي مما يلي يعتبر حلقة تكرار؟",
                "options": ["if", "while", "print", "return"],
                "answer": 1
            },
            {
                "question": "ما ناتج العملية 5 // 2 في بايثون؟",
                "options": ["2.5", "3", "2", "خطأ"],
                "answer": 2
            },
            {
                "question": "ما الكلمة المفتاحية لتعريف دالة في بايثون؟",
                "options": ["function", "define", "def", "fun"],
                "answer": 2
            },
            {
                "question": "ما نوع البيانات الناتج عن True أو False؟",
                "options": ["int", "string", "bool", "float"],
                "answer": 2
            },
            {
                "question": "أي رمز يُستخدم للتعليق في بايثون؟",
                "options": ["//", "#", "/* */", "--"],
                "answer": 1
            },
            {
                "question": "ما الغاية من استخدام if؟",
                "options": [
                    "تكرار الكود",
                    "اتخاذ قرار",
                    "تخزين قيمة",
                    "إنهاء البرنامج"
                ],
                "answer": 1
            },
            {
                "question": "أي مما يلي مصفوفة في بايثون؟",
                "options": ["(1,2,3)", "{1,2,3}", "[1,2,3]", "1,2,3"],
                "answer": 2
            },
            {
                "question": "ما وظيفة break داخل الحلقة؟",
                "options": [
                    "تخطي التكرار الحالي",
                    "إيقاف الحلقة",
                    "إعادة الحلقة",
                    "لا شيء"
                ],
                "answer": 1
            }
        ]

        self.q_index = 0
        self.score = 0
        self.time_left = 15

        self.selected = tk.IntVar()

        self.timer_label = tk.Label(
            root,
            text="الوقت: 15",
            font=("Arial", 12, "bold"),
            fg="#ffd700",
            bg="#0b1c2d"
        )
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(
            root,
            text="",
            wraplength=480,
            font=("Arial", 14),
            fg="white",
            bg="#0b1c2d"
        )
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                root,
                text="",
                variable=self.selected,
                value=i,
                font=("Arial", 11),
                fg="white",
                bg="#0b1c2d",
                selectcolor="#1e3a5f",
                activebackground="#0b1c2d",
                activeforeground="white"
            )
            rb.pack(anchor="w", padx=40)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(
            root,
            text="التالي",
            font=("Arial", 11, "bold"),
            bg="#1e3a5f",
            fg="white",
            width=12,
            command=self.next_question
        )
        self.next_button.pack(pady=20)

        self.load_question()
        self.update_timer()

    def load_question(self):
        self.selected.set(-1)
        self.time_left = 15
        q = self.questions[self.q_index]
        self.question_label.config(text=q["question"])
        for i in range(4):
            self.radio_buttons[i].config(text=q["options"][i])

    def update_timer(self):
        self.timer_label.config(text=f"الوقت: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def next_question(self):
        if self.selected.get() == self.questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo(
            "النتيجة",
            f"علامتك: {self.score} من 10"
        )
        self.root.destroy()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()
