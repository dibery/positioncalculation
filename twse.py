'''
作者：dibery
最後修訂：2020/07/07
專案網址：https://github.com/dibery/positioncalculation
歡迎轉發，但必須完整保留此段內容
'''
import requests, json, datetime, sys, bs4

datetime = datetime.datetime
bs = bs4.BeautifulSoup
get = requests.get
date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%Y/%m/%d')

web = json.loads(get('https://www.twse.com.tw/fund/BFI82U?dayDate=%s' % date.replace('/', '')).text)
外資買超 = web['data'][3][-1].replace(',', '')

web = bs(get(f'https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={date}&commodityId=MXF').text, 'lxml')
外資小台未平口數 = int(web.findAll('table')[2].findAll('tr')[10].findAll('td')[-2].text.strip().replace(',', ''))
外資小台未平多方 = int(web.findAll('table')[2].findAll('tr')[10].findAll('td')[7].text.strip().replace(',', ''))
外資小台未平空方 = int(web.findAll('table')[2].findAll('tr')[10].findAll('td')[9].text.strip().replace(',', ''))
投信小台未平多方 = int(web.findAll('table')[2].findAll('tr')[9].findAll('td')[7].text.strip().replace(',', ''))
投信小台未平空方 = int(web.findAll('table')[2].findAll('tr')[9].findAll('td')[9].text.strip().replace(',', ''))
自營小台未平多方 = int(web.findAll('table')[2].findAll('tr')[8].findAll('td')[8].text.strip().replace(',', ''))
自營小台未平空方 = int(web.findAll('table')[2].findAll('tr')[8].findAll('td')[10].text.strip().replace(',', ''))

web = bs(get(f'https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={date}&commodityId=TXF').text, 'lxml')
外資大台未平口數 = int(web.findAll('table')[2].findAll('tr')[10].findAll('td')[-2].text.strip().replace(',', ''))
外資期貨未平口數 = 外資大台未平口數 + 外資小台未平口數 / 4

web = bs(get(f'https://www.taifex.com.tw/cht/3/dailyFXRate?queryStartDate={date}&queryEndDate={date}').text, 'lxml')
美元匯率 = web.findAll('table')[2].findAll('tr')[1].findAll('td')[1].text.strip()

web = bs(get(f'https://www.taifex.com.tw/cht/3/callsAndPutsDate?queryType=1&queryDate={date}&commodityId=TXO').text, 'lxml')
外資買權金額 = web.findAll('table')[2].findAll('tr')[7].findAll('td')[12].text.strip().replace(',', '')
外資賣權金額 = web.findAll('table')[2].findAll('tr')[10].findAll('td')[12].text.strip().replace(',', '')

web = bs(get(f'https://www.taifex.com.tw/cht/3/pcRatio?queryStartDate={date}&queryEndDate={date}').text, 'lxml')
PC_ratio = web.findAll('table')[3].findAll('tr')[1].findAll('td')[-1].text

web = bs(get(f'https://www.taifex.com.tw/cht/3/largeTraderFutQry?queryDate={date}&contractId=TX').text, 'lxml')
前十大所有買方 = int(web.findAll('table')[2].findAll('tr')[-1].findAll('td')[3].text.split()[0].replace(',', ''))
前十大所有賣方 = int(web.findAll('table')[2].findAll('tr')[-1].findAll('td')[7].text.split()[0].replace(',', ''))
前十大所有 = 前十大所有買方 - 前十大所有賣方
前十大近月買方 = int(web.findAll('table')[2].findAll('tr')[-2].findAll('td')[3].text.split()[0].replace(',', ''))
前十大近月賣方 = int(web.findAll('table')[2].findAll('tr')[-2].findAll('td')[7].text.split()[0].replace(',', ''))
前十大近月 = 前十大近月買方 - 前十大近月賣方
前十大未來看法 = 前十大所有 - 前十大近月

web = bs(get(f'https://www.taifex.com.tw/cht/3/futDailyMarketReport?commodity_id=MTX&queryDate={date}').text, 'lxml')
小台全部未沖銷 = int(web.findAll('table')[4].findAll('td', class_='12bk')[-1].text)
散戶看多 = 小台全部未沖銷 - 外資小台未平多方 - 投信小台未平多方 - 自營小台未平多方
散戶看空 = 小台全部未沖銷 - 外資小台未平空方 - 投信小台未平空方 - 自營小台未平空方
散戶多空比 = (散戶看多 - 散戶看空) / 小台全部未沖銷

web = json.loads(get('https://www.twse.com.tw/exchangeReport/MI_INDEX?date=%s' % date.replace('/', '')).text)
交易量 = web['data7'][0][1].replace(',', '')
web = json.loads(get('https://www.twse.com.tw/exchangeReport/MI_INDEX?date=%s&type=IND' % date.replace('/', '')).text)
指數 = web['data1'][1][1].replace(',', '')
print(date, 外資買超, 外資期貨未平口數, 前十大未來看法, 美元匯率, 外資買權金額, 外資賣權金額, PC_ratio, 散戶多空比, 指數, 交易量)
