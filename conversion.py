import csv
import os, glob
import sys
import xlsxwriter

def csv2xlsx(filename):
    # listOfFiles = os.listdir(directory)           #  list of all files in the directory
    listOfFiles = glob.glob(filename)
    for index, fileInList in enumerate(listOfFiles):
        fileName = fileInList[0:fileInList.find('.')]
        excelFile = xlsxwriter.Workbook(fileName + '.xlsx', {'strings_to_urls': False})
        worksheet = excelFile.add_worksheet()
        # with open(fileName + ".csv", 'rb') as f:
        with open(fileInList, 'rt', encoding="utf8") as f:
            content = csv.reader(f)
            for index_row, data_in_row in enumerate(content):
                for index_col, data_in_cell in enumerate(data_in_row):
                    worksheet.write(index_row, index_col, data_in_cell)

    excelFile.close()
    print(" === Conversion is done ===")

if __name__ == '__main__':
   csv2xlsx('file.csv')