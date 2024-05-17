import requests
api = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def search(word):
  content = word.upper() + "\n"
  raw = requests.get(api+word).json()
  
  partofspeech = {}
  examples = []
  synonyms = []
  antonyms = []
  
  for data in raw:
    if data.get('phonetic'):
      if not data['phonetic'] in content:
        content += data['phonetic'] + "\n"
  
    if data.get('antonyms'):
      for ay in data.get('antonyms'):
        synonyms.append(ay)
  
    if data.get('synonyms'):
      for sy in data.get('synonyms'):
        synonyms.append(sy)
  
  
    for m in data['meanings']:
  
      for sy in m.get('synonyms'):
        synonyms.append(sy)
      for ay in m.get('antonyms'):
        antonyms.append(ay)
  
      if not m['partOfSpeech'] in partofspeech:
        partofspeech[m['partOfSpeech']] = []
  
      for d in m['definitions']:
        definition = d['definition']
        for dsy in d['synonyms']:
          synonyms.append(dsy)
        for day in d['antonyms']:
          antonyms.append(day)
  
        partofspeech[m['partOfSpeech']].append(definition)
        examples.append(d.get('example',""))


  aysy = ""
  if synonyms:
    aysy += "Synonyms: "
    for sy in synonyms:
      if not sy in aysy:
        aysy += sy + ", "
    aysy = aysy[0:len(aysy)-2] + "\n"
  
  if antonyms:
    aysy += "Antonyms: "
    for ay in antonyms:
      if not ay in aysy:
        aysy += ay + ", "
    aysy = aysy[0:len(aysy)-2] + "\n"

  if aysy != "":
    content += "\n" + aysy
  
  
  
  counte = 0
 
  for e in examples:
    if e != "":
      if counte == 0:
        content += "\nExamples:\n"
      counte += 1
      content += "- " + e + "\n"
  
    
  for d in partofspeech:
    content +=  "\n" + d.upper() + "\n"
    for definition in partofspeech[d]:
      content +=   "- " + definition + "\n"
  
  
  
  #print(content)
  return content
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  