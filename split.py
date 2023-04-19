#!/usr/bin/env python3
from pypdf import PdfReader, PdfWriter
import os
import sys
import shutil


class pdf_splitter:
    """
    PDF Splitter class to split a pdf into multiple pdfs
    """

    def __init__(self, filename):
        """
        Constructor for PDF Splitter class
        :param filename: The filename of the pdf to split
        """

        self.filename = filename
        self.reader = PdfReader(filename)
        self.number_of_pages = len(self.reader.pages)
        self.folder_name = filename.split(".")[0]

    def create_folder(self):
        """
        Create a folder for the split pdfs
        """

        # Create new folder
        os.mkdir(self.folder_name)
        print(f"Created folder {self.folder_name} for {self.filename}")

    def split_pdf(self):
        """
        Split the pdf into multiple pdfs and save them in the folder
        """

        print(f"Splitting {self.filename} into {self.number_of_pages} pages")
        # Split each page into a new pdf each
        for i in range(self.number_of_pages):
            print(f"Processing page {i} of {self.number_of_pages}")
            page = self.reader.pages[i]
            new_filename = f"{self.folder_name}/{i}.pdf"
            writer = PdfWriter()
            writer.add_page(page)
            with open(new_filename, "wb") as f:
                writer.write(f)

    def compress_folder(self):
        """
        Compress the folder into a zip file
        """

        # Compress folder
        print(f"Compressing {self.folder_name} into {self.folder_name}.zip")
        shutil.make_archive(self.folder_name, "zip", self.folder_name)

    def remove_folder(self):
        """
        Clean up the folder. Users will be able to choose whether to remove the folder or not
        """

        # Remove folder
        print(f"Removing {self.folder_name}")
        shutil.rmtree(self.folder_name)

    def run(self):
        """
        Script execution process
        """

        self.create_folder()
        self.split_pdf()
        self.compress_folder()


if __name__ == "__main__":
    """
    Main function to run the script
    """

    args = sys.argv
    if len(args) > 1:
        filename = args[1]
        print(f"Filename provided: {filename}")
    else:
        print("No filename provided, exiting")
        exit()

    pdf_splitter = pdf_splitter(filename)
    pdf_splitter.run()

    print("Remove folder? (y/n)")
    remove_folder = input()
    pdf_splitter.remove_folder() if remove_folder == "y" else print("Not removing folder")

    print("Done")
