#!/usr/bin/env python3
"""
Quick GHOST PASS Website Deployment
Opens GitHub repository creation and guides through deployment
"""

import webbrowser
import subprocess
import time
import sys
import os

def open_github_create():
    """Open GitHub repository creation page"""
    print("🌐 Opening GitHub repository creation page...")
    
    # Pre-filled URL for repository creation
    repo_url = "https://github.com/new?name=ghostpass-website&description=Modern%2C%20responsive%20website%20for%20GHOST%20PASS%20privacy%20tool&public=true"
    
    try:
        webbrowser.open(repo_url)
        print("✅ GitHub repository creation page opened!")
        return True
    except:
        print("❌ Could not open browser automatically")
        print(f"Please visit: {repo_url}")
        return False

def wait_for_user():
    """Wait for user to create repository"""
    print("\n📋 Please follow these steps:")
    print("1. Repository name should be: ghostpass-website")
    print("2. Description should be: Modern, responsive website for GHOST PASS privacy tool")
    print("3. Make it Public")
    print("4. DO NOT initialize with README (we already have one)")
    print("5. Click 'Create repository'")
    print()
    
    input("Press Enter when you've created the repository...")

def push_code():
    """Push code to GitHub"""
    print("\n📤 Pushing code to GitHub...")
    
    try:
        # Check if remote exists
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        
        if "origin" not in result.stdout:
            print("❌ Remote origin not found!")
            print("Please make sure you've created the repository on GitHub")
            return False
        
        # Push to main branch
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Code pushed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def open_repository():
    """Open the repository in browser"""
    repo_url = "https://github.com/DarkNight30622/ghostpass-website"
    print(f"\n🌐 Opening repository: {repo_url}")
    
    try:
        webbrowser.open(repo_url)
    except:
        print(f"Please visit: {repo_url}")

def open_pages_settings():
    """Open GitHub Pages settings"""
    pages_url = "https://github.com/DarkNight30622/ghostpass-website/settings/pages"
    print(f"\n🌐 Opening GitHub Pages settings: {pages_url}")
    
    try:
        webbrowser.open(pages_url)
    except:
        print(f"Please visit: {pages_url}")

def main():
    """Main deployment function"""
    print("🎨 GHOST PASS Website - Quick Deployment")
    print("=" * 45)
    
    # Check if we're in the right directory
    if not os.path.exists("index.html"):
        print("❌ index.html not found!")
        print("Please run this script from the ghostpass-website directory")
        sys.exit(1)
    
    # Check git status
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        if "nothing to commit" not in result.stdout:
            print("⚠️  You have uncommitted changes!")
            print("Please commit your changes first:")
            print("git add .")
            print("git commit -m 'Your commit message'")
            sys.exit(1)
    except:
        print("⚠️  Could not check git status")
    
    # Step 1: Open GitHub repository creation
    if not open_github_create():
        sys.exit(1)
    
    # Step 2: Wait for user to create repository
    wait_for_user()
    
    # Step 3: Push code
    if not push_code():
        print("\n❌ Failed to push code")
        print("Please check:")
        print("1. Repository exists on GitHub")
        print("2. You have write permissions")
        print("3. Internet connection is working")
        sys.exit(1)
    
    # Step 4: Open repository
    open_repository()
    
    # Step 5: Guide through GitHub Pages setup
    print("\n🌐 Setting up GitHub Pages:")
    print("1. Click 'Settings' tab in your repository")
    print("2. Scroll down to 'Pages' section")
    print("3. Under 'Source', select 'Deploy from a branch'")
    print("4. Choose 'gh-pages' branch (will be created by GitHub Actions)")
    print("5. Click 'Save'")
    
    # Open pages settings
    time.sleep(3)
    open_pages_settings()
    
    # Final success message
    print("\n🎉 Deployment in Progress!")
    print("=" * 30)
    print("Your website will be available at:")
    print("https://darknight30622.github.io/ghostpass-website/")
    print("\n⏳ GitHub Actions will automatically build and deploy your site")
    print("Check the 'Actions' tab to monitor progress")
    
    # Wait and open the website
    print("\n⏳ Opening website in 30 seconds...")
    time.sleep(30)
    
    website_url = "https://darknight30622.github.io/ghostpass-website/"
    try:
        webbrowser.open(website_url)
        print(f"✅ Website opened: {website_url}")
    except:
        print(f"Please visit: {website_url}")

if __name__ == "__main__":
    main() 