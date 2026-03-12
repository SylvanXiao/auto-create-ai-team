#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Create AI Team Skill v2.0
支持双团队模式（内部AI团队 + 互联网团队）
根据项目类型智能配置团队结构
"""

import os
import sys
import json
import argparse
from pathlib import Path

def detect_project_type(project_path):
    """自动检测项目类型"""
    project_name = os.path.basename(project_path).lower()
    
    # ALM知识库项目
    if 'alm' in project_name or 'knowledge' in project_name or '知识库' in project_name:
        return 'alm'
    
    # 面试模拟器项目  
    elif 'interview' in project_name or '面试' in project_name or 'pm' in project_name:
        return 'interview'
    
    # AI壁纸项目
    elif 'wallpaper' in project_name or '壁纸' in project_name or 'ai' in project_name:
        return 'ai_wallpaper'
    
    # 通用项目
    else:
        return 'generic'

def ask_user_for_team_type(project_path):
    """询问用户需要什么类型的团队"""
    print(f"项目: {project_path}")
    print("请选择团队类型:")
    print("1. 单团队 (内部AI团队)")
    print("2. 双团队 (内部AI团队 + 互联网团队)") 
    print("3. 自定义 (手动指定)")
    
    while True:
        try:
            choice = input("请输入选择 (1/2/3): ").strip()
            if choice == '1':
                return 'single'
            elif choice == '2':
                return 'dual'
            elif choice == '3':
                return 'custom'
            else:
                print("无效选择，请输入 1, 2, 或 3")
        except KeyboardInterrupt:
            print("\n操作已取消")
            sys.exit(1)

def create_internal_ai_team(project_path, project_type):
    """创建内部AI团队"""
    ai_team_dir = os.path.join(project_path, 'ai-team', 'internal-team')
    os.makedirs(ai_team_dir, exist_ok=True)
    
    # 创建团队信息目录
    team_info_dir = os.path.join(ai_team_dir, 'team-info')
    os.makedirs(team_info_dir, exist_ok=True)
    
    # 根据项目类型创建不同的团队成员
    if project_type == 'alm':
        members = ['Data Updater', 'Research Analyst', 'Innovation Specialist', 'Quality Assurance']
    elif project_type == 'interview':
        members = ['Product Manager', 'Technical Architect', 'Frontend Developer', 'Backend Developer', 'QA Engineer', 'UX/UI Designer', 'DevOps Engineer']
    elif project_type == 'ai_wallpaper':
        members = ['Creative Designer', 'Technical Developer', 'Market Analyst', 'Quality Assurance', 'Content Curator']
    else:
        members = ['AI Assistant', 'Data Processor', 'Content Generator', 'Quality Checker']
    
    # 创建团队配置文件
    config_content = f"""# 内部AI团队配置
项目类型: {project_type}
团队类型: 内部AI团队
创建时间: {os.popen('date').read().strip()}
团队成员: {', '.join(members)}
"""
    
    with open(os.path.join(team_info_dir, 'AI_TEAM_CONFIG.md'), 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    # 创建团队成员文件
    members_content = f"""# 团队成员介绍

## 内部AI团队成员

{chr(10).join([f"- **{member}**: 负责相关任务" for member in members])}

## 团队职责
- 自动监控和更新项目数据
- 分析相关信息，完善项目内容
- 探索创新点和优化方案
- 确保数据质量和准确性
"""
    
    with open(os.path.join(team_info_dir, 'TEAM_MEMBERS.md'), 'w', encoding='utf-8') as f:
        f.write(members_content)
    
    return ai_team_dir

def create_internet_team(project_path, project_type):
    """创建互联网团队"""
    internet_team_dir = os.path.join(project_path, 'ai-team', 'internet-team')
    os.makedirs(internet_team_dir, exist_ok=True)
    
    # 创建团队信息目录
    team_info_dir = os.path.join(internet_team_dir, 'team-info')
    os.makedirs(team_info_dir, exist_ok=True)
    
    # 互联网团队成员（通用）
    members = ['Product Manager', 'Marketing Specialist', 'Social Media Operator', 'Data Analyst', 'Business Development Manager', 'User Researcher']
    
    # 创建团队配置文件
    config_content = f"""# 互联网团队配置
项目类型: {project_type}
团队类型: 互联网团队
创建时间: {os.popen('date').read().strip()}
团队成员: {', '.join(members)}
"""
    
    with open(os.path.join(team_info_dir, 'INTERNET_TEAM_CONFIG.md'), 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    # 创建团队成员文件
    members_content = f"""# 互联网团队成员介绍

## 互联网团队成员

{chr(10).join([f"- **{member}**: 负责相关任务" for member in members])}

## 团队职责
- 产品规划和商业化策略
- 品牌推广和用户获取
- 社交媒体运营和社区管理
- 用户行为分析和产品优化
- 商务合作和收入拓展
- 用户反馈收集和需求调研
"""
    
    with open(os.path.join(team_info_dir, 'TEAM_MEMBERS.md'), 'w', encoding='utf-8') as f:
        f.write(members_content)
    
    return internet_team_dir

def create_project_progress_file(project_path, team_type, project_type):
    """创建项目进展概览文件"""
    progress_file = os.path.join(project_path, 'ai-team', 'PROJECT_PROGRESS.md')
    
    if team_type == 'dual':
        team_desc = "双团队架构（内部AI团队 + 互联网团队）"
    elif team_type == 'single':
        team_desc = "单团队架构（内部AI团队）"
    else:
        team_desc = "自定义团队架构"
    
    content = f"""# 项目进展概览

## 项目基本信息
- **项目名称**: {os.path.basename(project_path)}
- **项目类型**: {project_type}
- **团队架构**: {team_desc}
- **创建时间**: {os.popen('date').read().strip()}

## 团队状态
- **内部AI团队**: ✅ 已创建并启动
- **互联网团队**: {'✅ 已创建并启动' if team_type == 'dual' else '❌ 未创建'}

## 当前任务
- 监控项目进展
- 自动执行团队任务
- 定期生成进展报告

## 下一步计划
- 根据项目需求调整团队配置
- 优化团队协作流程
- 持续改进团队能力
"""
    
    os.makedirs(os.path.dirname(progress_file), exist_ok=True)
    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Auto Create AI Team Skill v2.0')
    parser.add_argument('--project-path', required=True, help='项目路径')
    parser.add_argument('--project-type', choices=['alm', 'interview', 'ai_wallpaper', 'generic'], help='项目类型')
    parser.add_argument('--team-type', choices=['single', 'dual', 'custom'], help='团队类型')
    parser.add_argument('--auto-detect', action='store_true', help='自动检测项目类型')
    parser.add_argument('--ask-user', action='store_true', help='询问用户配置')
    
    args = parser.parse_args()
    
    # 确保项目路径存在
    if not os.path.exists(args.project_path):
        print(f"错误: 项目路径不存在: {args.project_path}")
        sys.exit(1)
    
    # 确定项目类型
    if args.project_type:
        project_type = args.project_type
    elif args.auto_detect:
        project_type = detect_project_type(args.project_path)
        print(f"自动检测到项目类型: {project_type}")
    else:
        project_type = 'generic'
    
    # 确定团队类型
    if args.team_type:
        team_type = args.team_type
    elif args.ask_user:
        team_type = ask_user_for_team_type(args.project_path)
    else:
        # 默认根据项目类型决定
        if project_type in ['ai_wallpaper', 'interview']:
            team_type = 'dual'  # AI壁纸和面试模拟器默认双团队
        else:
            team_type = 'single'  # 其他项目默认单团队
    
    print(f"正在为项目创建AI团队...")
    print(f"项目路径: {args.project_path}")
    print(f"项目类型: {project_type}")
    print(f"团队类型: {team_type}")
    
    # 创建内部AI团队
    internal_team_path = create_internal_ai_team(args.project_path, project_type)
    print(f"✅ 内部AI团队创建完成: {internal_team_path}")
    
    # 创建互联网团队（如果是双团队）
    if team_type == 'dual':
        internet_team_path = create_internet_team(args.project_path, project_type)
        print(f"✅ 互联网团队创建完成: {internet_team_path}")
    
    # 创建项目进展文件
    create_project_progress_file(args.project_path, team_type, project_type)
    print(f"✅ 项目进展概览文件创建完成")
    
    print(f"\n🎉 AI团队创建成功！")
    print(f"团队目录: {os.path.join(args.project_path, 'ai-team')}")

if __name__ == '__main__':
    main()