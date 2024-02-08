
import re
url = input("url: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
  print(f"USERNAME:", matches.group(1))
