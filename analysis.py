import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

from data_preprocessing import save_to_excel


# Define a function to find similar items based on purchase history
def find_similar_items(data, item_name):
    print("you add to cart:" + item_name)
    print("You may also be interested in buying:")
    # Step 1: Find unique BillNo for the specified Itemname
    similar_billNo = data[(data["Itemname"] == item_name)]["BillNo"].unique()

    # Step 2: Filter data for items purchased in the same BillNo
    similar_billNo_recs = data[data["BillNo"].isin(similar_billNo)]["Itemname"]

    # Step 3: Calculate the frequency of each item in the similar BillNo
    similar_billNo_recs = similar_billNo_recs.value_counts() / len(similar_billNo)

    # Step 4: Keep items with a frequency greater than 10%
    similar_billNo_recs = similar_billNo_recs[similar_billNo_recs > .10]

    # Step 5: Filter all data for items purchased in the similar BillNo
    all_billNo = data[data["Itemname"].isin(similar_billNo_recs.index)]
    all_billNo_recs = all_billNo["Itemname"].value_counts() / len(all_billNo["Itemname"].unique())

    # Step 6: Concatenate the similar and all data
    rec_percetages = pd.concat([similar_billNo_recs, all_billNo_recs], axis=1)

    # Step 7: Rename columns
    rec_percetages.columns = ["similar", "all"]

    # Step 8: Calculate the score based on the frequency
    rec_percetages["score"] = rec_percetages["similar"] / rec_percetages["all"]

    # Step 9: Sort the data by score in descending order
    rec_percetages = rec_percetages.sort_values("score", ascending=False)

    # Step 10: Reset index and select the top 5 similar items
    return rec_percetages.reset_index().loc[1:5, "Itemname"]


def Frequency_purchases_by_bill_no(data):
    # Assuming 'data' is your DataFrame with columns 'BillNo', 'Itemname', 'Quantity'

    # Drop duplicate rows to ensure each product pair is counted only once per BillNo
    unique_purchases = data[['BillNo', 'Itemname']].drop_duplicates()

    # Transform the data into a binary matrix (1 if an item was purchased in a transaction, 0 otherwise)
    basket = pd.crosstab(unique_purchases['BillNo'], unique_purchases['Itemname']).applymap(lambda x: 1 if x > 0 else 0)

    # Apply Apriori algorithm to find frequent itemsets
    frequent_itemsets = apriori(basket, min_support=0.02, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    # Print the top rules
    # Define the filtering criteria
    criteria = {

        'confidence': 0.50,
        'lift': 1,
        'leverage': 1,
        'conviction': 2,
        'zhangs_metric': 0.95
    }

    # Apply the filtering criteria
    filtered_rules = rules[

        (rules['confidence'] >= criteria['confidence']) &
        (rules['lift'] >= criteria['lift']) &
        (rules['leverage'] >= criteria['leverage']) &
        (rules['conviction'] >= criteria['conviction']) &
        (rules['zhangs_metric'] >= criteria['zhangs_metric'])
        ]

    save_to_excel(filtered_rules, 'Data/processed_data/test.xlsx')
