import kagglehub
import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the environment variable for Kaggle cache directory
os.environ['KAGGLE_CONFIG_DIR'] = current_dir

# Download latest version
path = kagglehub.dataset_download("nih-chest-xrays/data")

print("Path to dataset files:", path)