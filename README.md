# Auto-Create-AI-Team Skill

[![中文](https://img.shields.io/badge/lang-中文-red)](#chinese) [![English](https://img.shields.io/badge/lang-English-blue)](#english)

## 中文

### 概述
**自动为任何项目创建完整的AI团队架构**，智能配置最适合的团队结构和角色分工。

### 主要特性

#### ✅ 智能项目识别
- 自动分析项目类型（Web应用、电商平台、内容管理系统等）
- 智能推荐最适合的团队配置方案

#### ✅ 双团队架构支持
- **内部AI团队**：负责产品开发、技术实现、内容创作
- **互联网团队**：负责市场推广、用户增长、商业化运营

#### ✅ 多项目类型支持
| 项目类型 | 团队结构 | 核心角色 |
|---------|---------|---------|
| **通用Web应用** | 单团队 | 产品经理、前端开发、后端开发、QA工程师 |
| **电商平台** | 双团队 | 技术架构师、全栈开发、UX设计师、市场营销专家、数据分析师 |
| **内容管理系统** | 单团队 | 系统架构师、开发工程师、内容策略师、质量保证 |
| **移动应用** | 双团队 | 移动开发、后端工程师、UI/UX设计师、增长营销、用户研究员 |
| **通用项目** | 单团队 | AI助手、数据处理员、内容生成器、质量检查员 |

#### ✅ 完整工作流
- 自动生成团队配置文件
- 创建详细的团队成员说明
- 生成项目进展跟踪文档
- 支持MCP服务集成

### 安装

```bash
# 克隆技能
git clone https://github.com/your-username/auto-create-ai-team.git ~/.openclaw/skills/auto-create-ai-team

# 或复制到OpenClaw技能目录
cp -r auto-create-ai-team ~/.openclaw/workspace/skills/
```

### 使用方法

#### 基本用法
```bash
python3 create_ai_team.py --project-path /path/to/your/project
```

#### 自动检测模式（推荐）
```bash
python3 create_ai_team.py --project-path /path/to/your/project --auto-detect
```

#### 交互模式
```bash
python3 create_ai_team.py --project-path /path/to/your/project --ask-user
```

#### 指定团队配置
```bash
# 单团队（仅开发）
python3 create_ai_team.py --project-path /path/to/project --team-type single

# 双团队（开发+营销）
python3 create_ai_team.py --project-path /path/to/project --team-type dual
```

### 项目结构

运行技能后，你的项目将具有以下结构：

```
your-project/
└── ai-team/
    ├── internal-team/          # 内部AI开发团队
    │   └── team-info/
    │       ├── AI_TEAM_CONFIG.md
    │       └── TEAM_MEMBERS.md
    ├── internet-team/          # 互联网营销团队（仅双团队模式）
    │   └── team-info/
    │       ├── INTERNET_TEAM_CONFIG.md  
    │       └── TEAM_MEMBERS.md
    ├── logs/                  # 执行日志
    └── PROJECT_PROGRESS.md    # 项目进展概览
```

### MCP服务集成

该技能设计为可作为MCP服务工作。API调用示例：

```bash
POST /create-ai-team
{
  "project_path": "/path/to/project",
  "auto_detect": true,
  "team_type": "dual"
}
```

### 测试

运行完整测试以确保功能正常：

```bash
python3 test_comprehensive.py
```

### 贡献

1. Fork仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

### 许可证

基于MIT许可证分发。详见 `LICENSE` 文件。

### 联系方式

Your Name - your.email@example.com

项目链接: [https://github.com/your-username/auto-create-ai-team](https://github.com/your-username/auto-create-ai-team)

---

## English

### Overview
Automatically create complete AI teams for any project with intelligent configuration.

### Features

- **Intelligent Project Detection**: Automatically identifies project type and configures appropriate team structure
- **Dual Team Support**: Creates both internal AI development teams and internet marketing teams
- **Customizable Templates**: Extensible team templates for different project types
- **MCP Service Ready**: Designed for easy integration with MCP services
- **Comprehensive Testing**: Full test coverage ensures reliability

### Supported Project Types

| Project Type | Team Structure | Key Roles |
|-------------|----------------|-----------|
| Generic Web App | Single Team | Product Manager, Frontend Developer, Backend Developer, QA Engineer |
| E-commerce Platform | Dual Team | Technical Architect, Full-stack Developer, UX Designer, Marketing Specialist, Data Analyst |
| Content Management System | Single Team | System Architect, Developer, Content Strategist, Quality Assurance |
| Mobile Application | Dual Team | Mobile Developer, Backend Engineer, UI/UX Designer, Growth Marketer, User Researcher |
| Generic Projects | Single Team | AI Assistant, Data Processor, Content Generator, Quality Checker |

### Installation

```bash
# Clone the skill
git clone https://github.com/your-username/auto-create-ai-team.git ~/.openclaw/skills/auto-create-ai-team

# Or copy to your OpenClaw skills directory
cp -r auto-create-ai-team ~/.openclaw/workspace/skills/
```

### Usage

#### Basic Usage
```bash
python3 create_ai_team.py --project-path /path/to/your/project
```

#### Auto-Detection Mode (Recommended)
```bash
python3 create_ai_team.py --project-path /path/to/your/project --auto-detect
```

#### Interactive Mode
```bash
python3 create_ai_team.py --project-path /path/to/your/project --ask-user
```

#### Specify Team Configuration
```bash
# Single team (development only)
python3 create_ai_team.py --project-path /path/to/project --team-type single

# Dual team (development + marketing)
python3 create_ai_team.py --project-path /path/to/project --team-type dual
```

### Project Structure

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

### MCP Service Integration

The skill is designed to work as an MCP service. Example API call:

```bash
POST /create-ai-team
{
  "project_path": "/path/to/project",
  "auto_detect": true,
  "team_type": "dual"
}
```

### Testing

Run comprehensive tests to ensure functionality:

```bash
python3 test_comprehensive.py
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License

Distributed under the MIT License. See `LICENSE` for more information.

### Contact

Your Name - your.email@example.com

Project Link: [https://github.com/your-username/auto-create-ai-team](https://github.com/your-username/auto-create-ai-team)