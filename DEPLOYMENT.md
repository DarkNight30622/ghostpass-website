# 🚀 GHOST PASS Website Deployment Guide

This guide will help you deploy the GHOST PASS website to GitHub Pages.

## 📋 Prerequisites

- GitHub account
- Git installed on your computer
- Basic knowledge of Git commands

## 🎯 Quick Deployment

### Option 1: Manual Repository Creation (Recommended)

1. **Create GitHub Repository**
   - Go to [https://github.com/new](https://github.com/new)
   - Repository name: `ghostpass-website`
   - Description: `Modern, responsive website for GHOST PASS privacy tool`
   - Make it **Public**
   - **Don't** initialize with README (we already have one)
   - Click "Create repository"

2. **Push Your Code**
   ```bash
   # Make sure you're in the ghostpass-website directory
   cd ghostpass-website
   
   # Add remote origin
   git remote add origin https://github.com/DarkNight30622/ghostpass-website.git
   
   # Push to GitHub
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click **Settings** tab
   - Scroll down to **Pages** section
   - Under **Source**, select **Deploy from a branch**
   - Choose **gh-pages** branch (will be created by GitHub Actions)
   - Click **Save**

4. **Wait for Deployment**
   - GitHub Actions will automatically build and deploy your site
   - Check the **Actions** tab to monitor progress
   - Your site will be available at: `https://darknight30622.github.io/ghostpass-website/`

### Option 2: Using GitHub CLI

If you have GitHub CLI installed:

```bash
# Create repository
gh repo create ghostpass-website --public --description "Modern, responsive website for GHOST PASS privacy tool"

# Push code
git remote add origin https://github.com/DarkNight30622/ghostpass-website.git
git push -u origin main
```

### Option 3: Using Python Script

```bash
# Install requests if needed
pip install requests

# Set GitHub token (optional)
export GITHUB_TOKEN=your_token_here

# Run deployment script
python create_repo.py
```

## 🔧 Customization

### Update Repository URL

If you want to use a different repository name or username:

1. **Update HTML file**
   ```html
   <!-- In index.html, replace all instances of: -->
   https://github.com/DarkNight30622/ghostpass-website
   
   <!-- With your repository URL: -->
   https://github.com/yourusername/your-repo-name
   ```

2. **Update CSS file**
   ```css
   /* In css/style.css, update any hardcoded URLs */
   ```

3. **Update README.md**
   ```markdown
   <!-- Update all GitHub links in README.md -->
   ```

### Custom Domain (Optional)

1. **Add Custom Domain**
   - Go to repository **Settings** > **Pages**
   - Enter your custom domain (e.g., `ghostpass.com`)
   - Click **Save**

2. **Configure DNS**
   - Add CNAME record pointing to `darknight30622.github.io`
   - Wait for DNS propagation (up to 24 hours)

3. **Add CNAME File**
   ```bash
   # Create CNAME file in your repository
   echo "yourdomain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

## 🐛 Troubleshooting

### Common Issues

1. **Repository not found**
   - Make sure the repository exists on GitHub
   - Check the repository URL is correct
   - Ensure you have write permissions

2. **GitHub Pages not working**
   - Check the **Actions** tab for build errors
   - Verify the **gh-pages** branch was created
   - Wait a few minutes for deployment

3. **Website not loading**
   - Check the GitHub Pages URL is correct
   - Verify the repository is public
   - Check browser console for errors

4. **Styling issues**
   - Clear browser cache
   - Check CSS file paths are correct
   - Verify all assets are committed

### Debug Commands

```bash
# Check git status
git status

# Check remote URL
git remote -v

# Check branch
git branch

# Check GitHub Pages status
curl -I https://darknight30622.github.io/ghostpass-website/
```

## 📊 Performance Optimization

### Before Deployment

1. **Minify CSS/JS** (optional)
   ```bash
   # Install minifier
   npm install -g clean-css-cli uglify-js
   
   # Minify CSS
   cleancss -o css/style.min.css css/style.css
   
   # Minify JS
   uglifyjs js/script.js -o js/script.min.js
   ```

2. **Optimize Images**
   - Use WebP format for better compression
   - Compress SVG files
   - Use appropriate image sizes

3. **Enable Compression**
   - GitHub Pages automatically serves gzipped content
   - No additional configuration needed

### After Deployment

1. **Test Performance**
   - Use Google PageSpeed Insights
   - Check Core Web Vitals
   - Test on multiple devices

2. **Monitor Analytics**
   - Add Google Analytics (optional)
   - Monitor GitHub Pages traffic
   - Track user engagement

## 🔄 Updates and Maintenance

### Regular Updates

1. **Update Content**
   ```bash
   # Make changes to files
   git add .
   git commit -m "Update website content"
   git push
   ```

2. **Update Dependencies**
   - Check for Font Awesome updates
   - Update Google Fonts if needed
   - Review security updates

3. **Backup**
   - Repository is automatically backed up on GitHub
   - Consider local backup for critical changes

### Version Control

```bash
# Create feature branch
git checkout -b feature/new-section

# Make changes
git add .
git commit -m "Add new section"

# Push feature branch
git push origin feature/new-section

# Create pull request on GitHub
# Merge after review
```

## 📞 Support

- **GitHub Issues**: [Report bugs](https://github.com/DarkNight30622/ghostpass-website/issues)
- **GitHub Discussions**: [Get help](https://github.com/DarkNight30622/ghostpass-website/discussions)
- **Documentation**: [GHOST PASS Docs](https://github.com/DarkNight30622/GhostPass)

## 🎉 Success!

Once deployed, your website will be available at:
**https://darknight30622.github.io/ghostpass-website/**

Share this URL to promote GHOST PASS! 🔒 