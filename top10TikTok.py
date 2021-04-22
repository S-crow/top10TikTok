# execute commands :
# pip uninstall TikTokApi-pyppeteer
# pip install TikTokApi --upgrade

import wget, os
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()
results = 10
i = 0
trending = api.trending(count=results, custom_verifyFp="")

for tiktok in trending:
    i += 1
    url = tiktok['video']['downloadAddr']
    if not os.path.exists('/Users/Public/trends'):
        os.makedirs('/Users/Public/trends')
    wget.download(url, '/Users/Public/trends/video' + str(i) + '.mp4')
    

