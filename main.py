from datetime import datetime
import os

def print_something_now():

    now = datetime.now()
    
    print(f"something logged at: {now}.\n")
    if env = os.getenv('VCAP_APPLICATION'):
        print(env)
    else:
        print("No env vars inside this container...")

if __name__ == '__main__':
    print_something_now()