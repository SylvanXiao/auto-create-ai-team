# 自动创建项目AI团队 Skill v2.1

## 📋 功能概述
这是一个自动化工具，可以为任何新项目一键创建完整的AI团队，并支持**自动化运行机制**。支持单团队、双团队和自定义团队模式。

## 🚀 主要特性

### ✅ 双团队支持
- **内部AI团队**：负责产品开发、技术实现、内容创作
- **互联网团队**：负责市场推广、用户增长、商业化运营
- 根据项目类型自动推荐合适的团队结构

### ✅ 智能交互
- 当无法确定项目类型时，会主动询问用户需求
- 支持交互式配置团队规模和角色
- 提供团队配置预览功能

### ✅ 项目类型识别
- **ALM知识库项目**：数据更新、研究分析、创新探索
- **面试模拟器项目**：完整产品开发团队（PM、架构师、前后端等）
- **AI壁纸项目**：创意设计 + 互联网运营双团队
- **通用项目**：基础AI团队配置
- **自定义项目**：用户指定具体配置

### ✅ 多模型支持
- 免费模型优先策略
- 付费模型精准使用
- 自动故障转移机制
- 智能路由选择

### ✅ 🆕 AI团队自动化运行机制
- **自动监控**：持续跟踪项目进展和状态
- **任务分配**：根据项目需求自动分配团队任务
- **定期报告**：自动生成项目进展报告
- **智能优化**：根据反馈自动调整团队配置
- **错误修复**：自动检测和修复常见问题

## 🛠️ 使用方法

### 基本用法
```bash
python create_ai_team.py --project-path /path/to/your/project
```

### 指定项目类型
```bash
python create_ai_team.py --project-path /path/to/project --project-type alm
```

### 指定团队模式
```bash
# 单团队模式
python create_ai_team.py --project-path /path/to/project --team-type single

# 双团队模式  
python create_ai_team.py --project-path /path/to/project --team-type dual

# 交互模式（推荐）
python create_ai_team.py --project-path /path/to/project --ask-user
```

### 自动化运行
创建团队后，AI团队会**自动启动并持续运行**：
- 监控 `PROJECT_PROGRESS.md` 文件
- 执行团队任务
- 定期更新项目状态

## 📂 目录结构

```
project/
└── ai-team/
    ├── internal-team/      # 内部AI团队
    │   └── team-info/
    ├── internet-team/      # 互联网团队（双团队模式）
    │   └── team-info/
    ├── logs/              # 运行日志
    └── PROJECT_PROGRESS.md # 项目进展概览（自动化更新）
```

## 🎯 支持的项目类型

| 项目类型 | 团队模式 | 主要角色 |
|---------|---------|---------|
| alm | 单团队 | Data Updater, Research Analyst, Innovation Specialist |
| interview | 双团队 | Product Manager, Technical Architect, Frontend/Backend Developer + Marketing Team |
| ai-wallpaper | 双团队 | 创意设计师+市场营销专家+社交媒体运营 |
| generic | 单团队 | 基础AI团队配置 |
| custom | 自定义 | 用户指定配置 |

## 🔧 高级功能

### 交互式配置
在交互模式下，Skill会：
1. 分析项目目录内容
2. 推荐合适的团队结构
3. 询问用户确认或调整
4. 生成最终的团队配置

### MCP服务集成
此Skill已集成到MCP服务中，可以通过HTTP API调用：
```bash
POST /create-ai-team
{
  "project_path": "/path/to/project",
  "interactive": true
}
```

### 🆕 自动化运行机制
AI团队创建后会自动：
- **监控项目状态**：读取项目文件和进度
- **执行分配任务**：根据团队角色分工协作
- **生成进展报告**：更新 `PROJECT_PROGRESS.md`
- **自我优化**：根据项目反馈调整策略

## 📈 未来扩展

- 支持更多项目类型模板
- 添加团队性能监控和优化
- 集成到OpenClaw CLI命令
- 支持图形化配置界面
- 增强自动化运行的智能程度