import websockets
import json
import asyncio

async def subscribe():
 uri = "wss://stream.binance.com/stream"
 async with websockets.connect(uri) as websocket:
  payload = dict(
   method="SUBSCRIBE",
   params=["!miniTicker@arr@3000ms",
           "btcbusd@aggTrade",
           "btcbusd@kline_1d",
           "btcbusd@depth"
           ],
   id=2
  )
  await websocket.send(json.dumps(payload))
  while True:
     d = await websocket.recv()
     print(d)


asyncio.get_event_loop().run_until_complete(subscribe())
