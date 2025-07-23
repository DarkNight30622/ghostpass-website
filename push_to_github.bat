@echo off
echo 🎨 GHOST PASS Website - GitHub Push Helper
echo ========================================

echo.
echo 📋 Step 1: Create GitHub Repository
echo Please follow these steps:
echo 1. Go to https://github.com/new
echo 2. Repository name: ghostpass-website
echo 3. Description: Modern, responsive website for GHOST PASS privacy tool
echo 4. Make it Public
echo 5. DO NOT initialize with README (we already have one)
echo 6. Click "Create repository"
echo.

pause

echo.
echo 📤 Step 2: Pushing Code to GitHub...
echo.

git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Success! Code pushed to GitHub
    echo.
    echo 🌐 Step 3: Enable GitHub Pages
    echo 1. Go to your repository on GitHub
    echo 2. Click "Settings" tab
    echo 3. Scroll down to "Pages" section
    echo 4. Under "Source", select "Deploy from a branch"
    echo 5. Choose "gh-pages" branch (will be created by GitHub Actions)
    echo 6. Click "Save"
    echo.
    echo 🎉 Your website will be available at:
    echo https://darknight30622.github.io/ghostpass-website/
    echo.
) else (
    echo.
    echo ❌ Failed to push code
    echo Please check:
    echo 1. Repository exists on GitHub
    echo 2. You have write permissions
    echo 3. Internet connection is working
    echo.
)

pause 