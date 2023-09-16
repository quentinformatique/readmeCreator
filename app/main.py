import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class READMEGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("README Generator")

        # Créez un cadre principal
        main_frame = ttk.Frame(root, padding=20)
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Titre
        title_label = ttk.Label(main_frame, text="Titre du Projet:")
        title_label.grid(column=0, row=0, sticky=tk.W)
        self.title_entry = ttk.Entry(main_frame, width=40)
        self.title_entry.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

        # Logo
        logo_label = ttk.Label(main_frame, text="Logo (URL):")
        logo_label.grid(column=0, row=4, sticky=tk.W)
        self.logo_entry = ttk.Entry(main_frame, width=40)
        self.logo_entry.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

        # Description
        description_label = ttk.Label(main_frame, text="Description:")
        description_label.grid(column=0, row=1, sticky=tk.W)
        self.description_text = tk.Text(main_frame, width=40, height=5)
        self.description_text.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

        # Capture d'écran
        screenshot_label = ttk.Label(main_frame, text="Capture d'écran (URL):")
        screenshot_label.grid(column=0, row=2, sticky=tk.W)
        self.screenshot_entry = ttk.Entry(main_frame, width=40)
        self.screenshot_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

        # Sources
        sources_label = ttk.Label(main_frame, text="Sources (URL):")
        sources_label.grid(column=0, row=5, sticky=tk.W)
        self.sources_entry = ttk.Entry(main_frame, width=40)
        self.sources_entry.grid(column=1, row=5, columnspan=2, padx=5, pady=5)

        # Auteur
        author_label = ttk.Label(main_frame, text="Auteur:")
        author_label.grid(column=0, row=6, sticky=tk.W)
        self.author_entry = ttk.Entry(main_frame, width=40)
        self.author_entry.grid(column=1, row=6, columnspan=2, padx=5, pady=5)

        # Version
        version_label = ttk.Label(main_frame, text="Version:")
        version_label.grid(column=0, row=7, sticky=tk.W)
        self.version_entry = ttk.Entry(main_frame, width=40)
        self.version_entry.grid(column=1, row=7, columnspan=2, padx=5, pady=5)

        # Instructions d'Installation
        install_label = ttk.Label(main_frame, text="Instructions d'Installation:")
        install_label.grid(column=0, row=3, sticky=tk.W)
        self.install_text = tk.Text(main_frame, width=40, height=5)
        self.install_text.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

        # Aide
        help_button = ttk.Button(main_frame, text="Aide", command=self.help)
        help_button.grid(column=0, row=8, columnspan=3, padx=5, pady=10)

        # Bouton Générer README
        generate_button = ttk.Button(main_frame, text="Générer README", command=self.generate_readme)
        generate_button.grid(column=0, row=9, columnspan=3, padx=5, pady=10)

    def help(self):
        # Nouvelle fenêtre décrivant comment utiliser l'app
        help_window = tk.Toplevel(self.root)
        help_window.title("Aide")
        help_window.resizable(False, False)
        help_window.grab_set()

        # Créez un cadre principal
        main_frame = ttk.Frame(help_window, padding=20)
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Contenu
        help_label = ttk.Label(main_frame,
                               text="Pour utiliser l'application, remplissez les champs avec les informations demandées.\n"
                                    "Une fois les champs remplis, cliquez sur le bouton 'Générer README'.\n"
                                    "Le README sera généré dans le dossier 'output' du projet. Si un champ n'est pas rempli, il sera ignoré.")
        help_label.grid(column=0, row=0, sticky=tk.W)

        # Bouton Fermer
        close_button = ttk.Button(main_frame, text="Fermer", command=help_window.destroy)
        close_button.grid(column=0, row=1, columnspan=3)

    def generate_readme(self):
        # Récupérez les données saisies par l'utilisateur et générez le README ici
        title = self.title_entry.get()
        description = self.description_text.get("1.0", "end-1c")
        screenshot = self.screenshot_entry.get()
        install_instructions = self.install_text.get("1.0", "end-1c")
        sources = self.sources_entry.get()
        author = self.author_entry.get()
        version = self.version_entry.get()
        logo_url = self.logo_entry.get()

        # Vous pouvez maintenant utiliser ces données pour générer le README dans le format souhaité.


if __name__ == "__main__":
    root = ThemedTk(theme="black")
    app = READMEGeneratorApp(root)
    root.mainloop()
