THRESHOLD = 5000
TAX_RATE = 0.03
SPECIAL_RATIO = 0.24

PER_BABY_DEDUCTION = 2000
PER_ELDER_DEDUCTION = 3000
PER_CHILD_DEDUCTION = 2000



income = float(input("请输入您的税前收入："))
baby_num = int(input("请输入家中3岁以下婴幼儿人数："))
elder_num = int(input("请输入家中60岁以上老人人数："))
child_num = int(input("请输入接受教育的子女人数："))



special_deduction = income * SPECIAL_RATIO

additional_deduction = (
    baby_num * PER_BABY_DEDUCTION
    + elder_num * PER_ELDER_DEDUCTION
    + child_num * PER_CHILD_DEDUCTION
)


taxable_income = max(
    0,
    income
    - THRESHOLD
    - special_deduction
    - additional_deduction
)


tax = taxable_income * TAX_RATE


real_income = income - special_deduction - tax



print(f"应纳税所得额：{taxable_income:.2f} 元")
print(f"需缴纳个税：{tax:.2f} 元")
print(f"税后收入：{real_income:.2f} 元")

#简单给教科书上的源代码优化了一下，其次就是说，我实在是没搞懂手抄代码到作业本上对计算机学习有什么意义，处处透露着形式主义的味道
