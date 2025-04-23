from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime
# Load environment variables from .env file
# Get the current date and time
now = datetime.now()
# Format the date and time as a string
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
# Print the current date and time
print("Current date and time:", current_time)

password = os.getenv('PASSWORD')
# print('hello world! >>>>> ' + password)


