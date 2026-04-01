def generate_alert(df):
    alerts = []

    if df is None or df.empty:
        return alerts

    if "fare" in df.columns and df["fare"].max() > 90000:
        alerts.append("High Fare Detected")

    if len(df) > 100:
        alerts.append("High Traffic Volume")

    return alerts