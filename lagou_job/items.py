# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_no = scrapy.Field
    position_name = scrapy.Field
    salary = scrapy.Field
    city = scrapy.Field
    address = scrapy.Field
    business_zone = scrapy.Field
    line_station = scrapy.Field
    company = scrapy.Field
    company_size = scrapy.Field
    education = scrapy.Field
    work_year = scrapy.Field
    finance_stage = scrapy.Field
    industry_field = scrapy.Field
    industry_label = scrapy.Field
    company_advantage = scrapy.Field
    first_type = scrapy.Field
    create_time = scrapy.Field
    gmt_create = scrapy.Field
    gmt_modify = scrapy.Field
    pass
