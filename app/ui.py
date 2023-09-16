import customtkinter


class mainPage:

    def __init__(self, app):
        app.title("README Generator")
        app.geometry("1425x700")
        app.resizable(False, False)
        app.grab_set()

        title_label = customtkinter.CTkLabel(app, text="Remplissez les champs", fg_color="transparent", font=("Arial", 25, "bold", "underline"))
        title_label.pack(padx=10, pady=10)

        # séparatione en 3 frames, une coolonne de gauche et une de centre et une de droite
        # colonne de gauche
        left_frame = customtkinter.CTkFrame(app)
        left_frame.pack(side="left", padx=10, pady=10)

        # colonne du centre
        center_frame = customtkinter.CTkFrame(app)
        center_frame.pack(side="left", padx=10, pady=10)

        # colonne de droite
        right_frame = customtkinter.CTkFrame(app)
        right_frame.pack(side="left", padx=10, pady=10)


        # Nom du projet
        project_name_label = customtkinter.CTkLabel(left_frame, text="Nom du projet:", fg_color="transparent", font=("Arial", 15, "bold"))
        project_name_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)
        self.project_name_entry = customtkinter.CTkEntry(left_frame, width=200)
        self.project_name_entry.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

        # Description
        description_label = customtkinter.CTkLabel(left_frame, text="Description:", fg_color="transparent", font=("Arial", 15, "bold"))
        description_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
        self.description_text = customtkinter.CTkTextbox(left_frame, width=400, height=150)
        self.description_text.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

        # key features
        features_label = customtkinter.CTkLabel(left_frame, text="Features:", fg_color="transparent", font=("Arial", 15, "bold"))
        features_label.grid(column=0, row=2, sticky="w", padx=5, pady=5)
        add_feature_button = customtkinter.CTkButton(left_frame, text="Ajouter une feature", font=("Arial", 13, "bold"), command=self.add_feature)
        remove_feature_button = customtkinter.CTkButton(left_frame, text="Supprimer une feature", font=("Arial", 13, "bold"), command=self.remove_feature)
        remove_feature_button.grid(column=2, row=2, sticky="w")
        add_feature_button.grid(column=1, row=2, sticky="w")
        self.features_frame = customtkinter.CTkFrame(left_frame, width=400, height=150)
        self.features_frame.grid(column=1, row=3, columnspan=4, padx=5, pady=5)

        # sreenchots
        screenshots_label = customtkinter.CTkLabel(left_frame, text="Screenshots:", fg_color="transparent",
                                                   font=("Arial", 15, "bold"))
        screenshots_label.grid(column=0, row=4, sticky="w", padx=5, pady=5)
        add_screenshot_button = customtkinter.CTkButton(left_frame, text="Ajouter un screenshot",
                                                        font=("Arial", 13, "bold"), command=self.add_screenshot)
        remove_screenshot_button = customtkinter.CTkButton(left_frame, text="Supprimer un screenshot",
                                                           font=("Arial", 13, "bold"), command=self.remove_screenshot)
        remove_screenshot_button.grid(column=2, row=4, sticky="w")
        add_screenshot_button.grid(column=1, row=4, sticky="w")
        self.screenshots_frame = customtkinter.CTkFrame(left_frame, width=400, height=150)
        self.screenshots_frame.grid(column=1, row=5, columnspan=4, padx=5, pady=5)

        # tutoriel d'installation et d'utilisation
        tutorial_label = customtkinter.CTkLabel(center_frame, text="Tutoriel d'installation et d'utilisation:",
                                                fg_color="transparent", font=("Arial", 15, "bold"))
        tutorial_label.grid(column=0, row=6, sticky="w", padx=5, pady=5)
        self.tutorial_text = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.tutorial_text.grid(column=1, row=6, columnspan=2, padx=5, pady=5)

        # sources
        sources_label = customtkinter.CTkLabel(center_frame, text="Sources:", fg_color="transparent", font=("Arial", 15, "bold"))
        sources_label.grid(column=0, row=7, sticky="w", padx=5, pady=5)
        self.sources_text = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.sources_text.grid(column=1, row=7, columnspan=2, padx=5, pady=5)

        # champ personnalisé
        custom_field_label = customtkinter.CTkLabel(center_frame, text="Champ personnalisé:", fg_color="transparent", font=("Arial", 15, "bold"))
        custom_field_label.grid(column=0, row=8, sticky="w", padx=5, pady=5)
        self.custom_field_entry = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.custom_field_entry.grid(column=1, row=8, columnspan=2, padx=5, pady=5)

        # version
        version_label = customtkinter.CTkLabel(center_frame, text="Version:", fg_color="transparent",
                                               font=("Arial", 15, "bold"))
        version_label.grid(column=0, row=9, sticky="w", padx=5, pady=5)
        self.version_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.version_entry.grid(column=1, row=9, columnspan=2, padx=5, pady=5)

        # auteur
        author_label = customtkinter.CTkLabel(center_frame, text="Auteur:", fg_color="transparent",
                                              font=("Arial", 15, "bold"))
        author_label.grid(column=0, row=10, sticky="w", padx=5, pady=5)
        self.author_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.author_entry.grid(column=1, row=10, columnspan=2, padx=5, pady=5)

        # contact
        contact_label = customtkinter.CTkLabel(center_frame, text="Contact:", fg_color="transparent",
                                                  font=("Arial", 15, "bold"))
        contact_label.grid(column=0, row=11, sticky="w", padx=5, pady=5)
        self.contact_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.contact_entry.grid(column=1, row=11, columnspan=2, padx=5, pady=5)





        # bouton pour générer le README
        generate_button = customtkinter.CTkButton(right_frame, text="Générer le README", font=("Arial", 10, "bold"), command=self.generate_readme)
        generate_button.grid(column=0, row=0, padx=5, pady=5)

        # bouton pour quitter l'application
        quit_button = customtkinter.CTkButton(right_frame, text="Quitter", font=("Arial", 10, "bold"), command=app.destroy)
        quit_button.grid(column=0, row=1, padx=5, pady=5)

        # bouton pour ouvrir le README
        open_button = customtkinter.CTkButton(right_frame, text="Ouvrir le README", font=("Arial", 10, "bold"), command=self.open_readme)
        open_button.grid(column=0, row=2, padx=5, pady=5)

        # aide
        help_button = customtkinter.CTkButton(right_frame, text="Aide", font=("Arial", 10, "bold"), command=self.open_help)
        help_button.grid(column=0, row=3, padx=5, pady=5)

        # petit texte en bas de page
        footer_label = customtkinter.CTkLabel(right_frame, text="tout les champs \n non rempli ne seront \n pas dans le readme", fg_color="transparent", font=("Arial", 10, "bold"))
        footer_label.grid(column=0, row=4, padx=5, pady=5)



    def add_feature(self):
        # ajoute un feature
        pass

    def remove_feature(self):
        # supprime un feature
        pass

    def add_screenshot(self):
        # ajoute un screenshot
        pass

    def remove_screenshot(self):
        # supprime un screenshot
        pass

    def generate_readme(self):
        # génère le README
        pass

    def open_readme(self):
        # ouvre le README
        pass

    def open_help(self):
        # ouvre l'aide
        pass







if __name__ == "__main__":
    root = customtkinter.CTk()
    mainPage(root)
    root.mainloop()

