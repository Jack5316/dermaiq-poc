# Building DermaIQ: From Concept to Presentation with Windsurf IDE

*April 12, 2025*

## Introduction

Over the past few months, I've had the privilege of developing DermaIQ, an AI-powered skincare ingredient analysis application, as part of my UCL MSc Computer Science Entrepreneurship coursework. This blog post details our journey from initial concept to final presentation, highlighting how Windsurf IDE and various AI tools streamlined our development process.

## The DermaIQ Concept

DermaIQ addresses a critical gap in the skincare market: the lack of transparency and understanding around product ingredients. Our market research revealed some compelling statistics:

- 87% of consumers struggle with understanding ingredient labels
- 92% are concerned about potentially harmful ingredients
- 76% would use an ingredient decoding app
- 68% are willing to pay for personalized recommendations

These findings validated our core hypothesis: consumers need a reliable, AI-powered tool to decode complex skincare ingredients and receive personalized recommendations.

## Technical Development Process

### 1. Leveraging Windsurf IDE for End-to-End Development

Windsurf IDE became our central development environment for all DermaIQ deliverables. Unlike traditional IDEs focused solely on code, Windsurf provided an integrated environment for:

- Markdown documentation
- LaTeX document preparation
- Version control integration
- PDF generation
- AI-assisted content creation

This unified environment eliminated the need to switch between multiple tools, significantly accelerating our development process.

### 2. Document Preparation and Conversion

One of the most interesting technical challenges was efficiently converting our Markdown documents to presentation-ready PDFs. After exploring several options, we implemented a solution using Grip, a GitHub-flavored Markdown renderer:

```bash
/Users/jack/Library/Python/3.9/bin/grip dermaiq_inclass_presentation.md --export dermaiq_inclass_presentation.pdf
```

This approach allowed us to:
- Maintain content in easily editable Markdown format
- Generate professionally styled PDFs with GitHub's rendering
- Preserve formatting consistency across all documents
- Avoid complex LaTeX installations and configurations

### 3. Version Control and Collaboration

We established a structured GitHub repository ([Jack5316/dermaiq-poc](https://github.com/Jack5316/dermaiq-poc)) with multiple branches to manage different aspects of the project:

- `main`: Core project documentation and proof of concept
- `add-course-materials`: Additional coursework deliverables
- `coursework-presentation`: Presentation materials and PDFs

This branching strategy enabled parallel development of different components while maintaining a clean, organized repository structure.

## Key Technical Components

### 1. iOS Application Architecture

The DermaIQ iOS application leverages several cutting-edge technologies:

- **Computer Vision**: Core ML and Vision Framework for ingredient label recognition
- **Machine Learning**: Custom models for ingredient analysis and skin compatibility
- **Cloud Infrastructure**: AWS for backend services and database management
- **Data Processing**: Python-based ingredient analysis pipeline

### 2. Data Structure and Management

Our database architecture includes:

- 15,000+ ingredient database with comprehensive properties
- User profile schema capturing 50+ individual skin variables
- Context-aware recommendation engine
- Secure, privacy-focused data storage

### 3. Integration with Strategic Partners

We designed our system with API endpoints for integration with key partners:

- UCL Hatchery Programme for academic resources
- NHS Digital Health for clinical validation
- Look Fantastic for product database access and e-commerce integration

## Presentation Development

For our final coursework presentation, we created three key deliverables:

1. **In-class Presentation**: A concise 10-slide deck highlighting DermaIQ's value proposition, market opportunity, and business model
2. **Video Script**: A detailed 3-5 minute script with visual cues and speaker assignments
3. **Video Ingenuity Plan**: A comprehensive strategy for leveraging our video across digital platforms, investor relations, and partnership development

Using Windsurf IDE, we were able to:
- Draft content in Markdown for easy editing and version control
- Convert to PDFs using Grip for submission
- Maintain consistent branding and messaging across all materials
- Push updates directly to our GitHub repository

## Leveraging AI Tools

Throughout this project, we utilized several AI-powered tools to enhance our development process:

- **Alpha-Vantage MCP**: For financial data and market analysis
- **Tavily MCP**: For comprehensive market research and competitive analysis
- **Perplexity MCP**: For technological insights and problem-solving
- **Sequential Thinking MCP**: For structured problem decomposition
- **Memory MCP**: For maintaining context across development sessions
- **GitHub MCP**: For repository management and code analysis
- **Fetch MCP**: For gathering the latest industry data

These tools significantly accelerated our research, analysis, and content creation processes.

## Challenges and Solutions

### Challenge 1: PDF Generation

**Problem**: Converting Markdown to professional-quality PDFs without complex LaTeX installations.
**Solution**: Implemented Grip for GitHub-flavored Markdown rendering and PDF export.

### Challenge 2: Repository Organization

**Problem**: Managing multiple deliverables with different formats and purposes.
**Solution**: Created a structured branching strategy in GitHub to organize different components.

### Challenge 3: Consistent Branding

**Problem**: Maintaining consistent branding across various document formats.
**Solution**: Established DermaIQ brand guidelines (blue #0097a9 and orange #ea7600) and applied them consistently across all materials.

## Business Model and Future Development

DermaIQ employs a freemium business model:
- **Free Tier**: Basic scanning and ingredient analysis
- **Premium Subscription**: £3.99/month for unlimited scans and personalized recommendations
- **Additional Revenue Streams**: B2B API licensing, affiliate marketing, and anonymized market research data

Our financial projections indicate:
- Year 1 Target: 50,000 users
- Year 3 Projection: £5.5M revenue
- Customer Acquisition Cost: £2.50
- Lifetime Value: £35.90

## Conclusion

Developing DermaIQ using Windsurf IDE has been a transformative experience, demonstrating how integrated development environments can streamline the creation of not just code, but comprehensive business and presentation materials.

The combination of Markdown for content creation, GitHub for version control, and Grip for PDF generation proved to be an efficient, flexible workflow that could be valuable for many entrepreneurial projects.

As we move forward with DermaIQ, we're excited to apply these technical learnings to our MVP development and eventual market launch in Q3 2025.

## About the Authors

**Jack Tan** (Technical Lead) - MSc Computer Science Entrepreneurship student at UCL with a background in iOS development and machine learning.

**Catherine Liang** (UI/UX & Brand Design) - Experienced designer specializing in healthcare applications and user-centered design methodologies.

---

*This blog post was created as part of the UCL MSc Computer Science Entrepreneurship coursework for the COMP0039 Technology Entrepreneurship module.*
