import requests
import json
with requests.Session() as sess:
 sess.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
 sess.headers['referer'] = 'https://finance.yahoo.com/quote/META/chart?p=META'
 result = sess.get('https://query1.finance.yahoo.com/v8/finance/chart/META?symbol=META&period1=1652972400&period2=1699345389&useYfid=true&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=ZRx%2Fd7gF6Rx&corsDomain=finance.yahoo.com').text
 data = json.loads(result)
 ochlv = data['chart']['result'][0]['indicators']['quote'][0]
 time_data = data['chart']['result'][0]['timestamp']
 print(ochlv['open'])
 print(len(time_data))
 print(len(ochlv['open']))