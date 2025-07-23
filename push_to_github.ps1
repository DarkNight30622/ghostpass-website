Write-Host "🎨 GHOST PASS Website - GitHub Push Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host ""
Write-Host "📋 Step 1: Create GitHub Repository" -ForegroundColor Yellow
Write-Host "Please follow these steps:" -ForegroundColor White
Write-Host "1. Go to https://github.com/new" -ForegroundColor Gray
Write-Host "2. Repository name: ghostpass-website" -ForegroundColor Gray
Write-Host "3. Description: Modern, responsive website for GHOST PASS privacy tool" -ForegroundColor Gray
Write-Host "4. Make it Public" -ForegroundColor Gray
Write-Host "5. DO NOT initialize with README (we already have one)" -ForegroundColor Gray
Write-Host "6. Click 'Create repository'" -ForegroundColor Gray
Write-Host ""

Read-Host "Press Enter when you've created the repository"

Write-Host ""
Write-Host "📤 Step 2: Pushing Code to GitHub..." -ForegroundColor Yellow
Write-Host ""

try {
    git push -u origin main
    
    Write-Host ""
    Write-Host "✅ Success! Code pushed to GitHub" -ForegroundColor Green
    Write-Host ""
    Write-Host "🌐 Step 3: Enable GitHub Pages" -ForegroundColor Yellow
    Write-Host "1. Go to your repository on GitHub" -ForegroundColor Gray
    Write-Host "2. Click 'Settings' tab" -ForegroundColor Gray
    Write-Host "3. Scroll down to 'Pages' section" -ForegroundColor Gray
    Write-Host "4. Under 'Source', select 'Deploy from a branch'" -ForegroundColor Gray
    Write-Host "5. Choose 'gh-pages' branch (will be created by GitHub Actions)" -ForegroundColor Gray
    Write-Host "6. Click Save" -ForegroundColor Gray
    Write-Host ""
    Write-Host "🎉 Your website will be available at:" -ForegroundColor Green
    Write-Host "https://darknight30622.github.io/ghostpass-website/" -ForegroundColor Cyan
    Write-Host ""
    
} catch {
    Write-Host ""
    Write-Host "❌ Failed to push code" -ForegroundColor Red
    Write-Host "Please check:" -ForegroundColor Yellow
    Write-Host "1. Repository exists on GitHub" -ForegroundColor Gray
    Write-Host "2. You have write permissions" -ForegroundColor Gray
    Write-Host "3. Internet connection is working" -ForegroundColor Gray
    Write-Host ""
}

Read-Host "Press Enter to exit" 