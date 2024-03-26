import csv
import sys
import unittest

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