# positioncalculation

本 repo 實作了「麥克連教你挑選會飆的法人認養股」裡面的選股方式，目前只實作了大盤分析的部份，選個股部份有空再補 XD。

# 系統需求

## 執行環境

本程式是用 python3 寫的，所以你必須在系統裡安裝 [python](https://www.python.org) 才能用。如果你用的是 Mac 或 Linux 系統，你可以跳過這段，Windows 的話請下載[安裝檔](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)，安裝過程中會有一項問你要不要把 python 加入環境變數，請勾選。

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

取得指定日資料：
```
py twse.py 2020/01/01
```

## Linux & Mac

取得當日資料：
```
python3 twse.py
```

取得指定日資料：
```
python3 twse.py 2020/01/01
```

# 輸出

輸出範例
```
2020/07/06 20152618292 37322.5 -2464 29.551 -70861 50259 140.57 -0.11168045697005334 12116.70 229522399499
```
各欄依次為日期、外資買超量、外資未平期貨口數、前十大交易人未來看法、匯率、買權金額、賣權金額、P/C ratio、散戶多空比、大盤指數、成交量，負數表示作空或賣出

複製輸出之後，可以在附上的 Excel 檔新增一列，在該列第一欄貼上，選擇[文字匯入精靈](https://www.tcte.edu.tw/register/download/OpenTXTtoExcel.pdf)，你就完成今天的資料了！
