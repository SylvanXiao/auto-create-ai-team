#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive test suite for Auto-Create-AI-Team Skill
"""

import os
import sys
import tempfile
import shutil
import subprocess
import unittest

class TestAutoCreateAITeam(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.skill_path = "/root/.openclaw/workspace/skills/auto-create-ai-team"
        self.create_ai_team_script = os.path.join(self.skill_path, "create_ai_team.py")
        
    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.test_dir)
        
    def test_basic_interview_project(self):
        """Test creating AI team for interview simulator project"""
        project_path = os.path.join(self.test_dir, "test-interview-project")
        os.makedirs(project_path)
        
        # Run the skill
        result = subprocess.run([
            "python3", self.create_ai_team_script,
            "--project-path", project_path,
            "--project-type", "interview",
            "--team-type", "dual"
        ], capture_output=True, text=True)
        
        # Check if successful
        self.assertEqual(result.returncode, 0)
        self.assertIn("AI团队创建成功", result.stdout)
        
        # Check if directories were created
        ai_team_dir = os.path.join(project_path, "ai-team")
        self.assertTrue(os.path.exists(ai_team_dir))
        
        internal_team = os.path.join(ai_team_dir, "internal-team")
        self.assertTrue(os.path.exists(internal_team))
        
        internet_team = os.path.join(ai_team_dir, "internet-team")  
        self.assertTrue(os.path.exists(internet_team))
        
        # Check config files
        config_file = os.path.join(internal_team, "team-info", "AI_TEAM_CONFIG.md")
        self.assertTrue(os.path.exists(config_file))
        
    def test_generic_project_single_team(self):
        """Test creating single team for generic project"""
        project_path = os.path.join(self.test_dir, "test-generic-project")
        os.makedirs(project_path)
        
        result = subprocess.run([
            "python3", self.create_ai_team_script,
            "--project-path", project_path,
            "--project-type", "generic",
            "--team-type", "single"
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("AI团队创建成功", result.stdout)
        
        # Check only internal team exists
        ai_team_dir = os.path.join(project_path, "ai-team")
        internal_team = os.path.join(ai_team_dir, "internal-team")
        internet_team = os.path.join(ai_team_dir, "internet-team")
        
        self.assertTrue(os.path.exists(internal_team))
        self.assertFalse(os.path.exists(internet_team))
        
    def test_auto_detection(self):
        """Test automatic project type detection"""
        # Test interview project detection
        interview_project = os.path.join(self.test_dir, "my-interview-simulator")
        os.makedirs(interview_project)
        
        result = subprocess.run([
            "python3", self.create_ai_team_script,
            "--project-path", interview_project,
            "--auto-detect"
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        # Should detect as interview project and create dual team
        
    def test_error_handling_invalid_path(self):
        """Test error handling for invalid project path"""
        invalid_path = "/nonexistent/path"
        
        result = subprocess.run([
            "python3", self.create_ai_team_script,
            "--project-path", invalid_path,
            "--project-type", "generic"
        ], capture_output=True, text=True)
        
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("错误", result.stdout)
        
    def test_progress_file_creation(self):
        """Test PROJECT_PROGRESS.md file creation"""
        project_path = os.path.join(self.test_dir, "test-progress-project")
        os.makedirs(project_path)
        
        subprocess.run([
            "python3", self.create_ai_team_script,
            "--project-path", project_path,
            "--project-type", "interview",
            "--team-type", "dual"
        ], capture_output=True, text=True)
        
        progress_file = os.path.join(project_path, "ai-team", "PROJECT_PROGRESS.md")
        self.assertTrue(os.path.exists(progress_file))
        
        # Check content
        with open(progress_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("项目进展概览", content)
            self.assertIn("双团队架构", content)

if __name__ == '__main__':
    unittest.main()