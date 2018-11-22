import scrapy
import json
import time
import requests

class LagouJobSpider(scrapy.Spider):
    name = 'test'
    pn = 1
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%B9%BF%E5%B7%9E',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    headers1 = {
        'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%C3%A5%C2%B9%C2%BF%C3%A5%C2%B7%C2%9E',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }

    def start_requests(self):
        for i in range(1, 10):
            formdata = {
                'first': 'false',
                'pn': str(i),
                'kd': 'Java'
            }
            if i % 2 == 1:
                yield scrapy.FormRequest(url = self.url, headers = self.headers, callback = self.parse, formdata = formdata)
            else:
                yield scrapy.FormRequest(url=self.url, headers=self.headers1, callback=self.parse, formdata=formdata)

    def parse(self, response):
        jsonBody = json.loads(response.body)
        success = jsonBody['success']
        pn = self.pn
        result_size = 0
        if success is True:
            position_list = jsonBody['content']['positionResult']['result']
            page_no = jsonBody['content']['pageNo']
            result_size = jsonBody['content']['positionResult']['resultSize']
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            for position in position_list:
                print(position)
                business_zone = position['businessZones']
                industry_label = position['industryLables']
                business_zone_str = ''
                industry_label_str = ''
                if business_zone:
                    business_zone_str = ','.join(business_zone)
                if industry_label:
                    industry_label_str = ','.join(industry_label)
                yield {
                    'page_no': page_no,
                    'position_name': position['positionName'],
                    'salary': position['salary'],
                    'city': position['city'],
                    'address': position['district'],
                    'business_zone': business_zone_str,
                    'line_station': position['linestaion'],
                    'company': position['companyFullName'],
                    'company_size': position['companySize'],
                    'education': position['education'],
                    'work_year': position['workYear'],
                    'finance_stage': position['financeStage'],
                    'industry_field': position['industryField'],
                    'industry_label': industry_label_str,
                    'company_advantage': position['positionAdvantage'],
                    'first_type': position['firstType'],
                    'create_time': position['createTime'],
                    'gmt_create': current_time
                }





