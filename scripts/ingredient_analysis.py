#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingredient Analysis Script for DermaIQ

This script analyzes skincare ingredients using NumPy and Pandas for data processing.
It provides functionality to categorize ingredients, identify potential harmful chemicals,
and generate ingredient safety reports.
"""

import numpy as np
import pandas as pd
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ingredient_analysis.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ingredient_analysis")

class IngredientAnalyzer:
    """Class for analyzing skincare product ingredients."""
    
    def __init__(self, ingredient_db_path: str):
        """Initialize the analyzer with ingredient database.
        
        Args:
            ingredient_db_path: Path to the ingredient database CSV file
        """
        try:
            self.ingredients_df = pd.read_csv(ingredient_db_path)
            logger.info(f"Loaded ingredient database with {len(self.ingredients_df)} entries")
        except Exception as e:
            logger.error(f"Failed to load ingredient database: {e}")
            raise
        
        # Initialize ingredient categories
        self.categories = {
            "moisturizing": ["glycerin", "hyaluronic acid", "ceramides", "squalane"],
            "exfoliating": ["salicylic acid", "glycolic acid", "lactic acid"],
            "antioxidant": ["vitamin c", "vitamin e", "niacinamide", "resveratrol"],
            "potentially_harmful": ["parabens", "phthalates", "formaldehyde", "triclosan"]
        }
    
    def categorize_ingredients(self, ingredient_list: List[str]) -> Dict[str, List[str]]:
        """Categorize ingredients into functional groups.
        
        Args:
            ingredient_list: List of ingredients to categorize
            
        Returns:
            Dictionary mapping categories to lists of ingredients
        """
        result = {category: [] for category in self.categories}
        
        # Normalize ingredient names for comparison
        normalized_ingredients = [ing.lower().strip() for ing in ingredient_list]
        
        for ing in normalized_ingredients:
            for category, category_ingredients in self.categories.items():
                if any(category_ing in ing for category_ing in category_ingredients):
                    result[category].append(ing)
        
        logger.info(f"Categorized {len(ingredient_list)} ingredients")
        return result
    
    def safety_analysis(self, ingredient_list: List[str]) -> Dict[str, any]:
        """Analyze ingredient list for safety concerns.
        
        Args:
            ingredient_list: List of ingredients to analyze
            
        Returns:
            Dictionary with safety analysis results
        """
        try:
            # Convert ingredient list to lowercase for matching
            normalized_ingredients = [ing.lower().strip() for ing in ingredient_list]
            
            # Match ingredients against database
            matched_ingredients = self.ingredients_df[
                self.ingredients_df['ingredient_name'].str.lower().isin(normalized_ingredients)
            ]
            
            # Count potentially harmful ingredients
            harmful_ingredients = []
            for ing in normalized_ingredients:
                for harmful in self.categories["potentially_harmful"]:
                    if harmful in ing:
                        harmful_ingredients.append(ing)
            
            # Calculate safety score (simple version)
            safety_score = 100 - (len(harmful_ingredients) / len(ingredient_list) * 100)
            
            return {
                "safety_score": safety_score,
                "total_ingredients": len(ingredient_list),
                "potentially_harmful": harmful_ingredients,
                "matched_in_database": len(matched_ingredients),
                "unmatched_ingredients": [ing for ing in normalized_ingredients 
                                         if ing not in matched_ingredients['ingredient_name'].str.lower().tolist()]
            }
        except Exception as e:
            logger.error(f"Error in safety analysis: {e}")
            return {"error": str(e)}
    
    def generate_report(self, product_name: str, ingredient_list: List[str]) -> Dict[str, any]:
        """Generate a comprehensive ingredient analysis report.
        
        Args:
            product_name: Name of the product being analyzed
            ingredient_list: List of ingredients in the product
            
        Returns:
            Dictionary containing the analysis report
        """
        try:
            categories = self.categorize_ingredients(ingredient_list)
            safety = self.safety_analysis(ingredient_list)
            
            report = {
                "product_name": product_name,
                "analysis_date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ingredient_count": len(ingredient_list),
                "categories": categories,
                "safety_analysis": safety
            }
            
            logger.info(f"Generated report for {product_name} with {len(ingredient_list)} ingredients")
            return report
        except Exception as e:
            logger.error(f"Failed to generate report: {e}")
            return {"error": str(e)}
    
    def save_report(self, report: Dict[str, any], output_path: str) -> bool:
        """Save the analysis report to a JSON file.
        
        Args:
            report: Report dictionary to save
            output_path: Path where to save the report
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Write report to file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Saved report to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save report: {e}")
            return False


def main():
    """Main function to demonstrate the ingredient analyzer."""
    # Example usage
    try:
        # Sample ingredient list
        sample_product = "Sample Moisturizer"
        sample_ingredients = [
            "Water", "Glycerin", "Cetearyl Alcohol", "Ceteareth-20",
            "Caprylic/Capric Triglyceride", "Butylene Glycol", "Dimethicone",
            "Phenoxyethanol", "Tocopheryl Acetate", "Sodium Hyaluronate",
            "Ethylhexylglycerin", "Disodium EDTA", "Parfum"
        ]
        
        # Initialize analyzer with a placeholder path
        # In a real scenario, this would be a path to an actual database
        analyzer = IngredientAnalyzer("data/ingredients_database.csv")
        
        # Generate and print a sample report
        report = analyzer.generate_report(sample_product, sample_ingredients)
        print(json.dumps(report, indent=2))
        
        # Save the report
        analyzer.save_report(report, "reports/sample_report.json")
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
