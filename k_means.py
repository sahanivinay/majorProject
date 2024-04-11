import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import time
import os
import csv

# Function to read data from CSV files in a folder
def read_data_from_folder(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            data.append(df.values)
    return data

# Function to perform k-means clustering
def kmeans_clustering(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids

# Function to evaluate clustering performance using silhouette score
def evaluate_clustering(data, labels):
    silhouette_avg = silhouette_score(data, labels)
    print("Silhouette Score:", silhouette_avg)

# Path to the folder containing CSV files
folder_path = '/home/debian/project/'

# Number of clusters to detect
n_clusters = 3  

# Run clustering continuously
while True:
    try:
        # Read data from CSV files
        data = read_data_from_folder(folder_path)

        # Merge data from all CSV files
        merged_data = pd.concat([pd.DataFrame(d) for d in data], ignore_index=True)

        # Perform feature scaling
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(merged_data)

        # Perform k-means clustering
        labels, centroids = kmeans_clustering(scaled_data, n_clusters)

        # Evaluate clustering performance
        evaluate_clustering(scaled_data, labels)

        # Print cluster labels for each data point
        print("Cluster Labels:")
        print(labels)

    except Exception as e:
        print("Error:", e)

    # Wait for a certain period before checking for updates again
    time.sleep(10)  # Adjust the time interval as needed
