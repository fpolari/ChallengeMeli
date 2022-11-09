order_items = [
                        { "item": 
                            {
                            "id": "MLB1691332726",
				                        "title": "Item test 2",
				                        "category_id": "MLB430121",
				                        "variation_id": 66536467307,
				                        "seller_custom_field": '',
				        "variation_attributes": [
                                        {
						                    "id": "COLOR",
						                    "name": "Cor",
						                    "value_id": "52099",
						                    "value_name": "amarelo"
					                    }
				        ],
                        "warranty": "Sem garantia",
                        "condition": "new",
                        "seller_sku": '',
                        "global_price": '',
                        "net_weight": ''
			                },
			    "quantity": 1,
			    "requested_quantity": {
				"value": 1,
				"measure": "unit"
			 },
			"picked_quantity": '',
			"unit_price": 35,
			"full_unit_price": 35,
			"currency_id": "BRL",
			"manufacturing_days": '',
			"sale_fee": 8.85,
			"listing_type_id": "gold_special",
			"base_exchange_rate": '',
			"base_currency_id": '',
			"element_id": '',
			"bundle": '',
			"discounts": ''
		}
	]

print(order_items[0]["item"]["id"])
print("")
#print(order_items[0]["item"]["variation_attributes"])

atributos = order_items[0]["item"]["variation_attributes"]

for datos in atributos:
    print(f'{datos["value_name"]}')

import json
import csv

if __name__ == '__main__':
    #url = 'https://6f008c57-99e0-4a2e-8d80-782a71cf99db.mock.pstmn.io/orders/orders.json'
    #response = requests.get(url)
    #print(response.url)


#if response.status_code == 200:
    """
    response_json = response.json()
    id =  response_json['id']
    print(id)
    """
    """

    n_file = open ('test1.csv','w')
    with n_file:
            writer = csv.writer(n_file)
            writer.writerows(origin)

            
    response_json =  json.loads(response.text)
    origin = response_json['order_items']
    #print(origin)


    print("Escritura OK")

#myData = [["col_id" ,  "col_item"],
#                 [orders['order_items'.keys('id')] ] ]
                
"""
#for fin_var_prod in list_var_prod:
#    print(f'{fin_var_prod["value_name"]}')
