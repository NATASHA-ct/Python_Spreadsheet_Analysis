import csv


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    sales = []
    dictionary = {}

    for row in data:
        sale = int(row['sales'])
        month = row['month']
        sales.append(sale)

        dictionary[sale] = month

    total = sum(sales)
    print('Total sales: {}'.format(total))

    max_value = max(sales)
    min_value = min(sales)

    max_month = dictionary.get(max_value)
    min_month = dictionary.get(min_value)

    number_of_sales = len(sales)
    average_sales_value = total / number_of_sales

    print('The max month is: {}'.format(max_month))
    print('The min month is: {}'.format(min_month))
    print('The max value is: {}'.format(max_value))
    print('The min value is: {}'.format(min_value))
    print('The average value is: {}'.format(average_sales_value))


run()
