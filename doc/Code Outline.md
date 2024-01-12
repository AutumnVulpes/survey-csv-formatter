# Transforming KS Backer Survey Response for Fulfilment

1.  Initial KS file is sorted by backer number
    1.  Things to note
        1.  KS Data is in FULL NAME
2.  Just to check, sweep initial CSV for bad cells/entries
    1.  Eg. Missing data from name, address, etc and throw up where errors were encountered for manual inspection
3.  Sort by backer tier
4.  Format the new blank csv for fulfillers with appropriate headers
    1.  Headers
        1.  Warehouse
        2.  Reference Number (Can use backer ID)
        3.  FIRST NAME
        4.  LAST NAME
        5.  Address Line 1
        6.  Address Line 2
        7.  City
        8.  State
        9.  Country/Region Code
        10. Zip Code
        11. Phone
        12. SKU
        13. Quantity
        14. Shipping Method (fill with Becky)
        15. Email
    2.  Notes
        1.  Note: Each individual item must be assigned it's own row (ie only 1 product SKU per row constraint)
            1.  Therefore, bundle would take 3 rows (base game, coins, zine)
        2.  Some recipients have special instruction
        3.  Check if we need inured value
5.  One loop per tier
    1.  Adding the base items of that tier per backer (Eg, Only AP box for basic, or box + zine + coins for bundle tier)
    2.  For each backer, check for addons and add
        1.  If person with bundle added on more coins/zine, increment the existing qty by 1
    3.  Handling of names
        1.  Current proposal: Slice last word as "Last Name", remove space and everything before it as "First Name"
