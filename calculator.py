#声明两个用户输入的变量

first_number = input("请输入第一个数字:")
operation = input("请输入运算符:")
second_number = input("请输入第二个数字:")



#开发思路
#两组变量进行运算，可分为四种情况，第一个变量为整数或者浮点数，第二个变量也可为整数或者浮点数，
# 那么有整数和整数，整数和浮点数，浮点数和整数，浮点数和浮点数，
# 因此要判断用户输入的两组变量数值中是否包含浮点数，没有则为整数类型
# 用条件控制语句将其分别进行对应的转换再做运算操作，
# 最后将结果result转换为字符串类型输出结果



#根据有没有"." 判断用户输入数字类型，并进行字符串到数字类型转换
if "." in first_number:
    first_number = float(first_number)
else:
    first_number = int(first_number)

if "." in second_number:
    second_number = float(second_number)
else:
    second_number = int(second_number)

#条件控制部分 根据用户输入的符号执行相应的计算及结果输出，同时对result进行数字到字符串的转换，
# 将整数类型的result转换为字符串类型然后赋值给要输出的result
#运行过程，利用 if条件语句，“==”，判断用户输入的运算符和下列哪一组运算过程的执行条件相符，执行相应的一组代码，
#然后输出结果

if operation == "+":
    result = first_number + second_number
    result = str(result)
    print("加法运算结果="+result)

elif operation == "-":
    result = first_number - second_number
    result = str(result)
    print("减法运算结果="+result)

elif operation == "*":
    result = first_number * second_number
    result = str(result)
    print("乘法运算结果="+result)

elif operation == "/":
    result = first_number / second_number
    result = str(result)
    print("除法运算结果="+result)

elif operation == "%":
    result = first_number % second_number
    result = str(result)
    print("第一个数字除以第二个数字，取模运算结果="+result)

elif operation == "**":
    result = first_number ** second_number
    result = str(result)
    print("第一个数字的'第二个数字'次方，幂运算结果="+result)

elif operation == "//":
    result = first_number // second_number
    result = str(result)
    print("第一个数字除以第二个数字，取整除运算结果="+result)

elif operation == "+=":
    first_number += second_number
    result = str(first_number)
    print("第一个数字加等于第二个数字，运算结果="+result)

elif operation == "-=":
    first_number -= second_number
    result = str(first_number)
    print("第一个数字减等于第二个数字，运算结果="+result)

elif operation == "*=":
    first_number *= second_number
    result = str(first_number)
    print("第一个数字乘等于第二个数字，运算结果="+result)

elif operation == "/=":
    first_number /= second_number
    result = str(first_number)
    print("第一个数字除等于第二个数字，运算结果="+result)

elif operation == "%=":
    first_number %= second_number
    result = str(first_number)
    print("第一个数字模等于第二个数字，运算结果="+result)

elif operation == "**=":
    first_number **= second_number
    result = str(first_number)
    print("第一个数字幂等于第二个数字，运算结果="+result)

elif operation == "//=":
    first_number //= second_number
    result = str(first_number)
    print("第一个数字整除等于第二个数字，运算结果="+result)