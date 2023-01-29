import requests
import datetime
import smtplib

COIN_TICKER = "BTC"
COIN_NAME = "Bitcoin"


MY_EMAIL = "hubert.smtp.test@gmail.com"
PASSWORD = "gcttfrotdomgzvev"

alpha_api = "1E8UK1BXDOQXO9XU"
newsdata_api = "9e88f15bc85c4ce39c95c85c942406a3"
price_move = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": COIN_TICKER,
    "market": "USD",
    "apikey": alpha_api,
}
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
two_days_before = str(datetime.date.today() - datetime.timedelta(days=2))
response = requests.get(url='https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
data = response.json()
days = data["Time Series (Digital Currency Daily)"]

yesterday_close = float(days[yesterday]['4a. close (USD)'])
two_days_before_close = float(days[two_days_before]['4a. close (USD)'])

price_diff = yesterday_close - two_days_before_close
percent = round(price_diff * 100 / two_days_before_close)

def check_price_diff():
    if price_diff > 0:
        price_move = f"+{percent}%"
    else:
        price_move = f"{percent}%"
    return price_move


if percent >= 5 or percent <= -5:
    content = []

    parameters = {

        "apiKey": newsdata_api,
        "q": COIN_NAME,
        "sortBy": "popularity",

    }

    response = requests.get(url='https://newsapi.org/v2/everything', params=parameters)
    response.raise_for_status()
    data = response.json()
    news = data["articles"][:3]

    for info in news:
        message = f"{COIN_TICKER} {check_price_diff()}\nHeadline: {info['title']}\nAuthor: {info['source']['Name']}\nLink: {info['url']}\n"
        content.append(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:BTC ALERT {check_price_diff()} \n\n{content[0]}\n{content[1]}\n{content[2]}"
        )
else:
    print(f"Price difference is {check_price_diff()}, so nothing important happened :)")
