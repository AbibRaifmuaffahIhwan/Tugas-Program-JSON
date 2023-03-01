import json

# membuka file json
with open('Tugas.json') as f:
    data = json.load(f)

# cetak data
print(data)