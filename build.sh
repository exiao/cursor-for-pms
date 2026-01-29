#!/bin/bash
# Build script for Render.com static sites
# Injects environment variables into HTML files

# Default values (override with Render environment variables)
SITE_URL="${SITE_URL:-https://cursorpm.com}"
OG_IMAGE="${OG_IMAGE:-og-cursor.png}"
OG_TITLE="${OG_TITLE:-Cursor for Product Managers}"

FAVICON_TYPE="${FAVICON:-cursor}"
echo "Building with SITE_URL=$SITE_URL, OG_IMAGE=$OG_IMAGE, OG_TITLE=$OG_TITLE, FAVICON=$FAVICON_TYPE"

# Replace placeholders in index.html
sed -i.bak "s|__SITE_URL__|$SITE_URL|g" index.html
sed -i.bak "s|__OG_IMAGE__|$OG_IMAGE|g" index.html
sed -i.bak "s|__OG_TITLE__|$OG_TITLE|g" index.html

# Replace favicon only if FAVICON=terminal (cursor is the default in HTML)
if [ "$FAVICON_TYPE" = "terminal" ]; then
    sed -i.bak "s|favicon-cursor.svg|favicon-terminal.svg|g" index.html
fi

# Clean up backup files
rm -f *.bak

echo "Build complete!"
