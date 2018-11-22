import requests
import json
import math
import pymysql
import time

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
headers = {
    'Cookie': 'user_trace_token=20180918161605-b0aa247c-9147-4a2b-b17a-e9b062b2976e; _ga=GA1.2.1163668928.1537258570; LGUID=20180918161615-1c9f39a0-bb1b-11e8-a1e7-525400f775ce; _gid=GA1.2.1211841727.1542091991; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFCAAEG81E919169EE7B34CE723C22206049FBC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542191779,1542243544,1542329364,1542330122; TG-TRACK-CODE=index_navigation; SEARCH_ID=156ced6798c84977b34998041a653646; LGRID=20181116091825-84488291-e93d-11e8-88dd-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542331109',
    'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%B9%BF%E5%B7%9E',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 获取最大分页数
def get_max_page():
    formdata = {
        'first': 'false',
        'pn': str(1),
        'kd': 'Java'
    }
    req = requests.post(url=url, data=formdata, headers=headers)
    response = req.content.decode('utf-8')
    json_body = json.loads(response)
    count = json_body['content']['positionResult']['totalCount']
    return math.floor(count / 15)

def get_data(max_page):
    for i in range(1, max_page + 1):
        formdata = {
            'first': 'false',
            'pn': str(i),
            'kd': 'Java'
        }
        req = requests.post(url = url, data = formdata, headers = headers)
        response = req.content.decode('utf-8')
        json_body = json.loads(response)
        position_list = json_body['content']['positionResult']['result']
        page_no = json_body['content']['pageNo']
        for position in position_list:
            print(position)
            business_zone = position['businessZones']
            industry_label = position['industryLables']
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            business_zone_str = ''
            industry_label_str = ''
            if business_zone:
                business_zone_str = ','.join(business_zone)
            if industry_label:
                industry_label_str = ','.join(industry_label)
            page_no = page_no
            position_name = position['positionName']
            salary = position['salary']
            city = position['city']
            address = position['district']
            business_zone = business_zone_str
            line_station = position['linestaion']
            company =  position['companyFullName']
            company_size = position['companySize']
            education = position['education']
            work_year = position['workYear']
            finance_stage = position['financeStage']
            industry_field = position['industryField']
            industry_label = industry_label_str
            company_advantage = position['positionAdvantage']
            first_type = position['firstType']
            create_time = position['createTime']
            gmt_create = current_time

            connection, cursor = get_connection()
            sql = 'insert into lagou_job(page_no, position_name, salary, city, address, business_zone, line_station, company, company_size,' \
                  ' education, work_year, finance_stage, industry_field, industry_label, company_advantage, first_type, create_time, gmt_create)' \
                  ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            try:
                cursor.execute(sql, (
                    page_no, position_name, salary, city, address, business_zone,
                    line_station,
                    company, company_size, education, work_year, finance_stage,
                    industry_field,
                    industry_label, company_advantage, first_type, create_time, gmt_create))
                connection.commit()
            except pymysql.Error as e:
                print(e.args)


def get_connection():
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'pytest',
        'charset': 'utf8'
    }

    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    return connection, cursor

if __name__ == '__main__':
    print("start")
    max_page = get_max_page()
    get_data(max_page)

