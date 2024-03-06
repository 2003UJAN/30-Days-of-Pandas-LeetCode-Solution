import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    result = result[['product_id']]
    return result

products_df = pd.DataFrame({
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
})

filtered_products = find_products(products_df)
print(filtered_products)
