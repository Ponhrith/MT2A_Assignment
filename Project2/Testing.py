import xlsxwriter 

workbook = xlsxwriter.Workbook('Test2.xlsx')

worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold':1})

headings = ['Continental Region', 'Number of Countries', 'Average price of 1GB(USD)']

data = [
    ["EASTERN EUROPE","ASI(EX.NEAR EAST)","NORTHERN AFRICA","CARIBBEAN","SUB-SAHARAN AFRICA", "NEAR EAST","SOUTH AMERICA",
    "SOUTH AMERICA", "WESTERN EUROPE", "CIS(FORMER USSR)", "NORTHERN AMERICA", "OCEANIA","BALTICS","CENTRAL AMERICA"],
    [14,24,5,7,17,14,10,17,10,2,3,3,7],
    [2.49,2.38,2.37,2.33,2.30,2.30,2.28,2.26,2.25,2.23,2.16,2.01]
]

worksheet.write_row('A1', headings, bold)

worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

chart1 = workbook.add_chart({'type': 'bar'})

chart1.add_series({
    'name':       '= Sheet1 !$B$1',
    'categories': '= Sheet1 !$A$2:$A$7',
    'values':     '= Sheet1 !$B$2:$B$7',
})
 
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 6, 0],
    'values':     ['Sheet1', 1, 2, 6, 2],
})

chart1.set_title({'name': 'AVERAGE PRICE PER CONTINENTAL REGION'})

chart1.set_style(11)

worksheet.insert_chart('E2', chart1)
workbook.close()