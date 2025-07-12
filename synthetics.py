import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler

# Configuration
NUM_USERS = 80
MIN_DATES = 25
MAX_DATES = 30
DATE_START = datetime(2025, 7, 1)
DATE_END = datetime(2025, 7, 31)
np.random.seed(42)
random.seed(42)

# Generate user IDs
user_ids = [f"U{str(i + 1).zfill(3)}" for i in range(NUM_USERS)]
date_range = pd.date_range(DATE_START, DATE_END)

# Generate user-date combinations
user_date_rows = []
for uid in user_ids:
    n_dates = random.randint(MIN_DATES, MAX_DATES)
    selected_dates = sorted(random.sample(list(date_range), n_dates))
    for date in selected_dates:
        user_date_rows.append((uid, date.strftime("%Y-%m-%d")))

base_df = pd.DataFrame(user_date_rows, columns=["user_id", "date"])
n_rows = len(base_df)

# 1. Typing + Mouse Features
typing_mouse_df = base_df.copy()
typing_mouse_df["mean_hold"] = np.round(np.random.uniform(0.05, 0.3, n_rows), 3)
typing_mouse_df["std_flight"] = np.round(np.random.uniform(0.01, 0.15, n_rows), 3)
typing_mouse_df["min_dd"] = np.round(np.random.uniform(0.01, 0.1, n_rows), 3)
typing_mouse_df["max_dd"] = np.round(np.random.uniform(0.05, 0.3, n_rows), 3)
typing_mouse_df["mean_speed"] = np.round(np.random.uniform(100, 1200, n_rows), 1)
typing_mouse_df["max_speed"] = np.round(np.random.uniform(300, 2500, n_rows), 1)
typing_mouse_df["speed_std"] = np.round(np.random.uniform(50, 800, n_rows), 1)
typing_mouse_df["idle_time"] = np.round(np.random.uniform(0, 20, n_rows), 2)
typing_mouse_df["click_rate"] = np.round(np.random.uniform(0.2, 2.0, n_rows), 2)
typing_mouse_df["path_length"] = np.round(np.random.uniform(200, 5000, n_rows), 1)
typing_mouse_df["duration"] = np.round(np.random.uniform(10, 120, n_rows), 1)

# 2. Screen Features
screen_df = base_df.copy()
screen_df["total_screen_time"] = np.round(np.random.uniform(60, 600, n_rows), 1)
screen_df["num_sessions"] = np.random.randint(1, 20, n_rows)
screen_df["num_breaks"] = np.random.randint(0, 15, n_rows)
screen_df["num_night_sessions"] = np.random.randint(0, 5, n_rows)
screen_df["avg_session_duration"] = np.round(
    screen_df["total_screen_time"] / (screen_df["num_sessions"] + screen_df["num_night_sessions"]), 1
)
screen_df["night_ratio"] = np.round(
    screen_df["num_night_sessions"] / screen_df["num_sessions"], 2
)

# 3. Voice Features (placeholders)
voice_df = base_df.copy()

emotion_labels = ["ANG", "DIS", "FEA", "HAP", "NEU", "SAD"]
# Emotion → Fatigue score mapping
emotion_to_range = {
    "ANG": (1.5, 3.0),
    "DIS": (5.5, 6.0),
    "FEA": (4.3, 5.0),
    "HAP": (3.5, 4.0),
    "NEU": (4.8, 5.3),
    "SAD": (6.0, 6.5)
}
voice_df["emotion"] = np.random.choice(emotion_labels, size=len(voice_df))

# Assign fatigue score based on emotion
def assign_fatigue(emotion):
    low, high = emotion_to_range.get(emotion, (4.0, 5.0))
    return np.round(np.random.uniform(low, high), 2)

voice_df["voice_score"] = voice_df["emotion"].apply(assign_fatigue)

# Save CSVs
typing_mouse_df.to_csv("typing_input.csv", index=False)
screen_df.to_csv("screen_input.csv", index=False)
voice_df.to_csv("voice_input.csv", index=False)

print("✅ Synthetic input CSVs generated!")



# Load the three input files
typing_df = pd.read_csv("typing_input.csv")
screen_df = pd.read_csv("screen_input.csv")
voice_df = pd.read_csv("voice_input.csv")

# Merge on 'user_id' and 'date'
merged_df = typing_df.merge(screen_df, on=["user_id", "date"])
merged_df = merged_df.merge(voice_df, on=["user_id", "date"])

# Save the merged file
merged_df.to_csv("merged_input_dataset.csv", index=False)

print("✅ Merged dataset saved as merged_input_dataset.csv")

#Merging output columns from screen and typing module
merged_df = pd.read_csv("merged_input_dataset.csv")

pritesh_df = pd.read_csv("pritesh_output.csv")  # or use the DataFrame if it's already loaded
pravajya_df= pd.read_csv("pravajya_output.csv")  # or use the DataFrame if it's already loaded

# 1. Extract only required columns
screen_cols = pritesh_df[["behavior_score", "usage_label"]].rename(columns={
    "behavior_score": "screen_score",
    "usage_label": "screen_label"
})

typing_cols = pravajya_df[["predicted_label", "top_feature_1", "top_feature_2"]].rename(columns={
    "predicted_label": "typing_label",
    "top_feature_1": "typing_feature_1",
    "top_feature_2": "typing_feature_2"
})

# 2. Concatenate both to your main dataset
merged_df = pd.concat([merged_df, screen_cols, typing_cols], axis=1)
# Save the updated dataset
merged_df.to_csv("merged_input_dataset_updated.csv", index=False)

print("done***")

df = pd.read_csv("merged_input_dataset_updated.csv")

# Select relevant typing fatigue features
typing_features = ["idle_time", "speed_std", "mean_hold", "max_dd"]

temp_typing = df[typing_features].copy()

# 2. Normalize only in the temp DataFrame
scaler = MinMaxScaler()
temp_typing_scaled = scaler.fit_transform(temp_typing)

# 3. Calculate typing score using normalized values
df["typing_score"] = np.round((
    0.4 * temp_typing_scaled[:, 0] +  # idle_time
    0.3 * temp_typing_scaled[:, 1] +  # speed_std
    0.2 * temp_typing_scaled[:, 2] +  # mean_hold
    0.1 * temp_typing_scaled[:, 3]    # max_dd
) * 10, 2) 

#burnout score calculation
df["burnout_score"] = (
    0.3 * df["typing_score"] +
    0.4 * df["voice_score"] +
    0.3 * df["screen_score"]
).round(2)

df.to_csv("synthetic_output_final.csv", index=False)

print("✅ Typing fatigue score calculated and normalized.")



