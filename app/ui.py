import customtkinter
import generator.readme_generator as generator
import app.otherPages as pages


class mainPage:
    featuresCount = 0
    screenshotsCount = 0
    featuresEntryList = []
    screenshotsEntryList = []

    def __init__(self, app):
        app.title("README Generator")
        app.geometry("1390x800")
        app.resizable(False, False)
        app.grab_set()
        app.iconbitmap("img/logo.ico")

        title_label = customtkinter.CTkLabel(app, text="Fill up the fields and generate your file", fg_color="transparent",
                                             font=("Arial", 25, "bold", "underline"))
        title_label.pack(padx=10, pady=10)

        # Left frame
        left_frame = customtkinter.CTkFrame(app)
        left_frame.pack(side="left", padx=10, pady=10)

        # Middle frame
        center_frame = customtkinter.CTkFrame(app)
        center_frame.pack(side="left", padx=10, pady=10)

        # Right frame
        right_frame = customtkinter.CTkFrame(app)
        right_frame.pack(side="left", padx=10, pady=10)

        # Project Name
        project_name_label = customtkinter.CTkLabel(left_frame, text="Project name: ", fg_color="transparent",
                                                    font=("Arial", 15, "bold"))
        project_name_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)
        self.project_name_entry = customtkinter.CTkEntry(left_frame, width=200)
        self.project_name_entry.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

        # Logo
        logo_label = customtkinter.CTkLabel(left_frame, text="Logo:", fg_color="transparent",
                                            font=("Arial", 15, "bold"))
        logo_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
        self.logo_entry = customtkinter.CTkEntry(left_frame, width=200)
        self.logo_entry.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

        # Description
        description_label = customtkinter.CTkLabel(left_frame, text="Description:", fg_color="transparent",
                                                   font=("Arial", 15, "bold"))
        description_label.grid(column=0, row=3, sticky="w", padx=5, pady=5)
        self.description_text = customtkinter.CTkTextbox(left_frame, width=400, height=150)
        self.description_text.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

        # check box for download link, Change log, Report a bug, Request a feature
        self.download_link_var = customtkinter.IntVar()
        self.report_bug_var = customtkinter.IntVar()
        self.request_feature_var = customtkinter.IntVar()
        self.download_link_checkbox = customtkinter.CTkCheckBox(left_frame, text="Download link     ",
                                                                     variable=self.download_link_var,
                                                                        font=("Arial", 15, "bold"))
        self.report_bug_checkbox = customtkinter.CTkCheckBox(left_frame, text="Report a bug",
                                                                    variable=self.report_bug_var,
                                                                        font=("Arial", 15, "bold"))
        self.request_feature_checkbox = customtkinter.CTkCheckBox(left_frame, text="Request a feature",
                                                                        variable=self.request_feature_var,
                                                                        font=("Arial", 15, "bold"))
        self.download_link_checkbox.grid(column=0, row=4, sticky="w", padx=5, pady=5)
        self.report_bug_checkbox.grid(column=1, row=4, sticky="w", padx=5, pady=5)
        self.request_feature_checkbox.grid(column=2, row=4, sticky="w", padx=5, pady=5)


        # Key Features
        features_label = customtkinter.CTkLabel(left_frame, text="Features:", fg_color="transparent",
                                                font=("Arial", 15, "bold"))
        features_label.grid(column=0, row=6, sticky="w", padx=5, pady=5)
        add_feature_button = customtkinter.CTkButton(left_frame, text="Add a feature", font=("Arial", 13, "bold"),
                                                     command=self.add_feature)
        remove_feature_button = customtkinter.CTkButton(left_frame, text="Delete a feature",
                                                        font=("Arial", 13, "bold"), command=self.remove_feature)
        remove_feature_button.grid(column=2, row=6, sticky="w")
        add_feature_button.grid(column=1, row=6, sticky="w")
        self.features_frame = customtkinter.CTkFrame(left_frame, width=400, height=35)
        self.features_frame.grid(column=1, row=7, columnspan=4, padx=5, pady=5)

        # Screenshots
        screenshots_label = customtkinter.CTkLabel(left_frame, text="Screenshots:", fg_color="transparent",
                                                   font=("Arial", 15, "bold"))
        screenshots_label.grid(column=0, row=8, sticky="w", padx=5, pady=5)
        add_screenshot_button = customtkinter.CTkButton(left_frame, text="Add a screenshot",
                                                        font=("Arial", 13, "bold"), command=self.add_screenshot)
        remove_screenshot_button = customtkinter.CTkButton(left_frame, text="Delete a screenshot",
                                                           font=("Arial", 13, "bold"), command=self.remove_screenshot)
        remove_screenshot_button.grid(column=2, row=8, sticky="w")
        add_screenshot_button.grid(column=1, row=8, sticky="w")
        self.screenshots_frame = customtkinter.CTkFrame(left_frame, width=400, height=35)
        self.screenshots_frame.grid(column=1, row=9, columnspan=4, padx=5, pady=5)

        # Installation and Usage Tutorial
        tutorial_label = customtkinter.CTkLabel(center_frame, text="Installation tutorial:",
                                                fg_color="transparent", font=("Arial", 15, "bold"))
        tutorial_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)
        self.tutorial_text = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.tutorial_text.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

        # Sources
        sources_label = customtkinter.CTkLabel(center_frame, text="Sources:", fg_color="transparent",
                                               font=("Arial", 15, "bold"))
        sources_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
        self.sources_text = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.sources_text.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

        # Custom Field
        custom_field_label = customtkinter.CTkLabel(center_frame, text="Customized field title:", fg_color="transparent",
                                                    font=("Arial", 15, "bold"))
        custom_field_label.grid(column=0, row=2, sticky="w", padx=5, pady=5)
        # the title of the field
        self.custom_field_title = customtkinter.CTkEntry(center_frame, width=200)
        self.custom_field_title.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
        # the content of the field
        custom_field_label = customtkinter.CTkLabel(center_frame, text="Customized field content:",
                                                    fg_color="transparent",
                                                    font=("Arial", 15, "bold"))
        custom_field_label.grid(column=0, row=3, sticky="w", padx=5, pady=5)
        self.custom_field_entry = customtkinter.CTkTextbox(center_frame, width=400, height=150)
        self.custom_field_entry.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

        # Version
        version_label = customtkinter.CTkLabel(center_frame, text="Version:", fg_color="transparent",
                                               font=("Arial", 15, "bold"))
        version_label.grid(column=0, row=4, sticky="w", padx=5, pady=5)
        self.version_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.version_entry.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

        # Contact
        contact_label = customtkinter.CTkLabel(center_frame, text="Contact:", fg_color="transparent",
                                               font=("Arial", 15, "bold"))
        contact_label.grid(column=0, row=6, sticky="w", padx=5, pady=5)
        self.contact_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.contact_entry.grid(column=1, row=6, columnspan=2, padx=5, pady=5)

        # Contributors
        contributor_label = customtkinter.CTkLabel(center_frame, text="contributors:", fg_color="transparent",
                                              font=("Arial", 15, "bold"))
        contributor_label.grid(column=0, row=7, sticky="w", padx=5, pady=5)
        self.contributor_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.contributor_entry.grid(column=1, row=7, columnspan=2, padx=5, pady=5)

        # Author
        author_label = customtkinter.CTkLabel(center_frame, text="github username:", fg_color="transparent",
                                              font=("Arial", 15, "bold"))
        author_label.grid(column=0, row=8, sticky="w", padx=5, pady=5)
        self.author_entry = customtkinter.CTkEntry(center_frame, width=200)
        self.author_entry.grid(column=1, row=8, columnspan=2, padx=5, pady=5)

        # Right frame
        # Generate README button
        generate_button = customtkinter.CTkButton(right_frame, text="Generate README", font=("Arial", 13, "bold"),
                                                  command=lambda: self.generate())
        generate_button.grid(column=0, row=0, padx=5, pady=5)

        # Quit button
        quit_button = customtkinter.CTkButton(right_frame, text="Quit", font=("Arial", 15, "bold"),
                                              command=app.destroy)
        quit_button.grid(column=0, row=1, padx=5, pady=5)

        # Help button
        help_button = customtkinter.CTkButton(right_frame, text="Help", font=("Arial", 15, "bold"),
                                              command=pages.open_help)
        help_button.grid(column=0, row=3, padx=5, pady=5)

        # Footer
        footer_label = customtkinter.CTkLabel(right_frame,
                                              text="Fields that are not\nfilled will not appear\n in the readme",
                                              fg_color="transparent", font=("Arial", 10, "bold"))
        footer_label.grid(column=0, row=4, padx=5, pady=5)
        footer_label = customtkinter.CTkLabel(right_frame,
                                              text="You can write Markdown\n in the fields",
                                              fg_color="transparent", font=("Arial", 10, "bold"))
        footer_label.grid(column=0, row=5, padx=5, pady=5)
        footer_label = customtkinter.CTkLabel(right_frame,
                                              text="For images, enter their\n relative links (they must\n be in the readme folder)",
                                              fg_color="transparent", font=("Arial", 10, "bold"))
        footer_label.grid(column=0, row=6, padx=5, pady=5)
        footer_label = customtkinter.CTkLabel(right_frame,
                                              text="for the chexbox,\n make sure that the\n project name is\n the same as the repo name\n and your enter your username",
                                              fg_color="transparent", font=("Arial", 10, "bold"))
        footer_label.grid(column=0, row=7, padx=5, pady=5)

    def add_feature(self):
        # Add a feature to the list
        if self.featuresCount < 6:
            self.featuresEntryList.append(customtkinter.CTkEntry(self.features_frame, width=400))
            self.featuresEntryList[self.featuresCount].pack(padx=5, pady=5)
            self.featuresCount += 1
            self.featuresEntryList[self.featuresCount - 1].focus()
        else:
            pages.error_window("You can't add more than 6 features!")


    def remove_feature(self):
        # Remove a feature from the list
        if self.featuresCount > 0:
            self.featuresEntryList[self.featuresCount - 1].destroy()
            self.featuresEntryList.pop()
            self.featuresCount -= 1
        else:
            pages.error_window("You can't remove more features!")

    def add_screenshot(self):
        # Add a screenshot to the list
        if self.screenshotsCount < 3:
            self.screenshotsEntryList.append(customtkinter.CTkEntry(self.screenshots_frame, width=400))
            self.screenshotsEntryList[self.screenshotsCount].pack(padx=5, pady=5)
            self.screenshotsCount += 1
            self.screenshotsEntryList[self.screenshotsCount - 1].focus()
        else:
            pages.error_window("You can't add more than 3 screenshots!")

    def remove_screenshot(self):
        # Remove a screenshot from the list
        if self.screenshotsCount > 0:
            self.screenshotsEntryList[self.screenshotsCount - 1].destroy()
            self.screenshotsEntryList.pop()
            self.screenshotsCount -= 1
        else:
            pages.error_window("You can't remove more screenshots!")

    def generate(self):
        features = []
        screenshots = []

        checkboxs= (self.download_link_var.get(), self.report_bug_var.get(), self.request_feature_var.get())

        for entry in self.featuresEntryList:
            features.append(entry.get())

        for entry in self.screenshotsEntryList:
            screenshots.append(entry.get())

        generator.GenerateReadme(self.project_name_entry.get(), self.logo_entry.get(), self.description_text.get("1.0", "end"),
                                 checkboxs, features, screenshots, self.tutorial_text.get("1.0", "end"),
                                 self.sources_text.get("1.0", "end"), self.custom_field_entry.get("1.0", "end"),
                                 self.custom_field_title.get(), self.version_entry.get(),
                                 self.author_entry.get(), self.contributor_entry.get(), self.contact_entry.get())
