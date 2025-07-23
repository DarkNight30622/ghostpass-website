@echo off
echo 🎨 GHOST PASS Website - Automatic Deployment
echo ============================================

echo.
echo 🌐 Opening GitHub repository creation page...
start https://github.com/new?name=ghostpass-website^&description=Modern%2C%20responsive%20website%20for%20GHOST%20PASS%20privacy%20tool^&public=true

echo.
echo 📋 Please follow these steps:
echo 1. Repository name should be: ghostpass-website
echo 2. Description should be: Modern, responsive website for GHOST PASS privacy tool
echo 3. Make it Public
echo 4. DO NOT initialize with README (we already have one)
echo 5. Click "Create repository"
echo.

pause

echo.
echo 📤 Pushing code to GitHub...
echo.

git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Success! Code pushed to GitHub
    echo.
    echo 🌐 Opening repository...
    start https://github.com/DarkNight30622/ghostpass-website
    
    timeout /t 3 /nobreak >nul
    
    echo 🌐 Opening GitHub Pages settings...
    start https://github.com/DarkNight30622/ghostpass-website/settings/pages
    
    echo.
    echo 🌐 Setting up GitHub Pages:
    echo 1. Under "Source", select "Deploy from a branch"
    echo 2. Choose "gh-pages" branch (will be created by GitHub Actions)
    echo 3. Click "Save"
    echo.
    echo 🎉 Your website will be available at:
    echo https://darknight30622.github.io/ghostpass-website/
    echo.
    echo ⏳ Opening website in 30 seconds...
    timeout /t 30 /nobreak >nul
    start https://darknight30622.github.io/ghostpass-website/
    
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