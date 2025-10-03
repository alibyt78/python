import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_stock(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    df = pd.read_csv(file_path)

    if 'Date' not in df.columns or 'Close' not in df.columns:
        raise ValueError("CSV must contain 'Date' and 'Close' columns.")

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Calculate moving averages
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()

    # Drop rows with NaN values in MA columns for clean plotting
    df.dropna(subset=['MA50', 'MA200'], inplace=True)

    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['MA50'], label='50-Day MA', color='orange')
    plt.plot(df['Date'], df['MA200'], label='200-Day MA', color='red')
    plt.legend()
    plt.title('Stock Price Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.tight_layout()

    # Save the output chart
    plt.savefig('stock_price_analysis.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    analyze_stock('stock_data.csv')
