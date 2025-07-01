import time
import uuid
from datetime import datetime, timezone

def generate_random_string():
    """Generate a random UUID string."""
    return str(uuid.uuid4())
    
def main():
    random_string = generate_random_string()
    print(f"Generated string: {random_string}")
    
    while True:
        # Get current UTC time with timezone info and milliseconds
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + f"Z"
        print(f"{timestamp}: {random_string}")
        time.sleep(5)

if __name__ == "__main__":
    main()
