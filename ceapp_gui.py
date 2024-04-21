"""
CEApp - Cash Exchange Application - GUI

2024

"""

from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image
from ceapp_engine import *
import time
import webbrowser


class SetApp(customtkinter.CTk):

    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")

    def __init__(self, title, app_x, app_y):
        super().__init__()

        # Basic window setup
        self.title(title)

        screen_x = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x_position = (screen_x / 2) - (int(app_x) / 2)
        y_position = (screen_y / 2) - (int(app_y) / 2)
        self.geometry(f'{app_x}x{app_y}+{x_position}+{y_position}')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Image Loading System - Navigation Frame
        nav_logo = customtkinter.CTkImage(Image.open(
            'images/CEApp_logo.png'), size=(100, 100))
        home_button_logo = customtkinter.CTkImage(
            Image.open('images/home.png'), size=(90, 90))
        exchange_button_logo = customtkinter.CTkImage(
            Image.open('images/search.png'), size=(80, 80))
        converter_button_logo = customtkinter.CTkImage(
            Image.open('images/exchange.png'), size=(80, 80))
        author_button_logo = customtkinter.CTkImage(
            Image.open('images/author.png'), size=(80, 80))
        exit_button_logo = customtkinter.CTkImage(
            Image.open('images/exit.png'), size=(80, 80))
        home_ceapp = customtkinter.CTkImage(Image.open(
            'images/CEApp_logo_full.png'), size=(500, 100))
        usa_flag = customtkinter.CTkImage(Image.open(
            'images/usd.png'), size=(50, 35))
        eur_flag = customtkinter.CTkImage(Image.open(
            'images/eur.png'), size=(50, 35))
        chf_flag = customtkinter.CTkImage(Image.open(
            'images/chf.png'), size=(50, 35))
        gbp_flag = customtkinter.CTkImage(Image.open(
            'images/gbp.png'), size=(50, 35))
        uah_flag = customtkinter.CTkImage(Image.open(
            'images/uah.png'), size=(50, 35))
        czk_flag = customtkinter.CTkImage(Image.open(
            'images/czk.png'), size=(50, 35))
        dkk_flag = customtkinter.CTkImage(Image.open(
            'images/dkk.png'), size=(50, 35))
        sek_flag = customtkinter.CTkImage(Image.open(
            'images/sek.png'), size=(50, 35))
        bgn_flag = customtkinter.CTkImage(Image.open(
            'images/bgn.png'), size=(50, 35))
        ron_flag = customtkinter.CTkImage(Image.open(
            'images/ron.png'), size=(50, 35))
        ils_flag = customtkinter.CTkImage(Image.open(
            'images/ils.png'), size=(50, 35))
        brl_flag = customtkinter.CTkImage(Image.open(
            'images/brl.png'), size=(50, 35))
        nor_flag = customtkinter.CTkImage(Image.open(
            'images/nor.png'), size=(50, 35))
        mex_flag = customtkinter.CTkImage(Image.open(
            'images/mex.png'), size=(50, 35))
        sgd_flag = customtkinter.CTkImage(Image.open(
            'images/sgd.png'), size=(50, 35))
        cny_flag = customtkinter.CTkImage(Image.open(
            'images/cny.png'), size=(50, 35))
        hkd_flag = customtkinter.CTkImage(Image.open(
            'images/hkd.png'), size=(50, 35))
        aud_flag = customtkinter.CTkImage(Image.open(
            'images/aud.png'), size=(50, 35))
        thb_flag = customtkinter.CTkImage(Image.open(
            'images/thb.png'), size=(50, 35))
        mod_a = customtkinter.CTkImage(Image.open(
            'images/A.png'), size=(150, 100))
        converter_title = customtkinter.CTkImage(Image.open(
            'images/converter_title.png'), size=(300, 100))
        history_search_title = customtkinter.CTkImage(Image.open(
            'images/historic_title.png'), size=(300, 100))
        gold_converter_title = customtkinter.CTkImage(Image.open(
            'images/gold_title.png'), size=(300, 100))
        author_converter_title = customtkinter.CTkImage(Image.open(
            'images/author_logo.png'), size=(500, 100))
        clock_main_title = customtkinter.CTkImage(Image.open(
            'images/clock.png'), size=(100, 100))
        nbp_main_title = customtkinter.CTkImage(Image.open(
            'images/nbp.png'), size=(100, 100))

        # Navigation Menu Frame
        self.navigation_menu = customtkinter.CTkFrame(self)
        self.navigation_menu.grid(row=0, column=0, sticky="nsew")
        navigation_logo_menu = CTkLabel(
            self.navigation_menu,
            text=' Menu',
            text_color=(
                '#000000'),
            font=(
                'Unispace',
                30,
                'bold'),
            compound='left',
            image=nav_logo,
            pady=30)
        navigation_logo_menu.grid(row=0, column=0)

        self.home_button = customtkinter.CTkButton(
            self.navigation_menu,
            text='Home',
            font=(
                'Unispace',
                30),
            fg_color='transparent',
            border_spacing=10,
            width=380,
            height=40,
            text_color=(
                '#000000'),
            hover_color=(
                "gray70",
                "gray30"),
            anchor='w',
            image=home_button_logo,
            command=self.home_event)
        self.home_button.grid(row=1, column=0)

        self.exchange_button = customtkinter.CTkButton(
            self.navigation_menu,
            text='Exchange Values',
            font=(
                'Unispace',
                30),
            fg_color='transparent',
            border_spacing=10,
            width=340,
            height=40,
            text_color=(
                '#000000'),
            hover_color=(
                "gray70",
                "gray30"),
            anchor='w',
            image=exchange_button_logo,
            command=self.exchange_event)
        self.exchange_button.grid(row=2, column=0)

        self.converter_button = customtkinter.CTkButton(
            self.navigation_menu,
            text='Converter',
            font=(
                'Unispace',
                30),
            fg_color='transparent',
            border_spacing=10,
            width=380,
            height=40,
            text_color=(
                '#000000'),
            hover_color=(
                "gray70",
                "gray30"),
            anchor='w',
            image=converter_button_logo,
            command=self.converter_event)
        self.converter_button.grid(row=3, column=0)

        self.author_button = customtkinter.CTkButton(
            self.navigation_menu,
            text='Credits',
            font=(
                'Unispace',
                30),
            fg_color='transparent',
            border_spacing=10,
            width=380,
            height=40,
            text_color=(
                '#000000'),
            hover_color=(
                "gray70",
                "gray30"),
            anchor='w',
            image=author_button_logo,
            command=self.author_event)
        self.author_button.grid(row=4, column=0)

        self.exit_button = customtkinter.CTkButton(
            self.navigation_menu,
            text='Exit',
            font=(
                'Unispace',
                30),
            fg_color='transparent',
            border_spacing=10,
            width=380,
            height=40,
            text_color=(
                '#000000'),
            hover_color=(
                "gray70",
                "gray30"),
            anchor='w',
            image=exit_button_logo,
            compound='left',
            command=self.exit_event)
        self.exit_button.grid(row=5, column=0)

        self.apperance_chooser = customtkinter.CTkOptionMenu(
            self.navigation_menu,
            values=[
                'dark',
                'light',
                'system'],
            font=(
                'Unispace',
                15),
            fg_color='#3158a6',
            command=self.appearance_changer,
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)
        self.apperance_chooser.grid(row=6, column=0, sticky='s')

        # Home Frame
        def nbp_web():
            nbp = webbrowser.open(
                'https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/', new=2)
            return nbp

        def gold_web():
            gold = webbrowser.open(
                'https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/cena-zlota/', new=2)
            return gold
        self.home = customtkinter.CTkFrame(self, fg_color='transparent')
        self.home.grid_rowconfigure(0, weight=4)
        self.home.grid_rowconfigure(1, weight=3)
        self.home.grid_rowconfigure(2, weight=2)
        
        home_row_0_label = customtkinter.CTkLabel(
            self.home, text='', image=home_ceapp, compound="top")
        publication_logo_row_1_label = customtkinter.CTkLabel(
            self.home, text='', pady=50, image=clock_main_title)
        publication_data = APIDataCalls.complex_calls('usd')
        publication_data_text = publication_data['rates'][0]['effectiveDate']
        publication_row_1_label = customtkinter.CTkLabel(
            self.home, text=f'Publication Date:\n{publication_data_text}', font=(
                'Unispace', 20), pady=40, text_color=(
                '#3158a6'))
        disclaimer_row2_label = customtkinter.CTkLabel(
            self.home, text=f'Exchange values data colected from \n'
                            f'National Bank of Poland (Narodowy Bank Polski) \n'
                            f'Sources:', font=(
                'Unispace', 12), pady=50, text_color=(
                '#3158a6'))
        nbp_logo_row3_label = customtkinter.CTkLabel(
            self.home, text='', pady=50, image=nbp_main_title)
        nbp_button_row3 = customtkinter.CTkButton(self.home, fg_color='#3158a6',
            corner_radius=100,
            width=50,
            height=30,
            text='https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/',
            font=(
                'Unispace',
                10),
            command=nbp_web)

        gold_button_row3 = customtkinter.CTkButton(self.home, fg_color='#3158a6',
                                                  corner_radius=100,
                                                  width=50,
                                                  height=30,
                                                  text='https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/cena-zlota/',
                                                  font=(
                                                      'Unispace',
                                                      10),
                                                  command=gold_web)

        home_row_0_label.grid(row=0, column=1)
        publication_logo_row_1_label.grid(row=1, column=0)
        publication_row_1_label.grid(row=1, column=1)
        disclaimer_row2_label.grid(row=2, column=1)
        nbp_logo_row3_label.grid(row=2, column=0)
        nbp_button_row3.grid(row=3, column=1, pady=10)
        gold_button_row3.grid(row=4, column=1, pady=10)




        # Exchange Frame
        self.exchangeframe = customtkinter.CTkFrame(
            self, fg_color='transparent')
        self.row0 = customtkinter.CTkLabel(
            self.exchangeframe,
            text='Pick Your\ncurrency:',
            font=(
                'Unispace',
                15),
            text_color='#000000')

        currencies = [
            'PLN',
            'USD',
            'EUR',
            'CHF',
            'GBP',
            'UAH',
            'CZK',
            'DKK',
            'SEK',
            'BGN',
            'RON',
            'ILS',
            'BRL',
            'NOK',
            'MXN',
            'SGD',
            'CNY',
            'HKD',
            'AUD',
            'THB'
        ]

        self.row0_chosen_input = StringVar()
        self.row0_chooser = customtkinter.CTkOptionMenu(
            self.exchangeframe,
            fg_color='#3158a6',
            variable=self.row0_chosen_input,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)

        self.row0_button = customtkinter.CTkButton(
            self.exchangeframe,
            fg_color='#3158a6',
            corner_radius=100,
            width=50,
            height=30,
            text='Refresh',
            font=(
                'Unispace',
                15),
            command=self.refresh
            )

        self.row1_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=usa_flag)
        self.row1_data = APIDataCalls.complex_calls('usd')
        self.row1_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='U.S Dollar', font=(
                'Unispace', 20), text_color='#000000')
        self.row1_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row1_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row1_value = StringVar()
        self.row1_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row1_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row1_currency = StringVar()
        self.row1_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row1_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row2_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=eur_flag)
        self.row2_data = APIDataCalls.complex_calls('eur')
        self.row2_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Euro', font=(
                'Unispace', 20), text_color='#000000')
        self.row2_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row2_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row2_value = StringVar()
        self.row2_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row2_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row2_currency = StringVar()
        self.row2_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row2_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row3_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=chf_flag)
        self.row3_data = APIDataCalls.complex_calls('chf')
        self.row3_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Swiss franc', font=(
                'Unispace', 20), text_color='#000000')
        self.row3_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row3_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row3_value = StringVar()
        self.row3_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row3_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row3_currency = StringVar()
        self.row3_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row3_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row4_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=gbp_flag)
        self.row4_data = APIDataCalls.complex_calls('gbp')
        self.row4_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Pound sterling', font=(
                'Unispace', 20), text_color='#000000')
        self.row4_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row4_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row4_value = StringVar()
        self.row4_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row4_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row4_currency = StringVar()
        self.row4_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row4_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row5_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=uah_flag)
        self.row5_data = APIDataCalls.complex_calls('uah')
        self.row5_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Hryvnia', font=(
                'Unispace', 20), text_color='#000000')
        self.row5_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row5_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row5_value = StringVar()
        self.row5_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row5_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row5_currency = StringVar()
        self.row5_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row5_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row6_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=czk_flag)
        self.row6_data = APIDataCalls.complex_calls('czk')
        self.row6_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Czech koruna', font=(
                'Unispace', 20), text_color='#000000')
        self.row6_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row6_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row6_value = StringVar()
        self.row6_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row6_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row6_currency = StringVar()
        self.row6_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row6_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row7_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=dkk_flag)
        self.row7_data = APIDataCalls.complex_calls('dkk')
        self.row7_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Danish krona', font=(
                'Unispace', 20), text_color='#000000')
        self.row7_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row7_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row7_value = StringVar()
        self.row7_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row7_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row7_currency = StringVar()
        self.row7_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row7_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row8_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=sek_flag)
        self.row8_data = APIDataCalls.complex_calls('sek')
        self.row8_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Swedish krona', font=(
                'Unispace', 20), text_color='#000000')
        self.row8_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row8_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row8_value = StringVar()
        self.row8_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row8_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row8_currency = StringVar()
        self.row8_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row8_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row9_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=bgn_flag)
        self.row9_data = APIDataCalls.complex_calls('bgn')
        self.row9_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Lev', font=(
                'Unispace', 20), text_color='#000000')
        self.row9_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row9_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row9_value = StringVar()
        self.row9_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row9_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row9_currency = StringVar()
        self.row9_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row9_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row10_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=ron_flag)
        self.row10_data = APIDataCalls.complex_calls('ron')
        self.row10_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Romanian leu', font=(
                'Unispace', 20), text_color='#000000')
        self.row10_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row10_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row10_value = StringVar()
        self.row10_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row10_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row10_currency = StringVar()
        self.row10_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row10_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row11_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=ils_flag)
        self.row11_data = APIDataCalls.complex_calls('ils')
        self.row11_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='New shekel', font=(
                'Unispace', 20), text_color='#000000')
        self.row11_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row11_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row11_value = StringVar()
        self.row11_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row11_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row11_currency = StringVar()
        self.row11_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row11_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row12_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=brl_flag)
        self.row12_data = APIDataCalls.complex_calls('brl')
        self.row12_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Real', font=(
                'Unispace', 20), text_color='#000000')
        self.row12_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row12_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row12_value = StringVar()
        self.row12_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row12_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row12_currency = StringVar()
        self.row12_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row12_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row13_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=nor_flag)
        self.row13_data = APIDataCalls.complex_calls('nok')
        self.row13_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Norwegian krona', font=(
                'Unispace', 20), text_color='#000000')
        self.row13_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row13_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row13_value = StringVar()
        self.row13_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row13_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row13_currency = StringVar()
        self.row13_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row13_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row14_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=mex_flag)
        self.row14_data = APIDataCalls.complex_calls('mxn')
        self.row14_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Mexican peso', font=(
                'Unispace', 20), text_color='#000000')
        self.row14_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row14_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row14_value = StringVar()
        self.row14_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row14_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row14_currency = StringVar()
        self.row14_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row14_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row15_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=sgd_flag)
        self.row15_data = APIDataCalls.complex_calls('sgd')
        self.row15_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Singapore Dollar', font=(
                'Unispace', 20), text_color='#000000')
        self.row15_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row15_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row15_value = StringVar()
        self.row15_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row15_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row15_currency = StringVar()
        self.row15_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row15_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row16_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=cny_flag)
        self.row16_data = APIDataCalls.complex_calls('cny')
        self.row16_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Renminbi (Yuan)', font=(
                'Unispace', 20), text_color='#000000')
        self.row16_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row16_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row16_value = StringVar()
        self.row16_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row16_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row16_currency = StringVar()
        self.row16_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row16_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row17_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=hkd_flag)
        self.row17_data = APIDataCalls.complex_calls('hkd')
        self.row17_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Hongkong Dollar', font=(
                'Unispace', 20), text_color='#000000')
        self.row17_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row17_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row17_value = StringVar()
        self.row17_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row17_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row17_currency = StringVar()
        self.row17_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row17_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row18_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=aud_flag)
        self.row18_data = APIDataCalls.complex_calls('aud')
        self.row18_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Australian Dollar', font=(
                'Unispace', 20), text_color='#000000')
        self.row18_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row18_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row18_value = StringVar()
        self.row18_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row18_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row18_currency = StringVar()
        self.row18_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row18_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row19_flag = customtkinter.CTkLabel(
            self.exchangeframe, text='', image=thb_flag)
        self.row19_data = APIDataCalls.complex_calls('thb')
        self.row19_curency_title = customtkinter.CTkLabel(
            self.exchangeframe, text='Thai Bhat', font=(
                'Unispace', 20), text_color='#000000')
        self.row19_currency_code = customtkinter.CTkLabel(
            self.exchangeframe, text=self.row19_data['code'], font=(
                'Unispace', 20), text_color='#000000')
        self.row19_value = StringVar()
        self.row19_currency_value = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row19_value, font=(
                'OCR A Extended', 20), text_color='#e80c0c')
        self.row19_currency = StringVar()
        self.row19_currency_end = customtkinter.CTkLabel(
            self.exchangeframe, textvariable=self.row19_currency, font=(
                'Unispace', 20), text_color='#3158a6')

        self.row0.grid(row=0, column=0, padx=40, pady=20)
        self.row0_chooser.grid(row=0, column=1, padx=40, pady=20)
        self.row0_button.grid(row=0, column=2, padx=10, pady=20)

        self.row1_flag.grid(row=1, column=0, padx=30, pady=5)
        self.row1_curency_title.grid(row=1, column=1, padx=30, pady=5)
        self.row1_currency_code.grid(row=1, column=2, padx=30, pady=5)
        self.row1_currency_value.grid(row=1, column=3, pady=5)
        self.row1_currency_end.grid(row=1, column=4, padx=30, pady=5)

        self.row2_flag.grid(row=2, column=0, padx=30, pady=5)
        self.row2_curency_title.grid(row=2, column=1, padx=30, pady=5)
        self.row2_currency_code.grid(row=2, column=2, padx=30, pady=5)
        self.row2_currency_value.grid(row=2, column=3, pady=5)
        self.row2_currency_end.grid(row=2, column=4, padx=30, pady=5)

        self.row3_flag.grid(row=3, column=0, padx=30, pady=5)
        self.row3_curency_title.grid(row=3, column=1, padx=30, pady=5)
        self.row3_currency_code.grid(row=3, column=2, padx=30, pady=5)
        self.row3_currency_value.grid(row=3, column=3, pady=5)
        self.row3_currency_end.grid(row=3, column=4, padx=30, pady=5)

        self.row4_flag.grid(row=4, column=0, padx=30, pady=5)
        self.row4_curency_title.grid(row=4, column=1, padx=30, pady=5)
        self.row4_currency_code.grid(row=4, column=2, padx=30, pady=5)
        self.row4_currency_value.grid(row=4, column=3, pady=5)
        self.row4_currency_end.grid(row=4, column=4, padx=30, pady=5)

        self.row5_flag.grid(row=5, column=0, padx=30, pady=5)
        self.row5_curency_title.grid(row=5, column=1, padx=30, pady=5)
        self.row5_currency_code.grid(row=5, column=2, padx=30, pady=5)
        self.row5_currency_value.grid(row=5, column=3, pady=5)
        self.row5_currency_end.grid(row=5, column=4, padx=30, pady=5)

        self.row6_flag.grid(row=6, column=0, padx=30, pady=5)
        self.row6_curency_title.grid(row=6, column=1, padx=30, pady=5)
        self.row6_currency_code.grid(row=6, column=2, padx=30, pady=5)
        self.row6_currency_value.grid(row=6, column=3, pady=5)
        self.row6_currency_end.grid(row=6, column=4, padx=30, pady=5)

        self.row7_flag.grid(row=7, column=0, padx=30, pady=5)
        self.row7_curency_title.grid(row=7, column=1, padx=30, pady=5)
        self.row7_currency_code.grid(row=7, column=2, padx=30, pady=5)
        self.row7_currency_value.grid(row=7, column=3, pady=5)
        self.row7_currency_end.grid(row=7, column=4, padx=30, pady=5)

        self.row8_flag.grid(row=8, column=0, padx=30, pady=5)
        self.row8_curency_title.grid(row=8, column=1, padx=30, pady=5)
        self.row8_currency_code.grid(row=8, column=2, padx=30, pady=5)
        self.row8_currency_value.grid(row=8, column=3, pady=5)
        self.row8_currency_end.grid(row=8, column=4, padx=30, pady=5)

        self.row9_flag.grid(row=9, column=0, padx=30, pady=5)
        self.row9_curency_title.grid(row=9, column=1, padx=30, pady=5)
        self.row9_currency_code.grid(row=9, column=2, padx=30, pady=5)
        self.row9_currency_value.grid(row=9, column=3, pady=5)
        self.row9_currency_end.grid(row=9, column=4, padx=30, pady=5)

        self.row10_flag.grid(row=10, column=0, padx=30, pady=5)
        self.row10_curency_title.grid(row=10, column=1, padx=30, pady=5)
        self.row10_currency_code.grid(row=10, column=2, padx=30, pady=5)
        self.row10_currency_value.grid(row=10, column=3, pady=5)
        self.row10_currency_end.grid(row=10, column=4, padx=30, pady=5)

        self.row11_flag.grid(row=11, column=0, padx=30, pady=5)
        self.row11_curency_title.grid(row=11, column=1, padx=30, pady=5)
        self.row11_currency_code.grid(row=11, column=2, padx=30, pady=5)
        self.row11_currency_value.grid(row=11, column=3, pady=5)
        self.row11_currency_end.grid(row=11, column=4, padx=30, pady=5)

        self.row12_flag.grid(row=12, column=0, padx=30, pady=5)
        self.row12_curency_title.grid(row=12, column=1, padx=30, pady=5)
        self.row12_currency_code.grid(row=12, column=2, padx=30, pady=5)
        self.row12_currency_value.grid(row=12, column=3, pady=5)
        self.row12_currency_end.grid(row=12, column=4, padx=30, pady=5)

        self.row13_flag.grid(row=13, column=0, padx=30, pady=5)
        self.row13_curency_title.grid(row=13, column=1, padx=30, pady=5)
        self.row13_currency_code.grid(row=13, column=2, padx=30, pady=5)
        self.row13_currency_value.grid(row=13, column=3, pady=5)
        self.row13_currency_end.grid(row=13, column=4, padx=30, pady=5)

        self.row14_flag.grid(row=14, column=0, padx=30, pady=5)
        self.row14_curency_title.grid(row=14, column=1, padx=30, pady=5)
        self.row14_currency_code.grid(row=14, column=2, padx=30, pady=5)
        self.row14_currency_value.grid(row=14, column=3, pady=5)
        self.row14_currency_end.grid(row=14, column=4, padx=30, pady=5)

        self.row15_flag.grid(row=15, column=0, padx=30, pady=5)
        self.row15_curency_title.grid(row=15, column=1, padx=30, pady=5)
        self.row15_currency_code.grid(row=15, column=2, padx=30, pady=5)
        self.row15_currency_value.grid(row=15, column=3, pady=5)
        self.row15_currency_end.grid(row=15, column=4, padx=30, pady=5)

        self.row16_flag.grid(row=16, column=0, padx=30, pady=5)
        self.row16_curency_title.grid(row=16, column=1, padx=30, pady=5)
        self.row16_currency_code.grid(row=16, column=2, padx=30, pady=5)
        self.row16_currency_value.grid(row=16, column=3, pady=5)
        self.row16_currency_end.grid(row=16, column=4, padx=30, pady=5)

        self.row17_flag.grid(row=17, column=0, padx=30, pady=5)
        self.row17_curency_title.grid(row=17, column=1, padx=30, pady=5)
        self.row17_currency_code.grid(row=17, column=2, padx=30, pady=5)
        self.row17_currency_value.grid(row=17, column=3, pady=5)
        self.row17_currency_end.grid(row=17, column=4, padx=30, pady=5)

        self.row18_flag.grid(row=18, column=0, padx=30, pady=5)
        self.row18_curency_title.grid(row=18, column=1, padx=30, pady=5)
        self.row18_currency_code.grid(row=18, column=2, padx=30, pady=5)
        self.row18_currency_value.grid(row=18, column=3, pady=5)
        self.row18_currency_end.grid(row=18, column=4, padx=30, pady=5)

        self.row19_flag.grid(row=19, column=0, padx=30, pady=5)
        self.row19_curency_title.grid(row=19, column=1, padx=30, pady=5)
        self.row19_currency_code.grid(row=19, column=2, padx=30, pady=5)
        self.row19_currency_value.grid(row=19, column=3, pady=5)
        self.row19_currency_end.grid(row=19, column=4, padx=30, pady=5)

        # Converter Frame
        self.converter = customtkinter.CTkFrame(self, fg_color='transparent')
        self.converter.configure(width=700, height=760)
        self.converter.grid_columnconfigure(0, weight=1)
        self.converter.grid_columnconfigure(1, weight=3)
        self.converter.grid_columnconfigure(2, weight=2)

        self.mod_a_label = customtkinter.CTkLabel(
            self.converter, text='', image=mod_a)
        self.converter_title_label = customtkinter.CTkLabel(
            self.converter, text='', image=converter_title)

        self.amount_label = customtkinter.CTkLabel(
            self.converter, text='Amount: ', font=(
                'Unispace', 15), text_color='black')
        self.amount_entry = customtkinter.CTkEntry(
            self.converter, width=150, height=20, font=('Unispace', 15))
        self.input_label = customtkinter.CTkLabel(
            self.converter, text='Input Currency: ', font=(
                'Unispace', 15), text_color='black')

        currencies = [
            'PLN',
            'USD',
            'EUR',
            'CHF',
            'GBP',
            'UAH',
            'CZK',
            'DKK',
            'SEK',
            'BGN',
            'RON',
            'ILS',
            'BRL',
            'NOK',
            'MXN',
            'SGD',
            'CNY',
            'HKD',
            'AUD',
            'THB'
        ]

        self.chosen_input = StringVar(self)
        self.input_chooser = customtkinter.CTkOptionMenu(
            self.converter,
            fg_color='#3158a6',
            variable=self.chosen_input,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)

        self.output_label = customtkinter.CTkLabel(
            self.converter, text='Output Currency: ', font=(
                'Unispace', 15), text_color='black')
        self.chosen_output = StringVar(self)
        self.output_chooser = customtkinter.CTkOptionMenu(
            self.converter,
            fg_color='#3158a6',
            variable=self.chosen_output,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)

        self.txt_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Save to TXT',
            font=(
                'Unispace',
                15),
            command=self.calculation_txt_generator)

        self.calculated_label = customtkinter.CTkLabel(
            self.converter, text='Calculated Amount: ', font=(
                'Unispace', 15), text_color='black')
        self.calculated_result = StringVar()
        self.calculated_result_label = customtkinter.CTkLabel(
            self.converter, textvariable=self.calculated_result, font=(
                'Unispace', 15), text_color='black')
        self.calculate_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Calculate!',
            font=(
                'Unispace',
                15),
            command=self.gui_calculation)

        self.history_title_label = customtkinter.CTkLabel(
            self.converter, text='', image=history_search_title)
        self.date_label = customtkinter.CTkLabel(
            self.converter,
            text='Date \n[yyyy-mm-dd]: ',
            font=(
                'Unispace',
                15),
            text_color='black')
        self.date_entry = customtkinter.CTkEntry(
            self.converter, width=150, height=20, font=('Unispace', 15))
        self.currency_label = customtkinter.CTkLabel(
            self.converter, text='Currency: ', font=(
                'Unispace', 15), text_color='black')
        self.history_choosen = StringVar(self)
        self.currency_chooser = customtkinter.CTkOptionMenu(
            self.converter,
            fg_color='#3158a6',
            variable=self.history_choosen,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)
        self.history_result = StringVar()
        self.history_result_label = customtkinter.CTkLabel(
            self.converter, textvariable=self.history_result, font=(
                'Unispace', 15), text_color='black')
        self.txt2_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Save to TXT',
            font=(
                'Unispace',
                15),
            command=self.history_txt_generator)
        self.result_label = customtkinter.CTkLabel(
            self.converter, text='Result: ', font=(
                'Unispace', 15), text_color='black')
        self.history_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Search!',
            font=(
                'Unispace',
                15),
            command=self.history_calculation)
        self.currency_result_label = customtkinter.CTkLabel(
            self.converter, text='Result currency: ', font=(
                'Unispace', 15), text_color='black')
        self.currency_result_choosen = StringVar()
        self.currency_result_chooser = customtkinter.CTkOptionMenu(
            self.converter,
            fg_color='#3158a6',
            variable=self.currency_result_choosen,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)
        self.gold_title_label = customtkinter.CTkLabel(
            self.converter, text='', image=gold_converter_title)
        self.gold_amount_label = customtkinter.CTkLabel(
            self.converter, text='Gold Amount: ', font=(
                'Unispace', 15), text_color='black')
        self.gold_entry = customtkinter.CTkEntry(
            self.converter, width=150, height=20, font=('Unispace', 15))
        self.txt3_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Save to TXT',
            font=(
                'Unispace',
                15),
            command=self.gold_txt_generator)

        self.gold_result_label = customtkinter.CTkLabel(
            self.converter, text='Calculated \nGold Value', font=(
                'Unispace', 15), text_color='black')
        self.gold_result = StringVar()
        self.gold_value_result_label = customtkinter.CTkLabel(
            self.converter, textvariable=self.gold_result, font=(
                'Unispace', 15), text_color='black')
        self.gold_calculation_button = customtkinter.CTkButton(
            self.converter,
            fg_color='#3158a6',
            corner_radius=100,
            width=150,
            height=30,
            text='Calculate! ',
            font=(
                'Unispace',
                15),
            command=self.gold_calculation)
        self.gold_currency_label = customtkinter.CTkLabel(
            self.converter, text='Currency: ', font=(
                'Unispace', 15), text_color='black')
        self.gold_choosen = StringVar(self)
        self.currency_gold_chooser = customtkinter.CTkOptionMenu(
            self.converter,
            fg_color='#3158a6',
            variable=self.gold_choosen,
            values=currencies,
            font=('Unispace', 15),
            button_color='#3158a6',
            button_hover_color='#3158a6',
            corner_radius=50)


        self.converter_title_label.grid(row=0, column=1, padx=20, pady=20)
        self.amount_label.grid(row=1, column=0, pady=7)
        self.amount_entry.grid(row=1, column=1, pady=7)
        self.input_label.grid(row=2, column=0, pady=7)
        self.input_chooser.grid(row=2, column=1, pady=7)
        self.output_label.grid(row=3, column=0, pady=7)
        self.output_chooser.grid(row=3, column=1, pady=7)
        self.txt_button.grid(row=3, column=2, pady=7)
        self.calculated_label.grid(row=4, column=0, pady=7)
        self.calculated_result_label.grid(row=4, column=1, pady=7)
        self.calculate_button.grid(row=4, column=2, pady=7)

        self.history_title_label.grid(row=5, column=1, padx=20, pady=20)
        self.date_label.grid(row=6, column=0, pady=7)
        self.date_entry.grid(row=6, column=1, pady=7)
        self.currency_label.grid(row=7, column=0, pady=7)
        self.currency_chooser.grid(row=7, column=1, pady=7)
        self.txt2_button.grid(row=8, column=2, pady=7)
        self.currency_result_label.grid(row=8, column=0, pady=7)
        self.currency_result_chooser.grid(row=8, column=1, pady=7)
        self.result_label.grid(row=9, column=0, pady=7)
        self.history_result_label.grid(row=9, column=1, pady=7)
        self.history_button.grid(row=9, column=2, pady=7)

        self.gold_title_label.grid(row=10, column=1, padx=20, pady=20)
        self.gold_amount_label.grid(row=11, column=0, pady=7)
        self.gold_entry.grid(row=11, column=1, pady=7)
        self.txt3_button.grid(row=12, column=2, pady=7)
        self.gold_currency_label.grid(row=12, column=0, pady=7)
        self.currency_gold_chooser.grid(row=12, column=1, pady=7)
        self.gold_result_label.grid(row=13, column=0, pady=7)
        self.gold_value_result_label.grid(row=13, column=1, pady=7)
        self.gold_calculation_button.grid(row=13, column=2, pady=7)

        # Author Frame
        self.author = customtkinter.CTkFrame(self, fg_color='transparent')
        self.author.grid_rowconfigure(0, weight=4)
        self.author.grid_rowconfigure(1, weight=3)
        self.author.grid_rowconfigure(2, weight=2)

        author_row_1_label = customtkinter.CTkLabel(
            self.author, text='', image=author_converter_title, compound="top")
        author_row_1_label.grid(row=0, column=0)

        with open('credits.txt', 'r') as autor_txt:
            a = autor_txt.read()
        author_row_2_label = customtkinter.CTkLabel(
            self.author, text=a, font=(
                'Unispace', 17), pady=20, text_color=(
                '#000000'))
        author_row_2_label.grid(row=1, column=0)

        author_row_3_label = customtkinter.CTkLabel(
            self.author, text='https://github.com/MarcinPec', font=(
                'Unispace', 19), pady=20, text_color=(
                '#000000'))
        author_row_3_label.grid(row=2, column=0)

        author_row_4_label = customtkinter.CTkLabel(
            self.author, text='Copyright by Marcin MarcinPec Pecuch, 2024', font=(
                'Unispace', 20), pady=20, text_color=(
                '#3158a6'))
        author_row_4_label.grid(row=3, column=0)

        # Default Frame
        self.choose_by_navigation('home')

        # Run
        self.mainloop()

    # Methods
    def exit_event(self):
        self.destroy()

    def appearance_changer(self, aper_name):
        customtkinter.set_appearance_mode(aper_name)

    def choose_by_navigation(self, title):
        if title == 'home':
            self.home.grid(row=0, column=1)
            self.home_button.configure(fg_color=('gray75', 'gray25'))
        else:
            self.home.grid_forget()
            self.home_button.configure(fg_color='transparent')
        if title == 'exchange':
            self.exchangeframe.grid(row=0, column=1)
            self.exchange_button.configure(fg_color=('gray75', 'gray25'))
        else:
            self.exchangeframe.grid_forget()
            self.exchange_button.configure(fg_color='transparent')
        if title == 'converter':
            self.converter.grid(row=0, column=1)
            self.converter_button.configure(fg_color=('gray75', 'gray25'))
        else:
            self.converter.grid_forget()
            self.converter_button.configure(fg_color='transparent')
        if title == 'author':
            self.author.grid(row=0, column=1)
            self.author_button.configure(fg_color=('gray75', 'gray25'))
        else:
            self.author.grid_forget()
            self.author_button.configure(fg_color='transparent')

    def home_event(self):
        self.choose_by_navigation('home')

    def exchange_event(self):
        self.choose_by_navigation('exchange')

    def converter_event(self):
        self.choose_by_navigation('converter')

    def author_event(self):
        self.choose_by_navigation('author')

    def refresh(self):
        output_v = self.row0_chosen_input.get()
        func0 = TableConverterCodes(output_v)
        func1 = TableConverterValue(self.row1_data['code'], output_v)
        func2 = TableConverterValue(self.row2_data['code'], output_v)
        func3 = TableConverterValue(self.row3_data['code'], output_v)
        func4 = TableConverterValue(self.row4_data['code'], output_v)
        func5 = TableConverterValue(self.row5_data['code'], output_v)
        func6 = TableConverterValue(self.row6_data['code'], output_v)
        func7 = TableConverterValue(self.row7_data['code'], output_v)
        func8 = TableConverterValue(self.row8_data['code'], output_v)
        func9 = TableConverterValue(self.row9_data['code'], output_v)
        func10 = TableConverterValue(self.row10_data['code'], output_v)
        func11 = TableConverterValue(self.row11_data['code'], output_v)
        func12 = TableConverterValue(self.row12_data['code'], output_v)
        func13 = TableConverterValue(self.row13_data['code'], output_v)
        func14 = TableConverterValue(self.row14_data['code'], output_v)
        func15 = TableConverterValue(self.row15_data['code'], output_v)
        func16 = TableConverterValue(self.row16_data['code'], output_v)
        func17 = TableConverterValue(self.row17_data['code'], output_v)
        func18 = TableConverterValue(self.row18_data['code'], output_v)
        func19 = TableConverterValue(self.row19_data['code'], output_v)
        result1a = self.row1_currency.set(func0)
        result2a = self.row2_currency.set(func0)
        result3a = self.row3_currency.set(func0)
        result4a = self.row4_currency.set(func0)
        result5a = self.row5_currency.set(func0)
        result6a = self.row6_currency.set(func0)
        result6a = self.row6_currency.set(func0)
        result7a = self.row7_currency.set(func0)
        result8a = self.row8_currency.set(func0)
        result9a = self.row9_currency.set(func0)
        result10a = self.row10_currency.set(func0)
        result11a = self.row11_currency.set(func0)
        result12a = self.row12_currency.set(func0)
        result13a = self.row13_currency.set(func0)
        result14a = self.row14_currency.set(func0)
        result15a = self.row15_currency.set(func0)
        result16a = self.row16_currency.set(func0)
        result17a = self.row17_currency.set(func0)
        result18a = self.row18_currency.set(func0)
        result19a = self.row19_currency.set(func0)
        result1 = self.row1_value.set(func1)
        result2 = self.row2_value.set(func2)
        result3 = self.row3_value.set(func3)
        result4 = self.row4_value.set(func4)
        result5 = self.row5_value.set(func5)
        result6 = self.row6_value.set(func6)
        result7 = self.row7_value.set(func7)
        result8 = self.row8_value.set(func8)
        result9 = self.row9_value.set(func9)
        result10 = self.row10_value.set(func10)
        result11 = self.row11_value.set(func11)
        result12 = self.row12_value.set(func12)
        result13 = self.row13_value.set(func13)
        result14 = self.row14_value.set(func14)
        result15 = self.row15_value.set(func15)
        result16 = self.row16_value.set(func16)
        result17 = self.row17_value.set(func17)
        result18 = self.row18_value.set(func18)
        result19 = self.row19_value.set(func19)

        return (result1, result1a, result2, result2a, result3, result3a, result4, result4a, result5, result5a, result6,
                result6a, result7, result7a, result8, result8a, result9, result9a, result10, result10a, result11,
                result11a, result12, result12a, result13, result13a, result14, result14a, result15, result15a, result16,
                result16a, result17, result17a, result18, result18a, result19, result19a)

    def gui_calculation(self):
        try:
            amount = int(self.amount_entry.get())
            entery = self.chosen_input.get()
            exite = self.chosen_output.get()
            func1 = ExchangeRatesCalculator(amount, entery, exite)
            result = self.calculated_result.set(func1)
            return result
        except ValueError:
            return self.calculated_result.set('Wrong Value!')

    def calculation_txt_generator(self):
        time_stamp = time.localtime()
        now = time.strftime('%H_%M_%S', time_stamp)
        dt = time.asctime()
        file_name = f'CEApp_CalculationLog_{now}'
        with open(f'{file_name}.txt', 'w') as logfile:
            logfile.write(
                f'CEApp Calculation Log File\n'
                f'Generated at: {dt}\n'
                f'Amount inserted by User: {self.amount_entry.get()}\n'
                f'Input currency: {self.chosen_input.get()}\n'
                f'Output currency: {self.chosen_output.get()}\n'
                f'Calculated value: {self.calculated_result.get()}\n')

    def history_calculation(self):
        date = self.date_entry.get()
        target_currency = self.history_choosen.get()
        result_currency = self.currency_result_choosen.get()
        func2 = ExchangeRatesHistory(date, target_currency, result_currency)
        result = self.history_result.set(func2)
        return result

    def history_txt_generator(self):
        time_stamp = time.localtime()
        now = time.strftime('%H_%M_%S', time_stamp)
        dt = time.asctime()
        file_name = f'CEApp_HistorySearchLog_{now}'
        with open(f'{file_name}.txt', 'w') as logfile:
            logfile.write(f'CEApp History Search Log File\n'
                          f'Generated at: {dt}\n'
                          f'Date inserted by User: {self.date_entry.get()}\n'
                          f'Searched currency: {self.history_choosen.get()}\n'
                          f'Calculated value in {self.currency_result_choosen.get()}: {self.history_result.get()}\n'
                          )

    def gold_calculation(self):
        try:
            mass = int(self.gold_entry.get())
            currency = self.gold_choosen.get()
            func3 = ExchangeRatesGold(mass, currency)
            result = self.gold_result.set(func3)
            return result
        except ValueError:
            return self.gold_result.set('Wrong Value!')

    def gold_txt_generator(self):
        time_stamp = time.localtime()
        now = time.strftime('%H_%M_%S', time_stamp)
        dt = time.asctime()
        file_name = f'CEApp_GoldLog_{now}'
        with open(f'{file_name}.txt', 'w') as logfile:
            logfile.write(
                f'CEApp Gold Value Calculation Log File\n'
                f'Generated at: {dt}\n'
                f'Mass of gold inserted by User: {self.gold_entry.get()} grams\n'
                f'Calculated gold value in {self.gold_choosen.get()}: {self.gold_result.get()}\n')


def app_initialization():
    try:
        SetApp("CEAp - Cash Exchange Application", 1100, 950)
    except Exception:
        return CTkMessagebox(
            SetApp,
            title='Conection Error!',
            message='Connection Error',
            icon="cancel")


app_initialization()
