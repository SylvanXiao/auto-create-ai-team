# Auto-Create-AI-Team Skill

## Description
Automatically creates AI team structures for any project with support for single team, dual team (internal + internet), and custom team modes. Integrates with MCP services and OpenClaw for seamless automation.

## Usage
```bash
python create_ai_team.py --project-path /path/to/project
```

## Features
- Dual team architecture (internal development team + internet marketing team)
- Intelligent project type detection (generic web applications, e-commerce, content management, mobile apps, generic projects)
- Interactive configuration with preview
- Multi-model strategy with free model priority and paid model precision
- MCP service integration with HTTP API support
- OpenClaw integration for command-line and API usage

## Output Structure
```
project/
└── ai-team/
    ├── internal-team/     # Internal AI team
    │   └── team-info/
    ├── internet-team/     # Internet team (dual mode)
    │   └── team-info/
    ├── logs/              # Execution logs
    └── PROJECT_PROGRESS.md
```

## Integration
This skill can be integrated into automated workflows to automatically configure AI teams for new projects, providing standardized team structures and optimized resource allocation.