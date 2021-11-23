from requests_html import HTMLSession
import sqlite3
conn = sqlite3.connect("emoji.db")
cursor = conn.cursor()
cursor.execute('create table emoji (value varchar(20) primary key, keyword varchar(20))')

def getDataAndSaveToFile():
  session = HTMLSession()
  res = session.get("https://www.emojiall.com/zh-hans/all-emojis")
  emojiList = res.html.find('.emoji_card .emoji_font')
  keywordList = res.html.find('.emoji_card .emoji_name')
  for emoji,keyword in zip(emojiList, keywordList):
    key = emoji.text.strip()
    value = keyword.text.strip()
    cursor.execute(f'insert into emoji (value, keyword) values (\'{key}\', \'{value}\')')
  cursor.close()
  conn.commit()
  conn.close()

if __name__ == "__main__":
  getDataAndSaveToFile();

