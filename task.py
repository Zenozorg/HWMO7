# import os
# import requests
# import random

#
# image_urls = [
#     'https://example.com/image1.jpg',
#     'https://example.com/image2.jpg',
#      #etc...
# ]
# for i in range(10):
#     folder_name = f'image_folder_{i}'
#     os.makedirs(folder_name, exist_ok=True)
    
#     url = random.choice(image_urls)
#     response = requests.get(url)
    
#     with open(f'{folder_name}/image.jpg', 'wb') as f:
#         f.write(response.content) #task a

# import os
# import aiohttp
# import aiofiles
# import asyncio
# import random

# image_urls = [
#     'https://example.com/image1.jpg',
#     'https://example.com/image2.jpg',
#     #etc...
# ]

# async def download_image(url, folder_name):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             image_data = await response.read()
            
#             os.makedirs(folder_name, exist_ok=True)
#             async with aiofiles.open(f'{folder_name}/image.jpg', 'wb') as f:
#                 await f.write(image_data)

# async def main():
#     tasks = []
#     for i in range(10):
#         folder_name = f'image_folder_{i}'
#         url = random.choice(image_urls)
#         tasks.append(download_image(url, folder_name))
#     await asyncio.gather(*tasks)

# asyncio.run(main()) #task b



# import requests

# url = 'https://example.com/weather'
# response = requests.get(url)

# content = response.text
# split_content = content.split('<div class="temperature">')
# if len(split_content) > 1:
#     weather_data = split_content[1].split('</div>')[0]
#     print("Погода в Астане:", weather_data) task c




# import requests
# from bs4 import BeautifulSoup

# url = 'https://example.com/weather'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# weather_data = soup.find('div', class_='temperature').text
# print("Погода в Астане:", weather_data) task d