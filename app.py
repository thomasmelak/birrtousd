import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
from os import makedirs, path



url = "https://combanketh.et/exchange-rate-detail"
date = date.today()
postData = {'date':date}
data = list
home = path.expanduser("~")
appHome = "{}/.birrExchangeRate".format(home)
coloredFile = "{}/Colored Data.txt".format(appHome)
rawFile = "{}/Raw Data.txt".format(appHome)


#Try to connect to website, may fail due to network error
try:
    response = requests.post(url,postData)
except:
    print("Network request failed")
    quit()

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    tableHead = soup.thead
    tableRow = tableHead.find_next_sibling("tr")
    data = list(tableRow.stripped_strings)
else:
    print("Server responded with {}".format(response.status_code))
    print("Exiting")
    quit()





#Check if default path exists and create it if it doesn't

if not path.exists(appHome):
    makedirs(appHome)

# Write to color coded file for shell

resultFile = open(file=coloredFile, mode='a+')

resultFile.write("\n\033[0m---------USD to BIRR Latest Update: {}---------\n".format(datetime.now().strftime("%B %d, %Y %H:%M")))

resultFile.write("\033[0;32mCash Buy: {} \t \033[0;31mCash Sell: {}\t \033[0;32mTransaction Buy: {}\t \033[0;31mTransaction Sell: {}\t \n".format(data[2],data[3],data[4],data[5]))

resultFile.close()

# Write raw data

resultFile = open(file=rawFile, mode='a+')

resultFile.write("---------USD to BIRR Latest Update: {}---------\n".format(datetime.now().strftime("%B %d, %Y %H:%M")))

resultFile.write("Cash Buy: {} \t Cash Sell: {}\t Transaction Buy: {}\t Transaction Sell: {}\t \n".format(data[2],data[3],data[4],data[5]))

resultFile.close()
