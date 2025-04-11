#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Processing Script for DermaIQ

This script handles data processing tasks for the DermaIQ application,
including data cleaning, transformation, and export functions.
"""

import numpy as np
import pandas as pd
import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data_processing.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("data_processing")

class DataProcessor:
    """Class for processing skincare product and ingredient data."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the data processor.
        
        Args:
            data_dir: Directory containing data files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initialized DataProcessor with data directory: {data_dir}")
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """Load data from various file formats.
        
        Args:
            file_path: Path to the data file
            
        Returns:
            Pandas DataFrame containing the loaded data
        """
        try:
            file_path = Path(file_path)
            extension = file_path.suffix.lower()
            
            if extension == ".csv":
                df = pd.read_csv(file_path)
            elif extension == ".xlsx" or extension == ".xls":
                df = pd.read_excel(file_path)
            elif extension == ".json":
                df = pd.read_json(file_path)
            else:
                raise ValueError(f"Unsupported file format: {extension}")
            
            logger.info(f"Loaded data from {file_path} with {len(df)} rows and {len(df.columns)} columns")
            return df
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {e}")
            raise
    
    def clean_ingredient_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and preprocess ingredient data.
        
        Args:
            df: DataFrame containing ingredient data
            
        Returns:
            Cleaned DataFrame
        """
        try:
            # Make a copy to avoid modifying the original
            cleaned_df = df.copy()
            
            # Remove duplicates
            initial_rows = len(cleaned_df)
            cleaned_df.drop_duplicates(inplace=True)
            logger.info(f"Removed {initial_rows - len(cleaned_df)} duplicate rows")
            
            # Handle missing values
            missing_before = cleaned_df.isna().sum().sum()
            
            # For text columns, replace NaN with empty string
            text_columns = cleaned_df.select_dtypes(include=['object']).columns
            cleaned_df[text_columns] = cleaned_df[text_columns].fillna('')
            
            # For numeric columns, replace NaN with 0 or mean depending on context
            numeric_columns = cleaned_df.select_dtypes(include=['number']).columns
            for col in numeric_columns:
                # Use mean for columns that represent measurements or ratings
                if 'rating' in col.lower() or 'score' in col.lower():
                    cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())
                else:
                    cleaned_df[col] = cleaned_df[col].fillna(0)
            
            missing_after = cleaned_df.isna().sum().sum()
            logger.info(f"Handled {missing_before - missing_after} missing values")
            
            # Normalize text data (lowercase)
            for col in text_columns:
                if 'name' in col.lower() or 'ingredient' in col.lower():
                    cleaned_df[col] = cleaned_df[col].str.lower().str.strip()
            
            return cleaned_df
        except Exception as e:
            logger.error(f"Error cleaning ingredient data: {e}")
            raise
    
    def transform_survey_data(self, survey_df: pd.DataFrame) -> Dict[str, any]:
        """Transform survey data into analysis-ready format.
        
        Args:
            survey_df: DataFrame containing survey responses
            
        Returns:
            Dictionary with transformed survey data and summary statistics
        """
        try:
            # Aggregate responses
            response_counts = {}
            for col in survey_df.columns:
                if col.startswith('Q'):
                    response_counts[col] = survey_df[col].value_counts().to_dict()
            
            # Calculate summary statistics
            numeric_cols = survey_df.select_dtypes(include=['number']).columns
            summary_stats = {}
            for col in numeric_cols:
                summary_stats[col] = {
                    'mean': survey_df[col].mean(),
                    'median': survey_df[col].median(),
                    'std': survey_df[col].std(),
                    'min': survey_df[col].min(),
                    'max': survey_df[col].max()
                }
            
            # Group data by demographic factors if available
            demographic_insights = {}
            demo_cols = [col for col in survey_df.columns if any(x in col.lower() for x in ['age', 'gender', 'location'])]
            
            for demo_col in demo_cols:
                for response_col in [col for col in survey_df.columns if col.startswith('Q')]:
                    cross_tab = pd.crosstab(survey_df[demo_col], survey_df[response_col], normalize='index')
                    demographic_insights[f"{demo_col}_{response_col}"] = cross_tab.to_dict()
            
            return {
                'response_counts': response_counts,
                'summary_statistics': summary_stats,
                'demographic_insights': demographic_insights,
                'total_responses': len(survey_df)
            }
        except Exception as e:
            logger.error(f"Error transforming survey data: {e}")
            raise
    
    def export_data(self, df: pd.DataFrame, output_path: str, format: str = "csv") -> bool:
        """Export processed data to various formats.
        
        Args:
            df: DataFrame to export
            output_path: Path where to save the exported data
            format: Export format (csv, json, excel)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Export based on format
            if format.lower() == "csv":
                df.to_csv(output_path, index=False)
            elif format.lower() == "json":
                df.to_json(output_path, orient="records", indent=2)
            elif format.lower() in ["excel", "xlsx"]:
                df.to_excel(output_path, index=False)
            else:
                raise ValueError(f"Unsupported export format: {format}")
            
            logger.info(f"Exported data to {output_path} in {format} format")
            return True
        except Exception as e:
            logger.error(f"Error exporting data: {e}")
            return False
    
    def generate_summary_report(self, df: pd.DataFrame, report_name: str) -> Dict[str, any]:
        """Generate a summary report of the dataset.
        
        Args:
            df: DataFrame to summarize
            report_name: Name for the report
            
        Returns:
            Dictionary containing the summary report
        """
        try:
            # Basic dataset information
            report = {
                "report_name": report_name,
                "generated_at": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "dataset_info": {
                    "rows": len(df),
                    "columns": len(df.columns),
                    "column_names": df.columns.tolist(),
                    "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()}
                },
                "missing_values": df.isna().sum().to_dict(),
                "summary_statistics": {}
            }
            
            # Summary statistics for numeric columns
            numeric_cols = df.select_dtypes(include=['number']).columns
            for col in numeric_cols:
                report["summary_statistics"][col] = {
                    "mean": df[col].mean(),
                    "median": df[col].median(),
                    "std": df[col].std(),
                    "min": df[col].min(),
                    "max": df[col].max(),
                    "q1": df[col].quantile(0.25),
                    "q3": df[col].quantile(0.75)
                }
            
            # Frequency counts for categorical columns (limited to top 10)
            categorical_cols = df.select_dtypes(include=['object']).columns
            report["category_frequencies"] = {}
            for col in categorical_cols:
                report["category_frequencies"][col] = df[col].value_counts().head(10).to_dict()
            
            # Save the report
            report_path = self.data_dir / f"{report_name}.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Generated summary report: {report_path}")
            return report
        except Exception as e:
            logger.error(f"Error generating summary report: {e}")
            return {"error": str(e)}


def main():
    """Main function to demonstrate the data processor."""
    try:
        # Initialize processor
        processor = DataProcessor()
        
        # Create sample data for demonstration
        sample_data = {
            "ingredient_name": ["Glycerin", "Hyaluronic Acid", "Salicylic Acid", "Niacinamide", "Retinol"],
            "category": ["Humectant", "Humectant", "Exfoliant", "Vitamin", "Retinoid"],
            "safety_rating": [5, 5, 4, 5, 3],
            "common_in": ["Moisturizers", "Serums", "Acne treatments", "Serums", "Anti-aging"]
        }
        
        sample_df = pd.DataFrame(sample_data)
        
        # Process the sample data
        cleaned_df = processor.clean_ingredient_data(sample_df)
        
        # Export the processed data
        processor.export_data(cleaned_df, "data/processed_ingredients.csv")
        
        # Generate a summary report
        report = processor.generate_summary_report(cleaned_df, "ingredient_summary")
        print(json.dumps(report, indent=2))
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
