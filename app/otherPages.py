import customtkinter


def error_window(message):
    # Display an error message
    window = customtkinter.CTk()
    window.title("Error")
    window.resizable(False, False)
    window.iconbitmap("img/logo.ico")

    error_label = customtkinter.CTkLabel(window, text=message,
                                         fg_color="transparent", font=("Arial", 15, "bold"))
    error_label.pack(padx=5, pady=5)

    ok_button = customtkinter.CTkButton(window, text="OK", font=("Arial", 10, "bold"), command=window.destroy)
    ok_button.pack(padx=5, pady=5)

    window.mainloop()


def open_help():
    window = customtkinter.CTk()
    window.title("Help")
    window.resizable(False, False)
    window.iconbitmap("img/logo.ico")

    title_label = customtkinter.CTkLabel(window, text="Help", fg_color="transparent", font=("Arial", 20, "bold"))
    title_label.pack(padx=5, pady=5)

    help_label = customtkinter.CTkLabel(window, text="To use the application, fill in the fields \n"
                                                     "and add features and screenshots by clicking the corresponding buttons. \n"
                                                     "Once everything is filled out, click the \"Generate README\" button to create the README. \n"
                                                     "The readme will be generated in the project's root directory. \n"
                                                     "To exit the application, click the \"Quit\" button.",
                                        fg_color="transparent", font=("Arial", 15, "bold"))
    help_label.pack(padx=5, pady=5)

    author_label = customtkinter.CTkLabel(window, text="Author: Quentin Costes", fg_color="transparent",
                                          font=("Arial", 15, "bold"))
    author_label.pack(padx=5, pady=5)

    contact_label = customtkinter.CTkLabel(window, text="Contact: discord: Quentinou", fg_color="transparent",
                                           font=("Arial", 15, "bold"))
    contact_label.pack(padx=5, pady=5)

    button_quit = customtkinter.CTkButton(window, text="Quit", font=("Arial", 15, "bold"),
                                          command=window.destroy)
    button_quit.pack(padx=5, pady=5)

    window.mainloop()

