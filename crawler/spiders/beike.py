import json

import scrapy

from crawler.items import CrawlerItem


class BeikeSpider(scrapy.Spider):
    name = 'beike'
    allowed_domains = ['ke.com']
    start_urls = ['https://bj.ke.com/ershoufang/pg1/']

    def parse_page(self, response):
        print('response', response)
        intro_list = response.css('.introContent ul li')
        intro_dict = {
            intro.css('.label::text').get(): intro.css('.label::text').get()
            for intro in intro_list
        }

        CrawlerItem(
            title=response.css('.main::text').get().strip(),  # 标题
            total_price=response.css('.total::text').get().strip(),  # 总价
            unit_price=response.css('.unitPriceValue::text').get().strip(),  # 单价
            room=scrapy.Field(),  # 厅室描述
            floor=scrapy.Field(),  # 楼层
            total_floor=scrapy.Field(),  # 总楼层
            face_to=scrapy.Field(),  # 朝向
            face_type=scrapy.Field(),  # 类型: 平层/精装
            total_area=scrapy.Field(),  # 总面积
            year=scrapy.Field(),  # 楼龄
            community=scrapy.Field(),  # 小区
            community_geo=scrapy.Field(),  # 小区地图位置
            area=scrapy.Field(),  # 所在区: 朝阳
            visit_time=scrapy.Field(),  # 看房时间
            house_id=scrapy.Field(),  # 贝壳编号
            list_time=scrapy.Field(),  # 挂牌时间
            last_txn=scrapy.Field(),  # 上次交易时间
            txn_ownership=scrapy.Field(),  # 交易权属: 商品房
            usage=scrapy.Field(),  # 用途: 普通住宅
            ownership=scrapy.Field(),  # 产权所属: 非共有
            owner_age=scrapy.Field(),  # 房屋所有年限: 满五年
            mortgage=scrapy.Field(),  # 抵押信息: 无抵押
            room_book_spare_parts=scrapy.Field(),  # 房本备件: 已上传房本照片

            layout=scrapy.Field(),  # 户型图
            down_payment=scrapy.Field(),  # 参考首付
            net_down_payment=scrapy.Field(),  # 净首付
            monthly_equal_principal_interest=scrapy.Field(),  # 等额本息月供
            monthly_equal_principal=scrapy.Field(),  # 等额本金月供
        )

    def parse(self, response):
        # print(response.body)
        house_list = response.css('.sellListContent .clear .info.clear .title a')
        for house_url in house_list:
            yield scrapy.Request(house_url.attrib['href'], callback=self.parse_page)

        # pages_json = response.css('.page-box.house-lst-page-box')[0].attrib['page-data']
        # try:
        #     pages = json.loads(pages_json)
        #     total_page = pages['totalPage']
        #     cur_page = pages['curPage']
        #     if cur_page + 1 <= total_page:
        #         yield scrapy.Request(f"/ershoufang/pg{cur_page + 1}", callback=self.parse)
        # except Exception as e:
        #     pass
