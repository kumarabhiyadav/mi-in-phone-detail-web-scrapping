import html
import requests
dataToExtract = '['
#URL ARRAY ONLY MI SITE
URLS = ['https://www.mi.com/in/redmi-note-8-pro/','https://www.mi.com/in/redmi-note-9-pro/','https://www.mi.com/in/redmi-note-7-pro/']
for URL in range(0,len(URLS)):
   r = requests.get(url = URLS[URL])                                    #Get HTML by get request
   data = html.unescape(r.text)                                         #removing escape sequence from html
#    print(type(data))                                                  #print for just confirmation
   startindex=data.find('<script type="application/ld+json">')+len('<script type="application/ld+json">')   #Find where the product details exists + len('str') is used for count index after string
   endIndex=data.find('</script>',startindex)                           #start for particular '</script>' after start index 
   for x in range (startindex,endIndex):                                #Loop For getting data from start index to end Index and append it to string
       dataToExtract = dataToExtract+data[x]                            #Appending

   if(len(URLS)-1 > URL ):
    dataToExtract+=','                                                  #added for JSON Formating 
  

dataToExtract += ']'                                                    #added for JSON Formating
# print(dataToExtract)                                                  #just for Test
# print(type(dataToExtract))  #just for test
with open('output.json', "w", encoding="utf-8") as f:     
    f.write(dataToExtract)                                              #Output file