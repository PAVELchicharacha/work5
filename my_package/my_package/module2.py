from my_package.my_package.module1 import filename_f

filename_c = 'file_c.txt'#запись
filename_v = 'file_v.txt'#запись большими буквами

#запись
with open(filename_c,'w',encoding='utf-8')as file_c:
    user_text=input("enter words")
    file_c.write(user_text)

#запись большими буквами
with open(filename_c,'r') as file_c,open(filename_v,'w',encoding='utf-8')as file_v:
    for line in file_c:
        file_v.write(user_text.upper())
