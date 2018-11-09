# ScrapyTestePratico

## Teste prático de Scrapping
### Target: [www.livrariacultura.com.br]

#### Objetivos
* Construir um crawler para uma loja online utilizando o Scrapy
* A spider deve realizar uma busca e extrair informalões de cada produto resultante
* Utilização de xpath na busca por links e na raspagem de dados 
* Utilizar logs para sinalização de ocorrências durante o scraping 
* Persistir os dados no MongoDB


#### Campos utilizados
* nome 
* valor
* valor_antigo 
* categoria 
* detalhes {origem, idioma}
* dimensoes {altura, largura, comprimento}

#### Comandos necessários
* pip install scrapy
* pip install pymongo
* mongod (iniciar o servidor do MongoDB)
* scrapy startproject nome_projeto (para criação do projeto)
* scrapy genspider nome_spider url_target (para criação do spider)
* scrapy crawl nome_spider (para iniciar o spider)


#### Visualização dos dados
* Instalar [MongoDB](https://www.mongodb.com/)
* Iniciar o servidor com o comando **mongod**
* Instalar [Robomongo](https://www.mongodb.com/) 


#### Spider
* parse 
    * Gera o link das categorias existentes no site
    * Encaminha para a página principal da categoria
* parse_categoria
    * Gera o link das sub categorias existentes
    * Encaminha para a página principal de cada sub-categoria
* parse_sub_categoria
    * Obtém o link de todos os produtos da página 
    * Passa para a proxima página enquanto existir sub-páginas dentro dessa sub-categoria
    * Encaminha para a página do produto
* produto
    * Acessa o link do produto
    * Retira as informações necessárias

#### Estudando + Resolvendo bugs: +- 8h
#### Desenvolvendo a solução: +- 6h

#### Referências:
* [Xpath for web scraping](https://www.slideshare.net/scrapinghub/xpath-for-web-scraping)
* [Xpath para raspagem de dados em HTML](https://escoladedados.org/tutoriais/xpath-para-raspagem-de-dados-em-html/)
* [Web Scraping na Nuvem com Scrapy](http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html)
* [Web Scraping com Scrapy ](https://pythonhelp.wordpress.com/2014/08/05/web-scraping-com-scrapy-primeiros-passos/)
* [How To Crawl A Web Page with Scrapy and Python 3 ](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
* [Scrapy](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Xpath](https://doc.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html)
* [MongoDB](https://www.mongodb.com/)
* [Robomongo](https://robomongo.org/)
* [Pymongo](https://api.mongodb.com/python/current/installation.html)
* [Tutorial Pymongo](http://api.mongodb.com/python/current/tutorial.html)
* [Web scraping with scrapy and mongodb](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)
