#!/usr/bin/env python
#-*- coding: utf-8 -*-

from selenium import webdriver
import time, lxml.html, csv
ChromePath = r"/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/archive/2014_07_05_Flight/chromedriver"
browser = webdriver.Chrome(executable_path=ChromePath)


csvPath="/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_08_21_MosVybory/problems/data3.csv"

# собранные id-шники
urlArray = [{"okrug":"ЮЗАО","zone_index":101,"name":"Академический","id":102},
	{"okrug":"СВАО","zone_index":50,"name":"Алексеевский","id":51},
	{"okrug":"СВАО","zone_index":50,"name":"Алтуфьевский","id":52},
	{"okrug":"ЦАО","zone_index":77,"name":"Арбат","id":78},
	{"okrug":"СВАО","zone_index":50,"name":"Бабушкинский","id":53},
	{"okrug":"САО","zone_index":33,"name":"Беговой","id":35},
	{"okrug":"САО","zone_index":33,"name":"Бескудниковский","id":36},
	{"okrug":"СВАО","zone_index":50,"name":"Бибирево","id":54},
	{"okrug":"ЮАО","zone_index":114,"name":"Бирюлево Восточное","id":115},
	{"okrug":"ЮАО","zone_index":114,"name":"Бирюлево Западное","id":116},
	{"okrug":"ВАО","zone_index":1,"name":"Богородское","id":2},
	{"okrug":"ЮАО","zone_index":114,"name":"Братеево","id":117},
	{"okrug":"СВАО","zone_index":50,"name":"Бутырский","id":55},
	{"okrug":"ЗАО","zone_index":19,"name":"Внуково","id":20},
	{"okrug":"САО","zone_index":33,"name":"Войковский","id":37},
	{"okrug":"САО","zone_index":33,"name":"Восточное Дегунино","id":38},
	{"okrug":"ВАО","zone_index":1,"name":"Восточное Измайлово","id":4},
	{"okrug":"ВАО","zone_index":1,"name":"Восточный","id":6},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Гагаринский","id":103},
	{"okrug":"ВАО","zone_index":1,"name":"Гольяново","id":7},
	{"okrug":"ЮАО","zone_index":114,"name":"Даниловский","id":118},
	{"okrug":"САО","zone_index":33,"name":"Дмитровский","id":40},
	{"okrug":"ЮАО","zone_index":114,"name":"Донской","id":119},
	{"okrug":"ЦАО","zone_index":77,"name":"Замоскворечье","id":80},
	{"okrug":"САО","zone_index":33,"name":"Западное Дегунино","id":41},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Зюзино","id":104},
	{"okrug":"ЮАО","zone_index":114,"name":"Зябликово","id":120},
	{"okrug":"ВАО","zone_index":1,"name":"Ивановское","id":8},
	{"okrug":"ВАО","zone_index":1,"name":"Измайлово","id":9},
	{"okrug":"ЮВАО","zone_index":88,"name":"Капотня","id":90},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Коньково","id":105},
	{"okrug":"САО","zone_index":33,"name":"Коптево","id":42},
	{"okrug":"ВАО","zone_index":1,"name":"Косино-Ухтомский","id":10},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Котловка","id":106},
	{"okrug":"ЦАО","zone_index":77,"name":"Красносельский","id":81},
	{"okrug":"ЗАО","zone_index":19,"name":"Крылатское","id":22},
	{"okrug":"ЗелАО","zone_index":131,"name":"Крюково","id":132},
	{"okrug":"ЗАО","zone_index":19,"name":"Кунцево","id":23},
	{"okrug":"СЗАО","zone_index":68,"name":"Куркино","id":69},
	{"okrug":"САО","zone_index":33,"name":"Левобережный","id":43},
	{"okrug":"ЮВАО","zone_index":88,"name":"Лефортово","id":92},
	{"okrug":"СВАО","zone_index":50,"name":"Лианозово","id":56},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Ломоносовский","id":107},
	{"okrug":"СВАО","zone_index":50,"name":"Лосиноостровский","id":57},
	{"okrug":"ЮВАО","zone_index":88,"name":"Люблино","id":93},
	{"okrug":"СВАО","zone_index":50,"name":"Марфино","id":58},
	{"okrug":"СВАО","zone_index":50,"name":"Марьина Роща","id":59},
	{"okrug":"ЮВАО","zone_index":88,"name":"Марьино","id":94},
	{"okrug":"ЗелАО","zone_index":131,"name":"Матушкино","id":133},
	{"okrug":"ВАО","zone_index":1,"name":"Метрогородок","id":11},
	{"okrug":"ЦАО","zone_index":77,"name":"Мещанский","id":82},
	{"okrug":"СЗАО","zone_index":68,"name":"Митино","id":70},
	{"okrug":"ЗАО","zone_index":19,"name":"Можайский","id":24},
	{"okrug":"САО","zone_index":33,"name":"Молжаниновский","id":44},
	{"okrug":"ЮАО","zone_index":114,"name":"Москворечье-Сабурово","id":121},
	{"okrug":"ЮАО","zone_index":114,"name":"Нагатино-Садовники","id":122},
	{"okrug":"ЮАО","zone_index":114,"name":"Нагатинский Затон","id":123},
	{"okrug":"ЮАО","zone_index":114,"name":"Нагорный","id":124},
	{"okrug":"ЮВАО","zone_index":88,"name":"Некрасовка","id":95},
	{"okrug":"ЮВАО","zone_index":88,"name":"Нижегородский","id":96},
	{"okrug":"ЗАО","zone_index":19,"name":"Ново-Переделкино","id":25},
	{"okrug":"ВАО","zone_index":1,"name":"Новогиреево","id":12},
	{"okrug":"ВАО","zone_index":1,"name":"Новокосино","id":13},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Обручевский","id":108},
	{"okrug":"ЮАО","zone_index":114,"name":"Орехово-Борисово Северное","id":125},
	{"okrug":"ЮАО","zone_index":114,"name":"Орехово-Борисово Южное","id":126},
	{"okrug":"СВАО","zone_index":50,"name":"Останкинский","id":60},
	{"okrug":"СВАО","zone_index":50,"name":"Отрадное","id":61},
	{"okrug":"ЗАО","zone_index":19,"name":"Очаково-Матвеевское","id":26},
	{"okrug":"ВАО","zone_index":1,"name":"Перово","id":14},
	{"okrug":"ЮВАО","zone_index":88,"name":"Печатники","id":97},
	{"okrug":"СЗАО","zone_index":68,"name":"Покровское-Стрешнево","id":71},
	{"okrug":"ВАО","zone_index":1,"name":"Преображенское","id":15},
	{"okrug":"ЦАО","zone_index":77,"name":"Пресненский","id":83},
	{"okrug":"ЗАО","zone_index":19,"name":"Проспект Вернадского","id":27},
	{"okrug":"ЗАО","zone_index":19,"name":"Раменки","id":28},
	{"okrug":"СВАО","zone_index":50,"name":"Ростокино","id":62},
	{"okrug":"САО","zone_index":33,"name":"Савеловский","id":45},
	{"okrug":"СВАО","zone_index":50,"name":"Свиблово","id":63},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Северное Бутово","id":109},
	{"okrug":"СВАО","zone_index":50,"name":"Северное Медведково","id":64},
	{"okrug":"СЗАО","zone_index":68,"name":"Северное Тушино","id":72},
	{"okrug":"СВАО","zone_index":50,"name":"Северный","id":65},
	{"okrug":"ЗелАО","zone_index":131,"name":"Силино","id":135},
	{"okrug":"САО","zone_index":33,"name":"Сокол","id":46},
	{"okrug":"ВАО","zone_index":1,"name":"Сокольники","id":18},
	{"okrug":"ЗАО","zone_index":19,"name":"Солнцево","id":29},
	{"okrug":"СЗАО","zone_index":68,"name":"Строгино","id":73},
	{"okrug":"ЦАО","zone_index":77,"name":"Таганский","id":84},
	{"okrug":"ЦАО","zone_index":77,"name":"Тверской","id":85},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Теплый Стан","id":110},
	{"okrug":"САО","zone_index":33,"name":"Тимирязевский","id":47},
	{"okrug":"ЗАО","zone_index":19,"name":"Тропарево-Никулино","id":30},
	{"okrug":"ЗАО","zone_index":19,"name":"Филевский Парк","id":31},
	{"okrug":"ЗАО","zone_index":19,"name":"Фили-Давыдково","id":32},
	{"okrug":"ЦАО","zone_index":77,"name":"Хамовники","id":86},
	{"okrug":"САО","zone_index":33,"name":"Ховрино","id":48},
	{"okrug":"САО","zone_index":33,"name":"Хорошевский","id":49},
	{"okrug":"ЮАО","zone_index":114,"name":"Царицыно","id":127},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Черемушки","id":111},
	{"okrug":"ЮАО","zone_index":114,"name":"Чертаново Северное","id":128},
	{"okrug":"ЮАО","zone_index":114,"name":"Чертаново Центральное","id":129},
	{"okrug":"ЮАО","zone_index":114,"name":"Чертаново Южное","id":130},
	{"okrug":"СЗАО","zone_index":68,"name":"Щукино","id":75},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Южное Бутово","id":112},
	{"okrug":"СВАО","zone_index":50,"name":"Южное Медведково","id":66},
	{"okrug":"СЗАО","zone_index":68,"name":"Южное Тушино","id":76},
	{"okrug":"ЮВАО","zone_index":88,"name":"Южнопортовый","id":100},
	{"okrug":"ЦАО","zone_index":77,"name":"Якиманка","id":87},
	{"okrug":"СВАО","zone_index":50,"name":"Ярославский","id":67},
	{"okrug":"ЮЗАО","zone_index":101,"name":"Ясенево","id":113},
	{"okrug":"ЗАО","zone_index":19,"name":"Дорогомилово","id":21},
	{"okrug":"ЗАО","zone_index":19,"name":"Филевский парк","id":31},
	{"okrug":"САО","zone_index":33,"name":"Аэропорт","id":34},
	{"okrug":"САО","zone_index":33,"name":"Головинский","id":39},
	{"okrug":"ЮВАО","zone_index":88,"name":"Рязанский","id":98},
	{"okrug":"ВАО","zone_index":1,"name":"Вешняки","id":3},
	{"okrug":"СВАО","zone_index":50,"name":"Марьина роща","id":59},
	{"okrug":"СЗАО","zone_index":68,"name":"Хорошево-Мневники","id":74},
	{"okrug":"ЮАО","zone_index":114,"name":"Нагатинский затон","id":123},
	{"okrug":"ЗелАО","zone_index":131,"name":"Савелки","id":134}
	]


def scrapeProblemsRegion(zone, region):
	url = "https://gorod.mos.ru/?show=problem&m=8&y=2014&zone=%d&district=%d" %(zone, region)

	browser.get(url)
	time.sleep(5)

	dom = lxml.html.fromstring(browser.page_source)
	
	problems = dom.cssselect('div.problem_block_head')
	
	pDict={'zone':zone, 'region':region}

	for problem in problems:
		if len(problem.cssselect('a'))>0:
			pType=problem.cssselect('a')[0].text.encode('utf-8')
			pCount = problem.cssselect('span.inscription')[0].text.encode('utf-8')
			pCount = int(pCount[1:-1])
			pDict[pType]=pCount
		else: print '!'

		
	return pDict

# HEADERS
headers = scrapeProblemsRegion(68,70)
headers['district']='Митино'
headers['zone']='СЗАО'

for key in headers.keys():
	headers[key]=key


# print
# print ','.join([str(key) for key in sorted(headers)])


# WRITER
with open(csvPath, 'a') as csvfile:
	writer = csv.DictWriter(csvfile, sorted(headers), restval='-', extrasaction='ignore', dialect='excel')

	writer.writerow(headers)
	# Понеслосьа
	for row in urlArray:
		district_id = row['id']
		district = row['name']
		okrug = row['okrug']
		okrug_id = row['zone_index']

		result = scrapeProblemsRegion(okrug_id,district_id)
		result['district'] = district
		result['zone'] = okrug

		writer.writerow(result)
		# print '|'.join([row[key] for key in sorted(row)])
		print district,' scraped!'
		time.sleep(5)
    	
  


# result = scrapeProblemsRegion(68,70)
# print '|'.join(result.keys())
# print '|'.join([str(result[x]) for x  in result.keys()])
print 'all done!'
browser.close()

