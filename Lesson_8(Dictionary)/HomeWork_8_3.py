
Dict_8_3 = {}

url = "https://store.steampowered.com/app/1405790/John_Wick_Hex/?l=ukrainian"
url_str = str(url)
for char in url_str:
  if char in Dict_8_3:
    Dict_8_3[char] += 1
  else:
    Dict_8_3[char] = 1

for key, value in Dict_8_3.items():
  print(f"{key}: {value}")
