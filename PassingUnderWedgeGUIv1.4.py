#PassingUnderWedgeGUIv1.4
#Author: Austin Smith
#Email: ThatSmittyDude@outlook.com
#github.com/ThatSmittyDude
#passingunderyellow.com
#Unix Timestamp: 1705017016

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
root = customtkinter.CTk()
root.geometry("650x450")

def calculate_wedge(event=None):
    LF = float(entry_LF.get())
    LR = float(entry_LR.get())
    RF = float(entry_RF.get())
    RR = float(entry_RR.get())
    total = LF + LR + RF + RR
    wedge = round((( RF + LR ) / total)*100, 1)
    
    label_result_total.configure(text=f"Total weight: {total}")
    label_result_wedge.configure(text=f"Wedge: {wedge}")

root = customtkinter.CTk()
root.geometry("400x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=5, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=frame, text="Passing Under Wedge")
label_title.pack(pady=5)

label_LF = customtkinter.CTkLabel(master=frame, text="LF corner weight:")
label_LF.pack(pady=5)
entry_LF = customtkinter.CTkEntry(master=frame, width=200)
entry_LF.pack(pady=5)

label_LR = customtkinter.CTkLabel(master=frame, text="LR corner weight:")
label_LR.pack(pady=5)
entry_LR = customtkinter.CTkEntry(master=frame, width=200)
entry_LR.pack(pady=5)

label_RF = customtkinter.CTkLabel(master=frame, text="RF corner weight:")
label_RF.pack(pady=5)
entry_RF = customtkinter.CTkEntry(master=frame, width=200)
entry_RF.pack(pady=5)

label_RR = customtkinter.CTkLabel(master=frame, text="RR corner weight:")
label_RR.pack(pady=5)
entry_RR = customtkinter.CTkEntry(master=frame, width=200)
entry_RR.pack(pady=5)

button_calculate_wedge = customtkinter.CTkButton(master=frame, text="Calculate wedge", command=calculate_wedge)
button_calculate_wedge.pack(pady=5)

label_result_total = customtkinter.CTkLabel(master=frame, text="Total weight:")
label_result_total.pack(pady=5)

label_result_wedge = customtkinter.CTkLabel(master=frame, text="Wedge:")
label_result_wedge.pack(pady=5)

label_puy = customtkinter.CTkLabel(master=frame, text="passingunderyellow.com")
label_puy.pack(pady=5)

label_git = customtkinter.CTkLabel(master=frame, text="github.com/ThatSmittyDude")
label_git.pack(pady=5)

root.bind('<Return>', lambda event=None: button_calculate_wedge.invoke())
root.mainloop()













