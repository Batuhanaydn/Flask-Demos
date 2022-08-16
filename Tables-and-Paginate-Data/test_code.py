from app import db, Stock

stocks = Stock.query.all()

for stock in stocks:
    print(stock.productName + " " + stock.productStore)
    print("Price:" , stock.productPrice)
    print("Stock:" , stock.productStock)
    print("Category:" , stock.productCategory)
    print("Product Code", stock.productCode) # Bunu mantıklı bir algoritmayla ayarlayabiliriz benim yazdığım çalışmadı sanırım
    if stock.productActive:
        print('Activate')
    else:
        print('İnactivate')

    print('---')

