"""
数据定义的类
"""


class Record:
    def __init__(self, date, order_id, money, province) -> None:
        self.date: str = date  # 订单日期
        self.order_id: str = order_id  # 订单id
        self.money: int = money  # 订单金额
        self.province: str = province  # 销售金额

    def __str__(self) -> str:
        return f"{self.date},{self.order_id},{self.money},{self.province}"
