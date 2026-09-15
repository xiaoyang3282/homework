income=float(input("请输入收入: "))
threshold=5000.0
tax_rate=0.03
special_deduction=income*0.24
expense_deduction=3000.0
tax=(
    income-threshold-special_deduction-expense_deduction)*tax_rate
real_income=income-special_deduction-tax
print("应纳税额: ", tax,"元")
print("实际收入: ", real_income,"元")
#神秘手抄代码
