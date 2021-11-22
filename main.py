from requests_html import HTMLSession
import json


def getDataAndSaveToFile():
  session = HTMLSession()
  res = session.get("https://www.emojiall.com/zh-hans/all-emojis")
  emojiList = res.html.find('.emoji_card .emoji_font')
  keywordList = res.html.find('.emoji_card .emoji_name')

  resObj = {}
  with open('emoji_data.json', 'w') as f:
    for emoji,keyword in zip(emojiList, keywordList):
      print(emoji.text.strip(), ':', keyword.text.strip())
      resObj[emoji.text.strip()] = keyword.text.strip()
      json.dump(resObj, f)


if __name__ == "__main__":
  getDataAndSaveToFile();

