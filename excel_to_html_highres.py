import pandas as pd
from jinja2 import Template
from pathlib import Path

# HTML template with embedded CSS for high-res, readable table
HTML_TEMPLATE = '''
<html>
<head>
<style>
body { background: #fff; }
table { border-collapse: collapse; font-size: 18px; }
th, td { border: 1px solid #dddddd; padding: 10px 16px; text-align: center; }
th { background: #e3eafc; color: #222; font-weight: bold; }
td { background: #f8fafc; }
tr:nth-child(even) td { background: #f1f6fc; }
tr:hover td { background: #d6eaff; }
</style>
</head>
<body>
{{ table|safe }}
</body>
</html>
'''

def excel_to_html(excel_path, output_html_path=None, sheet_name=0):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    html_table = df.to_html(index=False, border=0, justify='center', classes='excel-table', escape=False)
    html = Template(HTML_TEMPLATE).render(table=html_table)
    if output_html_path is None:
        output_html_path = str(Path(excel_path).with_suffix('.html'))
    with open(output_html_path, 'w') as f:
        f.write(html)
    print(f"Saved HTML: {output_html_path}")
    return output_html_path

if __name__ == "__main__":
    excel_file = "Financial Business Plan - Example.xlsx"
    excel_path = Path(excel_file).resolve()
    excel_to_html(str(excel_path))
