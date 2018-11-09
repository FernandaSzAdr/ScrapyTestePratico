# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CulturaItem(scrapy.Item):
    nome = scrapy.Field()
    valor = scrapy.Field()
    valor_antigo = scrapy.Field()
    categoria = scrapy.Field()
    detalhes = scrapy.Field()
    dimensoes = scrapy.Field()
    url = scrapy.Field()