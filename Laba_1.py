import csv
from io import StringIO
from typing import Optional

# Принимает - str
# Возвращает - list[dict]
def parse_csv(data: str) -> list[dict]:
    return list(csv.DictReader(StringIO(data)))

# Принимает - list[dict]
# Возвращает - float
def compute_revenue(rows: list[dict]) -> float:
    return float(
        sum(
            map(
                lambda row:
                    float(row.get("quantity", 0))
                    * float(row.get("price", 0)),
                rows
            )
        )
    )

# Принимает - list[dict]
# Возвращает - dict или None
def top_item(rows: list[dict]) -> Optional[dict]:
    return max(
        rows,
        key=lambda row:
            float(row.get("quantity", 0))
            * float(row.get("price", 0)),
        default=None
    )

#============ Проверка работы функций ===========


data = """date,item,quantity,price
2026-09-01,Apple,10,5.5
2026-09-02,Banana,20,2.0
2026-09-03,Orange,5,8.0
"""

print("Список строк:")
print(parse_csv(data))

print("\nОбщая выручка:")
print(compute_revenue(parse_csv(data)))

print("\nТовар с максимальной выручкой:")
print(top_item(parse_csv(data)))