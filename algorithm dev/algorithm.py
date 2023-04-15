import pandas as pd
import matplotlib.pyplot as plt


def preprocess(filename):
    """
    Takes a csv file and turns it into a dataframe

    Parameters:
        filename (csv): a csv file of your data

    Returns:
        df (dataframe): a dataframe
    """
    df = pd.read_csv(filename, header=0, index_col=0)
    return df

sample_temperatures = [20.1, 21.3, 22.4, 24.5, 26.0, 27.1, 28.2, 27.8, 25.6, 23.5, 22.2, 21.5, 
                       20.9, 20.5, 20.1, 19.8, 19.4, 19.2, 19.0, 18.8, 18.6, 18.5, 18.4, 18.3]
sample_solar_energy = [0.0, 0.2, 0.4, 1.1, 2.2, 3.5, 4.8, 5.0, 4.1, 2.8, 2.1, 1.7, 
                       1.2, 0.7, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
time = list(range(1, 25))



# Create the bar chart
plt.bar(time, sample_solar_energy)
plt.xlabel('Time')
plt.ylabel('Solar Energy in kwh')
plt.title('Solar Energy in kwh against time')
plt.show()
