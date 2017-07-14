#!/Users/bin/python3

import requests

def main():
    print("Enter the amount to Convert from USD to INR : ")

    # takes user input for amount ot convert
    toConvert = input()

    # fetches current price for USD
    response = requests.get(url="http://www.apilayer.net/api/live?access_key=8afdbe8d25317768468dbe6fe5725fd7&format=1")

    # converts the response
    jsonResponse = response.json()

    # fetches list of currency
    priceList = jsonResponse["quotes"]

    # fetches USD to INR Conversion rate
    usdinr = priceList["USDINR"]


    # Output
    print("The current USD Price is : Rs." + str(usdinr))

    print(float(toConvert) * usdinr)



