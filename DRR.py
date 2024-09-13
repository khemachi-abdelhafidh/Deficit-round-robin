import tkinter as tk
from tkinter import messagebox

class TableFrame(tk.Frame):
    def __init__(self, master=None, table_data=None):
        super().__init__(master)
        self.table_data = table_data
        self.create_widgets()
        self.locked = False

    def create_widgets(self):
        # Label for the interface purpose
        interface_label = tk.Label(self, text="L'interface de l'entrer")
        interface_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.table_entries = []

        # Create the table with one column
        for i, row_data in enumerate(self.table_data):
            cell_data_1 = row_data[0]
            cell_label_1 = tk.Label(self, text=cell_data_1, borderwidth=1, relief="solid", fg="black")
            cell_label_1.grid(row=i + 1, column=0, sticky="nsew")

            cell_entry = tk.Entry(self, textvariable=tk.StringVar(value=row_data[1]), borderwidth=1, relief="solid",
                                  fg="black", disabledforeground="black")
            cell_entry.grid(row=i + 1, column=1, sticky="nsew")
            self.table_entries.append(cell_entry)

            self.grid_rowconfigure(i + 1, weight=1)

        # Canvas for vector representation of table A (initially hidden)
        self.new_table_canvas_a = tk.Canvas(self, borderwidth=1, relief="solid", bg="white", height=20)
        self.new_table_canvas_a.grid(row=len(self.table_data) + 2, column=0, columnspan=2, sticky="nsew", pady=10)
        self.new_table_canvas_a.grid_remove()

        # Canvas for vector representation of table B (initially hidden)
        self.new_table_canvas_b = tk.Canvas(self, borderwidth=1, relief="solid", bg="white", height=20)
        self.new_table_canvas_b.grid(row=len(self.table_data) + 4, column=0, columnspan=2, sticky="nsew", pady=10)
        self.new_table_canvas_b.grid_remove()

        # Canvas for vector representation of table C (initially hidden)
        self.new_table_canvas_c = tk.Canvas(self, borderwidth=1, relief="solid", bg="white", height=20)
        self.new_table_canvas_c.grid(row=len(self.table_data) + 6, column=0, columnspan=2, sticky="nsew", pady=10)
        self.new_table_canvas_c.grid_remove()

        # Canvas for vector representation of Interface de sortie (initially hidden)
        self.new_table_canvas_output = tk.Canvas(self, borderwidth=1, relief="solid", bg="white", height=20)
        self.new_table_canvas_output.grid(row=len(self.table_data) + 8, column=0, columnspan= 21 , sticky="nsew", pady=10)
        self.new_table_canvas_output.grid_remove()

        # Label for table A
        label_a = tk.Label(self, text="file d'attent A:")
        label_a.grid(row=len(self.table_data) + 1, column=0, columnspan=2, sticky="nsew")

        # Label for table B
        label_b = tk.Label(self, text="Tfile d'attent B:")
        label_b.grid(row=len(self.table_data) + 3, column=0, columnspan=2, sticky="nsew")

        # Label for table C
        label_c = tk.Label(self, text="file d'attent C:")
        label_c.grid(row=len(self.table_data) + 5, column=0, columnspan=2, sticky="nsew")

        # Label for Interface de sortie
        label_output = tk.Label(self, text="Interface de sortie:")
        label_output.grid(row=len(self.table_data) + 7, column=0, columnspan=2, sticky="nsew")

        # Button "+" to add a new column
        self.add_column_button = tk.Button(self, text="+", command=self.add_column, state=tk.NORMAL)
        self.add_column_button.grid(row=len(self.table_data) + 9, column=0, columnspan=2, sticky="nsew")

        # Button "DRR" to calculate the number of cells and display counts
        self.drr_button = tk.Button(self, text="DRR", command=self.show_dc_frame)
        self.drr_button.grid(row=len(self.table_data) + 10, column=0, columnspan=2, sticky="nsew")

    def show_dc_frame(self):
        if not self.locked:
            dc_frame = DcFrame(self.master, self.calculate_stats)

    def add_column(self):
        if not self.locked:
            # Add an empty column to the table
            new_column_index = len(self.table_data[0])

            # Update column configuration
            new_column_index += 1
            self.grid_columnconfigure(new_column_index, weight=1)

            # Add Entry widgets for the new column
            for i, row_data in enumerate(self.table_data):
                # Check if the row has enough elements before adding a new one
                while len(row_data) <= new_column_index:
                    row_data.append('')

                cell_data = row_data[new_column_index]
                cell_entry = tk.Entry(self, textvariable=tk.StringVar(value=cell_data), borderwidth=1, relief="solid",
                                      fg="black", disabledforeground="black")
                cell_entry.grid(row=i + 1, column=new_column_index, sticky="nsew")
                self.table_entries.append(cell_entry)
    def calculate_stats(self, dc_value):
        if not self.locked:
            # Check if there are empty cells in the first column
            column_values_arrive = [entry.get() for entry in self.table_entries[::len(self.table_data)]]

            if '' in column_values_arrive:
                # If there is an empty cell in the first column, prompt the user
                messagebox.showwarning("Missing Data", "Please fill in all cells in the 'Les temps d\'arrive' column.")
                return

            # Replace empty cells in columns 'A', 'B', 'C', 'Interface de sortie' with '/'
            for i in range(1, 5):  # Columns 'A', 'B', 'C', 'Interface de sortie'
                for entry in self.table_entries[i::len(self.table_data)]:
                    if entry.get() == '':
                        entry.insert(0, '/')  # Insert '/' in empty cells

            # Continue with the statistics calculation
            # Display values for "Les temps d'arrive" (first column)
            column_values_arrive = [entry.get() for entry in self.table_entries[::len(self.table_data)]]
            print(f"Les temps d'arrive: {', '.join(column_values_arrive)}")

            # Display values for "Files d'attente A" (second column)
            values_a = [entry.get() for entry in self.table_entries[1::len(self.table_data)] if entry.get() != '/']
            print(f"Files d'attente A: {', '.join(values_a)}")

            # Display values for "Files d'attente B" (third column)
            values_b = [entry.get() for entry in self.table_entries[2::len(self.table_data)] if entry.get() != '/']
            print(f"Files d'attente B: {', '.join(values_b)}")

            # Display values for "Files d'attente C" (fourth column)
            values_c = [entry.get() for entry in self.table_entries[3::len(self.table_data)] if entry.get() != '/']
            print(f"Files d'attente C: {', '.join(values_c)}")

            # les temp arrive les paquet a la file d'attent A
            arr_a = [column_values_arrive[i] for i, entry in enumerate(self.table_entries[1::len(self.table_data)]) if entry.get() != '/']
            print(f"Files d'attente Arr A: {','.join(arr_a)}")

            # les temp arrive les paquet a la file d'attent B
            arr_b = [column_values_arrive[i] for i, entry in enumerate(self.table_entries[2::len(self.table_data)]) if entry.get() != '/']
            print(f"Files d'attente Arr B: {','.join(arr_b)}")

                        # les temp arrive les paquet a la file d'attent C
            arr_c = [column_values_arrive[i] for i, entry in enumerate(self.table_entries[3::len(self.table_data)]) if entry.get() != '/']
            print(f"Files d'attente Arr: {','.join(arr_c)}")

            # Calculate the sum of A, B, and C for Interface de sortie
            sum_of_abc = len(values_a) + len(values_b) + len(values_c)
            print(f"Interface de sortie: {sum_of_abc}")

#####             # Initialize the DC
            tmp = float(''.join(column_values_arrive[0]))
            dca, dcb, dcc = 0, 0, 0
            print(tmp)
            # Initialize the index to control the queues
            i, j, k, l = 0, 0, 0, 0

            F = [0] * sum_of_abc
            while l < int(sum_of_abc):
                # Update DC
                dca += dc_value
                dcb += dc_value
                dcc += dc_value
              #  print(f'tour{l}')
                # Give priority to A
                while dca != 0 and i < len(values_a) and int(values_a[i]) <= dca:
                  #  print(f'tour{l}')
                   # print('AAAAA')
                    if float(arr_a[i]) > tmp :
                        dca = 0
                        break
                    else:
                        tmp += int(values_a[i]) / 1000
                        F[l] = 'A(' + values_a[i] +')'  # set values Interface de sortie
                        dca -= int(values_a[i])
                        print(f"sortie{F[l]}")
                        print(dca)
                        l += 1
                        i += 1
                        print(f"tewmp{tmp}")
                        #print("AAAAAA")
                # Then B
                while dcb != 0 and j < len(values_b) and int(values_b[j]) <= dcb:
                    if float(arr_b[j]) > tmp:
                        dcb = 0
                        break
                    else:
                        F[l] = 'B(' +values_b[j]+')'  # set values Interface de sortie
                        tmp += int(values_b[j]) / 1000
                        dcb -= int(values_b[j])
                        print(f"sortie{F[l]}")
                        l += 1
                        j += 1
                        print(f"temp:{tmp}")
                #        print('BBBB')


                # Then C
                while dcc != 0 and k < len(values_c) and int(values_c[k]) <= dcc:
                   # print('CCCC')
                    if float(arr_c[k]) > tmp:
                        dcc = 0
                        break
                    else:
                        F[l] = 'C (' + values_c[k]+')'  # set values Interface de s
                        tmp += int(values_c[k]) / 1000
                        dcc -= int(values_c[k])
                        print(f"sortie{F[l]}")
                        l += 1
                        k += 1
                        print(f"temp:{tmp}")

            # Update the locked status
            self.locked = True

            # Disable the "Add Column" button after clicking "DRR"
            self.add_column_button.config(state=tk.DISABLED)

            # Disable all Entry widgets to prevent further changes
            for entry in self.table_entries:
                entry.config(state=tk.DISABLED)

            # Create and display the new tables
            self.display_new_table(self.new_table_canvas_a,list(reversed(values_a)) , "Files d'attente A:")
            self.display_new_table(self.new_table_canvas_b, list(reversed(values_b)), "Files d'attente B:")
            self.display_new_table(self.new_table_canvas_c, list(reversed(values_c)), "Files d'attente C:")
            self.display_new_table(self.new_table_canvas_output, list(reversed(F)), "Interface de sortie:")

    def display_new_table(self, canvas, values, table_name):
        # Display the new table as a vector on the canvas
        canvas.delete("all")  # Clear previous content
        canvas.config(height=20)

        if isinstance(values, int):
           values = [values]

        for i, value in enumerate(values):
            x1 = i * 48
            x2 = (i + 1) * 48
            center_x = (x1 + x2) // 2

            # Calculate the vertical center of the canvas
            center_y = canvas.winfo_reqheight() // 2

            canvas.create_line(x1, 0, x1, 20, fill="black")
            canvas.create_text(center_x, center_y, text=f"{value}", anchor=tk.CENTER, font=("Helvetica", 10))


        # Show the canvas and label
        canvas.grid()
        canvas.update()

        # Dynamically create and show the label for the table
        label = tk.Label(self, text=f"{table_name}: {', '.join(map(str, values))}")
        label.grid(row=len(self.table_data) + 1, column=0, columnspan=2, sticky="nsew")
        label.grid_remove()



class DcFrame(tk.Frame):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.create_widgets()

    def create_widgets(self):
        # Label and entry for setting 'DC' value
        dc_label = tk.Label(self, text="Set DC value:")
        dc_label.grid(row=0, column=0, padx=10, pady=10)

        self.dc_entry = tk.Entry(self)
        self.dc_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to apply 'DC' value and trigger callback
        apply_button = tk.Button(self, text="Apply", command=self.apply_dc)
        apply_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Show the frame
        self.pack()

    def apply_dc(self):
        dc_value = self.dc_entry.get()

        # Check if 'DC' value is valid (you may need to add more validation)
        if dc_value.isdigit():
            self.callback(int(dc_value))
            self.destroy()
        else:
            messagebox.showwarning("Invalid Input", "'DC' value must be a positive integer.")


if __name__ == "__main__":
    # Initialize the original table with one column
    table_data = [
        ['Les temps d\'arrive', '1'],
        ['A', ''],
        ['B', ''],
        ['C', '']
    ]

    root = tk.Tk()
    root.title("Table Frame Example")

    table_frame = TableFrame(root, table_data=table_data)
    table_frame.pack(expand=True, fill="both")

    root.mainloop()
