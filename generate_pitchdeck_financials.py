import xlsxwriter

# === CONFIG ===
currency = 'GBP'  # Change to 'USD' or 'GBP'
exchange_rate = 0.80 if currency == 'GBP' else 1.0  # 1 USD = 0.80 GBP (2025), adjust as needed
currency_symbol = '£' if currency == 'GBP' else '$'

# Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('PitchDeck_Financials.xlsx')
worksheet = workbook.add_worksheet('Income Statement')

# Data for the table (in USD, will convert if needed)
headers = [
    '', f'2021A ({currency})', f'2022E ({currency})', f'2023P ({currency})', f'2024P ({currency})', f'2025P ({currency})', f'2026P ({currency})', f'2027P ({currency})'
]
data_usd = [
    ['Revenue', '', '', '', '', '', '', ''],
    ['Platform Fees', 10000, 12000, 18000, 36000, 90000, 180000, 300000],
    ['Services', 5000, 7000, 14000, 28000, 56000, 112000, 168000],
    ['Maintenance', 2000, 3000, 6000, 12000, 24000, 48000, 72000],
    ['Total Revenue', 17000, 22000, 38000, 76000, 170000, 340000, 540000],
    ['COGS', 8000, 10000, 18000, 36000, 72000, 120000, 180000],
    ['Gross Profit', 9000, 12000, 20000, 40000, 98000, 220000, 360000],
    ['Expenses', '', '', '', '', '', '', ''],
    ['Sales & Mktg', 5000, 6000, 8000, 10000, 15000, 20000, 25000],
    ['R&D', 2000, 2500, 3000, 4000, 5000, 6000, 7000],
    ['G&A', 3000, 4000, 5000, 6000, 8000, 10000, 12000],
    ['Total Expenses', 10000, 12500, 16000, 20000, 28000, 36000, 44000],
    ['Net Income', -1000, -500, 4000, 20000, 70000, 184000, 316000],
]
# Convert USD values to target currency

def convert(val):
    if isinstance(val, (int, float)):
        return round(val * exchange_rate)
    return val

data = []
for row in data_usd:
    data.append([row[0]] + [convert(val) for val in row[1:]])

# Key assumptions
assumptions = [
    'Key Assumptions:',
    f'Platform fee per license: {currency_symbol}1,000',
    'Headcount: 2 founders, scaling with revenue',
    'Growth rates (orange): 50–100% YoY',
    'Breakeven: 2024 (first positive Net Income)',
    'Costs scale with revenue',
    f'All figures in {currency}',
]

# Formatting
bold = workbook.add_format({'bold': True})
header_format = workbook.add_format({'bold': True, 'bg_color': '#D9E1F2', 'border': 1, 'align': 'center'})
total_format = workbook.add_format({'bold': True, 'bg_color': '#BDD7EE', 'border': 1, 'num_format': f'"{currency_symbol}"#,##0'})
breakeven_format = workbook.add_format({'bold': True, 'bg_color': '#C6EFCE', 'font_color': '#006100', 'border': 1, 'num_format': f'"{currency_symbol}"#,##0'})
orange_format = workbook.add_format({'bg_color': '#FFD966', 'border': 1, 'num_format': f'"{currency_symbol}"#,##0'})
money_format = workbook.add_format({'num_format': f'"{currency_symbol}"#,##0'})

# Write headers
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Write data rows
for row_idx, row in enumerate(data):
    label = row[0]
    worksheet.write(row_idx + 1, 0, label, bold if label in ['Revenue', 'Expenses'] else None)
    for col_idx, val in enumerate(row[1:]):
        cell_format = None
        # Totals
        if label in ['Total Revenue', 'Gross Profit', 'Total Expenses', 'Net Income']:
            cell_format = total_format
        # Breakeven year (2024)
        if label == 'Net Income' and col_idx == 3:
            cell_format = breakeven_format
        # Editable (growth rates, pricing) - highlight with orange
        if label in ['Platform Fees', 'Services', 'Maintenance'] and col_idx > 0:
            cell_format = orange_format
        # Default: money format for all numbers
        if cell_format is None and isinstance(val, (int, float)):
            cell_format = money_format
        worksheet.write(row_idx + 1, col_idx + 1, val, cell_format)

# Write Key Assumptions below the table
start_row = len(data) + 3
for i, line in enumerate(assumptions):
    worksheet.write(start_row + i, 0, line)

# Autofit columns
worksheet.set_column(0, 0, 18)
worksheet.set_column(1, 7, 15)

workbook.close()
print('PitchDeck_Financials.xlsx created successfully with currency:', currency)
