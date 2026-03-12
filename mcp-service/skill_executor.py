"""
AI Team Creation Skill Executor
Handles the execution of the AI team creation skill with proper error handling
"""
import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import Dict, Any

# Add the skill directory to Python path
skill_dir = Path(__file__).parent.parent
sys.path.insert(0, str(skill_dir))

from create_ai_team import create_ai_team

logger = logging.getLogger(__name__)

def execute_ai_team_creation(
    project_path: str,
    project_type: str = "generic",
    team_size: str = "medium", 
    models: str = "mixed"
) -> Dict[str, Any]:
    """
    Execute AI team creation skill with given parameters
    
    Args:
        project_path: Path to the project directory
        project_type: Type of project (generic, custom)
        team_size: Size of the AI team (small, medium, large)
        models: Model strategy (free, premium, mixed)
    
    Returns:
        Dictionary with execution result
    """
    try:
        # Validate project path
        if not os.path.exists(project_path):
            return {
                "status": "error",
                "message": f"Project path does not exist: {project_path}",
                "team_path": None
            }
        
        # Execute the skill
        success = create_ai_team(
            project_path=project_path,
            project_type=project_type,
            team_size=team_size,
            models=models
        )
        
        if success:
            team_path = os.path.join(project_path, "ai-team")
            return {
                "status": "success",
                "message": "AI team created successfully",
                "team_path": team_path,
                "details": {
                    "project_type": project_type,
                    "team_size": team_size,
                    "models": models
                }
            }
        else:
            return {
                "status": "error", 
                "message": "AI team creation failed",
                "team_path": None
            }
            
    except Exception as e:
        logger.error(f"Error executing AI team creation: {str(e)}")
        return {
            "status": "error",
            "message": f"Execution error: {str(e)}",
            "team_path": None
        }