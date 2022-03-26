
from tkinter import *
from Request import RequestCurrency
from UsingRequestData import reorder_country_dictionary, calculate_exchange_rate


class MainWindow:

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Currency - Change Calculator")
    
        self.request_class = RequestCurrency() 
        self.raw_request = self.request_class.get_country_data()
                
        self.country_dict = reorder_country_dictionary(request_result= self.raw_request)
        

        self.country_dropdown_liste = []

        for key in self.country_dict.keys():
            self.country_dropdown_liste.append(key)

        self.country_dropdown_liste.sort()

        
        self.dropdown_var_1 = StringVar()
        self.dropdown_var_1.set(self.country_dropdown_liste[65])

        self.dropdown_var_2 = StringVar()
        self.dropdown_var_2.set(self.country_dropdown_liste[148])

        FRAME_STYLE = {"bg":"black"}
        LABEL_STYLE = {"bg": "black", "fg": "white", "text":"Currency exchange rates calculation".upper(), "font":("Calibri", 15, "bold")}
        BUTTON_WIDTH = 20
        BUTTON_HEIGTH = 2
        BUTTON_STYLE = {"width": BUTTON_WIDTH, "height": BUTTON_HEIGTH, "relief": GROOVE, "borderwidth": 1, "bg":"lightgrey", "font": ("Calibri", 12, "bold")}

        #Information header
        self.information_frame = self.create_frame_widget(**FRAME_STYLE)
        self.information_frame.pack(fill=BOTH)

        #Dropdown frame
        self.dropdown_frame = self.create_frame_widget(**FRAME_STYLE)
        self.dropdown_frame.pack(fill=BOTH, expand=TRUE)

        #Button Frame
        self.button_frame = self.create_frame_widget(**FRAME_STYLE)
        self.button_frame.pack(fill=BOTH)

        #Result Frame
        self.result_frame = self.create_frame_widget(**FRAME_STYLE)
        self.result_frame.pack(fill=BOTH)

        #Labels
        self.label_widget_1 = self.create_label_widget(master= self.information_frame, **LABEL_STYLE)
        self.label_widget_1.pack(fill=BOTH)

        #Dropdowns
        self.dropdown_currency_1 = OptionMenu(self.dropdown_frame, self.dropdown_var_1,self.country_dropdown_liste[0], *self.country_dropdown_liste, command= lambda: self.update_button_widget())
        self.dropdown_currency_1.grid(row= 1, column=0, sticky="NSWE")

        self.dropdown_currency_2 = OptionMenu(self.dropdown_frame, self.dropdown_var_2, self.country_dropdown_liste[55], *self.country_dropdown_liste, command= lambda: self.update_button_widget())
        self.dropdown_currency_2.grid(row= 1, column=2, sticky="NSWE")

        #Buttons
        self.calculate_button = self.create_button_widget(master= self.button_frame, text="Get exchange rates".upper(), **BUTTON_STYLE)
        self.calculate_button.pack(fill=X)
        self.calculate_button.config(command= lambda: self.get_result())

        self.quit_button = self.create_button_widget(master= self.button_frame, text="Quit Application".upper(), command=quit, **BUTTON_STYLE)
        self.quit_button.pack(fill=X)

        #Textbox
        self.result_textbox_1 = Text(self.dropdown_frame, bg="lightgrey", font=("Calibri", 17, "bold"), height=3, width=25, relief=GROOVE, borderwidth=3)
        self.result_textbox_1.tag_configure("tag_name", justify='center')
        self.result_textbox_1.grid(row=1, column=1)
        

    def create_frame_widget(self, **kwargs) -> None:
        return Frame(master= self.root, **kwargs)

    
    def create_label_widget(self, **kwargs) -> None:
        return Label(**kwargs)


    def create_button_widget(self, **kwargs) -> None:
        return Button(**kwargs,)


    def update_button_widget(self) -> None:
        """Updates the button widget to get new information out of the drop down menu."""

        calculate_exchange_rate(self.request_class, self.country_dict[self.dropdown_var_1.get()]["currencyId"], self.country_dict[self.dropdown_var_2.get()]["currencyId"])


    def clear_exchange_rate_textbox(self) -> None:
        """Clears the result text widget when clicking the calculation button to delete old information."""

        self.result_textbox_1.delete("0.0", END)


    def get_result(self) -> None:
        """Put out the information of the exchange rate"""

        try:
            self.clear_exchange_rate_textbox()
        
        finally:
            exchange_rate = calculate_exchange_rate(class_widget= self.request_class, currency_1= self.country_dict[self.dropdown_var_1.get()]["currencyId"], currency_2= self.country_dict[self.dropdown_var_2.get()]["currencyId"])
            self.show_result(exchange_rate= exchange_rate)
            self.colorize_textbox(exchange_rate= exchange_rate)


    def show_result(self, exchange_rate: list) -> None:
        """Shows the results, puts out the information into the result textbox"""

        result_text = f'1 {self.country_dict[self.dropdown_var_1.get()]["currencyId"]} = {exchange_rate[0]:2.4f} {self.country_dict[self.dropdown_var_2.get()]["currencyId"]}'
        
        self.result_textbox_1.insert("1.0", f'\n{result_text}')
        self.result_textbox_1.tag_add("tag_name", "1.0", END)
        

    def colorize_textbox(self, exchange_rate: list) -> None:
        """Colorizes the result textbox depending on the exchange rate. Base is the leftish currency."""

        if float(exchange_rate[0]) >= 1:
            self.result_textbox_1.config(bg="#36ff68")
        
        else:
            self.result_textbox_1.config(bg="#ed3434")
            

    def main(self) -> None:
        self.root.mainloop()