#!/bin/bash
# Build script for Render.com static sites
# Injects environment variables into HTML files

set -e

# Each Render service sets its own SITE_URL, OG_TITLE and OG_IMAGE (per-domain since #17).
SITE_URL="${SITE_URL:-https://claudecodepm.com}"
OG_IMAGE="${OG_IMAGE:-og-claude.png}"
OG_TITLE="${OG_TITLE:-Claude Code and Codex for Product Managers}"

echo "Building with SITE_URL=$SITE_URL, OG_IMAGE=$OG_IMAGE, OG_TITLE=$OG_TITLE"

# Render from the source before replacing it; a failed substitution aborts the build.
OG_TITLE_SED=$(printf '%s' "$OG_TITLE" | sed 's/[&|\\]/\\&/g')
sed -e "s|__SITE_URL__|$SITE_URL|g" \
    -e "s|__OG_IMAGE__|$OG_IMAGE|g" \
    -e "s|__OG_TITLE__|$OG_TITLE_SED|g" index.html > index.html.build
mv index.html.build index.html

echo "Build complete!"
