import tkinter as tk
from tkinter.constants import ROUND

import requests
from tkinter import ttk # 향상된 tkinter

res = requests.get("https://open.er-api.com/v6/latest/USD")
data = res.json()

ex_rates = {}
ex_rates = data['rates']

def convert_currency():
    usd = float(entry_usd.get())
    cur = currency.get()
    exchange_rate = data['rates'][f'{cur}']
    exchage = usd * exchange_rate
    result.config(text=f'{usd}USD = {exchage} {cur}')

app = tk.Tk()
app.title("환율 변환기")
app.geometry("300x200")

# USD 입력
tk.Label(app, text='USD 금액:').pack(pady=5)
entry_usd = tk.Entry(app)
entry_usd.pack()

# 통화 선택(콤보)
tk.Label(app, text='변환활 통화 선택:').pack(pady=5)
currency = ttk.Combobox(app, values=list(ex_rates.keys()))
currency.pack()

# 디폴트 값 설정
currency.set("KRW") # 값
# currency.current(0) # 인덱스

# 변환 버튼()
btn = tk.Button(app, text='변환!', command=convert_currency)
btn.pack(pady=5)

# 결과 출력
result = tk.Label(app, text='결과가 여기에 표시됨.')
result.pack(pady=10)

app.mainloop()