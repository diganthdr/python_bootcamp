import sys
import json
#print(sys.path)
#sys.path.insert(0,'C:\\Users\\dr\\Documents\\Python Course\\course code\\project\\covid_proj')
from input_data.collect_data import get_processed_data

from mail_service.send_mail import send_mail
from news.news import collect_news
from reports.covid_statewise_stats import get_total_cases

dashline = "------------------------------------"

def process_api_data():
    print("Processing data collected from API module..")
    data = get_processed_data()

    #load subscription json, map count data to subscribers
    fd = open("subscribe\\subscription_data.json")
    subscription_data = json.load(fd) 

    subscriber_mail_map = {}

    for mailid, list_of_states in subscription_data.items():
        tmp_list = []
        for state_name in list_of_states:
            total_cases = get_total_cases(state_name, data) #optimisation: pre calculate and keep statewise count
            sub_map = {state_name: total_cases}
            tmp_list.append(sub_map)
        sub_map = {mailid:tmp_list}
        subscriber_mail_map.update(sub_map)

    print(dashline)
    print(subscriber_mail_map)
    print(dashline)
    return subscriber_mail_map

def process_news():
    ''' process raw news, make it into simple list of news, with hyperlink. '''
    news_data =  collect_news()
    TAB ='\t'
    NEWLINE = '\n'
    print("Processing data collected from NEWS module..")
    processed_news_text = '----- HEADLINES -----'
    for link, headline in news_data.items():
        processed_news_text = processed_news_text + headline + TAB + link + NEWLINE

    print(processed_news_text)
    return processed_news_text

def aggregate_data():
    print("Report: Aggregating reports.. ")
    api_data = process_api_data()
    news_data =	process_news()
    prepare_xls_sheet()
    
    mail_content = ''
    #aggregate news and api reports.
    #mail_content = (api_data, news_data)

    return mail_content


def prepare_xls_sheet():
    data = get_processed_data() #optimisation: Instead of calling requests twice, store it once.

    if not isinstance(data, dict):
        print("API data is not in dictionary")
        return
        
    all_states = data.keys()
    state_stats_map = {}
    for state_name in all_states:
        total_cases = get_total_cases(state_name, data) #optimisation: pre calculate and keep statewise count
        state_stats_map.update({state_name: total_cases})

    create_xls(state_stats_map)

    #return state_stats_map


def create_xls(state_stats_map):
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('All states')

    #first row, Header
    #takes, row, column and text ast arg
    worksheet.write(0,0,"STATE")
    worksheet.write(0,1,"ACTIVE")

    for row, (state, count) in enumerate(state_stats_map.items(), 1):
        col = 0
        worksheet.write(row, col, state)
        worksheet.write(row, col+1, count)
    workbook.save('statewise_covid_report.xls')
    #Further task, use pandas library and write to xls/xlsx.

def trigger_mail():
    aggregated_data = aggregate_data()
    send_mail(aggregated_data)
