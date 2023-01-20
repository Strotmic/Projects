from datetime import datetime

test = "2023-01-20"
date_time_obj = datetime.strptime(test, '%Y-%m-%d')
print(f"Dag: {date_time_obj.day}, Maand: {date_time_obj.month}, Jaar: {date_time_obj.year}")