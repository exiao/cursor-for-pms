#!/bin/bash
# Build script for Render.com static sites
# Injects environment variables into HTML files

# Default values (override with Render environment variables)
SITE_URL="${SITE_URL:-https://claudecodepm.com}"
OG_IMAGE="${OG_IMAGE:-og-claude.png}"
OG_TITLE="${OG_TITLE:-Claude Code and Codex for Product Managers}"

echo "Building with SITE_URL=$SITE_URL, OG_IMAGE=$OG_IMAGE, OG_TITLE=$OG_TITLE"

# Replace placeholders in index.html
sed -i.bak "s|__SITE_URL__|$SITE_URL|g" index.html
sed -i.bak "s|__OG_IMAGE__|$OG_IMAGE|g" index.html
OG_TITLE_SED=$(printf '%s' "$OG_TITLE" | sed 's/[&|\\]/\\&/g')
sed -i.bak "s|__OG_TITLE__|$OG_TITLE_SED|g" index.html

# Clean up backup files
rm -f *.bak

echo "Build complete!"
