import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  country_name = country

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country_name, labels, values)

  
  # Solucion del profesor
  # countries = list(map(lambda x: x['Country/Territory'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))
  # charts.generate_pie_chart(countries, percentages)
  
  labels, values = utils.get_world_percentages(data)
  charts.generate_pie_chart(labels, values)

# Entry point
if __name__ == '__main__':
  run()
