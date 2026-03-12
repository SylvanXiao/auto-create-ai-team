"""
MCP Service Configuration - Generic Version
"""
import os

# Service configuration
SERVICE_HOST = os.getenv("MCP_HOST", "0.0.0.0")
SERVICE_PORT = int(os.getenv("MCP_PORT", "8085"))
SERVICE_DEBUG = os.getenv("MCP_DEBUG", "false").lower() == "true"

# Skill configuration - Use relative paths and environment variables
SKILL_PATH = os.getenv("SKILL_PATH", "./create_ai_team.py")
PROJECT_BASE_PATH = os.getenv("PROJECT_BASE_PATH", "./projects")

# Security configuration - Allow relative paths and common OpenClaw directories
ALLOWED_PROJECT_PATHS = [
    "./projects",
    "./workspace",
    "/root/.openclaw/workspace",
    "/home/user/.openclaw/workspace",
    "/opt/openclaw/workspace"
]

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")