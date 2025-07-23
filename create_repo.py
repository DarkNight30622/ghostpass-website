#!/usr/bin/env python3
"""
Script to create GitHub repository for GHOST PASS website
"""

import requests
import json
import os
import subprocess
import sys

def create_github_repo():
    """Create GitHub repository using GitHub API"""
    
    # Repository details
    repo_name = "ghostpass-website"
    repo_description = "Modern, responsive website for GHOST PASS privacy tool"
    repo_private = False
    
    # GitHub API endpoint
    api_url = f"https://api.github.com/user/repos"
    
    # Repository data
    repo_data = {
        "name": repo_name,
        "description": repo_description,
        "private": repo_private,
        "auto_init": False,
        "gitignore_template": "Node",
        "license_template": "mit",
        "has_issues": True,
        "has_wiki": True,
        "has_downloads": True,
        "has_projects": True
    }
    
    print("🚀 Creating GitHub repository...")
    print(f"Repository: {repo_name}")
    print(f"Description: {repo_description}")
    print(f"Visibility: {'Private' if repo_private else 'Public'}")
    
    # Check if GitHub token is available
    github_token = os.environ.get('GITHUB_TOKEN')
    
    if not github_token:
        print("\n❌ GitHub token not found!")
        print("Please set your GitHub token:")
        print("1. Go to GitHub Settings > Developer settings > Personal access tokens")
        print("2. Generate a new token with 'repo' permissions")
        print("3. Set the token: export GITHUB_TOKEN=your_token_here")
        print("\nOr create the repository manually:")
        print("1. Go to https://github.com/new")
        print("2. Name: ghostpass-website")
        print("3. Description: Modern, responsive website for GHOST PASS privacy tool")
        print("4. Make it public")
        print("5. Don't initialize with README (we already have one)")
        return False
    
    # Headers for GitHub API
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # Create repository
        response = requests.post(api_url, headers=headers, json=repo_data)
        
        if response.status_code == 201:
            repo_info = response.json()
            print(f"✅ Repository created successfully!")
            print(f"URL: {repo_info['html_url']}")
            return True
        else:
            print(f"❌ Failed to create repository: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating repository: {e}")
        return False

def push_to_github():
    """Push the website to GitHub"""
    
    print("\n📤 Pushing to GitHub...")
    
    try:
        # Add all files
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files staged")
        
        # Commit
        subprocess.run(["git", "commit", "-m", "🎨 Initial commit: Modern GHOST PASS website"], check=True)
        print("✅ Changes committed")
        
        # Push to main branch
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Code pushed to GitHub")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def setup_github_pages():
    """Instructions for setting up GitHub Pages"""
    
    print("\n🌐 Setting up GitHub Pages:")
    print("1. Go to your repository on GitHub")
    print("2. Click 'Settings' tab")
    print("3. Scroll down to 'Pages' section")
    print("4. Under 'Source', select 'Deploy from a branch'")
    print("5. Choose 'gh-pages' branch (will be created by GitHub Actions)")
    print("6. Click 'Save'")
    print("7. Wait a few minutes for deployment")
    print("8. Your site will be available at: https://darknight30622.github.io/ghostpass-website/")

def main():
    """Main function"""
    
    print("🎨 GHOST PASS Website Deployment")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("index.html"):
        print("❌ index.html not found!")
        print("Please run this script from the ghostpass-website directory")
        sys.exit(1)
    
    # Try to create repository
    if create_github_repo():
        # Push to GitHub
        if push_to_github():
            print("\n🎉 Website deployed successfully!")
            setup_github_pages()
        else:
            print("\n❌ Failed to push to GitHub")
    else:
        print("\n📝 Manual repository creation required")
        print("Please create the repository manually and then run:")
        print("git remote add origin https://github.com/DarkNight30622/ghostpass-website.git")
        print("git push -u origin main")

if __name__ == "__main__":
    main() 