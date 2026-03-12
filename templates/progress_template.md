# {{PROJECT_NAME}} - 项目进展概览

## 📋 项目基本信息
- **项目名称**: {{PROJECT_NAME}}
- **创建时间**: {{CREATION_DATE}}
- **项目类型**: {{PROJECT_TYPE}}
- **团队模式**: {{TEAM_MODE}}

## 🤖 团队结构
{% if TEAM_MODE == "dual" %}
### 内部AI团队（产品开发）
- **团队规模**: {{INTERNAL_TEAM_SIZE}}
- **主要角色**: {{INTERNAL_TEAM_ROLES}}
- **核心职责**: 产品开发、技术实现、质量保证

### 互联网团队（产品运营）  
- **团队规模**: {{INTERNET_TEAM_SIZE}}
- **主要角色**: {{INTERNET_TEAM_ROLES}}
- **核心职责**: 市场推广、用户增长、商业化运营

{% elif TEAM_MODE == "single" %}
### 单一AI团队
- **团队规模**: {{TEAM_SIZE}}
- **主要角色**: {{TEAM_ROLES}}
- **核心职责**: 全流程产品开发和运营

{% else %}
### 自定义团队
- **配置文件**: custom_team_config.json
- **团队详情**: 请查看自定义配置文件

{% endif %}

## 🎯 当前状态
- **团队创建**: ✅ 已完成
- **配置文件**: ✅ 已生成
- **自动化脚本**: ✅ 已部署
- **运行日志**: ✅ 已启用

## 📈 下一步计划
1. AI团队开始自动运行
2. 监控团队工作进展
3. 定期生成进展报告
4. 根据需要调整团队配置

## 📁 目录结构
```
{{PROJECT_PATH}}/
├── ai-team/
│   ├── team-info/          # 团队信息和配置
│   {% if TEAM_MODE == "dual" %}
│   ├── internal-team/      # 内部AI团队
│   └── internet-team/      # 互联网团队
│   {% else %}
│   └── single-team/        # 单一团队
│   {% endif %}
└── [项目原有目录]
```

---
*此文件由 Auto Create AI Team Skill v2.0 自动生成*