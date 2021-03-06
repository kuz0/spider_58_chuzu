# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://{}'.format(proxy_pool.pop())
        print()

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass
