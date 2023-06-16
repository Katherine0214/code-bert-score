'''
Description: 
version: 2.0
Author: Can Zhang
Date: 2023-06-14  
'''

from transformers import AutoTokenizer, AutoModel
import torch
import linecache
import xlwt

################################################## CodeCompletion ##############################################
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.cuda.set_device(1)


filename = 'query.txt'
file = open(filename,'r',encoding ='utf-8') 
countline_query = len(file.readlines())

pred = xlwt.Workbook()
pred_sheet = pred.add_sheet('Sheet1')
myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')

tokenizer = AutoTokenizer.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True).half().to(device)


task = "Please complete the following code and give only the next line of code: "
for i in range(1, countline_query + 1):
    code_query = linecache.getline(filename, i)
    query =  task + code_query 
    response, history = model.chat(tokenizer, query, history=[])    
    print(response)
    
    pred_sheet.write(i,0,response)  
pred.save('pred.xls')     



 












# ################################################## CodeSummarization ##############################################
# device = "cuda" if torch.cuda.is_available() else "cpu"
# torch.cuda.set_device(1)


# filename = 'query.txt'
# file = open(filename,'r',encoding ='utf-8') 
# countline_query = len(file.readlines())

# pred = open("pred.txt",'a',encoding ='utf-8') #创建写入的文件

# tokenizer = AutoTokenizer.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True).half().to(device)


# task = "Please give a short description of all the functions of the following code in no more than 100 words in English: "
# for i in range(1, 89):    # 90
#     code_query = linecache.getline(filename, i)
#     query =  task + code_query 
#     response, history = model.chat(tokenizer, query, history=[])    
#     print(response)
    
#     pred.write(response + '\n')  # + '\n'
# pred.close()    


