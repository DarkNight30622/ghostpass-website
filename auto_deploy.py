#!/usr/bin/env python3
"""
Automatic GHOST PASS Website Deployment Script
Creates GitHub repository and pushes code automatically
"""

import requests
import json
import os
import subprocess
import sys
import time
import webbrowser
from urllib.parse import urlparse

def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import requests
        return True
    except ImportError:
        print("❌ 'requests' library not found!")
        print("Installing requests...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
            print("✅ requests installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requests")
            return False

def get_github_token():
    """Get GitHub token from environment or prompt user"""
    token = os.environ.get('GITHUB_TOKEN')
    
    if not token:
        print("\n🔑 GitHub Token Required")
        print("To create a GitHub token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select 'repo' permissions")
        print("4. Copy the token")
        print()
        
        token = input("Enter your GitHub token: ").strip()
        
        if not token:
            print("❌ No token provided. Exiting.")
            return None
            
    return token

def create_github_repo(token):
    """Create GitHub repository using API"""
    repo_name = "ghostpass-website"
    repo_description = "Modern, responsive website for GHOST PASS privacy tool"
    
    api_url = "https://api.github.com/user/repos"
    
    repo_data = {
        "name": repo_name,
        "description": repo_description,
        "private": False,
        "auto_init": False,
        "has_issues": True,
        "has_wiki": True,
        "has_downloads": True,
        "has_projects": True
    }
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print(f"🚀 Creating repository: {repo_name}")
    
    try:
        response = requests.post(api_url, headers=headers, json=repo_data)
        
        if response.status_code == 201:
            repo_info = response.json()
            print(f"✅ Repository created successfully!")
            print(f"URL: {repo_info['html_url']}")
            return repo_info
        elif response.status_code == 422:
            print("⚠️  Repository already exists!")
            # Try to get existing repository info
            get_url = f"https://api.github.com/repos/DarkNight30622/{repo_name}"
            get_response = requests.get(get_url, headers=headers)
            if get_response.status_code == 200:
                return get_response.json()
            else:
                print("❌ Cannot access existing repository")
                return None
        else:
            print(f"❌ Failed to create repository: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error creating repository: {e}")
        return None

def push_to_github(repo_info):
    """Push code to GitHub repository"""
    if not repo_info:
        return False
        
    print("\n📤 Pushing code to GitHub...")
    
    try:
        # Check if remote is already set
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        
        if "origin" not in result.stdout:
            # Add remote origin
            repo_url = repo_info['clone_url']
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            print("✅ Remote origin added")
        
        # Push to main branch
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Code pushed successfully!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def enable_github_pages(token, repo_info):
    """Enable GitHub Pages via API"""
    if not repo_info:
        return False
        
    print("\n🌐 Enabling GitHub Pages...")
    
    repo_name = repo_info['name']
    owner = repo_info['owner']['login']
    
    # GitHub Pages API endpoint
    pages_url = f"https://api.github.com/repos/{owner}/{repo_name}/pages"
    
    pages_data = {
        "source": {
            "branch": "gh-pages",
            "path": "/"
        }
    }
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.post(pages_url, headers=headers, json=pages_data)
        
        if response.status_code in [201, 409]:  # 409 means already enabled
            print("✅ GitHub Pages enabled!")
            return True
        else:
            print(f"⚠️  Could not enable GitHub Pages via API: {response.status_code}")
            print("You'll need to enable it manually in the repository settings")
            return False
            
    except Exception as e:
        print(f"⚠️  Error enabling GitHub Pages: {e}")
        print("You'll need to enable it manually in the repository settings")
        return False

def open_repository(repo_info):
    """Open repository in browser"""
    if repo_info and 'html_url' in repo_info:
        url = repo_info['html_url']
        print(f"\n🌐 Opening repository: {url}")
        try:
            webbrowser.open(url)
        except:
            print(f"Please visit: {url}")

def wait_for_deployment(repo_info):
    """Wait for GitHub Actions deployment"""
    if not repo_info:
        return
        
    print("\n⏳ Waiting for GitHub Actions deployment...")
    print("This may take a few minutes...")
    
    # Check Actions status
    owner = repo_info['owner']['login']
    repo_name = repo_info['name']
    actions_url = f"https://github.com/{owner}/{repo_name}/actions"
    
    print(f"Monitor deployment at: {actions_url}")
    
    # Wait a bit for the workflow to start
    time.sleep(5)
    
    try:
        webbrowser.open(actions_url)
    except:
        print(f"Please visit: {actions_url}")

def main():
    """Main deployment function"""
    print("🎨 GHOST PASS Website - Automatic Deployment")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("index.html"):
        print("❌ index.html not found!")
        print("Please run this script from the ghostpass-website directory")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependencies not available")
        sys.exit(1)
    
    # Get GitHub token
    token = get_github_token()
    if not token:
        sys.exit(1)
    
    # Create repository
    repo_info = create_github_repo(token)
    if not repo_info:
        print("❌ Failed to create repository")
        sys.exit(1)
    
    # Push code
    if not push_to_github(repo_info):
        print("❌ Failed to push code")
        sys.exit(1)
    
    # Enable GitHub Pages
    enable_github_pages(token, repo_info)
    
    # Open repository
    open_repository(repo_info)
    
    # Wait for deployment
    wait_for_deployment(repo_info)
    
    # Final success message
    print("\n🎉 Deployment Complete!")
    print("=" * 50)
    print("Your website will be available at:")
    print(f"https://{repo_info['owner']['login']}.github.io/{repo_info['name']}/")
    print("\n📋 Next steps:")
    print("1. Wait for GitHub Actions to complete (check Actions tab)")
    print("2. If GitHub Pages wasn't enabled automatically, enable it manually")
    print("3. Share your website URL!")
    
    # Open the website URL after a delay
    website_url = f"https://{repo_info['owner']['login']}.github.io/{repo_info['name']}/"
    print(f"\n⏳ Opening website in 10 seconds: {website_url}")
    time.sleep(10)
    
    try:
        webbrowser.open(website_url)
    except:
        print(f"Please visit: {website_url}")

if __name__ == "__main__":
    main() 