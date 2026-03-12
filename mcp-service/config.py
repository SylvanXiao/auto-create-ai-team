"""
MCP Service Configuration
"""
import os

# Service configuration
SERVICE_HOST = os.getenv("MCP_HOST", "0.0.0.0")
SERVICE_PORT = int(os.getenv("MCP_PORT", "8085"))
SERVICE_DEBUG = os.getenv("MCP_DEBUG", "false").lower() == "true"

# Skill configuration
SKILL_PATH = os.getenv("SKILL_PATH", "D:/项目/openclaw/skills/auto-create-ai-team/create_ai_team.py")
PROJECT_BASE_PATH = os.getenv("PROJECT_BASE_PATH", "C:/Users/50473/.openclaw/workspace")

# Security configuration  
ALLOWED_PROJECT_PATHS = [
    "C:/Users/50473/.openclaw/workspace",
    "D:/wsl-ubuntu/rootfs/openclaw-vm/projects"
]

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")