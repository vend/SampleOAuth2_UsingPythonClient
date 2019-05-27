from django.db import models
from quickbooks.objects.salesreceipt import SalesReceipt
from quickbooks.objects.detailline import SalesItemLine, SalesItemLineDetail, Ref
import json

sale_json = """[
  {
    "id": "e541c29f-8657-a3be-11e9-802e3ba64743",
    "short_code": "a5bx9l",
    "sale_date": "2019-05-27T15:19:52+12:00",
    "status": "CLOSED",
    "customer_id": null,
    "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
    "user_id": "02dcd191-ae2b-11e6-f485-a54b98a2e27e",
    "invoice_number": "155",
    "invoice_sequence": 155,
    "total_tax": "0.65217",
    "total_price": "4.34783",
    "note": "cash payment single product",
    "receipt_address": "",
    "register_sale_products": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f65",
        "product_id": "product1-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      }
    ],
    "register_sale_payments": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e4abf2d57",
        "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
        "payment_type_id": 1,
        "retailer_payment_type_id": "02dcd191-ae2b-11e6-f485-a54b98a273f4",
        "payment_date": "2019-05-27T15:19:52+12:00",
        "amount": "5",
        "currency": "NZD"
      }
    ]
  },
  {
    "id": "e541c29f-8657-a3be-11e9-802e3ba64743",
    "short_code": "a5bx9l",
    "sale_date": "2019-05-27T15:19:52+12:00",
    "status": "CLOSED",
    "customer_id": null,
    "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
    "user_id": "02dcd191-ae2b-11e6-f485-a54b98a2e27e",
    "invoice_number": "155",
    "invoice_sequence": 155,
    "total_tax": "0.65217",
    "total_price": "4.34783",
    "note": "cash payment two line item, different product and different account code",
    "receipt_address": "",
    "register_sale_products": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f65",
        "product_id": "product1-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      },
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f64",
        "product_id": "product2-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      }
    ],
    "register_sale_payments": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e4abf2d57",
        "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
        "payment_type_id": 1,
        "retailer_payment_type_id": "02dcd191-ae2b-11e6-f485-a54b98a273f4",
        "payment_date": "2019-05-27T15:19:52+12:00",
        "amount": "10",
        "currency": "NZD"
      }
    ]
  },
  {
    "id": "e541c29f-8657-a3be-11e9-802e3ba64743",
    "short_code": "a5bx9l",
    "sale_date": "2019-05-27T15:19:52+12:00",
    "status": "CLOSED",
    "customer_id": null,
    "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
    "user_id": "02dcd191-ae2b-11e6-f485-a54b98a2e27e",
    "invoice_number": "155",
    "invoice_sequence": 155,
    "total_tax": "0.65217",
    "total_price": "4.34783",
    "note": "cash payment two line item 2 different product, same code",
    "receipt_address": "",
    "register_sale_products": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f65",
        "product_id": "product2-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      },
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f64",
        "product_id": "product3-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      }
    ],
    "register_sale_payments": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e4abf2d57",
        "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
        "payment_type_id": 1,
        "retailer_payment_type_id": "02dcd191-ae2b-11e6-f485-a54b98a273f4",
        "payment_date": "2019-05-27T15:19:52+12:00",
        "amount": "10",
        "currency": "NZD"
      }
    ]
  },
  {
    "id": "e541c29f-8657-a3be-11e9-802e3ba64743",
    "short_code": "a5bx9l",
    "sale_date": "2019-05-27T15:19:52+12:00",
    "status": "CLOSED",
    "customer_id": null,
    "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
    "user_id": "02dcd191-ae2b-11e6-f485-a54b98a2e27e",
    "invoice_number": "155",
    "invoice_sequence": 155,
    "total_tax": "0.65217",
    "total_price": "4.34783",
    "note": "cash payment two line item  same product, same code",
    "receipt_address": "",
    "register_sale_products": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f65",
        "product_id": "product2-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      },
      {
        "id": "e541c29f-8657-a3be-11e9-802e43390f64",
        "product_id": "product2-id",
        "price": 4.34783,
        "price_set": 0,
        "discount": 0,
        "tax": "0.65217",
        "tax_id": "02dcd191-ae2b-11e6-f485-a54b9896a941",
        "quantity": "1",
        "sequence": 0,
        "status": "SAVED",
        "attributes": [{ "name": "line_note", "value": "" }]
      }
    ],
    "register_sale_payments": [
      {
        "id": "e541c29f-8657-a3be-11e9-802e4abf2d57",
        "register_id": "02dcd191-ae2b-11e6-f485-a54b98a1d0bc",
        "payment_type_id": 1,
        "retailer_payment_type_id": "02dcd191-ae2b-11e6-f485-a54b98a273f4",
        "payment_date": "2019-05-27T15:19:52+12:00",
        "amount": "10",
        "currency": "NZD"
      }
    ]
  }
]
"""

# Create your models here.

product_to_account_code = {
    "product1-id": 1,
    "product2-id": 2,
    "product3-id": 2
}

sales = json.loads(sale_json)


def function_one(sales):
    sale_receipt = SalesReceipt()
    account_code_tax_code_mapping = {}

    # iterate over the sales to aggregate the line items by account code and tax code
    for sale in sales:
        for line_item in sale["register_sale_products"]:
            account_code = product_to_account_code[line_item["product_id"]]
            tax_code = line_item["tax_id"]

            key = (account_code, tax_code)
            price = float(line_item["price"])
            quantity = float(line_item["quantity"])
            tax = float(line_item["tax"])
            total_amount = (price + tax) * quantity

            if key in account_code_tax_code_mapping:
                account_code_tax_code_mapping[key] += total_amount
            else:
                account_code_tax_code_mapping[key] = total_amount

    for key, value in account_code_tax_code_mapping.items():
        account_code = key[0]
        tax_code = key[1]

        line_item = SalesItemLine()
        line_item.Amount = value
        line_item.Description = "Account code: {} and Tax code: {}".format(account_code, tax_code)


        line_item_detail = SalesItemLineDetail()
        line_item_detail.Qty = 1
        line_item_detail.UnitPrice = value

        item_ref = Ref()
        item_ref.value = account_code
        line_item_detail.ItemRef = item_ref

        tax_code_ref = Ref()
        tax_code_ref.value = tax_code
        line_item_detail.TaxCodeRef = tax_code_ref

        line_item.SalesItemLineDetail = line_item_detail
        sale_receipt.Line.append(line_item)

    print(sale_receipt.to_json())
    return sale_receipt


if __name__ == "__main__":
    function_one(sales)
