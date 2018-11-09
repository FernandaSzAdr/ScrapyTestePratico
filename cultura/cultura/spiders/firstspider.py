# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from cultura.items import CulturaItem

class FirstspiderSpider(scrapy.Spider):
    name = 'firstspider'
    allowed_domains = ['www.livrariacultura.com.br']
    start_urls = ['http://www.livrariacultura.com.br/']

    def parse(self, response):
        self.log('[PARSE] ACESSANDO URL: %s' %response.url)

        links_categoria = response.xpath('//li[@class="toggle-menu"]/a/@href').extract()

        for link in links_categoria:
            url_categoria = urljoin(response.url, link)
            yield scrapy.Request(url_categoria, self.parse_categoria)


    def parse_categoria(self, response):
        self.log('[PARSE_CATEGORIA]   ACESSANDO URL: %s' % response.url)

        links_sub_categoria = response.xpath('//div[@class="cat-links"]/ul/li/a/@href').extract()

        links_sub_categoria = links_sub_categoria

        for link in links_sub_categoria:
            url_sub_categoria = urljoin(response.url, link)
            yield scrapy.Request(url_sub_categoria, self.parse_sub_categoria)

    def parse_sub_categoria(self, response):
        self.log('[PARSE_SUB_CATEGORIA]   ACESSANDO URL: %s' % response.url)

        links_produtos_pagina = response.xpath('//section/div/div[@class="product-ev-content"]/div[@class="product-ev-box"]'
                                               + '/div[@class="product-font-ev product-title-ev "]/a/@href').extract()
        #self.log('[LINK] %s' %links_produtos_pagina)

        # Pega os produtos daquela página
        for link in links_produtos_pagina:
            yield scrapy.Request(link, self.produto)

        try:
            next_page = response.xpath('//ul[@class="pagination"]/li/a[@class="selected"]'
                                       + '/../following-sibling::li/a/@href').extract()[0]
            url_next_page = 'https://www.livrariacultura.com.br' + next_page

            # Passa para a proxima página se tiver:
            self.log('[INFO] Seguindo para a proxima página.')
            yield scrapy.Request(url_next_page, self.parse_sub_categoria)

        except:
            self.log('[INFO] Não existe mais páginas para serem lidas.')


    def produto(self, response):
        self.log('[PRODUTO]   ACESSANDO URL: %s' % response.url)

        item = CulturaItem()
        item['url'] = response.url
        item['nome'] = response.xpath('//h1[@class="title"]/text()').extract_first()

        valor = response.xpath('//div[@class="price-details"]/*[@class="price"]/text()').extract()
        # Alguns produtos estão de graça, então o campo valor não existirá
        if len(valor) > 0:
            valor = valor[0]
            valor = valor.split('R$ ')[1]
            item['valor'] = float(valor.replace(',', '.'))
        else:
            item['valor'] = 0.0

        valor = response.xpath('//div[@class="price-details"]/*[@class="price-original"]/text()').extract()
        # Alguns produtos não estão em promoção então o campo valor original não existirá
        if len(valor) > 0:
            valor = valor[0]
            valor = valor.split('R$ ')[1]
            item['valor_antigo'] = float(valor.replace(',', '.'))
        else:
            item['valor_antigo'] = 0.0

        item['categoria'] = response.xpath('//nav[@class="breadcrumb-wrapper"]/ol[@class="breadcrumb container"]'
                                           + '/li[2]/a/text()').extract_first()

        detalhes = {}
        detalhes['origem'] = response.xpath('//*[text()[contains(., "Origem")]]/following-sibling::text()').extract_first()
        detalhes['idioma'] = response.xpath('//ul[@class="details-column"]/li/*[text()[contains(., "Idioma")]]'
                                            + '/following-sibling::text()').extract_first()
        item['detalhes'] = detalhes

        dimensoes = {}
        dimensoes['altura'] = response.xpath('//*[text()[contains(., "Altura")]]/following-sibling::text()').extract_first()
        dimensoes['largura'] = response.xpath('//*[text()[contains(., "Largura")]]/following-sibling::text()').extract_first()
        dimensoes['comprimento'] = response.xpath('//*[text()[contains(., "Comprimento")]]/following-sibling::text()').extract_first()
        item['dimensoes'] = dimensoes

        yield item