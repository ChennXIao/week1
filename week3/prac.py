import json, urllib.request,csv
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with urllib.request.urlopen(url) as jsondata:
    data = json.loads(jsondata.read().decode('utf-8-sig')) 
    
data = data["result"]["results"]

#寫入Attraction.csv
with open('Attraction.csv', 'w',encoding='utf-8',newline='') as csv_f:
  for i in range(len(data)):
    MRT = data[i]["MRT"]
    Longitude = data[i]["longitude"]
    Address = data[i]["address"][4:8]
    Latitude = data[i]["latitude"]
    Attraction = data[i]["stitle"]
    File=data[i]["file"]
    File = "https"+File.split('https')[1]
    if MRT == None:
        MRT = ""
    writer = csv.writer(csv_f)
    writer.writerow([Attraction,Address, Longitude, Latitude, File ])



#寫入mrt.csv
with open('mrt.csv', 'w',encoding='utf-8',newline='') as csv_f:
  writer = csv.writer(csv_f)
  for i in range(len(data)):
    MRT = data[i]["MRT"]
    Attraction = data[i]["stitle"]
    if MRT == None:
        MRT = "無資料"
    writer.writerow([MRT, Attraction])


#彙整同一行政區的景點
L = []
with open('mrt.csv', 'r',encoding='utf-8',newline='') as csv_r:
   rows = csv.reader(csv_r)
   for row in rows:
        L.append(row)

L2 = {}
for i in L:
    if i[0] not in L2:
        L2[i[0]] = [i[1]]
    else:
        L2[i[0]].append(i[1])


L3_k = list(L2.keys())
L3_v = list(L2.values())


# 創建list, 加入key, 再加入value中的每一個元素
L4 = [[] for i in range(len(L3_k))]
for i in range(len(L3_k)):
    L4[i].append(L3_k[i])
    for j in range(len(L3_v[i])):
        L4[i].append(L3_v[i][j])

#寫入mrt.csv
with open('mrt.csv', 'w',encoding='utf-8',newline='') as csv_f:
  writer2 = csv.writer(csv_f)
  for i in range(len(L4)):
      writer2.writerow(L4[i])

