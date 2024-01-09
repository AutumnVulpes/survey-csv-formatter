# Transforming KS Backer Survey Response for Fulfilment

1.  Initial KS file is sorted by backer number
2.  Just to check, sweep initial CSV for bad cells/entries
    1.  Eg. Missing data from name, address, etc and throw up where errors were encountered for manual inspection
3.  Sort by backer tier
4.  Format the new blank csv for fulfillers with appropriate headers
    1.  Warehouse, Ref No, Name, etc
5.  One loop per tier
    1.  Adding the base items of that tier per backer (Eg, Only AP box for basic, or box + zine + coins for bundle tier)
    2.  For each backer, check for addons and add
        1.  If person with bundle added on more coins/zine, increment the existing qty by 1
6.  Note: Each individual item must be assigned it's own row (ie only 1 product SKU per row constraint)
    1.  Therefore, bundle would take 3 rows (base game, coins, zine)
