import argparse
import pandas as pd

def process_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df["Measurement Timestamp"] = pd.to_datetime(df["Measurement Timestamp"])
    df["Date"] = df["Measurement Timestamp"].dt.date

    
    daily_summary = (
        df.groupby(["Station Name", "Date"])
        .agg(
            Start_Temperature=("Air Temperature", lambda x: x.iloc[0]),
            End_Temperature=("Air Temperature", lambda x: x.iloc[-1]),
            High_Temperature=("Air Temperature", "max"),
            Low_Temperature=("Air Temperature", "min"),
        )
        .reset_index()
    )

    
    daily_summary.to_csv(output_file, index=False)
    print(f"Daily temperature aggregates saved to {output_file}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Aggregate hourly temperature data into daily statistics.")
    parser.add_argument("input_file", help="Path to the input CSV file with hourly temperature data.")
    parser.add_argument("output_file", help="Path to save the output CSV file with daily aggregates.")

    
    args = parser.parse_args()

    
    process_csv(args.input_file, args.output_file)
