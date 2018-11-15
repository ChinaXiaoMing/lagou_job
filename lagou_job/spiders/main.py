import scrapy
import json
import time

class LagouJobSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
        headers = {
            'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%B9%BF%E5%B7%9E',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # formdata = {
        #     'first': 'false',
        #     'pn': str(3),
        #     'kd': 'Java'
        # }
        formdata = {}
        yield scrapy.http.FormRequest(url = url, headers = headers, callback = self.parse, formdata = formdata)

    def parse(self, response):
        jsonBody = json.loads(response.body)
        position_list = jsonBody['content']['positionResult']['result']
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

