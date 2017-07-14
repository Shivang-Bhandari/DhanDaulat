#!/Users/bin/python3

import requests

def main():
    print("Enter the amount to Convert from USD to INR : ")

    toConvert = input()

    response = requests.get(url="http://www.apilayer.net/api/live?access_key=8afdbe8d25317768468dbe6fe5725fd7&format=1")

    jsonResponse = response.json()

    priceList = jsonResponse["quotes"]

    usdinr = priceList["USDINR"]

    print("The current USD Price is : Rs." + str(usdinr))

    print(float(toConvert) * usdinr)



