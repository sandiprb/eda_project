# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


def plot(data):
    data.boxplot(['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice'])
    plt.show()
