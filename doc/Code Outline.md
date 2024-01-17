# Transforming KS Backer Survey Response for Fulfilment

## Introduction

Different companies and businesses often have their own preferred templates for csv (comma seperated value) files, along with differences in the mandatory information required in them. Hence, this program is designed to automatically filter a csv file for empty cells, read and write desired data into a new csv with a different format, and even transform/edit the data depending on the requirements. This will save time, eliminate human error that could occur during manual copying and editing.

This is a self contained solo project, with the requirements to take in an input csv, filter out unwanted data with certain tags and empty cells. Then, read the remaining data to identify what is desired and finally write that into a new csv format which is the output, and needs no further editing.

## Context

In this use case, the program is being used to sort and filter a kickstarter backer survey csv, and prepare it in a template provided by a shipping and fulfilment company. The required fields are: Backer ID, first name, last name, address, city, state, country, zip code, telephone, product SKu to be shipped, and quantity.

Other requirements is that each row can only hold one product SKU at a time, so if a backer has backed at a tier with multiple items, or added them as add-ons, each item would need to be added as a seperate row; Also sorting out backers who have yet to respond to the survey into another csv for future follow up.

Finally, the fulfiller's template would require splitting it into a first and last name. While a model could be trained on a dataset of different names from different cultures and backgrounds in order to accurately read what would be a first and last name, that is outside the scope of this program.

## Design Details

1.  Filter out any backer without items to be shipped.
2.  Save any backer who has items that require shipping but "Survey Response Date" cell is empty to a new csv and output that to track which backers have yet to provide information. Then, remove those rows.
3.  Create dict of lists with all required info in new format.
    1.  For names, simply take the firsst word as first name and the rest as last name.
    2.  For each backer with addons or at a tier with additional items, add another list duplicating all their info except with the new SKU.
4.  Each entry in the intermediate dict gets inserted into the new csv, where each list is a row and each item is an individual cell.

## Alternatives considered \[WIP\]

Use of pandas vs csv only  
Dict of lists vs Dict of dicts  
Why not just read and write directly from input csv to output csv
