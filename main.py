import os
import re
from PIL import Image, ImageTk
from tkinter import END, Tk, filedialog, Label, Entry, Button


class window_UI:
    def __init__(self, window):
        self.window = window

    def setupUi(self):
        # Window Position
        window_width = 500
        window_height = 200
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # Configure
        self.window.configure(bg="Black")
        self.window.title("Files Renamer")
        self.window.resizable(False, False)

        # Style
        self.font_name_size = ("Times New Roman", 15)
        self.primary_background_color = "Gray"
        self.secondary_background_color = "Green"
        self.foreground_color = "White"

        # Folder Loc
        # Folder_Label
        self.folder_label = Label(
            self.window,
            text="Folder Location : ",
            font=self.font_name_size,
            bg=self.primary_background_color,
            fg=self.foreground_color,
        )
        self.folder_label.place(x=10, y=10)

        # Folder_Entry
        self.folder_entry = Entry(
            self.window, width=28, font=self.font_name_size, cursor="xterm"
        )
        self.folder_entry.place(x=170, y=10)

        # Open_Folder_Image
        self.img_file = r"folder_open.png"
        self.image = Image.open(self.img_file)
        max_width = 20
        self.pixels_x, self.pixels_y = tuple(
            [int(max_width / self.image.size[0] * x) for x in self.image.size]
        )

        self.img = ImageTk.PhotoImage(self.image.resize((self.pixels_x, self.pixels_y)))

        # Open_Folder_Button
        self.folder_btn = Button(
            self.window,
            width=25,
            bg=self.primary_background_color,
            image=self.img,
            cursor="hand2",
            command=self.ask_folder,
        )

        self.folder_btn.place(x=462, y=10)

        # Name_Label
        self.name_label = Label(
            self.window,
            text="Series Name : ",
            font=self.font_name_size,
            bg=self.primary_background_color,
            fg=self.foreground_color,
        )
        self.name_label.place(x=35, y=50)

        # Name_Entry
        self.name_entry = Entry(
            self.window, width=28, font=self.font_name_size, cursor="xterm"
        )
        self.name_entry.place(x=170, y=50)

        # Submit_Button
        self.submit_btn = Button(
            self.window,
            width=15,
            text="Rename",
            font=self.font_name_size,
            bg=self.primary_background_color,
            fg=self.foreground_color,
            cursor="hand2",
            command=self.on_submit_rename,
        )

        self.submit_btn.place(x=170, y=90)
        self.window.mainloop()

    # Open_Folder
    def ask_folder(self):
        folder_path = filedialog.askdirectory(
            initialdir="D:/", title="Please select a directory"
        )
        self.folder_entry.delete(0, END)
        self.folder_entry.insert(0, folder_path)

    # Submit
    def on_submit_rename(self):
        # Take Folder & Series name from user
        self.series_name = self.name_entry.get()
        self.folder_name = self.folder_entry.get()

        # Find folder in system
        os.chdir(self.folder_name)
        os.getcwd()
        self.files_list = os.listdir()

        # Traverse each file in folder
        for file in self.files_list:
            # Fetch Name and Extension of file
            self.old_file_name, self.extenstion = os.path.splitext(file)

            # Fetch Season and Episode from file
            season_regex = r"[Ss](\d+)"
            episode_regex = r"[Ee](\d+)"
            self.season = self.fetch_season_episode(self.old_file_name, season_regex)
            if self.season is None:
                continue
            self.episode = self.fetch_season_episode(self.old_file_name, episode_regex)

            # Rename file
            self.new_file_name = (
                f"{self.series_name} S{self.season}E{self.episode} {self.extenstion}"
            )
            os.rename(file, self.new_file_name)

        # Result
        self.result_label = Label(
            self.window,
            text="Successful",
            font=self.font_name_size,
            bg=self.secondary_background_color,
            fg=self.foreground_color,
        )
        self.result_label.place(x=200, y=145)

    # Check_Season/Episode_No.
    @staticmethod
    def fetch_season_episode(file_name, regex):
        try:
            sea_epi_num = int(re.search(regex, file_name).group(1))
            return f"0{sea_epi_num}" if sea_epi_num < 10 else sea_epi_num
        except:
            print("Filename not found in Regex")
            return None


if __name__ == "__main__":
    window = Tk()
    app = window_UI(window)
    app.setupUi()
