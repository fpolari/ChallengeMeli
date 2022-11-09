import requests
import csv

url_orders = requests.get('https://6f008c57-99e0-4a2e-8d80-782a71cf99db.mock.pstmn.io/orders/')
url_shipments = requests.get('https://6f008c57-99e0-4a2e-8d80-782a71cf99db.mock.pstmn.io/shipments/')
    
def server_status ():
    if url_orders.status_code == 200:
        response_json = url_orders.json()
        response_json2 = url_shipments.json()
    else:
        return "Mensaje del Servidor: ",url_orders.status_code   

if __name__ == '__main__':
    server_status();
    json_data_orders = url_orders.json()
    json_data_ships = url_shipments.json()

#Campos Orders
id_order = json_data_orders["id"]
id_item = json_data_orders["order_items"][0]["item"]["id"]
des_prod = json_data_orders["order_items"][0]["item"]["title"]
list_var_prod = json_data_orders["order_items"][0]["item"]["variation_attributes"]
find_var_prod = list_var_prod[0]["value_name"]

#Campos Shipments
id_ship = json_data_ships["id"]
estado_ship = json_data_ships["substatus_history"][0]["status"]
s_est_ship = json_data_ships["substatus_history"][0]["substatus"]
tipo_log = json_data_ships["logistic_type"]
direc_calle = json_data_ships["receiver_address"]["address_line"]
direc_ciudad = json_data_ships["receiver_address"]["city"]["name"]
direc_zip = json_data_ships["receiver_address"]["zip_code"]

valor = {}
for tipo_agency in json_data_ships["receiver_address"].keys():
    if tipo_agency == 'agency':
        valor[tipo_agency] = tipo_agency
        
 

myDataOrderShips = [[" ID_ORDEN" ,  "ID_ITEM", "DESCIP_PROD", "ID_ENVIO","ESTADO","SUBESTADO","TIP LOG","DEST ENVIO","DIREC RECP"],
                                 [id_order,id_item,find_var_prod,id_ship,estado_ship,s_est_ship,tipo_log,'',direc_calle + direc_ciudad + direc_zip] ] 
                
file_orders_ships = open ('order_ships.csv','w')
with file_orders_ships:
            writer = csv.writer(file_orders_ships)
            writer.writerows(myDataOrderShips)
print("File Generado")

