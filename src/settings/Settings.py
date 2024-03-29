FRAME_STYLE = {"bg": "black"}
LABEL_STYLE = {"bg": "black",
               "fg": "white",
               "text": "Currency exchange rates calculation".upper(),
               "font": ("Calibri", 15, "bold")}
BUTTON_WIDTH = 20
BUTTON_HEIGTH = 2
BUTTON_STYLE = {"width": BUTTON_WIDTH,
                "height": BUTTON_HEIGTH,
                "relief": "groove",
                "borderwidth": 1,
                "bg": "lightgrey",
                "font": ("Calibri", 12, "bold")}

BASE_URL = f"https://free.currconv.com/api/v7/"

# read file containing the api key.
FILENAME = "secret.txt"
with open(FILENAME, "r") as file:
    API_KEY = file.readline()
