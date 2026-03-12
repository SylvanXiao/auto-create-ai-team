#!/usr/bin/env python3
"""
MCP Service for Auto Create AI Team Skill
Provides HTTP API to automatically create AI teams for projects
"""

import os
import sys
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

# Add the skill directory to Python path
skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, skill_dir)

from mcp-service.config import Settings
from mcp-service.models import AI_Team_Request, AI_Team_Response
from mcp-service.skill_executor import execute_ai_team_creation

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load settings
settings = Settings()

# Initialize FastAPI app
app = FastAPI(
    title="Auto Create AI Team MCP Service",
    description="Automatically creates AI teams for new projects",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "auto-create-ai-team-mcp"}

@app.post("/create-ai-team", response_model=AI_Team_Response)
async def create_ai_team(request: AI_Team_Request):
    """
    Create an AI team for a project
    
    Args:
        request: AI_Team_Request containing project details
        
    Returns:
        AI_Team_Response with creation status and team info
    """
    try:
        logger.info(f"Received request to create AI team for project: {request.project_path}")
        
        # Validate project path
        if not os.path.exists(request.project_path):
            raise HTTPException(
                status_code=400,
                detail=f"Project path does not exist: {request.project_path}"
            )
        
        # Execute AI team creation
        result = execute_ai_team_creation(
            project_path=request.project_path,
            project_type=request.project_type,
            team_size=request.team_size,
            models=request.models
        )
        
        if result["success"]:
            logger.info(f"AI team created successfully for project: {request.project_path}")
            return AI_Team_Response(
                status="success",
                message=result["message"],
                team_path=result["team_path"],
                team_info=result["team_info"]
            )
        else:
            logger.error(f"AI team creation failed: {result['message']}")
            raise HTTPException(status_code=500, detail=result["message"])
            
    except Exception as e:
        logger.error(f"Unexpected error creating AI team: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    # Run the service
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    )