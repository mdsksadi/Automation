import os
from typing import Optional


try:
	from dotenv import load_dotenv
	load_dotenv()
except Exception:
	pass


class Settings:
	GMAIL_EMAIL: Optional[str] = os.getenv("GMAIL_EMAIL")
	GMAIL_PASSWORD: Optional[str] = os.getenv("GMAIL_PASSWORD")
	OUTLOOK_EMAIL: Optional[str] = os.getenv("OUTLOOK_EMAIL")
	OUTLOOK_PASSWORD: Optional[str] = os.getenv("OUTLOOK_PASSWORD")


settings = Settings()