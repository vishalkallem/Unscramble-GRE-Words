__author__ = 'Vishal'

import openpyxl as xl
import csv

def convert_csv_to_excel():
    wb = xl.Workbook()
    ws = wb.active
    ws.title = 'Membean Words'

    headings = ['Level', 'Word', 'Meaning']

    with open('Membean_words.csv', 'r') as file:
        for idx, value in enumerate(headings):
            ws.cell(row=1, column=idx+1, value=value)
        for row in csv.reader(file):
            ws.append(row)
    wb.save('Membean_words.xlsx')


if __name__ == '__main__':
    convert_csv_to_excel()
