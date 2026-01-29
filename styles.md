# Cursor for PMs — Style Guide

> Active design system for the Cursor for Product Managers landing page.

---

## Design Options

We currently have two design directions:

| Option | File | Aesthetic | Status |
|--------|------|-----------|--------|
| Studio | `option-c-studio.html` | Warm editorial | Active |
| Neural | `option-neural.html` | Dark tech brutalism | Active |

---

## Option: Studio (Warm Editorial)

### Color Palette

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| Cream | `#f7f5f0` | `--cream` | Page background |
| Cream Dark | `#ebe8e1` | `--cream-dark` | Borders, dividers |
| Ink | `#1a1a1a` | `--ink` | Primary text |
| Terracotta | `#c9553d` | `--terracotta` | Primary accent, CTAs |
| Terracotta Dark | `#a84632` | `--terracotta-dark` | Hover states |
| Sage | `#4a6741` | `--sage` | Secondary accent |

### Tailwind Config
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                cream: '#f7f5f0',
                'cream-dark': '#ebe8e1',
                ink: '#1a1a1a',
                terracotta: '#c9553d',
                'terracotta-dark': '#a84632',
                sage: '#4a6741',
            },
            fontFamily: {
                display: ['Playfair Display', 'serif'],
                body: ['Source Serif 4', 'serif'],
            }
        }
    }
}
```

### Typography

| Element | Font | Size | Weight | Class |
|---------|------|------|--------|-------|
| H1 (Hero) | Playfair Display | 5xl-7xl | 500 | `font-display text-5xl md:text-6xl lg:text-7xl font-medium` |
| H2 (Section) | Playfair Display | 3xl-4xl | 500 | `font-display text-3xl md:text-4xl font-medium` |
| H3 (Card) | Playfair Display | xl | 500 | `font-display text-xl font-medium` |
| Body | Source Serif 4 | base | 400 | `font-body text-base` |
| Small/Muted | Source Serif 4 | sm | 400 | `text-sm text-ink/70` |
| Label | Source Serif 4 | sm | 500 | `text-sm font-medium tracking-widest uppercase` |

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap" rel="stylesheet">
```

### Components

#### Primary Button
```html
<a class="bg-terracotta hover:bg-terracotta-dark text-white px-5 py-2.5 rounded-sm font-body text-sm font-medium transition-all duration-200 hover:shadow-lg flex items-center gap-2">
    <i class="fa-solid fa-rocket"></i>
    Join Waitlist — $1,950
</a>
```

#### Card
```html
<div class="bg-white border border-cream-dark rounded-sm p-8 hover:shadow-lg transition-shadow duration-300">
    <div class="w-14 h-14 bg-terracotta/10 rounded-full flex items-center justify-center mb-6">
        <i class="fa-solid fa-lightbulb text-2xl text-terracotta"></i>
    </div>
    <span class="text-terracotta font-display text-2xl font-semibold">01</span>
    <h3 class="font-display text-xl font-medium mt-4 mb-4">Title</h3>
    <p class="text-ink/70 leading-relaxed">Description</p>
</div>
```

#### Section Divider
```html
<div class="section-divider max-w-4xl mx-auto"></div>

<!-- CSS -->
.section-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #d4d0c8, transparent);
}
```

---

## Option: Neural (Dark Tech Brutalism)

### Color Palette

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| Void | `#0a0a0b` | `--void` | Page background |
| Surface | `#141416` | `--surface` | Elevated surfaces |
| Edge | `#2a2a2e` | `--edge` | Borders |
| Neon | `#00ff88` | `--neon` | Primary accent (green) |
| Hot | `#ff3366` | `--hot` | Secondary accent (pink) |
| Text | `#e8e8e8` | `--text` | Primary text |
| Muted | `#6b6b70` | `--muted` | Secondary text |

### Tailwind Config
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'void': '#0a0a0b',
                'surface': '#141416',
                'edge': '#2a2a2e',
                'neon': '#00ff88',
                'hot': '#ff3366',
                'text': '#e8e8e8',
                'muted': '#6b6b70',
            },
            fontFamily: {
                mono: ['Space Mono', 'monospace'],
                sans: ['IBM Plex Sans', 'sans-serif'],
                serif: ['Instrument Serif', 'serif'],
            }
        }
    }
}
```

### Typography

| Element | Font | Size | Weight | Class |
|---------|------|------|--------|-------|
| H1 (Hero) | Space Mono | 4xl-6xl | 700 | `font-mono text-4xl md:text-5xl lg:text-6xl font-bold` |
| H2 (Section) | Space Mono | 2xl-3xl | 700 | `font-mono text-2xl md:text-3xl font-bold` |
| H3 (Card) | Space Mono | lg | 700 | `font-mono font-bold text-lg` |
| Body | IBM Plex Sans | sm | 400 | `text-sm` |
| Code/Labels | Space Mono | sm/xs | 400 | `font-mono text-sm` |
| Accent | Instrument Serif | varies | 400 | `font-serif italic` |

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
```

### Visual Effects

#### Scanlines Overlay
```css
.scanlines::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0, 255, 136, 0.02) 2px,
        rgba(0, 255, 136, 0.02) 4px
    );
    pointer-events: none;
    z-index: 1000;
}
```

#### Glitch Hover Effect
```css
@keyframes glitch {
    0% { transform: translate(0); }
    20% { transform: translate(-2px, 2px); }
    40% { transform: translate(-2px, -2px); }
    60% { transform: translate(2px, 2px); }
    80% { transform: translate(2px, -2px); }
    100% { transform: translate(0); }
}
.glitch:hover {
    animation: glitch 0.3s ease;
    text-shadow: 2px 0 #ff3366, -2px 0 #00ff88;
}
```

#### Glow Pulse
```css
@keyframes glow-pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.3); }
    50% { box-shadow: 0 0 40px rgba(0, 255, 136, 0.6); }
}
.glow-pulse {
    animation: glow-pulse 2s ease-in-out infinite;
}
```

#### Grid Background
```css
.grid-bg {
    background-image:
        linear-gradient(rgba(42, 42, 46, 0.3) 1px, transparent 1px),
        linear-gradient(90deg, rgba(42, 42, 46, 0.3) 1px, transparent 1px);
    background-size: 40px 40px;
}
```

### Components

#### Primary Button
```html
<a class="bg-neon hover:bg-neon/90 text-void px-5 py-2.5 font-mono text-sm font-bold transition-all duration-200 glow-pulse flex items-center gap-2">
    <i class="fa-solid fa-terminal"></i>
    JOIN_WAITLIST
</a>
```

#### Card
```html
<div class="border border-edge bg-surface p-6 hover:border-neon transition-colors group">
    <div class="font-mono text-neon text-xs mb-4">[01]</div>
    <div class="w-12 h-12 border border-neon flex items-center justify-center mb-4 group-hover:bg-neon group-hover:text-void transition-colors">
        <i class="fa-solid fa-lightbulb text-xl"></i>
    </div>
    <h3 class="font-mono font-bold text-lg mb-3">TITLE</h3>
    <p class="text-muted text-sm leading-relaxed">Description</p>
</div>
```

#### ASCII Border Box
```html
<div class="ascii-border bg-surface p-6">
    Content here
</div>

<!-- CSS -->
.ascii-border {
    border: 1px solid #2a2a2e;
    position: relative;
}
.ascii-border::before {
    content: '┌';
    position: absolute;
    top: -1px;
    left: -1px;
    color: #00ff88;
    font-family: 'Space Mono', monospace;
}
.ascii-border::after {
    content: '┘';
    position: absolute;
    bottom: -1px;
    right: -1px;
    color: #00ff88;
    font-family: 'Space Mono', monospace;
}
```

---

## Shared Patterns

### Company Logo Grayscale Effect
```css
.company-logo {
    filter: grayscale(100%);
    opacity: 0.6;
    transition: all 0.3s ease;
}
.company-logo:hover {
    filter: grayscale(0%);
    opacity: 1;
}
```

### Fade In Animation
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.animate-fade-in {
    animation: fadeInUp 0.6s ease-out forwards;
}
.animate-delay-1 { animation-delay: 0.1s; opacity: 0; }
.animate-delay-2 { animation-delay: 0.2s; opacity: 0; }
.animate-delay-3 { animation-delay: 0.3s; opacity: 0; }
.animate-delay-4 { animation-delay: 0.4s; opacity: 0; }
```

### Font Awesome Icons Used

| Icon | Class | Usage |
|------|-------|-------|
| Rocket | `fa-solid fa-rocket` | CTA buttons |
| Calendar | `fa-solid fa-calendar-days` | Date badge |
| Star | `fa-solid fa-star` | Ratings |
| Lightbulb | `fa-solid fa-lightbulb` | Brainstorm module |
| Cubes | `fa-solid fa-cubes` | Prototype module |
| Wand | `fa-solid fa-wand-magic-sparkles` | Cursor module |
| Robot | `fa-solid fa-robot` | AI module |
| Briefcase | `fa-solid fa-briefcase` | Job title |
| Video | `fa-solid fa-video` | Live sessions |
| Users | `fa-solid fa-users` | Community |
| Infinity | `fa-solid fa-infinity` | Lifetime access |
| Slack | `fa-brands fa-slack` | Slack community |
| Certificate | `fa-solid fa-certificate` | Certification |
| Shield | `fa-solid fa-shield-halved` | Guarantee |
| LinkedIn | `fa-brands fa-linkedin` | Social link |
| X/Twitter | `fa-brands fa-x-twitter` | Social link |
| Terminal | `fa-solid fa-terminal` | Neural theme CTA |

---

## Layout Standards

### Container
```html
<div class="max-w-6xl mx-auto px-6">
```

### Section Spacing
- Hero: `pt-20 pb-24`
- Content sections: `py-24`
- Compact sections: `py-16`

### Grid
- 4-column: `grid md:grid-cols-2 lg:grid-cols-4 gap-6`
- 2-column: `grid md:grid-cols-2 gap-8`
- 3-column: `grid md:grid-cols-3 gap-6`
