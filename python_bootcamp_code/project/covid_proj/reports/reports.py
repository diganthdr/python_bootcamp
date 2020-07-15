import sys
#print(sys.path)
#sys.path.insert(0,'C:\\Users\\dr\\Documents\\Python Course\\course code\\project\\covid_proj')
from input_data.collect_data import get_processed_data

from mail_service.send_mail import send_mail
from news.news import collect_news

def process_api_data():
    print("Processing data collected from API module..")
    data = get_processed_data()
    #Process it here, get stats, return data
    processed_api_data = {} #excel sheet, stats
    return processed_api_data

def process_news():
    news_data =  collect_news()
    #process raw news, make it into simple list of news, with hyperlink.
    processed_news = {}
    print("Processing data collected from NEWS module..")
    return processed_news

def aggregate_data():
    api_data = process_api_data()
    news_data =	process_news()
    print("Report: Aggregating reports.. ")

    #aggregate news and api reports.
    mail_content = (api_data, news_data)

    send_mail(mail_content)
    return True

def trigger_mail():
    aggregate_data()
