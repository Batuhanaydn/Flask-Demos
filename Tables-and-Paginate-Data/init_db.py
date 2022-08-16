from datetime import date
from app import db, Stock

db.drop_all()
db.create_all()
number = 10000000000000000
p_code = Stock.productCategory + str(number) 

product_one = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_two = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productCategory="Mesrubat",
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productRate=5   
)
product_three = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_four = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_five = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_six = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_seven = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_eight = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_nine = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_ten = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_eleven = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_twelve = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_thirteen = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_fourteen = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
product_fifteen = Stock(productName='Türk Kahvesi',
                    productStock=14000,
                    productStore="ÖZBİRLİK KAHVE",
                    productCredit="Burası Kredi kartı detayları demo dosyası özelinde yazılmayacaktır.",
                    productDiscount=12,
                    productCode=str(p_code),
                    productPrice=96,
                    productPercent=9,
                    productActive=True,
                    productCategory="Mesrubat",
                    productRate=5   
)
db.session.add_all([product_one,product_two,product_three,product_four,product_five,
                    product_six,product_seven,product_eight,product_nine,product_ten,
                    product_eleven, product_twelve, product_thirteen, product_fourteen,
                    product_fifteen])

db.session.commit()