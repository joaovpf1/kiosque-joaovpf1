from menu import products


def get_product_by_id(product_id: int):
    if type(product_id) is not int:
        message = ("product id must be an int")
        raise TypeError(message)
    for item in products:
        if item["_id"] == product_id:
            return item
    return {}


def get_products_by_type(product_type: str):
    if type(product_type) is not str:
        message = ("product type must be a str")
        raise TypeError(message)
    item_filter = []
    for item in products:
        if item["type"] == product_type:
            item_filter.append(item)
    return item_filter


def add_product(menu: list, **product_list: dict):
    last_id = 0
    for item in menu:
        if item["_id"] > last_id:
            last_id = item["_id"]
    product_list["_id"] = last_id+1
    menu.append(product_list)
    return product_list


def menu_report():
    product_count = len(products)
    acumulator = 0
    list_types = {}
    for item in products:
        acumulator += item["price"]
        list_types[item["type"]] = 0
    average_price = acumulator/product_count
    for type in list_types:
        for product in products:
            if type == product["type"]:
                list_types[type] += 1
    return f"Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {max(list_types, key=list_types.get)}"
