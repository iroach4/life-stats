import tkinter as tk
import datetime


def get_input_text():
    year = text_box_year.get()
    month = text_box_month.get()
    day = text_box_day.get()
    return year, month, day
    
def get_stats():
    year = get_input_text()[0]
    month = get_input_text()[1]
    day = get_input_text()[2]
    try: 
        today = datetime.date.today()
        selected_date = datetime.date(int(year), int(month), int(day))
        years = today.year - selected_date.year
        if today.month == selected_date.year:
            months = 0
        elif today.month < selected_date.month:
            years -= 1
            today_month = today.month + 12
            months = today_month - selected_date.month
        else:
            months = today.month - selected_date.month
        weeks = (years * 52) + (months * 4)
        days = weeks * 7
        hours = days * 24

        year_result.delete(1.0, "end")
        year_result.insert(tk.END, str(round(years)) + " years")
        month_result.delete(1.0, "end")
        month_result.insert(tk.END, str(round(months)) + " months")
        week_result.delete(1.0, "end")
        week_result.insert(tk.END, str(round(weeks)) + " weeks")
        day_result.delete(1.0, "end")
        day_result.insert(tk.END, str(round(days)) + " days")
        hour_result.delete(1.0, "end")
        hour_result.insert(tk.END, str(round(hours)) + " hours")
    except:
        year_result.delete(1.0, "end")
        year_result.insert(tk.END, "Error")
        month_result.delete(1.0, "end")
        month_result.insert(tk.END, "Error")
        week_result.delete(1.0, "end")
        week_result.insert(tk.END, "Error")
        day_result.delete(1.0, "end")
        day_result.insert(tk.END, "Error")
        hour_result.delete(1.0, "end")
        hour_result.insert(tk.END, "Error")
    

root = tk.Tk()
root.title("Life Stats")
root.geometry("400x400")
root.resizable(False, False)

intro_label = tk.Label(root, text = "Plug in your birthday to discover some cool stats about your life!")
intro_label.grid(row = 0, column=0, columnspan=5)

label_1 = tk.Label(root, text = "Year:")
label_1.grid(row = 3, column=0)
label_2 = tk.Label(root, text = "Month:")
label_2.grid(row = 4, column=0, padx=15, pady=15)
label_3 = tk.Label(root, text = "Day:")
label_3.grid(row = 5, column=0)

text_box_year = tk.Entry(root)
text_box_year.grid(row = 3, column=1)
text_box_month = tk.Entry(root)
text_box_month.grid(row = 4, column=1)
text_box_day = tk.Entry(root)
text_box_day.grid(row = 5, column=1)

year_result = tk.Text(root, height = 2, width = 30)
year_result.grid(row = 8, column=1, pady = 10)
month_result = tk.Text(root, height = 2, width = 30)
month_result.grid(row = 9, column=1, pady = 5)
week_result = tk.Text(root, height = 2, width = 30)
week_result.grid(row = 10, column=1, pady = 5)
day_result = tk.Text(root, height = 2, width = 30)
day_result.grid(row = 11, column=1, pady = 5)
hour_result = tk.Text(root, height = 2, width = 30)
hour_result.grid(row = 12, column=1, pady = 5)


compute_button = tk.Button(root, text = "Compute", command = get_stats)
compute_button.grid(row = 7, column= 1)

root.mainloop()