# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from hub.settings import IMAGES_STORE

class HubPipeline(object):

    def process_item(self, item, spider):
        fold_name = "".join(item["title"])
        header = {
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/67.0.3396.79 Safari/537.36",
        }
        images = []
        dir_path = "{}".format(IMAGES_STORE)
        if not os.path.exists(dir_path) and len(item["src"]) != 0:
            os.makedirs(dir_path)
        if len(item["src"]) == 0:
            with open("..//check.txt","a+") as fp:
                fp.write("".join(item["title"]) + ":" + "".join(item["url"]))
                fp.write("\n")

        for jpg_url, name, num in zip(item["src"], item["alt"], range(0,100)):
            file_name = name + str(num)
            file_path = "{}//{}".format(dir_path, file_name)
            images.append(file_path)
            if os.path.exists(file_path) or os.path.exists(file_name):
                continue

            with open('{}//{}.jpg'.format(dir_path, file_name), 'wb') as f:
                req = requests.get(jpg_url, headers=header)
                f.write(req.content)


        return item
