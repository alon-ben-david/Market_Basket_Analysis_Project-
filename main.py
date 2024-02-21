# This is a sample Python script.
from data_preprocessing import *
from Data_Visualization_Charts import *
from analysis import *
from gui import MainApp


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    filePath = 'Data/raw_data/Consumer Behaviour_Data.xlsx'
    train_data = filereader(filePath)
    data = train_data.copy()
    top_sellers = data.groupby('Itemname')['Quantity'].sum().nlargest(10).reset_index()


    productList = data[['Itemname', 'Price']]

    print(productList.head())
    save_to_excel(productList, 'Data/processed_data/product_List.xlsx')

    # Print the top 5 best-selling items
    print(top_sellers[['Itemname', 'Quantity']].head(10))
    app = MainApp()
    app.mainloop()
    # All_Purchases, with_CustomerID, without_CustomerID = dataPreprocessing()
    # save_to_excel(All_Purchases, 'Data/processed_data/All_Purchases.xlsx')
    # save_to_excel(with_CustomerID, 'Data/processed_data/with_CustomerID.xlsx')
    # save_to_excel(without_CustomerID, 'Data/processed_data/without_CustomerID.xlsx')
    # visualize_all(data)
    print()
    print(find_similar_items(data, "MEDIUM CERAMIC TOP STORAGE JAR"))
    # Frequency_purchases_by_bill_no(All_Purchases)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
