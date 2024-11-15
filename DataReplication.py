import pickle
import os

def replicate_data(data, primary_file="primary_data.pkl", secondary_file="secondary_data.pkl"):
    """Replicate data to a secondary storage."""
    with open(primary_file, "wb") as f:
        pickle.dump(data, f)
    with open(secondary_file, "wb") as f:
        pickle.dump(data, f)
    print("Data replicated to secondary storage.")

def recover_data(primary_file="primary_data.pkl", secondary_file="secondary_data.pkl"):
    """Recover data from secondary storage if primary is unavailable."""
    try:
        with open(primary_file, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        with open(secondary_file, "rb") as f:
            return pickle.load(f)

# Simulate data replication and recovery
sample_data = {"important": "This is very important data"}
replicate_data(sample_data)

# Simulate primary data loss
os.remove("primary_data.pkl")
recovered_data = recover_data()
print(f"Recovered data: {recovered_data}")
