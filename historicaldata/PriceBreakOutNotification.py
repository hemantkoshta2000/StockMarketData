from unicodedata import decimal

import requests

from SendSmsToMobile import send_push_notification
import csv

nseUrl = "https://www.nseindia.com/api/quote-equity?symbol="
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Cookie': 'AKA_A2=A; ak_bmsc=2E741C53EEF1B3A41B346AAB9681D0DB~000000000000000000000000000000~YAAQv/Y3F4VnxEiNAQAAzs7PYhZFxQdBQEXJLWzF3x5sYsZr05kAEk2ULxB54zw1psnuyhsPS+1nuP9O6R7E3BFDjraqz42qWu8/7uHMeZ1rB4mAnm+7/ywr2Fm+3gW0KqUxkDpI74Qo+mHGPpYRKT+gCindtQnmSGcvYXoF/HqjStVGXHdq60UzVlbj70UkDbKAf9TkXh5ne+oscoyViiDSGkjncdCDfbi9x2XqtkxdeQZUCV7jDg2a+iRw5Ry32G5qtrCLAqJ/yXXuDZfkkJEN4EnND54tG+t3vLOTqloNWfVpLB1/ZH6vCIelAd91d2M76l7fkJG+7n/9oG/3xcV+pNLDPXWuHJAx67M0UzysTLdqwHm/S0xVZvIbSKB4YXfqXATDZI61sw==; bm_sv=EB9D2A76118387517D9FE1F1E46559F8~YAAQ5/Y3F1WYqV6NAQAAJ+vPYhbZzrRKTpSzdNjmgo/1TJsT0bz49vhZVcewVEYuW6ylHThYMDwOdg6qXq44yvfpUhkfOYfNpLpwmglxgDNR9+0632TwZ97IVDo3v4WxCykp9oBVuJE5lY6udDARj4y+jiAZDiS4URYmDY5i7jQYh/OVa9fvfptAC3jflJIIDXWiWB7wZoEp9+INUQic92MsRYEZT5PcADUxjUzszkIp6dlhzzrKsb64nnKpOq9oXjU=~1'
}
def convert(param):
    if param.__contains__("&"):
        param = param.replace("&", "%26")
    return param

with open('resorces/priceBreakOutNotification.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row in the CSV file
    count = 0
    for row in csv_reader:
        symbolFetch = convert(row[0])
        symbolUrl = (nseUrl + symbolFetch)
        print(symbolUrl)
        response = requests.get(symbolUrl, headers=headers).json()
        print(response)
        printvalue = (
                "" + str(response.get('metadata', {}).get('series', "series NA ")) + "," +
                str(response.get('metadata', {}).get('symbol', "symbol NA ")) + "," +
                str(response.get('info', {}).get('companyName', "companyName NA ")) + "," +
                str(response.get('metadata', {}).get('isin', "isin NA ")) + "," +
                str(response.get('metadata', {}).get('industry', "metadata industry NA ")) + "," +
                str(response.get('info', {}).get('industry', "info industry NA ")) + "," +
                str(response.get('priceInfo', {}).get('lastPrice', "lastPrice NA "))
        )
        if float(response.get('priceInfo', {}).get('lastPrice', "lastPrice NA ")) > float(row[1]):
            send_push_notification("Price Breakout", printvalue)