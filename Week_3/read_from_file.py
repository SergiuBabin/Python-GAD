import json
import csv


if __name__ == '__main__':
    standings = []


    # Read form Json
    with open('standing.json') as json_file:
        standings = json.load(json_file)
    print('[JSON] standings', standings)

    # Read from CSV
    with open('standing.csv') as csv_file:
        csv_rows = csv.reader(csv_file)
        csv_rows = list(csv_rows)

        columns = csv_rows[0]

        for row in csv_rows[1:]:
            standings.append({
                column: value for column, value in zip(column, value)
            })

    print(standings)