#!/usr/bin/env python3

# For chinese
# -*- coding: UTF-8 -*-


import requests, json
import pandas as pd
import numpy as np
import re
import time
import datetime

# from 2010/01/01 to today
start_dt = datetime.datetime(2018, 5, 1)
period = (datetime.datetime.today() - start_dt).days + 1

columns = ['證券代號','證券名稱','成交股數','成交筆數','成交金額',
           '開盤價','最高價','最低價','收盤價','漲跌(+/-)','漲跌價差',
           '最後揭示買價','最後揭示買量','最後揭示賣價','最後揭示賣量','本益比']

df_dict = {}

for i in range(period):
    time.sleep(3)

    dt = start_dt + datetime.timedelta(days = i)

    date = dt.strftime("%Y%m%d")

    url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={date}&type=ALL&_={mstime}'.format(
              date = date,
              mstime = int(time.time() * 1000
          ))
    print(url)
    rsp = requests.get(url)

    if rsp.status_code == 200:
        try:
            data = rsp.json()
        except:
            continue

        arr = data.get('data5', None)
        # list(zip(*arr)) can switch row/column for preprocessing
        if arr:
            df = pd.DataFrame(arr, columns=columns)

            # remove '--' and translate to float
            df['收盤價'] = [float(re.sub('[,]', '', n)) if n != '--' else 0 for n in df['收盤價'].values.tolist()]

            value_gt_270_df = df[df.loc[:, '收盤價'] > 270].sort_values(["收盤價"], ascending=True)
            df_dict[date] = value_gt_270_df

mtk_summary = []
for date in df_dict:
    df = df_dict[date]
    rows = df[df.loc[:, '證券代號'] == '2454'].values.tolist()
    if rows:
        mtk_summary.append([date] + rows[0])

print(pd.DataFrame(mtk_summary, columns = ['日期'] + columns))
