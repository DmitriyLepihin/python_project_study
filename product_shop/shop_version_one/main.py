from product_shop.shop_version_one.utils import opening


def main():
    print('Hello, in our prooduct shop. We have:')
    my_shop = opening()
    for key in my_shop.keys():
        print(key, ':')
        for product, value in my_shop[key].items():
            if product == 'total':
                print('\t', f"{value} sum")
                continue
            print('\t'f"{product}\t{value.get('count')} kg \ton \t{value.get('price')} sum ")


main()
