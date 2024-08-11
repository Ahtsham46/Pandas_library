import pandas as pd
def generate_date(start_date,end_date,filter_start,filter_end):
    date_series = pd.date_range(start=start_date,end=end_date)
    date_series = pd.Series(date_series)
    print(f'Date series is:\n{date_series}')
    filtered_date = date_series[(date_series >= filter_start) & (date_series <= filter_end)]
    return filtered_date
start_date = '2024-08-01'
end_date = '2024-08-31'
filter_start = '2024-08-10'
filter_end = '2024-08-20'
filter_dates = generate_date(start_date,end_date,filter_start,filter_end)
print(f'"Filtered dates within the specified range:\n {filter_dates}')