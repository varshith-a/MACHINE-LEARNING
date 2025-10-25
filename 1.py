import tkinter as tk
from tkinter import messagebox

# --- Simple ML logic for cloth suggestion ---
def suggest_design(age, gender):
    age = int(age)
    gender = gender.lower()

    if gender == "male":
        if age < 18:
            return "Trendy T-Shirt with Jeans"
        elif age <= 35:
            return "Casual Shirt with Slim Fit Pants"
        elif age <= 50:
            return "Formal Shirt with Trousers"
        else:
            return "Comfortable Kurta with Pajama"
    elif gender == "female":
        if age < 18:
            return "Floral Top with Skirt"
        elif age <= 35:
            return "Designer Kurti or Western Dress"
        elif age <= 50:
            return "Elegant Saree or Salwar"
        else:
            return "Comfort-fit Saree or Long Kurti"
    else:
        return "Invalid gender entered."

# --- Function to open new screen with output ---
def show_result():
    age = age_entry.get()
    gender = gender_entry.get()

    if not age.isdigit() or gender == "":
        messagebox.showerror("Input Error", "Please enter valid age and gender!")
        return

    result = suggest_design(age, gender)

    # Create new window to display result
    result_window = tk.Toplevel(root)
    result_window.title("Design Suggestion")
    result_window.geometry("400x200")
    result_window.config(bg="#F0E68C")

    tk.Label(result_window, text="👗 Cloth Design Suggestion 👕", 
             font=("Arial", 16, "bold"), bg="#F0E68C").pack(pady=10)
    tk.Label(result_window, text=f"Age: {age}", font=("Arial", 12), bg="#F0E68C").pack()
    tk.Label(result_window, text=f"Gender: {gender.title()}", font=("Arial", 12), bg="#F0E68C").pack()
    tk.Label(result_window, text=f"Suggested Design: {result}", 
             font=("Arial", 14, "italic"), bg="#F0E68C", wraplength=350).pack(pady=10)

# --- Main screen (input window) ---
root = tk.Tk()
root.title("AI Cloth Design System")
root.geometry("400x300")
root.config(bg="#ADD8E6")

tk.Label(root, text="AI Cloth Design", font=("Arial", 18, "bold"), bg="#ADD8E6").pack(pady=20)

tk.Label(root, text="Enter your Age:", font=("Arial", 12), bg="#ADD8E6").pack()
age_entry = tk.Entry(root, width=25)
age_entry.pack(pady=5)

tk.Label(root, text="Enter your Gender (Male/Female):", font=("Arial", 12), bg="#ADD8E6").pack()
gender_entry = tk.Entry(root, width=25)
gender_entry.pack(pady=5)

tk.Button(root, text="Get Design Suggestion", font=("Arial", 12, "bold"),
          bg="green", fg="white", command=show_result).pack(pady=20)

root.mainloop()
