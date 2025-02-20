import os
import pandas as pd
from sampling import stratified_sampling, random_sampling, cluster_sampling, systematic_sampling
from labeling_tool import labeling_tool
from data_loader import load_data  

def main():
    # Set the base directory to the current script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        print("🚀 Loading data...")
        df = load_data(os.path.join(base_dir, "../../data/cab_rides.csv"), 
                       os.path.join(base_dir, "../../data/weather.csv")) 
        
        print("🎉 Data loaded successfully!")

        # Comparison of sampling techniques
        sampling_methods = {
            "Stratified Sampling": (stratified_sampling, {"target_col": "price"}),
            "Random Sampling": (random_sampling, {}),
            "Cluster Sampling": (cluster_sampling, {"cluster_col": "source"}),
            "Systematic Sampling": (systematic_sampling, {})
        }

        all_samples = []

        for method_name, (method, params) in sampling_methods.items():
            print(f"📊 Performing {method_name}...")
            try:
                train_set, _ = method(df.copy(), **params)
                # Add sampling method information to the DataFrame
                train_set['sampling_method'] = method_name
                all_samples.append(train_set)
                print(f"🎉 {method_name} complete!")
            except Exception as e:
                print(f"⚠️ {method_name} failed, skipping...")
                continue

        if all_samples:
            combined_samples = pd.concat(all_samples, ignore_index=True)
            print("📝 Launching labeling tool with all sampling methods...")
            labeling_tool(combined_samples)
            print("🎉 Labeling complete!")
        else:
            print("❌ No samples were generated.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 