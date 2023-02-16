import tkinter as tk
from src.settings.Settings import *
from src.request_refactor.refactor_request_data import refactor_response, calculate_exchange_rate
from src.url_request.Request import RequestCurrency


class MainWindow(tk.Tk):

    """
    Base Window class, inheriting from tkinter tk root window. Used to display all the information
    about the currency exchange.
    """
    def __init__(self) -> None:
        super().__init__()

        self.request_class = RequestCurrency()
        self.raw_request = self.request_class.get_country_currency_data()

        self.country_dict = refactor_response(request_result=self.raw_request)
        self.country_dropdown_list = []

        if not self.country_dict:
            raise ValueError("Missing country values. API can not connect.")

        for key in self.country_dict.keys():
            # creates the country
            self.country_dropdown_list.append(key)

        self.country_dropdown_list.sort()

        self.dropdown_var_1 = tk.StringVar()
        self.dropdown_var_1.set(self.country_dropdown_list[65])  # defines country 65 as start value

        self.dropdown_var_2 = tk.StringVar()
        self.dropdown_var_2.set(self.country_dropdown_list[148])  # defines country 148 as start value

        # Information header
        self.information_frame = tk.Frame(master=self,
                                          **FRAME_STYLE)
        self.information_frame.pack(fill=tk.BOTH)

        # Dropdown frame
        self.dropdown_frame = tk.Frame(master=self,
                                       **FRAME_STYLE)
        self.dropdown_frame.pack(fill=tk.BOTH, expand=tk.TRUE)

        # Button Frame
        self.button_frame = tk.Frame(master=self,
                                     **FRAME_STYLE)
        self.button_frame.pack(fill=tk.BOTH)

        # Result Frame
        self.result_frame = tk.Frame(master=self,
                                     **FRAME_STYLE)
        self.result_frame.pack(fill=tk.BOTH)

        # Labels
        self.label_widget_1 = tk.Label(master=self.information_frame,
                                       **LABEL_STYLE)
        self.label_widget_1.pack(fill=tk.BOTH)

        # Dropdowns
        self.dropdown_currency_1 = tk.OptionMenu(self.dropdown_frame,
                                                 self.dropdown_var_1,
                                                 self.country_dropdown_list[0],
                                                 *self.country_dropdown_list,
                                                 command=lambda: self.update_button_widget())
        self.dropdown_currency_1.grid(row=1, column=0, sticky="NSWE")

        self.dropdown_currency_2 = tk.OptionMenu(self.dropdown_frame,
                                                 self.dropdown_var_2,
                                                 self.country_dropdown_list[55],
                                                 *self.country_dropdown_list,
                                                 command=lambda: self.update_button_widget())
        self.dropdown_currency_2.grid(row=1, column=2, sticky="NSWE")

        # Buttons
        self.calculate_button = tk.Button(master=self.button_frame,
                                          text="Get exchange rates".upper(),
                                          **BUTTON_STYLE)

        self.calculate_button.pack(fill=tk.X)
        self.calculate_button.config(command=lambda: self.get_result())

        self.quit_button = tk.Button(master=self.button_frame,
                                     text="Quit Application".upper(),
                                     command=quit,
                                     **BUTTON_STYLE)
        self.quit_button.pack(fill=tk.X)

        # Textbox
        self.result_textbox_1 = tk.Text(master=self.dropdown_frame,
                                        bg="lightgrey",
                                        font=("Calibri", 17, "bold"),
                                        height=3,
                                        width=25,
                                        relief=tk.GROOVE,
                                        borderwidth=3)
        self.result_textbox_1.tag_configure("tag_name", justify='center')
        self.result_textbox_1.grid(row=1, column=1)

    def update_button_widget(self) -> None:

        """
        Updates the button widget to get new information out of the drop down menu.
        """

        calculate_exchange_rate(self.request_class,
                                self.country_dict[self.dropdown_var_1.get()]["currencyId"],
                                self.country_dict[self.dropdown_var_2.get()]["currencyId"])

    def clear_exchange_rate_textbox(self) -> None:

        """
        Clears the result text widget when clicking the calculation button to delete old information.
        """

        self.result_textbox_1.delete("0.0", tk.END)

    def get_result(self) -> None:

        """
        Put out the information of the exchange rate
        """

        try:
            self.clear_exchange_rate_textbox()

        finally:
            exchange_rate = calculate_exchange_rate(class_widget=self.request_class,
                                                    currency_1=self.country_dict[self.dropdown_var_1.get()][
                                                        "currencyId"],
                                                    currency_2=self.country_dict[self.dropdown_var_2.get()][
                                                        "currencyId"])
            self.show_result(exchange_rate=exchange_rate)
            self.colorize_textbox(exchange_rate=exchange_rate)

    def show_result(self, exchange_rate: list) -> None:

        """
        Shows the results, puts out the information into the result textbox
        """

        result_text = f'1 {self.country_dict[self.dropdown_var_1.get()]["currencyId"]} = {exchange_rate[0]:2.4f} {self.country_dict[self.dropdown_var_2.get()]["currencyId"]}'

        self.result_textbox_1.insert("1.0", f'\n{result_text}')
        self.result_textbox_1.tag_add("tag_name", "1.0", tk.END)

    def colorize_textbox(self, exchange_rate: list) -> None:

        """
        Colorizes the result textbox depending on the exchange rate. Base is the leftish currency.
        """

        if float(exchange_rate[0]) >= 1:
            self.result_textbox_1.config(bg="#36ff68")

        else:
            self.result_textbox_1.config(bg="#ed3434")
