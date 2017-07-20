# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.start_user, include=self.user_query),
                             callback=self.parse_user)
        yield scrapy.Request(
            self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
            callback=self.parse_follows)

    def parse_user(self, response):
        res = json.loads(response.text)
        items = UserItem()
        for item in items.fields:
            if item in res.keys():
                items[item] = res.get(item)
        yield items

    def parse_follows(self, response):
        res = json.loads(response.text)
        if 'data' in res.keys():
            for token in res.get('data'):
                yield scrapy.Request(self.user_url.format(user=token.get('url_token'), include=self.user_query),
                                     callback=self.parse_user)

        if 'paging' in res.keys() and res.get('paging').get('is_end') == False:
            next_page = res.get('paging').get('next')
            yield scrapy.Request(url=next_page, callback=self.parse_follows)

    def parse(self, response):
        pass
