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

6. [**validation_plan.md**](./validation_plan.md) - Validation strategy outlining how to test core hypotheses and validate product-market fit.

## Problem Statement

Every day, the average person applies numerous chemicals to their body through everyday cosmetics, many of which may be harmful. For millions of consumers:
- **Data is incorrect**: Existing solutions provide unreliable information
- **UI is confusing**: Complex interfaces make ingredient analysis difficult
- **Subscription is annoying**: Valuable features hidden behind paywalls

## Our Solution

DermaIQ provides a comprehensive skincare ingredient analysis platform with:
- AI-powered ingredient analysis engine with 99.8% accuracy
- Personalized safety assessments for individual skin types
- Simple, trustworthy product recommendations
- Free core functionality with premium features for advanced users

## Market Validation

Our comprehensive market research included surveys with over 50 potential consumers at Boots, Selfridges, and SpaceNK between March-April 2025. Key findings include:

- 90% showed interest in a reliable ingredient analysis tool
- 80% don't have a helpful resource for understanding ingredients
- 70% signed up for our waitlist

For detailed survey findings, see [survey_findings.md](./survey_findings.md).

## Technical Implementation

DermaIQ is being developed as a native iOS application using:

- **Language**: Swift 5.9+
- **UI Framework**: SwiftUI for modern, declarative UI development
- **Architecture Pattern**: MVVM (Model-View-ViewModel)
- **State Management**: Combine framework for reactive programming
- **Persistence**: CoreData for local database storage
- **ML Framework**: CoreML for on-device ingredient analysis

For detailed technical information, see [technical_implementation.md](./technical_implementation.md).

## Business Model

### Revenue Streams
1. **Commission by recommending/linking users to skincare products**
   - Affiliate partnerships with clean beauty brands
   - Conversion-based revenue model

2. **Non-intrusive advertisements**
   - Targeted, relevant ads from vetted skincare brands
   - Focus on educational content

3. **Premium features (one-off payment)**
   - Advanced ingredient analysis
   - Personalized recommendations from dermatologists
   - Comprehensive skin profile analysis

4. **Optional subscription for enhanced features**
   - Professional consultation
   - Personalized skincare routines
   - Early access to new features

## Data Sources and Quality Assurance

DermaIQ's database is built using reliable sources to ensure accuracy:

1. **Official regulatory bodies**:
   - NICE (UK National Institute for Health and Care Excellence)
   - EMA (European Medicines Agency)
   - EWG Skin Deep database

2. **Retail partners**:
   - Boots
   - Selfridges
   - SpaceNK

For detailed information on our data structure, see [data_structure.md](./data_structure.md).

## Validation Approach

For our Proof of Concept, we have implemented a landing page with signup functionality at [https://derma-iq-waitlist.vercel.app/](https://derma-iq-waitlist.vercel.app/) and are developing a simple demo of our core ingredient analysis feature as an iOS application.

For detailed validation methodology, see [validation_plan.md](./validation_plan.md).

## Team

**Jiawei (Jack) Tan** - Developer & Product
- MSc Computer Science at UCL
- Expertise in ML and iOS application development
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