import os

token = os.environ["token"]
#token1 = 
#token2 = 
#token3 =  



sProps =  os.environ["sProps"]
#sProps2 = 
#sProps3 = 


referer = os.environ["referer"]
#referer1 = 
#referer2 = 
#referer3 = 


cookies = os.environ["cookies"]
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
