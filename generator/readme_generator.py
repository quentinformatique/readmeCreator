class GenerateReadme:
    def __init__(self, title, logo, description, checkboxs, features, screenshots, installation, sources, personalized,
                 personalizedTitle, version, author, contributors, contact):
        self.title = title
        self.logo = logo
        self.description = description
        self.features = features
        self.screenshots = screenshots
        self.installation = installation
        self.sources = sources
        self.personalized = personalized
        self.personalizedTitle = personalizedTitle
        self.version = version
        self.author = author
        self.contact = contact
        self.checkboxs = checkboxs
        self.contributors = contributors
        self.generate()

    def generate(self):
        print("generate")
        # If the file already exists, delete it
        try:
            readme = open("result.md", "x")
        except FileExistsError:
            readme = open("result.md", "w")
            # Remove the file's content
            readme.truncate(0)

        if self.title.strip() or self.logo.strip():
            if self.title.strip() and self.logo.strip():
                readme.write("<div align=\"center\">\n")
                readme.write("<img src=\""+self.logo+"\">\n\n")
                readme.write("# " + self.title+"\n\n---\n\n")
                readme.write("</div>\n\n")

            elif self.title.strip() and not self.logo.strip():
                readme.write("<div align=\"center\">\n\n")
                readme.write("# " + self.title+"\n\n---\n")
                readme.write("</div>\n\n")
            else:
                readme.write("<div align=\"center\">\n")
                readme.write("<img src=\""+self.logo+"\">\n")
                readme.write("</div>\n\n---\n\n")

        if self.description.strip():
            readme.write(self.description + "\n")

        if self.checkboxs[0] == 1 or self.checkboxs[1] == 1 or self.checkboxs[2] == 1:
            readme.write("<div align=\"center\">\n")
            if self.checkboxs[0] == 1:
                readme.write("-<a href=\"https://github.com/"+self.author+"/"+self.title+"/releases/latest\">Download</a>-")
            if self.checkboxs[1] == 1:
                readme.write("-<a href=\"https://github.com/"+self.author+"/"+self.title+"/issues/new/choose\">Report a bug</a>-")
            if self.checkboxs[2] == 1:
                readme.write("-<a href=\"https://github.com/"+self.author+"/"+self.title+"/issues/new/choose\">Request a feature</a>-\n")
            readme.write("</div>\n\n")

        if len(self.features) != 0:
            readme.write("## Features\n\n---\n")
            for feature in self.features:
                readme.write("- " + feature + "\n")

        if len(self.screenshots) != 0:
            readme.write("## Screenshots\n\n---\n")
            for screenshot in self.screenshots:
                readme.write("![alt text](" + screenshot + ")\n")

        if self.installation.strip():
            readme.write("## Installation\n\n---\n")
            readme.write(self.installation + "\n")

        if self.sources.strip():
            readme.write("## Sources\n\n---\n")
            readme.write(self.sources + "\n")

        if self.personalized.strip() or self.personalizedTitle.strip():
            readme.write("## " + self.personalizedTitle + "\n\n---\n")
            readme.write(self.personalized + "\n")

        if self.contact.strip():
            readme.write("## Contact: \n\n---\n")
            readme.write(self.contact + "\n")

        if self.contributors.strip():
            readme.write("## contributors: \n\n---\n")
            readme.write(self.author + "\n")

        if self.version.strip():
            readme.write("## Version: ")
            readme.write(self.version + "\n")

        readme.close()
