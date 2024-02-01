from nsepython import *
from nsepython import nsefetch
from pprint import pprint
import csv


# nseEquity = nsetools_get_quote('HDFCBANK')
# pprint(nseEquity)
# pprint(type(nseEquity))
class EquityStock:
    def __init__(self, id, name, symbol, market_cap):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.market_cap = market_cap


def process(input_line):
    input_data = input_line.split(",")
    market_cap = "".join(input_data[3:])

    return EquityStock(
        int(input_data[0].strip()),
        input_data[1].strip(),
        input_data[2].strip(),
        0 if "Not available" in market_cap else int(market_cap.strip())
    )

def nse_custom_function_secfno(symbol,attribute="lastPrice"):
    positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
    endp = len(positions['data'])
    for x in range(0, endp):
        if(positions['data'][x]['symbol']==symbol.upper()):
            return positions['data'][x][attribute]

with open('resorces/mCapEquityList.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        response = nsetools_get_quote(row[1])
        # response2 = nsefetch(row[1])
        # print(response2)
        print(response)
        print(response['meta']['symbol'],',',response['meta']['companyName'],',',response['meta']['industry'])
        print(nse_custom_function_secfno(row[1]))
        # 'row' is a list representing a single row in the CSV file
        # print(row)
        # print(row[1])
        # equity_stock_instance = process(str(row))
        # print(equity_stock_instance)
