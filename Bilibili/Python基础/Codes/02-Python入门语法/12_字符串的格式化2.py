"""
演示第二种字符串格式化的方式: f"{占位}"(不做精度限制 可以传导任意类型数据)
"""

name = "传智播客"
setup_year = 2006
stock_price = 19.99
# f: format
print(f"我是{name},我成立于{setup_year}年,我今天的股价是:{stock_price}")
