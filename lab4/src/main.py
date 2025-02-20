import os
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data
from preprocess import handle_missing_values, encode_features, scale_features

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        print("🚀 Loading data...")
        df = load_data(os.path.join(base_dir, "../../data/cab_rides.csv"), 
                       os.path.join(base_dir, "../../data/weather.csv"),
                       sample_fraction=0.1)  # Randomly sample 10% of the data
        
        print("🎉 Data loaded successfully!")

        # Handle missing values
        df = handle_missing_values(df)
        
        # Encode categorical features
        df = encode_features(df)
        
        # Scale numerical features
        feature_cols = ["price", "surge_multiplier"]  # Add other numerical features as needed
        df = scale_features(df, feature_cols)
        
        # Save the processed DataFrame to a CSV file
        output_csv_path = os.path.join(base_dir, "processed_data.csv")
        df.to_csv(output_csv_path, index=False)
        print(f"✅ Data saved to {output_csv_path}")

        # Visualization: Plotting the distribution of 'price'
        plt.figure(figsize=(10, 6))
        plt.hist(df['price'], bins=30, color='blue', alpha=0.7)
        plt.title('Distribution of Cab Ride Prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(os.path.join(base_dir, "../../data/price_distribution.png"))  # Save the plot
        plt.show()  # Display the plot

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 