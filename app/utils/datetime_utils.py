from datetime import datetime

def current_timestamp_iso() -> str:
    """Get current timestamp in ISO format"""
    return datetime.utcnow().isoformat() + "Z"