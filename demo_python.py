# ################################# lang='python' ###########################
import code_bert_score
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoConfig
import pickle
import pandas as pd
import xlrd


################################################## demo ###################################################
HF_DATASETS_OFFLINE=1 
TRANSFORMERS_OFFLINE=1

tokenizer = AutoTokenizer.from_pretrained("codebert-python", config="codebert-python")
model = AutoModelForMaskedLM.from_pretrained("codebert-python")


# predictions
pred = xlrd.open_workbook("pred.xlsx") #打开excel表格
pred = pred.sheets()[0]    #读取第一个sheet
pred_rows = pred.nrows  #excel文件的行数
pred_cols = pred.ncols  #ecel文件的列数

predictions = []
for rownum in range(0,pred_rows):    #读取行
    for colnum in range(0,pred_cols):    #读取列
        pred_celldata = pred.cell(rownum,colnum).value  #读取单元格数据，数据格式为float，下面判断将整数数据转化为int
        pred_celldata = str(pred_celldata)    #将数据转化为字符串，再对其中的换行符进行处理
        predictions.append(pred_celldata)


# references
refs = xlrd.open_workbook("refs.xlsx") #打开excel表格
refs = refs.sheets()[0]    #读取第一个sheet
refs_rows = refs.nrows  #excel文件的行数
refs_cols = refs.ncols  #ecel文件的列数

references = []
for rownum in range(0,refs_rows):    #读取行
    for colnum in range(0,refs_cols):    #读取列
        ref_celldata = refs.cell(rownum,colnum).value  #读取单元格数据，数据格式为float，下面判断将整数数据转化为int
        ref_celldata = str(ref_celldata)    #将数据转化为字符串，再对其中的换行符进行处理
        references.append(ref_celldata)

# evaluation
precision, recall, F1, F3 = code_bert_score.score(cands=predictions, refs=references, lang='python')
# print(F1)
print(f"System level F1 score: {F1.mean():.3f}")
print(f"System level F3 score: {F3.mean():.3f}")














# ################################################## before_demo ###################################################
# HF_DATASETS_OFFLINE=1 
# TRANSFORMERS_OFFLINE=1

# tokenizer = AutoTokenizer.from_pretrained("codebert-python", config="codebert-python")
# model = AutoModelForMaskedLM.from_pretrained("codebert-python")


# precision, recall, F1, F3 = code_bert_score.score(cands=['math.sqrt(x)'], refs=['x ** 0.5'], lang='python')
# # print(F1)
# print(f"System level F1 score: {F1.mean():.3f}")
# print(f"System level F3 score: {F3.mean():.3f}")