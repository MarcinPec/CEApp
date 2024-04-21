"""
CEApp - Cash Exchange Application - ENGINE

2024

"""
import requests
import json


def rounder2(func):
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            return round(result, 2)
        except TypeError:
            return f'Data problem!'
    return wrapper


def rounder3(func):
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            return round(result, 4)
        except TypeError:
            return f'Data problem!'
    return wrapper


class APIDataCalls:
    @staticmethod
    def complex_calls(code):
        try:
            if code == 'PLN':
                return 1
            else:
                api_call = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json')
                api_load = json.loads(api_call.content)
                return api_load
        except requests.exceptions.ConnectionError:
            return f'Connection Error'

    @staticmethod
    def code_calls(code):
        try:
            if code == 'PLN':
                return 'PLN'
            else:
                api_call = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json')
                api_load = json.loads(api_call.content)
                code_load = api_load['code']
                return code_load
        except requests.exceptions.ConnectionError:
            return f'Connection Error'

    @staticmethod
    def value_calls(code):
        try:
            if code == 'PLN':
                return 1
            else:
                api_call = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json')
                api_load = json.loads(api_call.content)
                api_value_extraction = api_load['rates'][0]['mid']
                return api_value_extraction
        except requests.exceptions.ConnectionError:
            return f'Connection Error'

    @staticmethod
    def history_calls(code, date):
        try:
            if code == 'PLN':
                return 1
            else:
                api_call = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json')
                api_load = json.loads(api_call.content)
                api_history_extraction = api_load["rates"][0]["mid"]
                return api_history_extraction
        except requests.exceptions.ConnectionError:
            return f'Connection Error'

    @staticmethod
    def gold_calls():
        try:
            api_call = requests.get(f'http://api.nbp.pl/api/cenyzlota')
            api_load = json.loads(api_call.content)
            gold_prize = api_load[0]['cena']
            return gold_prize
        except requests.exceptions.ConnectionError:
            return f'Connection Error'


class TableConverterValue(APIDataCalls):
    def __init__(self, entry_currency, output_currency):
        self.entry_currency = entry_currency
        self.output_currency = output_currency

    @rounder3
    def convert_table_value(self):
        entry_value_request = self.value_calls(self.entry_currency)
        output_value_request = self.value_calls(self.output_currency)

        if self.entry_currency == self.output_currency:
            return 1.000
        else:
            result = entry_value_request/output_value_request
            return result

    def __str__(self):
        try:
            return f'{self.convert_table_value()}'
        except json.decoder.JSONDecodeError:
            return f'No data!'


class TableConverterCodes(APIDataCalls):
    def __init__(self, output_currency):
        self.output_currency = output_currency

    def convert_table_code(self):
        return self.output_currency

    def __str__(self):
        try:
            return f'{self.convert_table_code()}'
        except json.decoder.JSONDecodeError:
            return f'No data!'


class ExchangeRatesCalculator(APIDataCalls):
    def __init__(self, amount, currency_input, currency_output):
        self.amount = amount
        self.currency_input = currency_input
        self.currency_output = currency_output

    @rounder2
    def exchange_calculation(self):
        entry = self.value_calls(self.currency_input)
        exit_1 = self.value_calls(self.currency_output)
        calculation = self.amount * (entry/exit_1)
        return calculation

    def __str__(self):
        try:
            return f'{self.exchange_calculation()} {self.currency_output}'
        except (ValueError, TypeError):
            return f'Wrong value/input/output!'


class ExchangeRatesHistory(APIDataCalls):
    def __init__(self, date, target_currency, result_currency):
        self.date = date
        self.target_currency = target_currency
        self.result_currency = result_currency

    @rounder3
    def history_searching(self):
        history_calculation = self.history_calls(self.target_currency, self.date)/self.value_calls(self.result_currency)
        return history_calculation

    def __str__(self):
        try:
            return f'{self.history_searching()} {self.result_currency}'
        except json.decoder.JSONDecodeError:
            return f'No data!'


class ExchangeRatesGold(APIDataCalls):
    def __init__(self, mass, currency):
        self.mass = mass
        self.currency = currency

    @rounder2
    def gold_calc(self):
        gold_price = self.gold_calls()/self.value_calls(self.currency)
        gold_value = self.mass*gold_price
        return gold_value

    def __str__(self):
        try:
            return f'{self.gold_calc()} {self.currency}'
        except json.decoder.JSONDecodeError:
            return f'Wrong value!'
