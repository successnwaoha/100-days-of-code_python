import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "nwaohasuccess01@gmail.com"
MY_PASSWORD = "hjvsjaksvmlaobgp"

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Request Line" : "GET / HTTP/1.1",
    "Host" : "myhttpheader.com",
    "sec-ch-ua" : '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "upgrade-insecure-requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site" : "none",
    "sec-fetch-mode" : "navigate",
    "sec-fetch-user" : "?1",
    "sec-fetch-dest" : "document",
    "Accept-Encoding" : "gzip, deflate, br, zstd",
    "Accept-Language" : "en-US,en;q=0.9,fr;q=0.8",
    "priority" : "u=0, i",
    "x-forwarded-proto" : "https",
    "x-https" :"on",
    "X-Forwarded-For" : "102.91.4.106"

}

response = requests.get(url=url, headers=header)
website = response.content

soup = BeautifulSoup(website, "html.parser")
print(soup.prettify())
price = soup.find(class_="aok-offscreen").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < 100:
    message = f"{title} is on sale today"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="nwaohasuccess2306@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nBuy now: {url}".encode("utf-8")
        )