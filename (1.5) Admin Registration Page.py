import customtkinter as ctk
import tkinter
import customtkinter
from PIL import ImageTk, Image
import re

def create_window(title):
    ctk.set_default_color_theme("green")
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("light")
    window.resizable(width=False, height=False)
    center_window(window)
    frame = create_frame(window)
    window.wm_title(title)
    return window, frame 

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_frame(window):
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def login_page():
    Login_page_window, frame = create_window("Login Page")
 
    LogPg_ad_txt = ctk.CTkLabel(master=frame, text="Login as Admin:", font=('Roboto', 25))
    LogPg_ad_txt.place(x=85, y=50)

    LogPg_emp_txt = ctk.CTkLabel(master=frame, text="Login as Employee:", font=('Roboto', 25))
    LogPg_emp_txt.place(x=450, y=50)

    LogPg_accreg1_txt = ctk.CTkLabel(master=frame, font=('Roboto', 19), text="Don't have an account?   Register here as an")
    LogPg_accreg1_txt.place(x=15, y=565)
    
    LogPg_accreg2_txt = ctk.CTkLabel(master=frame, text="Or an", font=('Roboto', 18))
    LogPg_accreg2_txt.place(x=535, y=565)

    LogPg_ad_underline = ctk.CTkButton(master=frame, width=190, height=3, corner_radius=0, text="")
    LogPg_ad_underline.place(x=78, y=80)
 
    LogPg_emp_underline = ctk.CTkButton(master=frame, width=230, height=3, corner_radius=0, text="")
    LogPg_emp_underline.place(x=442, y=80)

    LogPG_ad_compnam_entry = ctk.CTkEntry(master=frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    LogPG_ad_compnam_entry.place(x=43, y=140)

    LogPG_ad_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPG_ad_pass_entry.place(x=43, y=260)

    LogPg_emp_username_entry = ctk.CTkEntry(master=frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Username...')
    LogPg_emp_username_entry.place(x=428, y=140)

    LogPg_emp_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPg_emp_pass_entry.place(x=428, y=260)
    
    LogPg_log_button0 = ctk.CTkButton(master=frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_log_button0.place(x=75, y=350)

    LogPg_log_button1 = ctk.CTkButton(master=frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_log_button1.place(x=460, y=350)
    
    LogPg_refresh_button = ctk.CTkButton(master=frame, width=100, corner_radius=20, text="Refresh Page", font=('Roboto', 15))
    LogPg_refresh_button.place(x=5, y=5)

    LogPg_settings_button = ctk.CTkButton(master=frame, width=100, corner_radius=20, text="Settings", font=('Roboto', 15))
    LogPg_settings_button.place(x=645, y=5)

    LogPg_ad_reg_button = ctk.CTkButton(master=frame, width=115, text="Admin", corner_radius=20, font=('Roboto', 15))
    LogPg_ad_reg_button.configure(command=lambda: admin_registration_page(Login_page_window))
    LogPg_ad_reg_button.place(x=400, y=565)

    LogPg_emp_reg_button = ctk.CTkButton(master=frame, width=115, text="Employee", corner_radius=20, font=('Roboto', 15))
    LogPg_emp_reg_button.place(x=610, y=565)
    
    Login_page_window.mainloop()

def admin_registration_page(login_window):
    login_window.destroy()
    Admin_registration_window, admin_frame = create_window("Admin Registration")
    
    AdPg_return_button = ctk.CTkButton(master=admin_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    AdPg_return_button.configure(command=lambda: return_to_login(Admin_registration_window))
    AdPg_return_button.place(x=645, y=5)

    Admin_registration_window.mainloop()

def return_to_login(admin_registration_window):
    admin_registration_window.destroy()
    login_page()

if __name__ == "__main__":
    login_window, login_frame = login_page()
