# DermaIQ: Data Structure and Database Schema

## Overview

This document outlines the data structure and database schema for the DermaIQ iOS application. The database design is crucial for ensuring accurate ingredient analysis, efficient product searches, and reliable user recommendations.

## Data Sources

DermaIQ's database is built using reliable sources to ensure accuracy:

1. **Official regulatory bodies**:
   - NICE (UK National Institute for Health and Care Excellence)
   - EMA (European Medicines Agency) CosIng Database
   - EWG Skin Deep database

2. **Retail partners**:
   - Boots
   - Selfridges
   - SpaceNK

3. **Brand websites**:
   - Official product pages
   - Ingredient disclosure documentation

## Database Schema

### Core Entities

#### Products

```swift
struct Product: Codable, Identifiable {
    let id: UUID
    let name: String
    let brand: String
    let category: ProductCategory
    let imageUrl: URL?
    let ingredients: [Ingredient]
    let overallSafetyRating: Float
    let overallEffectivenessRating: Float
    let retailLinks: [RetailLink]
    let dateAdded: Date
    let lastUpdated: Date
}

enum ProductCategory: String, Codable, CaseIterable {
    case cleanser
    case moisturizer
    case serum
    case sunscreen
    case mask
    case toner
    case exfoliator
    case other
}
```

#### Ingredients

```swift
struct Ingredient: Codable, Identifiable {
    let id: UUID
    let name: String
    let alternativeNames: [String]
    let function: [IngredientFunction]
    let safetyRating: SafetyRating
    let concerns: [IngredientConcern]
    let description: String
    let scientificEvidence: [ScientificReference]
    let commonIn: [String]
    let goodFor: [SkinType]
    let badFor: [SkinType]
}

enum IngredientFunction: String, Codable, CaseIterable {
    case moisturizer
    case antioxidant
    case exfoliant
    case preservative
    case fragrance
    case sunscreen
    case emollient
    case humectant
    case surfactant
    case colorant
    case other
}

enum SafetyRating: Int, Codable {
    case safe = 1
    case moderateConcern = 2
    case highConcern = 3
    case insufficient = 0
}

struct IngredientConcern: Codable, Identifiable {
    let id: UUID
    let name: String
    let description: String
    let severityLevel: Int
    let scientificEvidence: [ScientificReference]
}

struct ScientificReference: Codable, Identifiable {
    let id: UUID
    let title: String
    let authors: [String]
    let journal: String
    let year: Int
    let doi: String?
    let url: URL?
    let summary: String
}

enum SkinType: String, Codable, CaseIterable {
    case dry
    case oily
    case combination
    case normal
    case sensitive
    case acneProne
    case mature
    case rosacea
}
```

#### Retail Links

```swift
struct RetailLink: Codable, Identifiable {
    let id: UUID
    let retailer: String
    let url: URL
    let price: Float
    let currency: String
    let lastUpdated: Date
    let inStock: Bool
}
```

#### User Profiles

```swift
struct UserProfile: Codable, Identifiable {
    let id: UUID
    let skinType: [SkinType]
    let concerns: [SkinConcern]
    let allergies: [String]
    let preferences: UserPreferences
    let savedProducts: [UUID]
    let searchHistory: [SearchRecord]
    let subscriptionTier: SubscriptionTier
}

struct UserPreferences: Codable {
    let preferredBrands: [String]
    let avoidIngredients: [String]
    let priceRange: PriceRange
    let notificationSettings: NotificationSettings
}

struct PriceRange: Codable {
    let min: Float
    let max: Float
    let currency: String
}

enum SkinConcern: String, Codable, CaseIterable {
    case acne
    case aging
    case dryness
    case sensitivity
    case redness
    case hyperpigmentation
    case dullness
    case other
}

enum SubscriptionTier: String, Codable {
    case free
    case premium
    case professional
}

struct SearchRecord: Codable {
    let query: String
    let timestamp: Date
    let resultCount: Int
}

struct NotificationSettings: Codable {
    let productAlerts: Bool
    let weeklyReports: Bool
    let newFeatures: Bool
    let marketingOffers: Bool
}
```

## Database Relationships

1. **Products to Ingredients**: Many-to-many relationship
   - Each product contains multiple ingredients
   - Each ingredient appears in multiple products

2. **Products to Retail Links**: One-to-many relationship
   - Each product can be sold at multiple retailers
   - Each retail link belongs to one product

3. **Ingredients to Scientific References**: One-to-many relationship
   - Each ingredient has multiple scientific references
   - Each scientific reference relates to specific ingredients

4. **Users to Products**: Many-to-many relationship
   - Users can save multiple products
   - Products can be saved by multiple users

## Data Quality Assurance

To ensure the highest quality of data, we implement the following processes:

1. **Initial Data Validation**:
   - Cross-reference ingredient information across multiple sources
   - Verify product formulations with official brand documentation
   - Standardize ingredient naming conventions

2. **Regular Updates**:
   - Weekly crawls of retail websites for new products
   - Monthly verification of existing product formulations
   - Quarterly updates of scientific research database

3. **Quality Checks**:
   - Automated tests for data consistency
   - Manual review of high-concern ingredients
   - Expert verification of safety ratings

4. **Data Integrity Rules**:
   - No user-uploaded ingredient data to maintain reliability
   - All ingredient safety ratings must be supported by scientific evidence
   - Product formulations must be verified against official sources

## Initial Database Population

For the PoC, we will focus on populating the database with the following:

1. **Products**: 500 popular skincare products from the UK market
   - Focus on bestsellers from Boots, Selfridges, and SpaceNK
   - Cover all major product categories
   - Include products from the following brands (based on Notion_KnowledgeBase):
     - Boots (Own-brand umbrella)
     - Clinique
     - No7 (Boots' flagship brand)
     - Clarins
     - Kiehl's
     - La Roche Posay
     - Nivea
     - L'Oreal
     - Estee Lauder
     - Garnier
     - Fresh
     - Olay
     - The Ordinary
     - Liz Earle
     - Dior
     - Chanel
     - YSL

2. **Ingredients**: 1,000 common skincare ingredients
   - Complete safety profiles for each ingredient
   - Scientific references for safety ratings
   - Detailed functional descriptions

3. **Retail Links**: Links to major UK retailers
   - Boots
   - Selfridges
   - SpaceNK
   - Look Fantastic
   - Cult Beauty
   - Amazon UK

## Data Collection Methodology

Our data collection process involves:

1. **Web Scraping**:
   - Custom scraping tools for retail websites
   - API integrations where available
   - Regular automated crawls for updates

2. **Data Processing**:
   - Natural language processing for ingredient extraction
   - Standardization of ingredient names
   - Classification of product categories

3. **Expert Verification**:
   - Dermatologist review of ingredient safety ratings
   - Cosmetic chemist verification of ingredient functions
   - Regular audits of data accuracy

## Technical Implementation

The database will be implemented using:

1. **Local Storage**:
   - CoreData for on-device storage
   - Efficient caching for offline functionality

2. **Cloud Backend**:
   - PostgreSQL for primary data storage
   - Redis for caching frequently accessed data
   - Elasticsearch for efficient product and ingredient searches

3. **Synchronization**:
   - Regular syncing between device and cloud
   - Incremental updates to minimize data transfer
   - Version control for data consistency

## Testing and Validation

To validate our database design and data quality, we will:

1. **Perform test queries** to ensure efficient retrieval of:
   - Products by name, brand, or category
   - Ingredients by name or function
   - Products containing specific ingredients
   - Products suitable for specific skin types

2. **Conduct accuracy tests** by:
   - Comparing our ingredient data with official regulatory databases
   - Verifying product formulations against physical product labels
   - Testing search functionality with common user queries

3. **Measure performance metrics**:
   - Query response times
   - Database size and growth rate
   - Synchronization efficiency

## References

European Commission. (2022). *Cosmetic Ingredient Database (CosIng)*. https://ec.europa.eu/growth/tools-databases/cosing/

Environmental Working Group. (2024). *EWG's Skin Deep® Cosmetics Database*. https://www.ewg.org/skindeep/

National Institute for Health and Care Excellence. (2023). *Skin conditions: general and site-specific*. https://www.nice.org.uk/guidance/conditions-and-diseases/skin-conditions

Tan, J. (2025). *DermaIQ Database Schema Design*. Unpublished technical documentation.

---

*This data structure documentation was developed as part of the UCL MSc Computer Science Technology Entrepreneurship coursework.*