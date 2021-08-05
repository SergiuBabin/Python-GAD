import json
import csv
import requests
from bs4 import BeautifulSoup

columns = ['position', 'name', 'games', 'goals', 'points']

if __name__ == '__main__':
    standings = []
    page = requests.get('https://lpf.ro/liga-1')
    soup = BeautifulSoup(page.content, features='html.parser')

    # table_parent = soup.find(id = 'clasament_ajax_playoff')
    # table = table_parent.find('table')
    table = soup.find(id = 'clasament_ajax_playoff').find('table')
    table_rows = table.findAll('tr', class_ ='echipa_row')
    # table_rows = [table_row for table_row in table_rows]
    for table_row in table_rows:
        text_from_tds = [
            td.text for td in table_row.find_all('td')
            if 'hiddenMobile' not in td.get('class', [])
        ]
        team_dict = {col: data for col, data in zip(columns, text_from_tds)}
        standings.append(team_dict)
    print(standings)

    with open('standing.json', mode='w') as json_file:
        json.dump(standings, json_file, indent=2)

    with open('standing.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)
        csv_writer.writerows([team_data.values() for team_data in standings])
