from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    f"singlestoredb://{os.getenv('SINGLESTORE_USER')}:{os.getenv('SINGLESTORE_PASS')}@{os.getenv('SINGLESTORE_HOST')}:{os.getenv('SINGLESTORE_PORT')}/{os.getenv('SINGLESTORE_DATABASE')}"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("✅ Connected! Response:", result.fetchone())
