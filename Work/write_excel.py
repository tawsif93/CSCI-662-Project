import re
from xlwt import Workbook
from nltk.tokenize import TweetTokenizer

from data import getData, demojize, remove_hashtags

data = getData() 

totalDataCount = len(data)
print(totalDataCount)
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

count = 0
for i in range(totalDataCount):
  isRetweet = False
  id = data[i]["id"]
  text = data[i]["text"]
  #text = demojize(text)
  text = remove_hashtags(text)
  text = re.sub("@(\w)+", "@USER", text)
  words = TweetTokenizer().tokenize(text)
  
  if(words[0] == "RT"):
    continue
  else:
    count += 1
  
  text = " ".join(words)
  text = demojize(text)

  sheet1.write(count, 0, id)
  sheet1.write(count, 1, text)
  
wb.save('xlwt example.xls')

