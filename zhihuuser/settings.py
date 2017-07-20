# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'authorization': 'Bearer Mi4wQUFCQWlLZERBQUFBTU1MWFMxNVJDeGNBQUFCaEFsVk5HZFo1V1FEM3FDMlVXQklsTGwyRlMyMUxrSEk0Yi1SN0VB|1498564889|b460d2f2d8138fecf17141267e0f50962e01debc',
    'Cookie': 'd_c0="ADDC10teUQuPThKy8KQs9DRy_tgeaEwn7w0=|1487219098"; _zap=9746dfd1-1a1f-419b-9ee5-86b51939fc89; q_c1=0c448a0c2d6340cc8950f91e763f54f1|1496475426000|1487219098000; r_cap_id="M2NjZWMwMTJhMzRkNGJkN2JkMzdlOTE0YTRmMzFkMGI=|1498564880|72d1ca82932115ad72735f1622212dad518f9d8b"; cap_id="ODFiOGJmNGEyYWFhNDg0Y2IxNjUyYmJhMDExYmFkNWM=|1498564880|0807dd10d52fc04650cffcd68a69165f6a2d9991"; z_c0=Mi4wQUFCQWlLZERBQUFBTU1MWFMxNVJDeGNBQUFCaEFsVk5HZFo1V1FEM3FDMlVXQklsTGwyRlMyMUxrSEk0Yi1SN0VB|1498564889|b460d2f2d8138fecf17141267e0f50962e01debc; q_c1=0c448a0c2d6340cc8950f91e763f54f1|1499139800000|1487219098000; aliyungf_tc=AQAAAEKoITceAQoArRFCcMa1zm+KtuaM; s-q=vczh; s-i=4; sid=iuuc2g3g; __utma=51854390.1889617245.1489822815.1499843830.1500272050.16; __utmb=51854390.0.10.1500272050; __utmc=51854390; __utmz=51854390.1500272050.16.8.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhu-shu-shu-60/following; __utmv=51854390.100-1|2=registration_date=20141211=1^3=entry_date=20141211=1; _xsrf=fc48217e-1608-4239-bd0f-d2154b152030',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
    #'zhihuuser.pipelines.ZhihuuserPipeline': 300,
}

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
