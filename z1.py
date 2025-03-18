import tkinter as tk

def convert_temperature():
    try:
        celsius_value = float(entry.get())
        fahrenheit_value = celsius_value * 9/5 + 32
        result_label.config(text=f"Температура в Фаренгейтах: {fahrenheit_value:.2f}")
    except ValueError:
        result_label.config(text="Введіть число")

root = tk.Tk()
root.title("Конвертер температури")

entry = tk.Entry(root)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Конвертувати", command=convert_temperature)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
