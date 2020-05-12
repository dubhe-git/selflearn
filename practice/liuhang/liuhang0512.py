import openpyxl 
wb=openpyxl.load_workbook('practice/liuhang/source.xls')
wb.active
sheet = wb['委托代征明细报告表']
# sheet.title
# sheet.title='new title'
# sheet['A1'] = '漫威宇宙'
# rows= [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]
# for i in rows:
#     sheet.append(i)
# print(sheet)
# wb.save('Marvel.xlsx')
print(sheet.title())