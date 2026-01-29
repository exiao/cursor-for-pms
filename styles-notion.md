# Notion-Style Design System
## For Cursor for PMs Course Landing Page

---

## Color Palette

### Primary Colors
| Name | Hex | Usage |
|------|-----|-------|
| Primary Blue | `#0075DE` | Primary buttons, links, key actions, CTAs |
| Light Blue Accent | `#E6F3FE` | Highlights, backgrounds, hover states, badges |
| Background | `#FFFFFF` | Main canvas, card backgrounds |
| Text Primary | `#191918` | Headings and body text |

### Secondary Colors
| Name | Hex | Usage |
|------|-----|-------|
| Text Secondary | `#787774` | Muted text, captions, descriptions |
| Border Gray | `#E3E2E0` | Card borders, dividers, input borders |
| Surface Gray | `#F7F6F3` | Section backgrounds, subtle fills |
| Success Green | `#0F7B6C` | Success states, checkmarks |
| Hover Blue | `#005BAB` | Button hover states |

### Tailwind Config
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        'notion-blue': '#0075DE',
        'notion-blue-light': '#E6F3FE',
        'notion-blue-dark': '#005BAB',
        'notion-text': '#191918',
        'notion-text-muted': '#787774',
        'notion-border': '#E3E2E0',
        'notion-surface': '#F7F6F3',
        'notion-success': '#0F7B6C',
      }
    }
  }
}
```

---

## Typography

### Font Stack
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, 'Apple Color Emoji', Arial, sans-serif;
```

### Hierarchy

| Element | Size | Weight | Line Height | Letter Spacing | Tailwind Class |
|---------|------|--------|-------------|----------------|----------------|
| H1 (Hero) | 64px / 4rem | 700 (Bold) | 1.1 | -0.02em | `text-6xl lg:text-7xl font-bold tracking-tight` |
| H2 (Section) | 36px / 2.25rem | 600 (Semibold) | 1.2 | -0.01em | `text-3xl md:text-4xl font-semibold` |
| H3 (Card) | 20px / 1.25rem | 600 (Semibold) | 1.3 | 0 | `text-xl font-semibold` |
| Body Large | 18px / 1.125rem | 400 (Normal) | 1.6 | 0 | `text-lg leading-relaxed` |
| Body | 16px / 1rem | 400 (Normal) | 1.6 | 0 | `text-base leading-relaxed` |
| Body Small | 14px / 0.875rem | 400 (Normal) | 1.5 | 0 | `text-sm` |
| Label | 12px / 0.75rem | 500 (Medium) | 1.4 | 0.05em | `text-xs font-medium tracking-wide uppercase` |

### Style Notes
- **Sans-serif only**: Inter is the primary typeface
- **Bold headlines**: Hero uses 700 weight with tight tracking
- **Generous line-height**: Body text uses 1.6 for readability
- **Clean hierarchy**: Weight and size work together

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
- **Section Padding**: `py-20 md:py-24 lg:py-32` (80-128px vertical)
- **Container Max Width**: `max-w-5xl` (1024px) or `max-w-7xl` (1280px)
- **Container Horizontal Padding**: `px-4 md:px-6` (16-24px)
- **Card Grid Gap**: `gap-6 md:gap-8` (24-32px)

### Layout Grid
- **Desktop**: 3-4 column grid (`grid-cols-3` or `grid-cols-4`)
- **Tablet**: 2 column grid (`md:grid-cols-2`)
- **Mobile**: Single column (`grid-cols-1`)

---

## Component Patterns

### Buttons

#### Primary Button
```html
<button class="bg-notion-blue hover:bg-notion-blue-dark text-white px-6 py-3 rounded-lg font-medium text-base transition-colors duration-200 inline-flex items-center gap-2">
  Get started
  <svg>→</svg>
</button>
```
- Background: `#0075DE`
- Hover: `#005BAB`
- Text: `#FFFFFF`
- Border Radius: `8px` (rounded-lg)
- Padding: `12px 24px` (py-3 px-6)
- Shadow: None
- Transition: 200ms

#### Secondary Button
```html
<button class="bg-notion-blue-light hover:bg-blue-100 text-notion-blue-dark px-6 py-3 rounded-lg font-medium text-base transition-colors duration-200">
  Learn more
</button>
```
- Background: `#E6F3FE`
- Hover: Slightly darker blue
- Text: `#005BAB`

#### Ghost Button
```html
<button class="bg-transparent hover:bg-notion-surface text-notion-text px-4 py-2 rounded-lg font-medium text-sm transition-colors duration-200">
  Sign in
</button>
```

### Cards

#### Standard Card
```html
<div class="bg-white border border-notion-border rounded-xl p-6 hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
  <!-- Content -->
</div>
```
- Background: `#FFFFFF`
- Border: `1px solid #E3E2E0`
- Border Radius: `12px` (rounded-xl)
- Padding: `24px` (p-6)
- Hover: Lift with shadow

#### Feature Card
```html
<div class="bg-notion-surface rounded-2xl p-8 border-0">
  <div class="w-12 h-12 bg-notion-blue-light rounded-xl flex items-center justify-center mb-4">
    <icon class="text-notion-blue text-xl" />
  </div>
  <h3 class="text-xl font-semibold mb-3">Title</h3>
  <p class="text-notion-text-muted">Description</p>
</div>
```

### Navigation

#### Header
```html
<header class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-notion-border">
  <div class="max-w-7xl mx-auto px-4 md:px-6 py-4 flex items-center justify-between">
    <!-- Logo, nav items, CTAs -->
  </div>
</header>
```
- Height: ~64px
- Background: White with 80% opacity + blur
- Border: 1px bottom border

#### Nav Links
```html
<a class="text-notion-text hover:text-notion-blue font-medium text-sm transition-colors duration-200">
  Product
</a>
```

### Badges / Tags
```html
<span class="bg-notion-blue-light text-notion-blue-dark px-3 py-1 rounded-full text-xs font-medium">
  2-Week Course
</span>
```

### Dividers
```html
<div class="h-px bg-gradient-to-r from-transparent via-notion-border to-transparent max-w-4xl mx-auto"></div>
```

---

## Visual Effects

### Transitions
- **Default Duration**: `200ms` for color changes
- **Hover Transform**: `300ms` for scale/translate
- **Shadow**: `300ms` for elevation changes

### Hover States
- Buttons: Color darken, 200ms
- Cards: Y translate -4px, shadow-lg appears, 300ms
- Images: `scale-105` with `duration-500`
- Links: Color change to blue

### Shadows
| Name | Value | Usage |
|------|-------|-------|
| none | none | Default buttons |
| sm | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elevation |
| md | `0 4px 6px rgba(0,0,0,0.07)` | Cards |
| lg | `0 10px 15px rgba(0,0,0,0.1)` | Hover cards, modals |

---

## Animation

### Fade In Up
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
<section class="pt-16 md:pt-24 pb-20 md:pb-32 px-4 md:px-6 bg-white">
  <div class="max-w-4xl mx-auto text-center">
    <span class="badge mb-6">Tag</span>
    <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight text-notion-text mb-6">
      Headline
    </h1>
    <p class="text-xl text-notion-text-muted max-w-2xl mx-auto mb-10">
      Supporting text
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="btn-primary">Primary CTA</button>
      <button class="btn-secondary">Secondary CTA</button>
    </div>
  </div>
</section>
```

### Feature Grid
```html
<section class="py-20 md:py-32 px-4 md:px-6 bg-notion-surface">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-semibold text-center mb-16">
      Section Title
    </h2>
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- Feature cards -->
    </div>
  </div>
</section>
```

### CTA Section
```html
<section class="py-20 md:py-24 px-4 md:px-6 bg-notion-text text-white">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="text-3xl md:text-4xl font-semibold mb-6">CTA Headline</h2>
    <p class="text-white/70 mb-10 text-lg">Supporting text</p>
    <button class="bg-white text-notion-text px-8 py-4 rounded-lg font-medium hover:bg-notion-surface transition-colors">
      Action
    </button>
  </div>
</section>
```

---

## Key Differences from Original (option-c-studio.html)

| Original | Notion Style |
|----------|--------------|
| Cream background (#f7f5f0) | Pure white (#FFFFFF) |
| Terracotta accent (#c9553d) | Notion blue (#0075DE) |
| Playfair Display (serif) | Inter (sans-serif) |
| Source Serif 4 (serif) | Inter (sans-serif) |
| Small rounded corners (rounded-sm) | Larger radius (rounded-lg, rounded-xl) |
| Warm, editorial feel | Clean, modern, professional |
| Muted sage green (#4a6741) | Light blue accent (#E6F3FE) |

---

## Brand Voice

### Tone
- **Professional**: Clean, workspace-focused
- **Collaborative**: Emphasizes team productivity
- **Modern**: Contemporary, tech-forward

### Copy Style
- Clear, direct sentences
- Focus on outcomes and benefits
- Minimal jargon
- Sentence case throughout (no all-caps except small labels)
