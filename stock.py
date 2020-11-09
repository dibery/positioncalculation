from io import StringIO
from csv import reader
from requests import get
from pandas import DataFrame
from datetime import datetime
from collections import Counter
import sys, json, pickle, os

date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%Y/%m/%d')
c_date = '/'.join([str(int(date.split('/')[0]) - 1911), *date.split('/')[1:]])
strip_date = date.replace('/', '')
DB_PATH = './record/'
if not os.path.isdir(DB_PATH):
    os.mkdir(DB_PATH)
try:
    上次紀錄 = dict(map(str.split, open(DB_PATH + sorted(os.listdir(DB_PATH))[-1])))
except:
    上次紀錄 = {}
#SIZE = 5

# 上市外資

url = f'https://www.twse.com.tw/fund/TWT38U?response=csv&date={strip_date}'
df = DataFrame(list(reader(StringIO(get(url).text)))[2:])[[1, 2, 11]].dropna()
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))
df['買賣超股數'] = df['買賣超股數'].str.replace(',', '').astype(int)
#df = df.sort_values('買賣超股數')
#buy = set(map(str.strip, df.iloc[-SIZE:][::-1]['證券名稱']))
#sell = set(map(str.strip, df.iloc[:SIZE]['證券名稱']))
外買 = set(map(str.strip, df[df['買賣超股數'] >= 0]['證券名稱']))
外賣 = set(map(str.strip, df[df['買賣超股數'] < 0]['證券名稱']))
#print(f'{strip_date}\t上市外買\t{buy}')
#print(f'{strip_date}\t上市外賣\t{sell}')

# 上市投信

url = f'https://www.twse.com.tw/fund/TWT44U?response=csv&date={strip_date}'
df = DataFrame(list(reader(StringIO(get(url).text)))[1:])[[1, 2, 5]].dropna()
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))
df['買賣超股數'] = df['買賣超股數'].str.replace(',', '').astype(int)
#df = df.sort_values('買賣超股數')
#buy = '\t'.join(map(str.strip, df.iloc[-SIZE:][::-1]['證券名稱']))
#sell = '\t'.join(map(str.strip, df.iloc[:SIZE]['證券名稱']))
投買 = set(map(str.strip, df[df['買賣超股數'] >= 0]['證券名稱']))
投賣 = set(map(str.strip, df[df['買賣超股數'] < 0]['證券名稱']))
#print(f'{strip_date}\t上市投買\t{buy}')
#print(f'{strip_date}\t上市投賣\t{sell}')
同買 = 外買 & 投買

# 上櫃外資

url = f'https://www.tpex.org.tw/web/stock/3insti/qfii_trading/forgtr_result.php?t=D&type=buy&d={c_date}'
外買 = set([i[2].strip() for i in json.loads(get(url).text)['aaData']])
#print(f'{strip_date}\t上櫃外買\t{buy}')
url = f'https://www.tpex.org.tw/web/stock/3insti/qfii_trading/forgtr_result.php?t=D&type=sell&d={c_date}'
外賣 = set([i[2].strip() for i in json.loads(get(url).text)['aaData']])
#print(f'{strip_date}\t上櫃外賣\t{sell}')

# 上櫃投信

url = f'https://www.tpex.org.tw/web/stock/3insti/sitc_trading/sitctr_result.php?t=D&type=buy&d={c_date}'
投買 = set([i[2].strip() for i in json.loads(get(url).text)['aaData']])
#print(f'{strip_date}\t上櫃投買\t{buy}')
url = f'https://www.tpex.org.tw/web/stock/3insti/sitc_trading/sitctr_result.php?t=D&type=sell&d={c_date}'
投賣 = set([i[2].strip() for i in json.loads(get(url).text)['aaData']])
#print(f'{strip_date}\t上櫃投賣\t{sell}')
同買 = 同買 | 外買 & 投買
#print(同買)
with open(DB_PATH + strip_date + '.txt', 'w') as f:
    for i in 同買:
        print(i, int(上次紀錄.get(i, 0)) + 1, file=f, sep='\t')
        print(i, int(上次紀錄.get(i, 0)) + 1, sep='\t')
#pickle.dump(同買, open(DB_PATH + strip_date + '.pkl', 'wb'))
