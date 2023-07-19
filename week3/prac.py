import json, urllib.request,csv
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with urllib.request.urlopen(url) as jsondata:
    data = json.loads(jsondata.read().decode('utf-8-sig')) 
    
data = data["result"]["results"]

with open('Attraction.csv', 'w',encoding='utf-8',newline='') as csv_f:
  for i in range(len(data)):
    MRT = data[i]["MRT"]
    Longitude = data[i]["longitude"]
    # Address = data[i]["address"][4:8]
    Latitude = data[i]["latitude"]
    Attraction = data[i]["stitle"]
    File=data[i]["file"]
    File = "https"+File.split('https')[1]
    if MRT == None:
        MRT = ""
    writer = csv.writer(csv_f)
    writer.writerow([Attraction,MRT, Longitude, Latitude, File ])




with open('mrt.csv', 'w',encoding='utf-8',newline='') as csv_f:
  writer = csv.writer(csv_f)
  for i in range(len(data)):
    MRT = data[i]["MRT"]
    Attraction = data[i]["stitle"]
    if MRT == None:
        MRT = "無資料"
    writer.writerow([MRT, Attraction])


L = []
with open('mrt.csv', 'r',encoding='utf-8',newline='') as csv_r:
   rows = csv.reader(csv_r)
   for row in rows:
        L.append(row)

L2 = {}
for i in L:
    if i[0] not in L2:
        L2[i[0]] = i[1]
    else:
        L2[i[0]] = L2[i[0]] +' '+ i[1]

L3 = list(L2.items())
with open('mrt.csv', 'w',encoding='utf-8',newline='') as csv_f:
  writer2 = csv.writer(csv_f)
  for i in range(len(L3)):
     writer2.writerow(L3[i])
