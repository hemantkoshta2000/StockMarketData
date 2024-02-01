import csv

import requests


def process_record(record1):
    # Example process: Convert age to integer
    record = record1.split(",")
    dict1 = {}
    dict1['Series'] = record[0]
    dict1['Symbol'] = record[1]
    dict1['EqName'] = record[2]
    dict1['Isin'] = record[3]
    dict1['Meta Industry'] = record[4]
    dict1['Info Industry'] = record[5]
    dict1['lastPrice'] = record[6]
    return dict1


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
    'Cookie': 'defaultLang=en; _ga=GA1.1.987803686.1705845565; _ga_QJZ4447QD3=GS1.1.1706023865.1.0.1706023865.0.0.0; AKA_A2=A; nsit=yjTn-M3zyEedGxonMcdNZP8v; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwNjI2MTM3NiwiZXhwIjoxNzA2MjY4NTc2fQ.R7bopC2T5a0gnZQnBTLJywp7nmCuAXdCLhZygWxql8s; bm_mi=D5EB5AA88789DA7913CBAFCDC3613912~YAAQTI0sMe0VGhKNAQAA+28aRRZw0JXuNie6lS5oT7JFPQeyYuvCntNzM24nd4Wq+zmEBDlWQ4MdEaDAonFmLTyFV70Thvq45sxNZ0q5fCcUy5gJCoeyFAJJisib5OMca47bzQDaAt1zuPj7ADm3ORKki7KgFSmU+MVDYGuYFi7lZ8quBGYTucl2zvOt4OliVqoYT9XZcQPNYfVIYLmNxBxQm8fWewV57bfpmUiKYnBFwJirHu8dKs+KzGRkBAu9nZWrVtI3e6L9pyB6J6OsQVXwEo+LpFyeiMdVRvqVd9Kz1nJq3R/ypZu6N+JliicV~1; _ga_87M7PJ3R97=GS1.1.1706261368.13.1.1706261375.0.0.0; ak_bmsc=64D05D63D7EA026CC0577552198B351D~000000000000000000000000000000~YAAQTI0sMTQWGhKNAQAAY3QaRRZAeyWrRSNIBUjn2YgTQLg+SpS+mSn+1iDVhZlOh4ND3scdCz3ktTNIEZUXJaCY0RgH2kfR5AhIZySiUFhuHgEVy3jq6auTTAI1JhqWgrD+5pYkbgZpxM4A8BY7HGtRjfQSKFK6w3OaVwTa9KYmJbPskAJ+wvACryS8yF/J+Cc3ac7QD7BRsR4om+VvID1mWr+4c1ZnCeeYj/PSWYY15VBKBmP84nWPqUn8iTnolwKrLwWUUhOInRX3qgMJzub/FtAwE8DGcal0F/PmTTZHjj7nqKHWAfcoO3vk/x8ax572pq8CcZMm8CNe+VsGmWE5C249aJ2YG4MEwX6Pz9gJKy6EPz+7O0ck1g8da89dJR2+AcFIP0WFdK52FdBqieQoZ8EqMrrTnJFztZSYIKmJDEnqg1rezJ6iyzM/jeagCtdJe6nCQ4u7Gy7wuc0DSBWvQ64DqPeVYPpoG+n4AqhAtinsnBcIu2LtiWs9hTmDVGaVww6MUSWpOK9Y8oonpuGy; RT="z=1&dm=nseindia.com&si=d944bc7d-47ee-44cd-868a-755723fedd11&ss=lrufyp2y&sl=1&se=8c&tt=y8&bcn=%2F%2F684d0d49.akstat.io%2F&ld=8av"; bm_sv=C3B2AF16E310BDC41DD9304698BDD8AD~YAAQPI0sMUnLWhONAQAAmLAaRRbDrCS8/or8OvyalT00+HI2iCXHBeES3nx/9z/YXUIcdPRUf205cTDdzO6FTMaOMTy0ciqLjCd7pRogagns+75bCGS/q3ug8/n4F+Z67XsD2PWw62CwrFCykRfEXRqtfJCXrzLQCcae0a0XSIQH2zUjMrRjW0dxTkc/oHtNCW1UpOmszNjF7mQ80GEDDe039cIr2iGYjk7Xq0VWIb4PihLsT/yvZlu+T6KuNGgaHkY1~1'
}


# equityMetadata.getMetadata().getSeries() + CoreCons
# equityMetadata.getInfo().getSymbol() + CoreConstant
# equityMetadata.getInfo().getCompanyName() + CoreCon
# equityMetadata.getInfo().getIndustry() + CoreConsta
# equityMetadata.getMetadata().getIndustry() + CoreCo
# equityMetadata.getPriceInfo().getPreviousClose() +
# equityMetadata.getMetadata().getListingDate() + Cor
# equityMetadata.getIndustryInfo().toString() + //Cor
def convert(param):
    if param.__contains__("&"):
        param = param.replace("&", "%26")
    return param


with open('../../historicaldata/resorces/mCapEquityList.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row in the CSV file
    count = 0
    for row in csv_reader:
        symbolFetch = convert(row[1])
        symbolUrl = (nseUrl + symbolFetch)
        print(symbolUrl)
        try:
            response = requests.get(symbolUrl, headers=headers).json()
            # print(response.text)
        except Exception as e:
            print(e)
        else:
            printvalue = (
                    "" + str(response.get('metadata', {}).get('series', "series NA ")) + "," +
                    str(response.get('metadata', {}).get('symbol', "symbol NA ")) + "," +
                    str(response.get('info', {}).get('companyName', "companyName NA ")) + "," +
                    str(response.get('metadata', {}).get('isin', "isin NA ")) + "," +
                    str(response.get('metadata', {}).get('industry', "metadata industry NA ")) + "," +
                    str(response.get('info', {}).get('industry', "info industry NA ")) + "," +
                    str(response.get('priceInfo', {}).get('lastPrice', "lastPrice NA "))
            )
            with open('../../historicaldata/resorces/mCapEquityListOutput.csv', mode='a', newline='') as output_file:
                # Define field names for the output CSV file
                fieldnames = ['Series', 'Symbol', 'EqName', 'Isin', 'Meta Industry', 'Info Industry', 'lastPrice']

                # Create a CSV writer object
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)

                # Write header to the output CSV file
                # writer.writeheader()
                writer.writerow(process_record(printvalue))
            print("", count, ":", printvalue)
            count = count + 1
