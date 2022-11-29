def get_diff(data):
    data['sales_diff'] = data.sales.diff()
    data = data.dropna()
    return data
stationary_df = get_diff(monthly_data)