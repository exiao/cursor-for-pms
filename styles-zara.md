# Zara Design System

> Style guide updated January 2026 based on analysis of zara.com's current design patterns.

---

## Color Palette

### Primary Colors
| Name | Hex | Usage |
|------|-----|-------|
| Black | `#000000` | Primary text, logo, headers |
| White | `#FFFFFF` | Background |
| Accent Green | `#00A878` | Links, highlights, CTAs, numbered lists |

### Neutral Colors
| Name | Hex | Usage |
|------|-----|-------|
| Light Gray | `#FAFAFA` | Section backgrounds |
| Border Gray | `#E0E0E0` | Borders, dividers |
| Text Muted | `#757575` | Secondary text |
| Text Light | `#9E9E9E` | Tertiary text, captions |

### Tailwind Config
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        'zara-white': '#FFFFFF',
        'zara-light': '#FAFAFA',
        'zara-border': '#E0E0E0',
        'zara-black': '#000000',
        'zara-accent': '#00A878',
        'zara-muted': '#757575',
        'zara-light-muted': '#9E9E9E',
      },
      letterSpacing: {
        'ultra-wide': '0.25em',
        'mega-wide': '0.35em',
      }
    }
  }
}
```

---

## Typography

### Font Stacks
```css
/* Body text */
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
font-weight: 300;

/* Headlines (italic serif) */
font-family: 'Instrument Serif', Georgia, serif;
font-style: italic;
```

### Hierarchy

| Element | Size | Weight | Line Height | Letter Spacing | Tailwind Class |
|---------|------|--------|-------------|----------------|----------------|
| H1 (Hero) | 48px / 3rem | 400 (Normal) | 1.1 | -0.02em | `text-5xl font-normal tracking-tight` |
| H2 (Section) | 24px / 1.5rem | 400 (Normal) | 1.2 | -0.01em | `text-2xl font-normal` |
| H3 (Card) | 15px / 0.9375rem | 500 (Medium) | 1.3 | 0 | `text-[15px] font-medium` |
| Body | 12px / 0.75rem | 400 (Normal) | 1.5 | 0.02em | `text-xs tracking-wide` |
| Caption | 11px / 0.6875rem | 400 (Normal) | 1.4 | 0.05em | `text-[11px] tracking-wider` |
| Nav/Button | 12px / 0.75rem | 500 (Medium) | 1 | 0.1em | `text-xs font-medium tracking-widest uppercase` |

### Style Notes
- **Minimalist approach**: Zara uses very little typographic variation
- **All caps**: Navigation, buttons, and category labels are uppercase
- **Tight spacing**: Headlines use negative letter-spacing
- **Clean hierarchy**: Size differences are subtle, weight does the work

---

## Spacing System

### Base Unit: 4px

| Token | Value | Tailwind |
|-------|-------|----------|
| xs | 4px | `p-1` / `m-1` |
| sm | 8px | `p-2` / `m-2` |
| md | 16px | `p-4` / `m-4` |
| lg | 24px | `p-6` / `m-6` |
| xl | 32px | `p-8` / `m-8` |
| 2xl | 48px | `p-12` / `m-12` |
| 3xl | 64px | `p-16` / `m-16` |
| 4xl | 96px | `p-24` / `m-24` |

### Section Spacing
- **Section Padding**: `py-24` (96px vertical)
- **Container Max Width**: `max-w-6xl` (1152px)
- **Container Horizontal Padding**: `px-6` (24px)
- **Card Grid Gap**: `gap-6` (24px)

### Layout Grid
- **Desktop**: 4-column grid (`grid-cols-4`)
- **Tablet**: 2-column grid (`md:grid-cols-2`)
- **Mobile**: Single column (`grid-cols-1`)

---

## Component Patterns

### Buttons

#### Primary Button (Black)
```html
<button class="bg-black text-white px-8 py-4 text-xs font-medium tracking-widest uppercase hover:bg-gray-900 transition-colors duration-200">
  Shop Now
</button>
```
- Background: `#000000`
- Text: `#FFFFFF`
- Border Radius: `0px` (sharp corners)
- Padding: `16px 32px` (py-4 px-8)
- Shadow: None
- Hover: Slight lighten (`bg-gray-900`)

#### Secondary Button (Outlined)
```html
<button class="bg-white text-black border border-black px-8 py-4 text-xs font-medium tracking-widest uppercase hover:bg-black hover:text-white transition-colors duration-200">
  View More
</button>
```
- Background: `#FFFFFF`
- Text: `#000000`
- Border: `1px solid #000000`
- Border Radius: `0px`
- Hover: Invert colors

#### Text Link
```html
<a class="text-xs font-medium tracking-widest uppercase underline underline-offset-4 hover:text-zara-accent transition-colors">
  Discover
</a>
```

### Cards

#### Product Card
```html
<div class="group cursor-pointer">
  <div class="aspect-[3/4] overflow-hidden bg-zara-gray-100">
    <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
  </div>
  <div class="pt-4">
    <h3 class="text-[15px] font-medium">Product Name</h3>
    <p class="text-xs text-zara-gray-600 mt-1">$99.00</p>
  </div>
</div>
```
- No border, no shadow
- Image hover: subtle scale (`scale-105`)
- Transition: `500ms`
- Aspect ratio: 3:4 portrait

#### Feature Card (From Original)
```html
<div class="bg-white border border-zara-gray-200 p-8 hover:shadow-lg transition-shadow duration-300">
  <span class="text-zara-accent text-2xl font-semibold">01</span>
  <h3 class="text-[15px] font-medium mt-4 mb-4">Feature Title</h3>
  <p class="text-xs text-zara-gray-600 leading-relaxed">Description text here.</p>
</div>
```

### Navigation

#### Header
```html
<header class="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-zara-gray-200">
  <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
    <a class="text-xl font-medium tracking-tight">ZARA</a>
    <nav class="hidden md:flex items-center gap-8">
      <a class="text-xs font-medium tracking-widest uppercase">Women</a>
      <a class="text-xs font-medium tracking-widest uppercase">Men</a>
    </nav>
    <button class="text-xs font-medium tracking-widest uppercase">Search</button>
  </div>
</header>
```

### Dividers

#### Section Divider
```html
<div class="h-px bg-gradient-to-r from-transparent via-zara-gray-200 to-transparent max-w-4xl mx-auto"></div>
```

---

## Visual Effects

### Transitions
- **Default Duration**: `200ms` for color changes
- **Hover Scale**: `500ms` for image transforms
- **Shadow**: `300ms` for elevation changes

### Hover States
- Buttons: Color inversion or slight shade change
- Images: `scale-105` with `duration-500`
- Cards: `shadow-lg` appears
- Links: Color change to accent

### Shadows
| Name | Value | Usage |
|------|-------|-------|
| sm | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elevation |
| lg | `0 10px 15px -3px rgba(0,0,0,0.1)` | Card hover |

---

## Animation

### Fade In Up (From Original)
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
```

### Stagger Delays
- `.delay-1`: 100ms
- `.delay-2`: 200ms
- `.delay-3`: 300ms
- `.delay-4`: 400ms

---

## Layout Templates

### Hero Section
```html
<section class="pt-20 pb-24 px-6">
  <div class="max-w-3xl mx-auto text-center">
    <p class="text-xs tracking-widest uppercase mb-6">Subtitle</p>
    <h1 class="text-5xl font-normal tracking-tight leading-tight mb-8">
      Main Headline
    </h1>
    <p class="text-lg text-zara-gray-600 mb-10">Supporting text</p>
  </div>
</section>
```

### Grid Section
```html
<section class="py-24 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-2xl font-normal text-center mb-16">Section Title</h2>
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- Cards -->
    </div>
  </div>
</section>
```

### CTA Section (Dark)
```html
<section class="py-24 px-6 bg-black text-white">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="text-3xl font-normal mb-6">CTA Headline</h2>
    <p class="text-white/70 mb-10">Supporting text</p>
    <button class="bg-white text-black px-10 py-4 text-xs font-medium tracking-widest uppercase">
      Action
    </button>
  </div>
</section>
```

---

## Brand Voice

### Tone
- **Modern**: Clean, contemporary aesthetic
- **Confident**: Minimal punctuation, direct statements
- **Understated**: Let imagery speak, sparse copy

### Copy Style
- Short, declarative sentences
- Minimal adjectives
- ALL CAPS for navigation and buttons
- Sentence case for body text

---

## Zara-Specific Adaptations

### From Original Design (option-c-studio.html)
| Original | Zara Adaptation |
|----------|-----------------|
| Cream background (#f7f5f0) | Pure white (#FFFFFF) |
| Terracotta accent (#c9553d) | Zara red (#EB4C4C) |
| Playfair Display (serif) | Helvetica Now Text (sans-serif) |
| Rounded corners (2px-8px) | Sharp corners (0px) |
| Warm, editorial | Cool, minimalist |

### Key Differences
1. **No serif fonts** - Zara is purely sans-serif
2. **Sharp corners** - No border-radius on buttons
3. **White space** - More aggressive use of negative space
4. **Monochrome** - Primarily black/white with sparse accent
5. **All caps** - More extensive use in UI elements
