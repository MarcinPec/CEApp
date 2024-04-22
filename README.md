
![Logo](https://i.ibb.co/CwfF91V/CEApp-logo-full.png)


# CEApp - Cash Exchange Application

It is a desktop application project that uses Python logic combined with an interactive graphical interface created using the pre-installed Tkinter and Custom Tkinter libraries. The intended purpose of this application is to convert amounts between currencies.


## Appendix
This application consists of two basic modules:

a. Currency Exchange Module

b. Converter module - combining three main functionalities:

- currency converter
- search engine for archived courses in various currencies
- gold value calculator in various currencies

The point of this application is to gain access to data from the National Bank of Poland (NBP) using the API in json format. This allows the data to be used for calculations and functions that are the core of the logic engine, which has been coupled to the graphical interface. 

EXCHANGE EXCHANGE module - it is a table presenting current rates of 19 sample currencies, designed using the Tkinter and Custom Tkinter and based on the json and requests libraries.

CURRENCY CONVERTER module - consists of three functions:

- converter of amounts to the selected currency - based on a function that uses 3 variables received from the user - amount, input currency and output currency, and returns the calculated value along with the target currency. 

- search engine for archive rates - based on the function of two variables downloaded from the user - date in the [yyyy-mm-dd] format and the target currency. This function returns the exchange rate for a given day of the target currency.

- gold value calculator in diffrent currencies - based on the function of one variable - gold mass in grams and target currency both collected from the user

Additionally, the ability to save the completed conversion/search results/gold values results to a txt file has been implemented.
## Related

Here are some related projects

[Custom Tkinter](https://github.com/TomSchimansky/CustomTkinter)


## Screenshots

![](https://i.ibb.co/4FtzJFJ/1.png)
![](https://i.ibb.co/WpmjtSf/2.png)

