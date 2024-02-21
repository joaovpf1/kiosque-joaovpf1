from management.product_handler import get_product_by_id


def calculate_tab(table_products):
    table_amount = 0
    for item in table_products:
        product = get_product_by_id(item["_id"])
        table_amount += product.get("price") * item["amount"]
    return {"subtotal": f"${round(table_amount, 2)}"}
