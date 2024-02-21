from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.product_handler import menu_report
from menu import products
from management.tab_handler import calculate_tab

new_data = {"description": " dark rustic style. top view.", "price": 30.62, "rating": 5, "title": "dark rustic", "type": "dairy"}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]


if __name__ == "__main__":
    #Seus prints de teste aqui
    print(get_product_by_id(8))
    print(get_products_by_type("dairy"))
    print(add_product(products, **new_data))
    print(calculate_tab(table_2))
    print(menu_report())
