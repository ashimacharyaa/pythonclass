# Lists for Month Names
import datetime
import nepali_datetime

bs_month = [
    "Baisakh", "Jesth", "Aasar", "Shrawan", "Bhadra", "Aashoj", 
    "Kartik", "Mangshir", "Poush", "Magh", "Falgun", "Chaitra"
]
ad_month = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

def get_ordinal_suffix(day):
    #Returning Correct suffix for Day
    if 11 <= day <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

def convert_date(date_str, from_cal, to_cal):
    #''' Convert date string (Simplified Math Method) '''
    if from_cal == to_cal: #if ad and bs same
        return date_str
    
    # Split the date into integer components
    year, month, day = map(int, date_str.split('-'))

    if from_cal == "AD" and to_cal == "BS":
        year += 56
    elif from_cal == "BS" and to_cal == "AD":
        year -= 56

    return f"{year:04d}-{month:02d}-{day:02d}"# eg 2006-02-28

def format_output(converted_date, to_cal, style):
    """Format converted date"""

    year, month, day = map(int, converted_date.split('-'))

    if style == "iso":
        return f"{converted_date} {to_cal}"

    elif style == "full":
        suffix = get_ordinal_suffix(day)
        months_list = bs_month if to_cal == "BS" else ad_month
        month_name = months_list[month - 1]
        return f"{day}{suffix} {month_name}, {year} {to_cal}"

    elif style == "nepali":
        months_list = bs_month if to_cal == "BS" else ad_month
        month_name = months_list[month - 1]
        return f"{day} {month_name}, {year} {to_cal}"

    return converted_date

# Sample Data
customers = [
    {"name": "Ashim Acharya", "date": "2006-02-28", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Manogya Guragai", "date": "2005-06-24", "cal": "AD", "need": "BS", "style": "full"},
]

# Process and Print
for c in customers:
    iso_converted = convert_date(c["date"], c["cal"], c["need"])
    formatted_date = format_output(iso_converted, c["need"], c["style"])
    
    print(f"{c['name']} | {c['date']} | {c['cal']} | Convert: {formatted_date}")