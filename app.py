from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import re


class window_UI():
    def setupUi(self, window):

        # Window Position
        window_width = 500
        window_height = 200
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window.geometry(
            f"{window_width}x{window_height}+{center_x}+{center_y}")

        # Configure
        window.configure(bg="Black")
        window.title("Files Renamer")
        window.resizable(False, False)

        # Folder Loc
        # Folder_Label
        self.folder_label = Label(
            window,
            text="Folder Location : ",
            font=("Times New ROman", 15),
            bg="Gray", fg="White"
        )
        self.folder_label.place(x=10, y=10)

        # Folder_Entry
        self.folder_entry = Entry(window, width=28, font=(
            "Times New Roman", 15), cursor="xterm")
        self.folder_entry.place(x=170, y=10)

        # Open_Folder_Image
        self.img_file = r"E:\Development\Python\My Project's\Files Renamer\folder_open.png"
        self.image = Image.open(self.img_file)
        max_width = 20
        self.pixels_x, self.pixels_y = tuple(
            [int(max_width/self.image.size[0] * x) for x in self.image.size])

        self.img = ImageTk.PhotoImage(
            self.image.resize((self.pixels_x, self.pixels_y)))

        # Open_Folder_Button
        self.folder_btn = Button(window,
                                 width=25,
                                 bg="Gray", image=self.img, cursor="hand2", command=self.open_folder)

        self.folder_btn.place(x=462, y=10)

        # Name_Label
        self.name_label = Label(
            window,
            text="Series Name : ",
            font=("Times New ROman", 15),
            bg="Gray", fg="White"
        )
        self.name_label.place(x=35, y=50)

        # Name_Entry
        self.name_entry = Entry(window, width=28, font=(
            "Times New Roman", 15), cursor="xterm")
        self.name_entry.place(x=170, y=50)

        # Submit_Button
        self.submit_btn = Button(window,
                                 width=15, text="Rename", font=("Times New Roman", 15),
                                 bg="Gray", fg="White",  cursor="hand2", command=self.submit)

        self.submit_btn.place(x=170, y=90)
        window.mainloop()

    # Open_Folder
    def open_folder(self):
        folder_path = filedialog.askdirectory(
            initialdir="D:/", title='Please select a directory')
        self.folder_entry.delete(0, END)
        self.folder_entry.insert(0, folder_path)

    # Submit
    def submit(self):
        self.series_name = self.name_entry.get()
        self.folder_name = self.folder_entry.get()
        os.chdir(self.folder_name)
        os.getcwd()
        self.files_list = os.listdir()
        for item in self.files_list:
            self.old_file_name = item
            season_regex = r"([Ss][\d]+)"
            episode_regex = r"([Ee][\d]+)"
            self.season = self.check_sea_ep(
                self.old_file_name, season_regex)
            self.episode = self.check_sea_ep(
                self.old_file_name, episode_regex)
            if self.season and self.episode:
                self.extenstion = self.chk_ext(self.old_file_name)
                self.new_file_name = f'{self.series_name} S{self.season}E{self.episode} {self.extenstion}'
                os.system(f'ren "{self.old_file_name}" "{self.new_file_name}"')
                print(
                    f"\n============================================\nName Changed from -> {self.old_file_name} to -> {self.new_file_name}\n============================================")

        # Result
        self.result_label = Label(
            window,
            text="Successful",
            font=("Times New Roman", 20),
            bg="Green", fg="White"
        )
        self.result_label.place(x=200, y=145)

    # Check_Season/Episode_No.
    @staticmethod
    def check_sea_ep(file, regex):
        try:
            string_SorE = (re.search(regex, file)).group(0)
            num_string = (re.search(r"[\d]+", string_SorE)).group(0)
            num_string = f'0{num_string}' if len(
                str(num_string)) == 1 and int(num_string) < 10 else num_string
            return num_string
        except:
            print("Filename not found in Regex")
            return None

    # Check_Extenstion
    @staticmethod
    def chk_ext(file):
        extenstion = ""
        for i in range(len(file)-1, -1, -1):
            if file[i] != ".":
                extenstion += file[i]
            else:
                break
        extenstion += "."
        return extenstion[::-1]


if __name__ == "__main__":
    app = window_UI()
    window = Tk()
    app.setupUi(window)
