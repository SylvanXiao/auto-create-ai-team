# Auto-Create-AI-Team Skill

Automatically create complete AI teams for any project with intelligent configuration.

## 中文说明

### 核心功能
**自动为任何项目创建完整的AI团队架构**，智能配置最适合的团队结构和角色分工。

### 主要特性

#### ✅ 智能项目识别
- 自动分析项目类型（面试模拟器、知识库、AI壁纸等）
- 智能推荐最适合的团队配置方案

#### ✅ 双团队架构支持
- **内部AI团队**：负责产品开发、技术实现、内容创作
- **互联网团队**：负责市场推广、用户增长、商业化运营

#### ✅ 多项目类型支持
| 项目类型 | 团队结构 | 核心角色 |
|---------|---------|---------|
| **ALM知识库** | 单团队 | 数据更新员、研究分析师、创新专家 |
| **面试模拟器** | 双团队 | 产品经理、技术架构师、前后端开发、市场营销专家 |
| **AI壁纸** | 双团队 | 创意设计师、技术开发者、市场分析师、社交媒体运营 |
| **通用项目** | 单团队 | AI助手、数据处理员、内容生成器、质量检查员 |

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
git clone https://github.com/barryxiao/auto-create-ai-team.git ~/.openclaw/skills/auto-create-ai-team

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