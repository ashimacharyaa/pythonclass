import csv
def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

data = read_csv('practice/customers-100.csv')
print(data[3]) 