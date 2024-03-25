"""
Date: 2024/3/25 19:10

Author: Fengchunyang

Contact: fengchunyang

Record:
    2024/3/25 Create file.

"""
import datetime


def get_month_days(date=None):
    """获取指定日期所属月的总天数

    Args:
        date(str): 日期: YYYY-MM-DD，如果不传则使用当前日期

    Returns:
        days(int): 所属月的总天数
    """
    date = datetime.datetime.strptime(date, "%Y-%m-%d") if date else datetime.date.today()

    current_month = date.month

    while current_month == date.month:
        date = date + datetime.timedelta(days=1)

    last_day_of_month = date - datetime.timedelta(days=1)
    return last_day_of_month.day




