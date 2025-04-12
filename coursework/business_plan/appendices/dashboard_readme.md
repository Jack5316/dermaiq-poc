# DermaIQ Business Analytics Dashboard

## Overview

This interactive dashboard visualizes key business metrics and projections for the DermaIQ startup. It provides a comprehensive view of our user growth, financial projections, market research insights, and competitive analysis in an easy-to-interpret format.

## Features

The dashboard includes four main sections:

1. **User Growth**
   - Total and paying user projections over 5 years
   - Conversion rate trends
   - Detailed quarterly breakdown by year

2. **Financial Projections**
   - Revenue and expense projections
   - EBITDA margin trends
   - Revenue breakdown by stream
   - Unit economics (CAC, LTV, LTV:CAC ratio)

3. **Market Research**
   - Consumer survey results visualization
   - Demographic breakdown of survey respondents
   - Geographic distribution of target market

4. **Competitor Analysis**
   - Current and projected market share comparison
   - User base comparison with competitors
   - Competitive positioning map based on scientific credibility and personalization

## Installation

1. Ensure you have Python 3.12 installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the dashboard:
   ```
   python dermaiq_dashboard.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8050/
   ```

3. Navigate between tabs to explore different aspects of the business plan data

4. Use the interactive dropdown selectors to filter data by year or time period

## Data Sources

The dashboard visualizes data from the following appendices:
- Appendix B: Market Research Data
- Appendix D: Competitor Analysis
- Appendix E: Financial Projections

## Technical Implementation

- Built with Dash, a Python framework for building analytical web applications
- Uses Plotly for interactive data visualization
- Implements a responsive design for optimal viewing on different devices
- Follows best practices for data visualization and user experience

## Customization

To update the data visualized in the dashboard:
1. Modify the data frames in the `dermaiq_dashboard.py` file
2. Adjust chart configurations as needed
3. Restart the dashboard application

## Contact

For any questions regarding this dashboard, please contact:
- Email: info@dermaiq.com
- Website: www.dermaiq.com
