# AI团队成员配置

## 团队模式选择
{{TEAM_MODE}}

## 内部AI团队（产品开发）
{% if TEAM_MODE in ['dual', 'internal'] %}
### 核心角色
- **{{INTERNAL_TEAM_LEAD}}** - 团队协调和任务分配
- **{{TECHNICAL_SPECIALIST}}** - 技术实现和工具集成
- **{{CONTENT_CREATOR}}** - 内容创作和素材管理
- **{{QUALITY_ASSURANCE}}** - 质量保证和用户体验
- **{{RESEARCH_ANALYST}}** - 研究分析和趋势洞察

### 模型分配
- 主模型: {{PRIMARY_MODEL}}
- 备用模型: {{FALLBACK_MODELS}}
{% endif %}

## 互联网团队（产品运营）
{% if TEAM_MODE in ['dual', 'internet'] %}
### 核心角色  
- **{{PRODUCT_MANAGER}}** - 产品规划和商业化策略
- **{{MARKETING_EXPERT}}** - 品牌推广和用户获取
- **{{SOCIAL_MEDIA_MANAGER}}** - 社交媒体运营和社区管理
- **{{DATA_ANALYST}}** - 数据分析和用户行为研究
- **{{BUSINESS_DEVELOPMENT}}** - 商务合作和收入拓展
- **{{UX_RESEARCHER}}** - 用户体验研究和需求调研

### 模型分配
- 主模型: {{INTERNET_PRIMARY_MODEL}}
- 备用模型: {{INTERNET_FALLBACK_MODELS}}
{% endif %}

## 团队协作机制
- 定期同步会议
- 共享知识库
- 跨团队项目协作
- 统一进度跟踪