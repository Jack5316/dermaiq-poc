# DermaIQ: Proof of Concept

## Overview
DermaIQ is an AI-powered skincare ingredient analysis iOS application that provides consumers with reliable, transparent information about the products they put on their skin every day. Our solution helps users decode complex ingredient labels, identify potential harmful chemicals, and make informed decisions about their skincare products through a simple, intuitive interface backed by scientific data.

## Repository Contents

This repository contains the comprehensive Proof of Concept documentation for DermaIQ:

1. [**DermaIQ_PoC.md**](./DermaIQ_PoC.md) - The main PoC document outlining the project concept, problem statement, solution, market validation, business model, and implementation plan.

2. [**market_analysis.md**](./market_analysis.md) - In-depth analysis of the skincare ingredient transparency market, including market size, competitive landscape, and growth opportunities.

3. [**technical_implementation.md**](./technical_implementation.md) - Technical plan detailing the iOS app architecture, Swift implementation, technology stack, and development phases.

4. [**data_structure.md**](./data_structure.md) - Database schema and data structure documentation for the DermaIQ iOS application.

5. [**survey_findings.md**](./survey_findings.md) - Detailed methodology and findings from our market research surveys conducted at UK retailers.

6. [**validation_plan.md**](./validation_plan.md) - Validation strategy outlining how to test core hypotheses and measure success metrics.

7. [**todo.md**](./todo.md) - Task management file for tracking project progress and priorities.

8. [**scripts/**](./scripts/) - Python scripts for data analysis, processing, and task management:
   - [**ingredient_analysis.py**](./scripts/ingredient_analysis.py) - Analyzes skincare ingredients using NumPy and Pandas
   - [**data_processing.py**](./scripts/data_processing.py) - Handles data cleaning and transformation
   - [**task_manager.py**](./scripts/task_manager.py) - Automates task management in todo.md

9. [**mockups/**](./mockups/) - UI/UX design mockups for the iOS application.

10. [**assets/**](./assets/) - Project assets including logos, images, and diagrams.

## Project Setup

### Python Environment
This project uses Python 3.12 for data analysis and processing. To set up the environment:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run ingredient analysis script
python scripts/ingredient_analysis.py

# Run task management script
python scripts/task_manager.py
```

### Key Libraries
- **NumPy**: Used for numerical computations and data analysis
- **Pandas**: Used for data manipulation and analysis
- **uv**: Used for asynchronous I/O operations
- **Pillow & OpenCV**: For image processing (JPEG, PNG)

## Problem Statement

Consumers face significant challenges when trying to understand skincare product ingredients:

1. **Complex Terminology**: Ingredient labels use scientific names that are difficult for average consumers to understand.

2. **Lack of Transparency**: Limited information about potential risks or benefits of specific ingredients.

3. **Information Overload**: Too much conflicting information online about skincare ingredients.

4. **Time-Consuming Research**: Researching each ingredient manually is impractical for most consumers.

5. **Personalization Gap**: Generic information doesn't account for individual skin types or conditions.

## Our Solution

DermaIQ addresses these challenges through a mobile application that:

- **Scans product labels** using computer vision to identify ingredients
- **Provides clear explanations** of each ingredient in plain language
- **Flags potential concerns** based on scientific research
- **Offers personalized recommendations** based on skin type and conditions
- **Maintains a comprehensive database** of skincare ingredients and products

## Market Validation

Our market research confirms strong demand for this solution:

- **87%** of surveyed consumers struggle to understand skincare ingredient labels
- **92%** are concerned about potentially harmful ingredients
- **76%** would use an app that helps decode ingredient lists
- **68%** would pay for premium features that offer personalized recommendations

See [survey_findings.md](./survey_findings.md) for detailed research methodology and results.

## Business Model

DermaIQ will operate on a freemium model:

**Free Tier:**
- Basic ingredient scanning and information
- Limited number of scans per month
- Access to common ingredient database

**Premium Tier (£3.99/month):**
- Unlimited product scans
- Personalized recommendations
- Product comparisons
- Skin diary and tracking
- Advanced analytics

Additional revenue streams will include:
- Partnerships with clean beauty brands
- Anonymized market research data
- API access for skincare professionals

## Technical Implementation

The application will be built using:

- **Swift** for iOS native development
- **Core ML** for on-device machine learning
- **Vision framework** for image recognition
- **Firebase** for backend services
- **Python** with NumPy and Pandas for data processing

See [technical_implementation.md](./technical_implementation.md) for detailed architecture and implementation plan.

## Team

**Jack Tan** - Technical Lead
- Expertise in iOS development and machine learning
- Background in computer vision and data science
- Email: ucabjt7@ucl.ac.uk

**Catherine Liang** - UI & Brand
- Expertise in UI/UX design
- Background in brand development
- Email: sejjc91@ucl.ac.uk

## Next Steps

Following successful PoC validation:

1. **Secure seed funding** for full product development
2. **Expand our database** to include more products and ingredients
3. **Enhance the iOS application** with all planned features
4. **Establish key partnerships** with skincare brands and experts
5. **Launch beta version** to our waitlist subscribers

## Task Management

We use [todo.md](./todo.md) to track project tasks and priorities. The file is managed both manually and through our [task_manager.py](./scripts/task_manager.py) script, which provides automated task tracking and reporting.

## References

Bom, S., Jorge, J., Ribeiro, H. M., & Marto, J. (2019). A step forward on sustainability in the cosmetics industry: A review. Journal of Cleaner Production, 225, 270-290. https://doi.org/10.1016/j.jclepro.2019.03.255

Cosmetics Europe. (2023). *Consumer Insights 2023: Understanding the European Cosmetics Consumer*. https://cosmeticseurope.eu/reports-publications/

European Commission. (2022). *Cosmetic Ingredient Database (CosIng)*. https://ec.europa.eu/growth/tools-databases/cosing/

Mintel. (2024). *Global Beauty and Personal Care Trends 2024*. Mintel Group Ltd.

National Institute for Health and Care Excellence. (2023). *Skin conditions: general and site-specific*. https://www.nice.org.uk/guidance/conditions-and-diseases/skin-conditions

Statista. (2024). *Skincare market worldwide - Statistics & Facts*. https://www.statista.com/topics/4976/skincare-market-worldwide/

Tan, J., & Liang, C. (2025). *Survey of UK Consumer Attitudes Toward Skincare Ingredient Transparency*. Unpublished raw data.

## UCL MSc Computer Science Entrepreneurship Project
This PoC was developed as part of the UCL MSc Computer Science Entrepreneurship coursework.