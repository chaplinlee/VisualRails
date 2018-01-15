import requests
import json


def spider():
    exampleUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-15&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=SNN&purpose_codes=ADULT'
    r = requests.get(url)
    obj = json.loads(r.text)
    print(obj)

    root_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?'
    url_date = 'leftTicketDTO.train_date='
    url_from_station = '&leftTicketDTO.from_station='
    url_to_station = '&leftTicketDTO.to_station='
    url_purpose_codes = '&purpose_codes=' #ADULT||0x00(student)



def main():
    spider()

if __name__ == '__main__':
    main()