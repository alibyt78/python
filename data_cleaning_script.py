import pandas as pd

def clean_data(file_path, output_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data('dirty_data.csv', 'clean_data.csv')
    print("Data cleaned successfully.")
