# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()                  # 标题
    total_price = scrapy.Field()            # 总价
    unit_price = scrapy.Field()             # 单价
    room = scrapy.Field()                   # 厅室描述
    floor = scrapy.Field()                  # 楼层
    total_floor = scrapy.Field()            # 总楼层
    face_to = scrapy.Field()                # 朝向
    face_type = scrapy.Field()              # 类型: 平层/精装
    total_area = scrapy.Field()             # 总面积
    year = scrapy.Field()                   # 楼龄
    community = scrapy.Field()              # 小区
    community_geo = scrapy.Field()          # 小区地图位置
    area = scrapy.Field()                   # 所在区: 朝阳
    visit_time = scrapy.Field()             # 看房时间
    house_id = scrapy.Field()               # 贝壳编号
    list_time = scrapy.Field()              # 挂牌时间
    last_txn = scrapy.Field()               # 上次交易时间
    txn_ownership = scrapy.Field()          # 交易权属: 商品房
    usage = scrapy.Field()                  # 用途: 普通住宅
    ownership = scrapy.Field()              # 产权所属: 非共有
    owner_age = scrapy.Field()              # 房屋所有年限: 满五年
    mortgage = scrapy.Field()               # 抵押信息: 无抵押
    room_book_spare_parts = scrapy.Field()  # 房本备件: 已上传房本照片

    layout = scrapy.Field()                            # 户型图
    down_payment = scrapy.Field()                      # 参考首付
    net_down_payment = scrapy.Field()                  # 净首付
    monthly_equal_principal_interest = scrapy.Field()  # 等额本息月供
    monthly_equal_principal = scrapy.Field()           # 等额本金月供
