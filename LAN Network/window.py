import tkinter as tk
import pandas as pd

class CsvVariableCycler:
    def __init__(self, master, filepath):
        self.master = master
        self.df = pd.read_csv(filepath)
        self.index = 0 #Start at the first column
        self.columns_per_view = 5 #number of variables to show at a time
        self.max_index = len(self.df.columns)  - self.columns_per_view

        # setup the GUI
        self.label = tk.Label(master, text=self.get_current_variables(), font=('Helvetica', 16))
        self.label.pack(pady=20)

        left_button = tk.Button(master, text="Left", command=self.prev_variables)
        left_button.pack(side=tk.LEFT, padx=20)

        right_button = tk.Button(master, text="Right", command=self.next_variables)
        right_button.pack(side=tk.RIGHT, padx=20)

    def get_current_variables(self):
        # Get curretn variables to display
        current_vars = self.df.columns[self.index:self.index + self.columns_per_view]
        display_text = []
        for var in current_vars:
            values = self.df[var].tolist()
            display_text.append(f"{var}: {values}")
        return "\n".join(display_text)
    
    def prev_variables(self):
        # Move to the previous set of varialbes
        if self.index > 0:
            self.index -= self.columns_per_view
        else:
            self.index = max(0, len(self.df.columns) -self.columns_per_view)
        self.update_label()

    def next_variables(self):
        # Move to the next set of variables
        if self.index < self.max_index:
            self.index += self.columns_per_view
        else:
            self.index = 0
        self.update_label()

    def update_label(self):
        # update the label with the new variable
        self.label.config(text=self.get_current_variables())

# Create the main window
root = tk.Tk()
root.title("CSV Variable Cycler")

# Start the application 
app = CsvVariableCycler(root, 'data_log.csv')

root.mainloop()

