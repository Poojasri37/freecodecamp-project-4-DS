import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data(filepath):
    """
    Load the time series data from a CSV file and return a DataFrame.
    """
    df = pd.read_csv(filepath, parse_dates=['date'], index_col='date')
    return df

# Clean and preprocess data
def preprocess_data(df):
    """
    Preprocess the data by filtering out anomalies and preparing it for analysis.
    """
    # Remove data points that are significantly out of the normal range (anomalies)
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    return df

# Visualize the data
def plot_page_views(df):
    """
    Plot the time series data of page views.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['value'], color='skyblue')
    plt.title('Daily Page Views')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

def plot_rolling_mean(df):
    """
    Plot the time series data with a rolling mean to smooth out short-term fluctuations.
    """
    df['rolling_mean'] = df['value'].rolling(window=30).mean()
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['value'], color='skyblue', alpha=0.5, label='Daily')
    plt.plot(df.index, df['rolling_mean'], color='orange', label='30-day Rolling Mean')
    plt.title('Daily Page Views with Rolling Mean')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.legend()
    plt.show()

def plot_monthly_average(df):
    """
    Plot the monthly average of page views.
    """
    df['year'] = df.index.year
    df['month'] = df.index.month
    monthly_avg = df.groupby(['year', 'month'])['value'].mean().unstack()
    monthly_avg.plot(kind='bar', figsize=(14, 7))
    plt.title('Monthly Average Page Views')
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# Main function
if __name__ == "__main__":
    # Load and preprocess data
    df = load_data('page_views.csv')
    df = preprocess_data(df)

    # Visualize data
    plot_page_views(df)
    plot_rolling_mean(df)
    plot_monthly_average(df)
