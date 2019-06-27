import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
import time

#parses a date within the email
tdy = datetime.date.today()
tdystr = tdy.strftime("%d-%m-%y")

#returns a response object
sourcecode = requests.get('https://www.amazon.com/').text

def priceregulator():
    #parsing webpage for individual pieces of information
    info = BeautifulSoup(sourcecode, 'lxml')

    #searches for string/price via class identification
    amzdeal = info.find('div')
    productname = info.find('div', class_='a-color-base truncate-2line').get_text()
    productprice = info.find('div', class_='a-offscreen').get_text()

    #concatenates the price as an integer, removing all decimal values
    price = float(productprice[0:5])

    if (price < 1000):  
        send_mail()

    def send_mail():
        
        #email subject in daily send
        header = "Deal of the Day//AMZ" + " " + tdystr

        #establishing server connection
        serverone = smtplib.SMTP('smtp.gmail.com', 587)
        serverone.ehlo()
        serverone.starttls()
        serverone.ehlo()

        serverone.login('aarav.makadia@gmail.com', 'amimayur')

        #structuring email format
        subject = header
        body = productname + ", " + price + ", " + "https://www.amazon.com/"

        message = f"subject: {subject}n/n/{body}"

        serverone.sendmail(
            'aarav.makadia@gmail.com',
            message
        )

        #clarification message
        print("Email Sent! Check GMAIL for Notification!")

        #end server connection
        serverone.quit()

while(True):
    priceregulator
    time.sleep(24 * (60 * 60))