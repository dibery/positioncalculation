# positioncalculation

本 repo 實作了「麥克連教你挑選會飆的法人認養股」裡面的選股方式，`twse.py` 為大盤資訊、`stock.py` 為個股資訊。

如果你覺得這個 repo 有幫助到你的話，請記得登入後幫我點一下右上角的 star 喔！

# 系統需求

## 執行環境

本程式是用 python3 寫的，所以你必須在系統裡安裝 3.6 版以後的 [python](https://www.python.org) 才能用。如果你用的是 Mac 或 Linux 系統，你可以跳過這段，Windows 的話請下載[安裝檔](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)，安裝過程中會有一項問你要不要把 python 加入環境變數，請勾選。

## 必需套件

因為有用到外部套件，所以請執行
```
pip install -r requirements.txt
```

# 執行方式

## Windows

取得當日資料：
```
py twse.py
```

```
py stock.py
```

取得指定日資料：
```
py twse.py 2020/07/06
```

```
py stock.py 2020/07/06
```

## Linux & Mac

取得當日資料：
```
python3 twse.py
```

```
python3 stock.py
```

取得指定日資料：
```
python3 twse.py 2020/07/06
```

```
python3 stock.py 2020/07/06
```

# 輸出

## 輸出範例 (`twse.py`)
```
2020/07/06 20152618292 37322.5 -2464 29.551 -70861 50259 140.57 -0.11168045697005334 12116.70 229522399499
```
各欄依次為日期、外資買超量、外資未平期貨口數、前十大交易人未來看法、匯率、買權金額、賣權金額、P/C ratio、散戶多空比、大盤指數、成交量，負數表示作空或賣出。

複製輸出之後，可以在附上的 Excel 檔新增一列，在該列第一欄貼上，選擇[文字匯入精靈](https://www.tcte.edu.tw/register/download/OpenTXTtoExcel.pdf)，你就完成今天的資料了！

更：2020/11/09 之後，每日晚上 8 點上傳本日資訊，你可以在 `index.record` 裡找到當日數值。

更：不知何許日起，改至每交易日晚上 6 點上傳本日資訊

## 輸出範例 (`stock.py`)
```
台積電	3
台泥	2
```
每行兩欄，TAB 分隔，第一欄為公司名，第二欄為外資及投信連續幾天同時買超。

更：2020/11/09 之後，每日晚上 8 點上傳本日資訊，你可以在 `record` 資料夾裡的本日日期裡找到當日外資投信同時買超個股。

# 欄位解讀

* 買超量：影響漲跌最重要的因素
* 未平期貨口數：正數時表示預期日後會漲
* 前十大未來看法：前十大交易人看未來的多空
* 匯率：值變小時易漲
* 買權金額：正為看大漲，負為看不大漲
* 賣權金額：正為看大跌，負為看不大跌
* P/C 比：數值增（> 100%）時易漲，但創近期新高時不易漲
* 散戶多空比：負值時易漲

# 後記

如果你覺得我的程式有用的話，請幫我點一下右上角的星星，轉載時請附來源。
