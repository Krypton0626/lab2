# Lab 2 - Sampling and Feature Engineering

## 1. Sampling and Labeling Training Data in Python

### Introduction

This lab explores various statistical sampling techniques using Python and Scikit-Learn. The goal is to understand different sampling strategies and their impact on data representation and model performance. The lab also incorporates a Tkinter-based labeling tool to manually annotate data. I selected the **Uber_Lyft_Fare_Prediction dataset** and had to preprocess the dataset by merging `weather.csv` and `cab_rides.csv` to create an optimal working dataset.

### Implemented Sampling Methods

I've implemented four sampling methods for Lab 3 work's extension:

- **Stratified Sampling:** Ensures proportional representation of different price ranges.
- **Random Sampling:** Selects records randomly without grouping.
- **Cluster Sampling:** Selects entire clusters (e.g., data grouped by source).
- **Systematic Sampling:** Selects every k-th record for training.

### Implementing the Tkinter Labeling Tool

The labeling tool provides an interface to manually classify records as "Valid" or "Invalid."

![TKinter Labelling Tool](/lab2_Images/tkinter_labelling_tool.png)

### Errors Encountered & Resolutions

- **Issue:** Initially, multiple Tkinter windows were opening for different sampling methods, which was cumbersome.
- **Resolution:** Consolidated all sampling data and displayed them in separate tabs within a single Tkinter window.

### Tkinter Interface

- This is the Tkinter-based labeling tool, where different sampling methods are displayed in separate tabs.
- We can select from a range of 5 randomly sampled data transactions showcasing ride transits and their prices.
- We can label them as Valid/Invalid for all four sampling methods.
- Based on our selection, it will save the manually labeled data into a CSV file along with the data transactions showcasing ride transits and their prices.

![TKinter Interface](/lab2_Images/tkinter_interface.png)
_Figure 2: Tkinter Interface_

### Conclusion

This lab successfully implemented various sampling techniques and built a manual labeling tool. The comparison of sampling techniques highlights the importance of choosing the appropriate method for data representation. Future extensions could involve automated labeling techniques or integrating active learning models.

---

## 2. Feature Engineering Techniques with Python

### Introduction

This lab explores various feature engineering techniques using Python and Scikit-Learn. The goal is to improve model performance by handling missing values, encoding categorical variables, and scaling numerical features. I implemented the following **feature engineering techniques** to enhance model quality:

- **Handling Missing Data:** Filled missing values using median and mean imputation.
- **Encoding Categorical Features:** Applied one-hot encoding to categorical variables (cab_type, name, source, destination).
- **Scaling Numerical Features:** Standardized numerical columns (price, surge_multiplier) using Scikit-Learn's StandardScaler.

### Feature Engineering

To enhance the data quality for Lab 4, I performed:

- **Missing Data Imputation:**
  - Price values were filled using **median imputation**.
  - Other numerical columns were filled using **mean imputation**.
- **One-Hot Encoding:** Converted categorical features into machine-readable formats using **one-hot encoding**.
- **Feature Scaling:** Applied **standardization** to normalize numerical values and improve model efficiency.

![Feature Engineering Process](/lab2_Images/feature_engineering_process.png)
_Figure 3: Feature Engineering Process_

### Errors Encountered & Resolutions

- **Issue:** Data leakage due to incorrect handling of missing values.
- **Resolution:** Missing values were filled before encoding and scaling to prevent inconsistencies.

- **Issue:** Library compatibility issues when applying transformations.
- **Resolution:** Updated dependencies and verified data types before encoding to avoid conflicts.

### Random Sampling Extension

- **Description:** Implemented **10% random sampling** to analyze model efficiency on a smaller dataset.
- **Implementation:** `df = load_data("cab_rides.csv", "weather.csv", sample_fraction=0.1)`
- **Rationale:** This technique aimed to evaluate model robustness while optimizing computation time.

![Random Sampling Implementation](/lab2_Images/random_sampling.png)
_Figure 4: Random Sampling Implementation_

After execution, we get a preprocessed .csv dataset and a distribution of cab ride prices.

![Distribution of Cab Ride Prices](/lab2_Images/distribution_cab.png)
_Figure 5: Distribution of Cab Ride Prices_

- The histogram shows a **right-skewed distribution** of cab ride prices, where most fares are **low-cost**, with a gradual decline in frequency as prices increase.
- The **peak near zero** suggests a high volume of short-distance rides, while the **long tail on the right** indicates fewer premium-priced rides.
- **Negative price values** appear, likely due to **scaling transformations**, requiring further investigation to ensure data accuracy.

### Conclusion

This lab successfully applied **feature engineering techniques**, including handling missing values, encoding categorical features, and scaling numerical variables. The analysis of price distribution highlights **the importance of preprocessing in machine learning workflows**. Addressing **data anomalies and outliers** will further enhance model reliability, paving the way for more robust predictions in real-world ride fare estimation.

---

## GitHub Repo URL:

## References

OpenAI. (2024). _ChatGPT (February 2025 version)_. [OpenAI](https://openai.com)
