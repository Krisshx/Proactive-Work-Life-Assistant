#calender_utils.py

def get_mock_availability():
    return {
        "team": ["krish@company.com", "alex@company.com", "priya@company.com"],
        "free_slots": [
            {"date": "2025-07-22", "time": "19:00-20:30"},
            {"date": "2025-07-23", "time": "20:00-21:00"}
        ]
    }