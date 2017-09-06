# -*- coding: utf-8 -*
import pymysql.cursors
import urllib2
import time
import json


class StockSpider():
    def __init__(self):
        pass

    def getDateTimeNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def getDateToday(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def getTimeNow(self):
        return time.strftime('%H:%M:%S', time.localtime(time.time()))

    def getConn(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='van_spider',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def addTest(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='van_spider',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()

    def addStockData(self, data):
        # Connect to the database
        connection = self.getConn()

        try:
            lastid = 0
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `stockdata` (`datas`) VALUES (%s)"
                cursor.execute(sql, (data,))
                lastid = cursor.lastrowid

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `datas` FROM `stockdata` WHERE `id`=%s"
                cursor.execute(sql, (lastid,))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    # data format:["14:59:56", "11.17", "4601", "S"],
    def addStockOrder(self, data):

        # Connect to the database
        connection = self.getConn()

        try:
            lastid = 0
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `van_spider`.`t_stock_order`(`order_time`,`price`,`total_price`,`num`,`type`,`create_time`)VALUES (%s,%s,%s,%s,%s,%s)"

                cursor.execute(sql, ("{0:s} {1:s}".format(self.getDateToday(), data[0]), data[1], 0, data[2], data[3],
                                     self.getDateTimeNow()))
                lastid = cursor.lastrowid

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `datas` FROM `stockdata` WHERE `id`=%s"
                cursor.execute(sql, (lastid,))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    def getApiData(self):
        requrl = "http://proxy.finance.qq.com/ifzqgtimg/appstock/app/HsDealinfo/getDadan?code=sz300672&_appName=android&_dev=Redmi+Note+4X&_devId=c50cb922972722424434833f4167e6721c90d991&_mid=c50cb922972722424434833f4167e6721c90d991&_md5mid=22523BE796DEE7EA0C09F1346EF28481&_omgid=d60a9565b0d6064e612955b535047ef779d10010212615&_omgbizid=096de883a6ae2d4b6f395e484189e416b9ba0140212718&_appver=5.8.2&_ifChId=119&_screenW=1080&_screenH=1920&_osVer=6.0.1&_uin=10000&_wxuin=20000&_net=WIFI&__random_suffix=38315"
        req = urllib2.Request(url=requrl)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res

spider = StockSpider()
apiresult = spider.getApiData()
print apiresult

jsondata = json.loads(apiresult)
if jsondata["code"] == 0:
    detaillist = jsondata["data"]["detail"]
    if len(detaillist) > 0:
        for detail in detaillist:
            dbresult = spider.addStockOrder(detail)
            # print dbresult
