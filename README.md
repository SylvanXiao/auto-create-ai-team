# Auto-Create-AI-Team Skill

Automatically create complete AI teams for any project with intelligent configuration.

## Features

- **Intelligent Project Detection**: Automatically identifies project type and configures appropriate team structure
- **Dual Team Support**: Creates both internal AI development teams and internet marketing teams
- **Customizable Templates**: Extensible team templates for different project types
- **MCP Service Ready**: Designed for easy integration with MCP services
- **Comprehensive Testing**: Full test coverage ensures reliability

## Supported Project Types

| Project Type | Team Structure | Key Roles |
|-------------|----------------|-----------|
| ALM Knowledge Base | Single Team | Data Updater, Research Analyst, Innovation Specialist |
| Interview Simulator | Dual Team | Product Manager, Technical Architect, Frontend/Backend Developers, Marketing Specialists |
| AI Wallpaper | Dual Team | Creative Designer, Technical Developer, Market Analyst, Social Media Operator |
| Generic Projects | Single Team | AI Assistant, Data Processor, Content Generator, Quality Checker |

## Installation

```bash
# Clone the skill
git clone https://github.com/your-username/auto-create-ai-team.git ~/.openclaw/skills/auto-create-ai-team

# Or copy to your OpenClaw skills directory
cp -r auto-create-ai-team ~/.openclaw/workspace/skills/
```

## Usage

### Basic Usage
```bash
python3 create_ai_team.py --project-path /path/to/your/project
```

### Auto-Detection Mode (Recommended)
```bash
python3 create_ai_team.py --project-path /path/to/your/project --auto-detect
```

### Interactive Mode
```bash
python3 create_ai_team.py --project-path /path/to/your/project --ask-user
```

### Specify Team Configuration
```bash
# Single team (development only)
python3 create_ai_team.py --project-path /path/to/project --team-type single

# Dual team (development + marketing)
python3 create_ai_team.py --project-path /path/to/project --team-type dual
```

## Project Structure

After running the skill, your project will have this structure:

```
your-project/
└── ai-team/
    ├── internal-team/          # Internal AI development team
    │   └── team-info/
    │       ├── AI_TEAM_CONFIG.md
    │       └── TEAM_MEMBERS.md
    ├── internet-team/          # Internet marketing team (dual mode only)
    │   └── team-info/
    │       ├── INTERNET_TEAM_CONFIG.md  
    │       └── TEAM_MEMBERS.md
    ├── logs/                  # Execution logs
    └── PROJECT_PROGRESS.md    # Project progress overview
```

## MCP Service Integration

The skill is designed to work as an MCP service. Example API call:

```bash
POST /create-ai-team
{
  "project_path": "/path/to/project",
  "auto_detect": true,
  "team_type": "dual"
}
```

## Testing

Run comprehensive tests to ensure functionality:

```bash
python3 test_comprehensive.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/barryxiao/auto-create-ai-team](https://github.com/barryxiao/auto-create-ai-team)