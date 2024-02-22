import csv
import sys

# Takes in csv from input file path in command line when code is run
input_csv = sys.argv[1]
ks_response = csv.DictReader(open(input_csv))

# Function to check if backer responded to survey
def is_survey_responder(ks_data_row):
    return bool(row["Shipping Address 1"])

# Function to create a dictionary of each backer's required info
def row_to_backer_dict(ks_data_row):

    temp_dict = {}

    temp_dict = {
        'backer_details' : {},
        'product_skus' : {},
        'remarks' : row["Shipping Delivery Notes"]
        }

    name_parse = row["Shipping Name"].split(" ", 1)
    if len(name_parse) == 1:
        first_name, last_name = row["Shipping Name"], ""
    else:
        first_name, last_name = row["Shipping Name"].split(" ", 1)

    temp_dict['backer_details']['first_name'] = first_name
    temp_dict['backer_details']['last_name'] = last_name
    temp_dict['backer_details']['email'] = row["Email"]
    temp_dict['backer_details']['address_line_1'] = row["Shipping Address 1"]
    temp_dict['backer_details']['address_line_2'] = row["Shipping Address 2"]
    temp_dict['backer_details']['city'] = row["Shipping City"]
    temp_dict['backer_details']['state'] = row["Shipping State"]
    temp_dict['backer_details']['country_code'] = row["Shipping Country Code"]
    temp_dict['backer_details']['zip_code'] = row["Shipping Postal Code"]
    temp_dict['backer_details']['phone'] = row["Shipping Phone Number"]

    temp_dict['product_skus']['AEY-PROP-01'] = (
       int(row["Everything in previous tier"]) + int(row["ARCANA PROPHETIA"])
    )
    temp_dict['product_skus']['AEY-PROP-02'] = (
       int(row["Everything in previous tier"]) + int(row["Additional Metal Sigils"])
    )
    temp_dict['product_skus']['AEY-PROP-03'] = (
       int(row["Everything in previous tier"]) + int(row["Physical Art and Lore Zine"])
    )
    temp_dict['product_skus']['AEY-KAWA-01'] = int(row["KAWA: A Game About Flow"])

    return temp_dict

# Creation of two dictionaries of backer data, one for responders, other for non-responders  
responder_dict = {}
non_response_dict = {}    
for row in ks_response:
  if is_survey_responder(row):
    row_to_backer_dict(row)
    responder_dict[int(row["Backer UID"])] = row_to_backer_dict(row)
  else:
    non_response_dict[int(row["Backer UID"])] = row_to_backer_dict(row)

# Function to convert above dictionaries into lists for csv writing
# Each SKU ordered by each is a new item in list (so backer with SKU A and B is 2 items)    
def collate_backer_dicts_for_output(target_dict):
    temp_list = []

    for backer in target_dict:
        for sku in target_dict[backer]['product_skus']:
            if target_dict[backer]['product_skus'][sku] > 0:

                temp_list.append([])
                csv_row = temp_list[(len(temp_list))-1]

                csv_row.append("HZ02")
                csv_row.append(backer)
                csv_row.append(target_dict[backer]['backer_details']['first_name'])
                csv_row.append(target_dict[backer]['backer_details']['last_name'])
                csv_row.append(target_dict[backer]['backer_details']['address_line_1'])
                csv_row.append(target_dict[backer]['backer_details']['address_line_2'])
                csv_row.append(target_dict[backer]['backer_details']['city'])
                csv_row.append(target_dict[backer]['backer_details']['state'])
                csv_row.append(target_dict[backer]['backer_details']['country_code'])
                csv_row.append(target_dict[backer]['backer_details']['zip_code'])
                csv_row.append(target_dict[backer]['backer_details']['phone'])
                csv_row.append(sku)
                csv_row.append(target_dict[backer]['product_skus'][sku])
                csv_row.append("by Becky")
                csv_row.append(target_dict[backer]['backer_details']['email'])
                csv_row.append(target_dict[backer]['remarks'])

    return temp_list

# Write responder and non-responder lists into csvs
def create_output_csv(new_csv, target_list):
    csvfile = open(new_csv, 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    c.writerow(['Warehouse Name', 'Reference No.', 'Recipient Name',
                'Recipient Address Line 1', 'Recipient Address Line 2', 'Recipient City',
                'Recipient State', 'Recipient Country/Region Code', 'Recipient Zip Code',
                'Recipient Tel', 'SKU', 'Quantity', 'Shipping Method', 'Recipient Email',
                'Special Remarks/Instructions'])

    for row in target_list:
        c.writerow(row)

    csvfile.close()

# Create two output csvs; responders and non-responders
create_output_csv('shipping_info.csv', collate_backer_dicts_for_output(responder_dict))
create_output_csv('non_response.csv', collate_backer_dicts_for_output(non_response_dict))