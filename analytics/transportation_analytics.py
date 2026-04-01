import pandas as pd
import os
import json

def load_data(path):
    if not os.path.exists(path):
        return pd.DataFrame()

    files = [f for f in os.listdir(path) if f.endswith(".json")]

    data = []
    for file in files:
        file_path = os.path.join(path, file)

        # skip file kosong
        if os.path.getsize(file_path) == 0:
            continue

        try:
            with open(file_path) as f:
                data.append(json.load(f))
        except json.JSONDecodeError:
            # skip file yang lagi ditulis / rusak
            continue

    return pd.DataFrame(data)

# =========================
# PREPROCESS
# =========================
def preprocess(df):
    if df.empty:
        return df

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    return df

# =========================
# METRICS
# =========================
def compute_metrics(df):
    if df.empty:
        return {
            "total_trips": 0,
            "total_fare": 0,
            "top_location": "-"
        }

    return {
        "total_trips": len(df),
        "total_fare": df["fare"].sum(),
        "top_location": df.groupby("location")["fare"].sum().idxmax()
    }

# =========================
# PEAK HOUR
# =========================
def detect_peak_hour(df):
    if df.empty:
        return None

    df["hour"] = df["timestamp"].dt.hour
    return df.groupby("hour").size().idxmax()

# =========================
# VISUALIZATION DATA
# =========================
def fare_per_location(df):
    if df.empty:
        return pd.Series()

    return df.groupby("location")["fare"].sum().sort_values(ascending=False)

def vehicle_distribution(df):
    if df.empty:
        return pd.Series()

    return df.groupby("vehicle_type").size().sort_values(ascending=False)

def mobility_trend(df):
    if df.empty:
        return pd.Series()

    df = df.set_index("timestamp")
    return df["fare"].resample("10S").sum()

# =========================
# ANOMALY DETECTION
# =========================
def detect_anomaly(df):
    if df.empty:
        return pd.DataFrame()

    # contoh: fare tinggi dianggap anomali
    return df[df["fare"] > 80000]