#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coursework Analyzer Script for DermaIQ

This script analyzes the Tech Entrepreneurship (COMP0039) coursework requirements
and reference materials to ensure alignment with the DermaIQ project.
"""

import os
import re
import json
import logging
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("coursework_analyzer.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("coursework_analyzer")

class CourseworkAnalyzer:
    """Class for analyzing coursework requirements and reference materials."""
    
    def __init__(self, course_materials_dir: str):
        """Initialize the analyzer with course materials directory.
        
        Args:
            course_materials_dir: Path to the course materials directory
        """
        self.course_materials_dir = Path(course_materials_dir)
        self.reference_materials = []
        self.coursework_requirements = {}
        logger.info(f"Initialized CourseworkAnalyzer with directory: {course_materials_dir}")
    
    def scan_course_materials(self) -> Dict[str, List[str]]:
        """Scan the course materials directory for relevant files.
        
        Returns:
            Dictionary mapping file categories to lists of file paths
        """
        try:
            if not self.course_materials_dir.exists():
                logger.error(f"Course materials directory not found: {self.course_materials_dir}")
                return {}
            
            # Categorize files
            materials_by_category = {
                "coursework": [],
                "business_planning": [],
                "guest_lectures": [],
                "legal_ip": [],
                "ai_technology": [],
                "other": []
            }
            
            # Scan directory for files
            for file_path in self.course_materials_dir.glob("**/*"):
                if file_path.is_file():
                    file_name = file_path.name.lower()
                    
                    # Categorize based on filename patterns
                    if "course work" in file_name or "coursework" in file_name:
                        materials_by_category["coursework"].append(str(file_path))
                    elif any(term in file_name for term in ["business", "plan", "canvas", "financial"]):
                        materials_by_category["business_planning"].append(str(file_path))
                    elif any(term in file_name for term in ["lecture", "presentation", "slides"]):
                        materials_by_category["guest_lectures"].append(str(file_path))
                    elif any(term in file_name for term in ["legal", "ip", "intellectual", "companies", "rights"]):
                        materials_by_category["legal_ip"].append(str(file_path))
                    elif any(term in file_name for term in ["ai", "technology", "tech", "machine", "learning"]):
                        materials_by_category["ai_technology"].append(str(file_path))
                    else:
                        materials_by_category["other"].append(str(file_path))
            
            # Store all reference materials
            self.reference_materials = []
            for category, files in materials_by_category.items():
                self.reference_materials.extend(files)
            
            logger.info(f"Found {len(self.reference_materials)} course materials across {len(materials_by_category)} categories")
            return materials_by_category
        except Exception as e:
            logger.error(f"Error scanning course materials: {e}")
            return {}
    
    def extract_reference_list(self, reference_list_path: str) -> List[str]:
        """Extract references from the reference list file.
        
        Args:
            reference_list_path: Path to the reference list markdown file
            
        Returns:
            List of reference items
        """
        try:
            reference_list_path = Path(reference_list_path)
            if not reference_list_path.exists():
                logger.error(f"Reference list file not found: {reference_list_path}")
                return []
            
            with open(reference_list_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract references (lines starting with - or numbered lists)
            references = []
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('- ') or re.match(r'^\d+\.\s', line):
                    references.append(line)
            
            logger.info(f"Extracted {len(references)} references from {reference_list_path}")
            return references
        except Exception as e:
            logger.error(f"Error extracting references: {e}")
            return []
    
    def analyze_coursework_requirements(self, coursework_file: str) -> Dict[str, any]:
        """Analyze the coursework requirements file.
        
        Note: This is a placeholder function since we can't directly extract text from PDF.
        In a real implementation, you would use a PDF extraction library.
        
        Args:
            coursework_file: Path to the coursework PDF file
            
        Returns:
            Dictionary with coursework requirements analysis
        """
        try:
            # This is a placeholder for PDF text extraction
            # In a real implementation, you would use PyPDF2, pdfminer, or similar
            
            # Simulate extracted requirements
            requirements = {
                "project_title": "DermaIQ: AI-Powered Skincare Ingredient Analysis",
                "submission_deadline": "2025-05-15",
                "key_deliverables": [
                    "Proof of Concept documentation",
                    "Market analysis",
                    "Technical implementation plan",
                    "Business model",
                    "Validation strategy"
                ],
                "assessment_criteria": [
                    "Innovation and originality",
                    "Market validation",
                    "Technical feasibility",
                    "Business model viability",
                    "Presentation quality"
                ]
            }
            
            self.coursework_requirements = requirements
            logger.info(f"Analyzed coursework requirements from {coursework_file}")
            return requirements
        except Exception as e:
            logger.error(f"Error analyzing coursework requirements: {e}")
            return {}
    
    def check_project_alignment(self, project_files: List[str]) -> Dict[str, any]:
        """Check alignment between project files and coursework requirements.
        
        Args:
            project_files: List of project file paths
            
        Returns:
            Dictionary with alignment analysis
        """
        try:
            if not self.coursework_requirements:
                logger.warning("Coursework requirements not analyzed yet")
                return {}
            
            # Extract key terms from requirements
            key_terms = set()
            for deliverable in self.coursework_requirements.get("key_deliverables", []):
                key_terms.update(deliverable.lower().split())
            for criterion in self.coursework_requirements.get("assessment_criteria", []):
                key_terms.update(criterion.lower().split())
            
            # Filter out common words
            common_words = {"and", "the", "of", "in", "for", "with", "a", "an", "to"}
            key_terms = {term for term in key_terms if term not in common_words}
            
            # Check project files for key terms
            alignment_scores = {}
            for file_path in project_files:
                file_path = Path(file_path)
                if not file_path.exists():
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().lower()
                    
                    # Count occurrences of key terms
                    term_counts = {term: content.count(term) for term in key_terms}
                    total_matches = sum(term_counts.values())
                    
                    # Calculate alignment score (simple version)
                    alignment_score = min(100, total_matches / len(key_terms) * 20)  # Scale to 0-100
                    
                    alignment_scores[str(file_path)] = {
                        "score": alignment_score,
                        "term_matches": term_counts
                    }
                except Exception as e:
                    logger.warning(f"Could not analyze file {file_path}: {e}")
            
            # Overall project alignment
            if alignment_scores:
                average_score = np.mean([data["score"] for data in alignment_scores.values()])
            else:
                average_score = 0
            
            return {
                "overall_alignment": average_score,
                "file_alignment": alignment_scores,
                "key_terms_analyzed": list(key_terms)
            }
        except Exception as e:
            logger.error(f"Error checking project alignment: {e}")
            return {}
    
    def generate_reference_report(self, reference_list_path: str) -> Dict[str, any]:
        """Generate a report on references used in the project.
        
        Args:
            reference_list_path: Path to the reference list file
            
        Returns:
            Dictionary with reference analysis
        """
        try:
            # Extract references
            references = self.extract_reference_list(reference_list_path)
            
            # Scan course materials
            materials_by_category = self.scan_course_materials()
            
            # Check which course materials are referenced
            referenced_materials = set()
            for ref in references:
                for material in self.reference_materials:
                    material_name = Path(material).name
                    if material_name.lower() in ref.lower():
                        referenced_materials.add(material)
            
            # Calculate coverage
            coverage_by_category = {}
            for category, materials in materials_by_category.items():
                if materials:
                    referenced = sum(1 for m in materials if m in referenced_materials)
                    coverage_by_category[category] = {
                        "total": len(materials),
                        "referenced": referenced,
                        "percentage": referenced / len(materials) * 100 if materials else 0
                    }
            
            # Overall coverage
            if self.reference_materials:
                overall_coverage = len(referenced_materials) / len(self.reference_materials) * 100
            else:
                overall_coverage = 0
            
            return {
                "total_references": len(references),
                "course_materials_referenced": len(referenced_materials),
                "overall_coverage": overall_coverage,
                "coverage_by_category": coverage_by_category,
                "unreferenced_materials": [m for m in self.reference_materials if m not in referenced_materials]
            }
        except Exception as e:
            logger.error(f"Error generating reference report: {e}")
            return {}
    
    def save_analysis(self, output_path: str) -> bool:
        """Save the analysis results to a JSON file.
        
        Args:
            output_path: Path where to save the analysis
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Prepare analysis data
            analysis = {
                "coursework_requirements": self.coursework_requirements,
                "reference_materials": {
                    "total": len(self.reference_materials),
                    "materials": [Path(m).name for m in self.reference_materials]
                },
                "analysis_timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Ensure directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2)
            
            logger.info(f"Saved analysis to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving analysis: {e}")
            return False


def main():
    """Main function to demonstrate the coursework analyzer."""
    try:
        # Example paths (would be replaced with actual paths in real usage)
        course_materials_dir = "Slides"
        reference_list_path = "Reference_List.md"
        coursework_file = "Slides/20250206 Tech Entrepreneurship COMP0039-0146 Course Work.pdf"
        project_files = ["DermaIQ_PoC.md", "market_analysis.md", "technical_implementation.md"]
        
        # Initialize analyzer
        analyzer = CourseworkAnalyzer(course_materials_dir)
        
        # Scan course materials
        materials_by_category = analyzer.scan_course_materials()
        print(f"Found {sum(len(files) for files in materials_by_category.values())} course materials")
        
        # Analyze coursework requirements
        requirements = analyzer.analyze_coursework_requirements(coursework_file)
        print(f"Analyzed coursework requirements: {len(requirements)} sections")
        
        # Check project alignment
        alignment = analyzer.check_project_alignment(project_files)
        print(f"Overall project alignment: {alignment.get('overall_alignment', 0):.2f}%")
        
        # Generate reference report
        reference_report = analyzer.generate_reference_report(reference_list_path)
        print(f"Reference coverage: {reference_report.get('overall_coverage', 0):.2f}%")
        
        # Save analysis
        analyzer.save_analysis("analysis/coursework_analysis.json")
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
