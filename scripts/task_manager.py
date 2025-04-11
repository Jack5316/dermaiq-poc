#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Manager Script for DermaIQ

This script automates task management by reading and updating the todo.md file.
It allows for adding, completing, and prioritizing tasks programmatically.
"""

import re
import os
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("task_manager.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("task_manager")

class TaskManager:
    """Class for managing tasks in a markdown todo file."""
    
    def __init__(self, todo_path: str):
        """Initialize the task manager with the path to the todo.md file.
        
        Args:
            todo_path: Path to the todo.md file
        """
        self.todo_path = Path(todo_path)
        self.sections = {
            "high": "## High Priority Tasks",
            "medium": "## Medium Priority Tasks",
            "low": "## Low Priority Tasks",
            "completed": "## Completed Tasks",
            "technical_debt": "## Technical Debt",
            "research": "## Research Tasks"
        }
        logger.info(f"Initialized TaskManager with todo file: {todo_path}")
    
    def read_todo_file(self) -> Dict[str, List[str]]:
        """Read the todo.md file and parse its contents.
        
        Returns:
            Dictionary mapping section names to lists of tasks
        """
        try:
            if not self.todo_path.exists():
                logger.warning(f"Todo file not found at {self.todo_path}")
                return {section: [] for section in self.sections}
            
            with open(self.todo_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse sections and tasks
            tasks_by_section = {}
            current_section = None
            
            for line in content.split('\n'):
                # Check if line is a section header
                for section_key, section_header in self.sections.items():
                    if line.strip() == section_header:
                        current_section = section_key
                        tasks_by_section[current_section] = []
                        break
                
                # If we're in a section and line is a task, add it
                if current_section and line.strip().startswith('- ['):
                    tasks_by_section[current_section].append(line.strip())
            
            # Fill in any missing sections
            for section in self.sections:
                if section not in tasks_by_section:
                    tasks_by_section[section] = []
            
            logger.info(f"Read todo file with {sum(len(tasks) for tasks in tasks_by_section.values())} tasks")
            return tasks_by_section
        except Exception as e:
            logger.error(f"Error reading todo file: {e}")
            return {section: [] for section in self.sections}
    
    def write_todo_file(self, tasks_by_section: Dict[str, List[str]]) -> bool:
        """Write tasks to the todo.md file.
        
        Args:
            tasks_by_section: Dictionary mapping section names to lists of tasks
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            self.todo_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Prepare content
            content = ["# DermaIQ Project Todo List\n"]
            
            # Add each section with its tasks
            for section_key, section_header in self.sections.items():
                content.append(f"\n{section_header}")
                if section_key in tasks_by_section and tasks_by_section[section_key]:
                    for task in tasks_by_section[section_key]:
                        content.append(task)
                else:
                    content.append("- [ ] No tasks yet")
            
            # Write to file
            with open(self.todo_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))
            
            logger.info(f"Updated todo file at {self.todo_path}")
            return True
        except Exception as e:
            logger.error(f"Error writing todo file: {e}")
            return False
    
    def add_task(self, task_description: str, priority: str = "medium") -> bool:
        """Add a new task to the todo list.
        
        Args:
            task_description: Description of the task
            priority: Priority level (high, medium, low, technical_debt, research)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Validate priority
            if priority not in self.sections or priority == "completed":
                logger.error(f"Invalid priority: {priority}")
                return False
            
            # Read current tasks
            tasks_by_section = self.read_todo_file()
            
            # Add new task
            task_entry = f"- [ ] {task_description}"
            tasks_by_section[priority].append(task_entry)
            
            # Write updated tasks
            success = self.write_todo_file(tasks_by_section)
            if success:
                logger.info(f"Added task: {task_description} with {priority} priority")
            
            return success
        except Exception as e:
            logger.error(f"Error adding task: {e}")
            return False
    
    def complete_task(self, task_description: str) -> bool:
        """Mark a task as completed.
        
        Args:
            task_description: Description of the task to complete
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Read current tasks
            tasks_by_section = self.read_todo_file()
            
            # Find the task in any section
            found = False
            for section in [s for s in self.sections if s != "completed"]:
                for i, task in enumerate(tasks_by_section[section]):
                    # Extract task description (removing checkbox)
                    task_text = re.sub(r'^- \[[ x]\] ', '', task)
                    
                    if task_description.lower() in task_text.lower():
                        # Remove from current section
                        tasks_by_section[section].pop(i)
                        
                        # Add to completed section
                        completed_task = f"- [x] {task_text}"
                        tasks_by_section["completed"].append(completed_task)
                        
                        found = True
                        break
                
                if found:
                    break
            
            if not found:
                logger.warning(f"Task not found: {task_description}")
                return False
            
            # Write updated tasks
            success = self.write_todo_file(tasks_by_section)
            if success:
                logger.info(f"Marked task as completed: {task_description}")
            
            return success
        except Exception as e:
            logger.error(f"Error completing task: {e}")
            return False
    
    def change_priority(self, task_description: str, new_priority: str) -> bool:
        """Change the priority of a task.
        
        Args:
            task_description: Description of the task
            new_priority: New priority level
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Validate priority
            if new_priority not in self.sections or new_priority == "completed":
                logger.error(f"Invalid priority: {new_priority}")
                return False
            
            # Read current tasks
            tasks_by_section = self.read_todo_file()
            
            # Find the task in any section
            found = False
            task_to_move = None
            
            for section in [s for s in self.sections if s != "completed"]:
                for i, task in enumerate(tasks_by_section[section]):
                    # Extract task description (removing checkbox)
                    task_text = re.sub(r'^- \[[ x]\] ', '', task)
                    
                    if task_description.lower() in task_text.lower():
                        # Save the task
                        task_to_move = task
                        
                        # Remove from current section
                        tasks_by_section[section].pop(i)
                        
                        found = True
                        break
                
                if found:
                    break
            
            if not found or not task_to_move:
                logger.warning(f"Task not found: {task_description}")
                return False
            
            # Add to new priority section
            tasks_by_section[new_priority].append(task_to_move)
            
            # Write updated tasks
            success = self.write_todo_file(tasks_by_section)
            if success:
                logger.info(f"Changed priority of task to {new_priority}: {task_description}")
            
            return success
        except Exception as e:
            logger.error(f"Error changing task priority: {e}")
            return False
    
    def list_tasks(self, priority: Optional[str] = None) -> List[str]:
        """List tasks, optionally filtered by priority.
        
        Args:
            priority: Priority level to filter by (None for all tasks)
            
        Returns:
            List of task descriptions
        """
        try:
            # Read current tasks
            tasks_by_section = self.read_todo_file()
            
            # Filter by priority if specified
            if priority and priority in self.sections:
                return tasks_by_section[priority]
            
            # Otherwise return all tasks grouped by priority
            all_tasks = []
            for section, tasks in tasks_by_section.items():
                if tasks:
                    all_tasks.append(f"\n{self.sections[section]}")
                    all_tasks.extend(tasks)
            
            return all_tasks
        except Exception as e:
            logger.error(f"Error listing tasks: {e}")
            return []
    
    def generate_report(self) -> Dict[str, any]:
        """Generate a report of task status.
        
        Returns:
            Dictionary with task statistics
        """
        try:
            # Read current tasks
            tasks_by_section = self.read_todo_file()
            
            # Count tasks by section
            task_counts = {section: len(tasks) for section, tasks in tasks_by_section.items()}
            
            # Count total tasks
            total_tasks = sum(task_counts.values())
            
            # Count incomplete tasks
            incomplete_tasks = sum(task_counts[s] for s in self.sections if s != "completed")
            
            # Calculate completion percentage
            completion_percentage = 0
            if total_tasks > 0:
                completion_percentage = (task_counts.get("completed", 0) / total_tasks) * 100
            
            return {
                "total_tasks": total_tasks,
                "completed_tasks": task_counts.get("completed", 0),
                "incomplete_tasks": incomplete_tasks,
                "completion_percentage": completion_percentage,
                "tasks_by_priority": task_counts,
                "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return {"error": str(e)}


def main():
    """Main function to demonstrate the task manager."""
    try:
        # Initialize task manager with path to todo.md
        manager = TaskManager("todo.md")
        
        # Example usage
        print("Current tasks:")
        for task in manager.list_tasks():
            print(task)
        
        # Add a new task
        manager.add_task("Implement user authentication", "high")
        
        # Complete a task
        manager.complete_task("Create initial project repository structure")
        
        # Change task priority
        manager.change_priority("Analyze market research data", "high")
        
        # Generate report
        report = manager.generate_report()
        print("\nTask Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
