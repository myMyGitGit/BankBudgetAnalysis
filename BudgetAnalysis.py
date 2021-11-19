# -*- coding: utf-8 -*-
# version 1.0 completed program
# V1.01 - minor change to save amounts as ABS()
# V1.02 - fixed month divisor error
# V1.2 - major change: remove class structure from dictionary, implement Dictionary methods for json and pandas methods to convert json to dataframe


import json
import pandas as pd
import os
import sys, getopt


def GenerateDictionary(Descriptn, Amount):

    etype = Descriptn[:9]
    expenseType = ExpenseDict.get(etype, Descriptn[:20])
    x = thisDict.get(expenseType, 'None')
    if (x == 'None'):
        thisDict.update({expenseType: Amount})
    else:
        x += Amount
        thisDict.setdefault(expenseType, x)




os.chdir("C:\\Development\\BankBudgetAnalysis")
thisDict = {}

ExpenseDict = {
    "JEWEL OSC": "FOOD",
    "MARIANOS ": "FOOD",
    "PPD  BANN": "INSURANCE",
    "PPD  Blue": "INSURANCE",
    "PPD  BMO ": "INSURANCE",
    "PPD  CMS ": "INSURANCE",
    "PPD  COMC": "CABLE",
    "PPD  COME": "UTILITY",
    "PPD  GENW": "INSURANCE",
    "PPD  Illi": "UTILITY",
    "PPD  IRS ": "TAX",
    "PPD  SAFE": "INSURANCE",
    "PPD  VERI": "CELL",
    "PPD  VILL": "UTILITY",
    "THE FRESH": "FOOD",
    "TRADER JO": "FOOD",
    "WEB  BCBS": "INSURANCE",
    "WEB  CHAS": "CREDIT-CARD",
    "WEB  DENT": "DENTAL",
    "WEB  DISC": "CREDIT-CARD",
    "WEB  PROT": "INSURANCE",
    "WEB  VIST": "VISTA"}

# =============================================================================
#
# x = ('Amount','Count')
# y = 0
# thisdict = dict.fromkeys(x, y)
#
# =========================================================================
# @@ filenames should be based on the input filename passed as argument
filename = "" # starting values
numMonths = 0
try:
   opts, args = getopt.getopt(sys.argv[1:],"i:m:",["inputfile=","numMonhs="])

except getopt.GetoptError:
      print ('test.py -i <inputfile> -m <numberofmonths>')
      sys.exit(2)

for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        filename = arg
    elif opt in ("-m", "--numMonths"):
        numMonths = int(arg)
if len(filename)==0 or numMonths==0:
    print("No file name or no number of months provided")
    sys.exit(2)
 # filename = "Bank_qtr1-2"
if filename.endswith('.csv'):
    filename = filename.replace('.csv','')

ExcelOutput = filename + "_MonthlyExpenses.xlsx"
MonthlyQtr = filename + '_' + str(numMonths) + '_Months'    # this is the sheet name inside the xls file
 # numMonths = 6
# "Bank_3qtrs.csv"
df = pd.read_csv(filename + '.csv')
for index in df.index:
    if (df.loc[index, 'Sign'] == 'Debit'):
        GenerateDictionary(df.loc[index, 'Description'], df.loc[index, 'Amount'])
# =============================================================================
#         print(df.loc[index,'Description'])
#         print(df.loc[index,'Amt'])
# =============================================================================

# nwdf = pd.DataFrame.from_dict(thisDict, orient='index', dtype=object)

#
jsonString = json.dumps(thisDict)
# jMapper = '{\"Expense\":EXP,\"Amount\":AMT}'
#
# for x in thisDict:
#     expType ="[["+ thisDict[x].Exp+"]]"
#     expAmt = abs(thisDict[x].Amt)
#     expType = expType.replace("[[","\"").replace("]]","\"")
#     jsonString = jsonString+jMapper.replace("EXP",expType).replace("AMT", str(int(expAmt/numMonths)))+","
# # at very end tack on []
# jsonString = "[" + jsonString + "]"
# jsonString = jsonString.replace(",]", "]")

print (jsonString)
nwdf = pd.read_json(jsonString, orient='index')
writer = pd.ExcelWriter(ExcelOutput)

nwdf.to_excel(writer, MonthlyQtr)
# save the excel file
writer.save()
writer.close()



