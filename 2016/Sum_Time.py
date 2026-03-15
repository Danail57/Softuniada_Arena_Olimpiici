def parse_to_minutes(time_str):
    if "::" in time_str:
        days_part, time_part = time_str.split("::")
        days = int(days_part)
    else:
        days = 0
        time_part = time_str
    hours, minutes = map(int, time_part.split(":"))
    return (days * 24 * 60) + (hours * 60) + minutes

line1 = input().strip()
line2 = input().strip()
total_minutes = parse_to_minutes(line1) + parse_to_minutes(line2)
total_hours, minutes = divmod(total_minutes, 60)
days, hours = divmod(total_hours, 24)
if days > 0:
    print(f"{days}::{hours}:{minutes:02d}")
else:
    print(f"{hours}:{minutes:02d}")
