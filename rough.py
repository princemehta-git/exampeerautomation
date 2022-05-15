# from openpyxl import load_workbook
# import pandas as pd
#
# wb = load_workbook('excels_weekly\\bank\\bank.xlsx')
# wsh = wb.get_sheet_by_name('sheet4')
# max_row = wsh.max_row
# for row in range(2, max_row+1):
#     # print(row)
#     if wsh.cell(row = row, column = 18).value != None:
#         wsh.cell(row = row, column = 18).value = 1
# wb.save('excels_weekly\\temp\\bank.xlsx')



import glob

# # getting excel files to be merged from the Desktop
path = 'C:\\Users\\PRINCE MEHTA\\PycharmProjects\\Rough_automation\\excels_weekly\\temp'

filenames = glob.glob(path + "\*.xlsx")

import os
import win32com.client as client

excel = client.Dispatch("excel.application")


for file in filenames:
    # file = os.path.abspath(file)
    filename, fileextension = os.path.splitext(file)
    wb = excel.Workbooks.Open(filename)
#     output_path = os.getcwd() + "/new version/" + filename
    filename = "ready_excels_weekly\\" + file.split('\\')[-1].strip('.xlsx') + '.xls'
    wb.SaveAs (filename, 56)
    wb.Close()
excel.Quit()

