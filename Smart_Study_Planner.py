import tkinter as tk
import matplotlib.pyplot as plt

def generate_plan():
    subjects = subject_entry.get().split(",")
    difficulties = difficulty_entry.get().split(",")
    priorities = priority_entry.get().split(",")
    total_hours = float(hours_entry.get())

    weights = []
    for i in range(len(subjects)):
        d = difficulties[i].strip().lower()
        p = int(priorities[i].strip())

        if d == "easy":
            dw = 1
        elif d == "medium":
            dw = 2
        elif d == "hard":
            dw = 3
        else:
            dw = 1

        weights.append(dw * p)

    total_weight = sum(weights)

    result = "Your Smart Study Plan:\n\n"
    times = []

    for i in range(len(subjects)):
        time = (weights[i] / total_weight) * total_hours
        times.append(round(time, 2))
        result += f"{subjects[i].strip()} → {round(time,2)} hrs\n"

    output_label.config(text=result)

    # Plot Graph
    plt.figure()
    plt.bar(subjects, times)
    plt.xlabel("Subjects")
    plt.ylabel("Study Hours")
    plt.title("Study Time Allocation")
    plt.show()


# GUI
root = tk.Tk()
root.title("Smart Study Planner (AI-Based)")
root.geometry("500x500")

tk.Label(root, text="Subjects (comma separated):").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Difficulty (easy/medium/hard):").pack()
difficulty_entry = tk.Entry(root, width=50)
difficulty_entry.pack()

tk.Label(root, text="Priority (1-5):").pack()
priority_entry = tk.Entry(root, width=50)
priority_entry.pack()

tk.Label(root, text="Total Study Hours:").pack()
hours_entry = tk.Entry(root, width=20)
hours_entry.pack()

tk.Button(root, text="Generate Plan", command=generate_plan).pack(pady=10)

output_label = tk.Label(root, text="", justify="left")
output_label.pack(pady=10)

root.mainloop()
