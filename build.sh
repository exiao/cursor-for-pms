#!/bin/bash
# Build script for Render.com static sites
# Injects environment variables into HTML files

set -e

# Only the domain and title vary (per-domain OG_TITLE since #17). The image is fixed.
SITE_URL="${SITE_URL:-https://claudecodepm.com}"
OG_IMAGE="og-claude.png"
OG_TITLE="${OG_TITLE:-Claude Code and Codex for Product Managers}"

echo "Building with SITE_URL=$SITE_URL, OG_IMAGE=$OG_IMAGE, OG_TITLE=$OG_TITLE"

# Render from the source before replacing it; a failed substitution aborts the build.
OG_TITLE_SED=$(printf '%s' "$OG_TITLE" | sed 's/[&|\\]/\\&/g')
sed -e "s|__SITE_URL__|$SITE_URL|g" \
    -e "s|__OG_IMAGE__|$OG_IMAGE|g" \
    -e "s|__OG_TITLE__|$OG_TITLE_SED|g" index.html > index.html.build
mv index.html.build index.html

echo "Build complete!"
