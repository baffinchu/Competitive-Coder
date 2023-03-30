#!/usr/bin/env python
#
# This script will fetch a list of challenges from hackerrank.com
# and save it to '/challenges.json'
#
# Dependency:
# * scrapy >=2.5
#
# This script is compatible with python 3.x

import json
import os.path
import scrapy
from scrapy import settings
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

tracks = []

class HackerSpider(scrapy.Spider):
    name = 'list-challenge'
  
    def start_requests(self):
        tracks_list = [
            {'title': 'Algorithms', 'name': 'algorithms'},
            # {'title': 'Data Structures', 'name': 'data-structures'},
            # {'title': 'Mathematics', 'name': 'mathematics'},
        ]
        for i, track in enumerate(tracks_list):
            tracks.append({
                'title': track['title'],
                'name': track['name'],
                'chapters': [],
            })
            url = f'https://www.hackerrank.com/rest/contests/master/tracks/{track["name"]}/chapters'
            yield Request(url=url, callback=self.parse_chapters, cb_kwargs={'track-id': i})
  
    def parse_chapters(self, response, track_id):
        json_object = json.loads(response.text)
        for i, chapter in enumerate(json_object['models']):
            tracks[track_id]['chapters'].append({
                'title': chapter['name'],
                'name': chapter['slug'],
                'challenges': [None] * chapter['challenges_count'],
                # 'difficulty': chapter['difficulty_name'],
            })
            for offset in range(0, chapter['challenges_count'], 10):
                url = (f'https://www.hackerrank.com/rest/contests/master/categories/'
                       f'{tracks[track_id]["name"]}%7C{chapter["slug"]}/challenges'
                       f'?offset={offset}&limit=10')
                yield Request(url=url, callback=self.parse_page,
                              cb_kwargs={'track-id': track_id, 'chapter-id': i, 'offset': offset})
      
    def parse_page(self, response, track_id, chapter_id, offset):
        json_object = json.loads(response.text)
        for i, challenge in enumerate(json_object['models']):
            tracks[track_id]['chapters'][chapter_id]['challenges'][offset + i] = {
                'title': challenge['name'],
                'name': challenge['slug'],
                'difficulty': challenge['difficulty_name'],
                'point': challenge['max_score'],
                'rate': challenge['success_ratio'],
            }
        
if __name__ == '__main__':
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    process = CrawlerProcess(settings=settings.Settings(custom_settings))
    process.crawl(HackerSpider)
    process.start()
    with open(os.path.join(os.path.dirname(__file__), '..', 'challenges.json'), 'w') as f:
        json.dump({'tracks': tracks}, f, indent=2, separators=(',', ': '))
