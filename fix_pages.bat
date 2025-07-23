@echo off
echo 🔧 Fixing GitHub Pages 404 Error
echo ================================

echo.
echo 📋 The issue is that GitHub Pages needs to be enabled manually.
echo.

echo 🌐 Opening GitHub Pages settings...
start https://github.com/DarkNight30622/ghostpass-website/settings/pages

echo.
echo 📋 Please follow these steps:
echo 1. Under "Source", select "Deploy from a branch"
echo 2. Choose "gh-pages" branch (will be created by GitHub Actions)
echo 3. Click "Save"
echo.

echo 🌐 Opening GitHub Actions to check deployment status...
start https://github.com/DarkNight30622/ghostpass-website/actions

echo.
echo ⏳ Waiting for deployment to complete...
echo This may take 2-5 minutes.
echo.

echo 🌐 Opening the website URL...
start https://darknight30622.github.io/ghostpass-website/

echo.
echo 📋 If the website still shows 404:
echo 1. Check the Actions tab for any build errors
echo 2. Make sure GitHub Pages is enabled
echo 3. Wait a few more minutes for deployment
echo 4. Try refreshing the page
echo.

pause 