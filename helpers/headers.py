import os

token = 'OTAxMzczNDU1MjIyNTg3NDMz.YXO7wg.cwngshO6QXmZDWPY83uekePHQ1o'
#token1 = 
#token2 = 
#token3 =  



sProps =  'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC41NCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTUuMC40NjM4LjU0Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMjExMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0'
#sProps1 = 
#sProps2 = 
#sProps3 = 


referer = 'https://discord.com/channels/901373944521691187/901373944521691190'
#referer1 = 
#referer2 = 
#referer3 = 


cookies = '_ga=GA1.2.213505624.1602872985; __stripe_mid=b00975bb-b80d-4ee5-9a38-1024fa055c21096503; _parsely_visitor={%22id%22:%22pid=20b3e63554182db3c8f4e6e4478885c2%22%2C%22session_count%22:3%2C%22last_session_ts%22:1609154305445}; __dcfduid=bc9cd2c9c7e3479abe529c4adbd0981b; __sdcfduid=208a44d0f42211ebafe6ffcea2391006d96e482b7c9a580270f5ffdbd7ad3a480dbdff86052d5b4d9ebbe6f76f05322e; _gcl_au=1.1.1940492944.1634540690; _gid=GA1.2.1682292481.1634917907; OptanonConsent=isIABGlobal=false&datestamp=Fri+Oct+22+2021+19%3A51%3A47+GMT%2B0400+(Gulf+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fsupport.discord.com%2Fhc%2Fen-us&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1'
#cookies1 = 
#cookies2 = 
#cookies3 = 

headers = [{
    'authority': 'discordapp.com',
    'x-super-properties': f'{sProps}',
    'origin': 'https://discordapp.com',
    'authorization': f'{token}',
    'accept-language': 'en-US',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': f"{referer}",
    'accept-encoding': 'gzip, deflate, br',
    'cookie': f"{cookies}",
},
{
    
}]