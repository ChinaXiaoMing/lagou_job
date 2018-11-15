# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'pytest',
    'charset': 'utf8'
}

class LagouJobPipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(**db_config)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = 'insert into lagou_job(position_name, salary, city, address, business_zone, line_station, company, company_size,' \
              ' education, work_year, finance_stage, industry_field, industry_label, company_advantage, first_type, create_time, gmt_create)' \
              ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql,(item['position_name'], item['salary'], item['city'], item['address'], item['business_zone'], item['line_station'],
                                     item['company'], item['company_size'], item['education'], item['work_year'], item['finance_stage'], item['industry_field'],
                                     item['industry_label'], item['company_advantage'], item['first_type'], item['create_time'], item['gmt_create']))
            self.connection.commit()
        except pymysql.Error as e:
            print(e.args)
        return item
