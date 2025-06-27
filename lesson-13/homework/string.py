# Homework Solutions

from datetime import datetime, date, timedelta
import time, re
import pytz

# 1. Age Calculator
birth = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birth, "%Y-%m-%d")
today = datetime.today()
age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
age_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
age_days = (today - birthdate).days
print(f"Age: {age_years} years, {age_months % 12} months, {age_days} days")

# 2. Days Until Next Birthday
next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_remaining = (next_birthday - today).days
print(f"Days until next birthday: {days_remaining}")

# 3. Meeting Scheduler
now = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_h = int(input("Enter meeting duration hours: "))
duration_m = int(input("Enter meeting duration minutes: "))
start_time = datetime.strptime(now, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=duration_h, minutes=duration_m)
print("Meeting ends at:", end_time)

# 4. Timezone Converter
source_zone = input("Enter source timezone (e.g., Asia/Tashkent): ")
dest_zone = input("Enter destination timezone (e.g., Europe/London): ")
date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
source_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
source_tz = pytz.timezone(source_zone)
dest_tz = pytz.timezone(dest_zone)
source_dt = source_tz.localize(source_dt)
dest_dt = source_dt.astimezone(dest_tz)
print("Converted datetime:", dest_dt.strftime("%Y-%m-%d %H:%M"))

# 5. Countdown Timer
future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
while True:
    now = datetime.now()
    if future <= now:
        print("Countdown complete!")
        break
    delta = future - now
    print(f"Time remaining: {delta}", end='\r')
    time.sleep(1)

# 6. Email Validator
email = input("Enter your email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# 7. Phone Number Formatter
phone = input("Enter 10-digit phone number: ")
if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number")

# 8. Password Strength Checker
password = input("Enter a password: ")
strong = (len(password) >= 8 and any(c.islower() for c in password)
          and any(c.isupper() for c in password) and any(c.isdigit() for c in password))
print("Strong password" if strong else "Weak password")

# 9. Word Finder
text = input("Enter a sample text: ")
word = input("Enter the word to search: ")
positions = [m.start() for m in re.finditer(rf'\b{re.escape(word)}\b', text)]
print("Occurrences at indices:", positions)

# 10. Date Extractor
text = input("Enter text containing dates: ")
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
print("Dates found:", dates)
