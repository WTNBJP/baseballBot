import discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
import time


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

    
@client.event
async def on_ready():
  print('ログインしました')
  
@client.event
async def on_message(message):
  global time
  if message.author.bot:
    return
  if message.content == '/who':
    start = time.time()
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://npb.jp/games/2023/')
    pitcher = driver.find_elements(By.CLASS_NAME,'pit_table')
    for pitchers in pitcher:
      pitchersText = pitchers
      await message.channel.send(pitchersText.text)
      await message.channel.send('--------------------------')
    print(time.time() - start)
  if message.content == '/when':
    start = time.time()
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://npb.jp/games/2023/')
    times = driver.find_elements(By.CLASS_NAME,'score_table_wrap')
    for timea in times:
      today_time = timea.find_element(By.CLASS_NAME,'state').text
      team1_name = timea.find_element(By.CLASS_NAME,'team1').find_element(By.TAG_NAME,'img').get_attribute('alt')
      team2_name = timea.find_element(By.CLASS_NAME,'team2').find_element(By.TAG_NAME,'img').get_attribute('alt')
      await message.channel.send(today_time)
      await message.channel.send(team1_name)
      await message.channel.send(team2_name)
      await message.channel.send('----------------------------------')
    print(time.time() - start)
  if message.content == '/score':
    start = time.time()
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://npb.jp/games/2023/')
    i = 1
    wrapers = driver.find_elements(By.CLASS_NAME,'score_table_wrap')
    for wraper in wrapers:
      await message.channel.send(wraper.find_element(By.CLASS_NAME,'team1').find_element(By.TAG_NAME,'img').get_attribute('alt'))
      await message.channel.send(wraper.find_element(By.XPATH,f'//*[@id="score_live_basic"]/div[{i}]/a/div/div[1]/table/tbody/tr[1]').text)
      await message.channel.send(wraper.find_element(By.CLASS_NAME,'team2').find_element(By.TAG_NAME,'img').get_attribute('alt'))
      await message.channel.send('----------------------------------')
      i = i + 1
    print(time.time() - start)
load_dotenv()
client.run(os.environ['TOKEN'])



