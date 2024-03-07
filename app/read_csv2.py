import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def convert_data(data):
  new_data = []
  for item in data:
    new_data.append({
      'Country': item['Country/Territory'],
      '2022': float(item['2022 Population']),
      '2020': float(item['2020 Population']),
      '2015': float(item['2015 Population']),
      '2010': float(item['2010 Population']),
      '2000': float(item['2000 Population']),
      '1990': float(item['1990 Population']),
      '1980': float(item['1980 Population']),
      '1970': float(item['1970 Population'])
})
  return new_data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  data = convert_data(data)
  print(data)
  