import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('BD_USER'))
print(os.getenv('BD_PASSWORD'))
