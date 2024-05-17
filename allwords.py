import json

def words_all():
  with open("words_dictionary.json") as f:
    allwords = json.load(f)
    
  letter = ""
  l = ""
  style = ""

  c = []
  for i in allwords:
    if len(i) >= 5:
      c.append(i)
  c.sort()

  for words in c:
  
    l = words[0].upper()
    if l != letter:
      letter = l
      style += f'''<div style="background-color: #333;color: white;size:30px;font-size: 23px;
      border-radius: 10px;" id="{l}"> &nbsp {l} </div>'''
    style += f"{words}<br>"

  with open("allwords.html","w") as f:
    f.write(style)


