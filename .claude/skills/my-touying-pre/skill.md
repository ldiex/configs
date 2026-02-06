# Lin's Touying Presentation Author

Author professional academic presentations using Typst and Touying, following Lin's personal style and best practices.

## Quick Start Template

```typst
#import "@preview/touying:0.6.1": *
#import themes.dewdrop: *

#import "@preview/numbly:0.1.0": numbly
#import "@preview/theorion:0.3.2": *
#import "@preview/mitex:0.2.5": *
#import "@preview/fontawesome:0.6.0": *
#import "@preview/cetz:0.4.2"

#import cosmos.clouds: *

// Customizable style variables
#let primary = rgb("#024e99")  // Primary color for the presentation
#let link-color = purple.darken(30%)  // Color for links and references
#let base-font-size = 22pt  // Base font size
#let base-font = ("Libertinus Serif", "Source Han Serif SC")  // Font family

#show ref: it => {
  text(link-color, it)
}

#show link: it => {
  text(link-color, it)
}

#let new-section-slide(config: (:), title: utils.i18n-outline-title, ..args, body) = touying-slide-wrapper(self => {
  self = utils.merge-dicts(
    self,
    config-page(
      footer: dewdrop-footer,
    ),
  )
  touying-slide(
    self: self,
    config: config,
    components.adaptive-columns(
      start: text(
        1.2em,
        fill: self.colors.primary,
        weight: "bold",
        utils.call-or-display(self, title),
      ),
      text(
        fill: self.colors.neutral-darkest,
        components.progressive-outline(
          alpha: self.store.alpha,
          title: none,
          indent: 1em,
          depth: 1,
          ..args,
        ),
      ),
    ),
  )
})

#show: dewdrop-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.author,  // Can also use self.info.title
  navigation: "mini-slides",
  config-common(
    slide-level: 2,
    new-section-slide-fn: new-section-slide,
  ),
  config-info(
    title: [Your Title Here],
    author: [Lin],  // Or use full name if needed
    date: datetime.today(),
    institution: [University of Chinese Academy of Sciences],
  ),
  config-colors(
    neutral-darkest: rgb("#000000"),
    neutral-dark: rgb("#202020"),
    neutral-light: rgb("#f3f3f3"),
    neutral-lightest: rgb("#ffffff"),
    primary: primary,
  )
)

#set heading(numbering: numbly("{1}.", default: "1.1"))
#set text(base-font-size, font: base-font)

#title-slide()

= First Section
== First Slide
Your content here.
```

## Lin's Style Guidelines

### 1. Theme and Configuration
- **Always use Dewdrop theme** with these settings:
  - `aspect-ratio: "16-9"`
  - `navigation: "mini-slides"`
  - `slide-level: 2` (level-2 headings create slides)
  - Custom `new-section-slide-fn` with progressive outline
- **Footer options**: Choose between `self.info.author`, `self.info.title`, or custom text
- **Color scheme**: Define custom `primary` color, use standard neutral palette
- **Navigation bar management**:
  - **Limit to ≤3 level-2 headings per section** to prevent oversized navigation bar
  - If more content needed, use `#pagebreak(weak: true)` within slides or create new sections

### 2. Standard Import Set
Always include this dependency suite:
```typst
#import "@preview/touying:0.6.1": *
#import themes.dewdrop: *
#import "@preview/numbly:0.1.0": numbly
#import "@preview/theorion:0.3.2": *
#import "@preview/mitex:0.2.5": *
#import "@preview/fontawesome:0.6.0": *
#import "@preview/cetz:0.4.2"
#import cosmos.clouds: *
```

### 3. Visual Customizations

**Style Variables (Define at top of file)**:
```typst
#let primary = rgb("#024e99")  // Customize per presentation
#let link-color = purple.darken(30%)  // Default: purple, but customizable
#let base-font-size = 22pt  // Adjust as needed
#let base-font = ("Libertinus Serif", "Source Han Serif SC")
```

**Applied Settings**:
- **References and links**: Use `link-color` variable (default: `purple.darken(30%)`)
- **Font**: Use `base-font` variable at `base-font-size`
- **Heading numbering**: Use `numbly("{1}.", default: "1.1")`
- **Icons**: **Strongly encouraged** to use FontAwesome for visual enhancement
  - Only free icons are supported (check: https://fontawesome.com/search?o=r&m=free)
  - Examples: `#fa-graduation-cap(fill: primary)`, `#fa-lightbulb(fill: primary)`, `#fa-rocket(fill: primary)`
  - Use icons to make slides more engaging and visually structured

### 4. Layout Techniques

#### Multi-column Layouts
Use `#slide(composer: ...)` for side-by-side content:
```typst
#slide(composer: (1fr, 1fr))[
  Left column content
][
  Right column content
]
```

#### Progressive Reveals
Use `#pause` for step-by-step content:
```typst
First point

#pause
Second point (appears on next step)

#pause
Third point
```

#### Page Breaks
Use `#pagebreak(weak: true)` to split content while staying in same section.

#### Icon-Enhanced Sections
**Strongly encourage using FontAwesome icons** to make content more visually appealing:
```typst
#fa-graduation-cap(fill: primary) \ *Education*
#fa-lightbulb(fill: primary) \ *Key Idea*
#fa-rocket(fill: primary) \ *Results*
```

**Note**: Only free FontAwesome icons are supported. Check availability at https://fontawesome.com/search?o=r&m=free

### 5. Color Customization

**Primary Color Examples** (set via `#let primary = ...`):
- Research/Academic: `rgb("#024e99")` (blue)
- Creative/Purple: `rgb("#db63ff")` (purple)
- Bright/Sky: `rgb("#70b4f8")` (sky blue)

**Link Color** (set via `#let link-color = ...`):
- Default: `purple.darken(30%)`
- Alternative: Match primary color with `primary.darken(20%)`
- Or use any custom color

**Result Colors** (for tables):
```typst
#let good(it) = text(fill: rgb("#008000"))[#it]  // Green for improvements
#let bad(it) = text(fill: rgb("#B00000"))[#it]   // Red for regressions
#let gray(it) = text(fill: rgb("#808080"))[#it]  // Gray for baseline
```

### 6. Academic Content Patterns

#### Author Information Cards
```typst
#slide(composer: (1fr, 1fr, 1fr))[
  #fa-graduation-cap(fill: primary) \ *Education*

  Content here
][
  #fa-school(fill: primary) \ *Academic Standing*

  Content here
][
  #fa-award(fill: primary) \ *Honors*

  Content here
]
```

#### Mathematical Content
Use native Typst math mode with proper formatting:
```typst
$
  cal(L) = sum_(i=1)^N norm(hat(y)_i - y_i)_1
$
```

**IMPORTANT**: When using subscript notation with function calls, **always add a space** before the opening parenthesis:
```typst
// CORRECT - space before parenthesis
$f_"name" (x, y)$
$r_"DIoU" (bold(G))$

// WRONG - no space, parenthesis becomes part of subscript
$f_"name"(x, y)$  // This will render incorrectly!
```

#### Tables for Results

**Preferred Style: Academic Minimal Table** (from pre1.typ)
```typst
#let good(it) = text(fill: rgb("#008000"))[#it]
#let bad(it) = text(fill: rgb("#B00000"))[#it]
#let gray(it) = text(fill: rgb("#808080"))[#it]

#figure(
  caption: [Your caption here],
  table(
    columns: 4,
    inset: 8pt,
    align: (left, center, center, center),
    stroke: none,  // No borders for clean academic look

    // Header with thick line
    table.hline(stroke: 1.5pt),
    table.header(
      [*Method*],
      [*Metric 1* \ (Direction $arrow.t$)],
      [*Metric 2* \ (Direction $arrow.b$)],
      [*Time*]
    ),
    table.hline(stroke: 0.5pt),

    // Data rows
    [Baseline],
    [78.5 \ #gray[-]],
    [10.2 \ #gray[-]],
    [10s],

    [Ours],
    [*85.3* \ #good[+6.8%]],
    [*8.7* \ #good[-14.7%]],
    [*0.2s*],

    // Bottom line
    table.hline(stroke: 1.5pt),
  )
)
```

**Key features**:
- `stroke: none` for no gridlines (clean academic style)
- `table.hline()` for horizontal rules only (top: 1.5pt, middle: 0.5pt, bottom: 1.5pt)
- Colored change indicators: `#good[...]`, `#bad[...]`, `#gray[...]`
- Multi-line headers with `\` for units/directions
- Bold (`*...*`) for best results

**Simple Alternative** (when comparison not needed):
```typst
#table(
  columns: 3,
  stroke: 1pt + black,
  inset: 8pt,
  align: center,
  [*Method*], [*Accuracy*], [*Speed*],
  [Baseline], [78.5%], [10s],
  [Ours], [*85.3%*], [*0.2s*],
)
```

#### Colored Text for Results
```typst
#let good(it) = text(fill: rgb("#008000"))[#it]
#let bad(it) = text(fill: rgb("#B00000"))[#it]
#let gray(it) = text(fill: rgb("#808080"))[#it]

[Accuracy: #good[+8.0%]]
```

#### Grid Layouts for Images
```typst
#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 1em,
  image("img1.png", width: 100%),
  image("img2.png", width: 100%),
  image("img3.png", width: 100%),
)
```

### 7. Optional Advanced Features

#### showybox for Callouts
```typst
#import "@preview/showybox:2.0.4": showybox

#let frameSettings = (
  border-color: primary,
  title-color: primary.lighten(20%),
  body-color: primary.lighten(95%),
  footer-color: primary.lighten(80%),
)

#showybox(
  title: "Important Note",
  frame: frameSettings,
)[
  Your content here
]
```

#### CeTZ for Diagrams
```typst
#figure(
  cetz.canvas({
    import cetz.draw: *
    rect((0, 0), (2, 2), fill: primary.lighten(80%))
    content((1, 1), [Text])
  })
)
```

## Workflow

1. **Start from template**: Copy the quick-start template above
2. **Customize colors**: Choose appropriate `primary` color
3. **Set metadata**: Update title, author (use "Lin" or full name if needed), date
4. **Structure with headings**:
   - Level 1 (`=`) for sections (triggers section slides)
   - Level 2 (`==`) for individual slides
   - **IMPORTANT**: Limit to **≤3 level-2 headings per section** to avoid oversized navigation bar
     - Too many slides → navigation bar takes excessive space
     - Solution: Use `#pagebreak(weak: true)` within slides or create new sections
5. **Use progressive reveals**: Add `#pause` for step-by-step content
6. **Layout with composers**: Use multi-column layouts for side-by-side content
7. **Enhance with icons**: Use FontAwesome for visual appeal
8. **Add math/tables**: Format academic content properly

## Common Patterns

### Title Slide
```typst
#title-slide()
```

### Section with Outline
```typst
= Section Name
// Touying automatically creates section slide with progressive outline
```

### Hiding Section Title
```typst
= Section Name <touying:hidden>
```

### Multi-Column with Icons
```typst
#slide(composer: (1fr, 0.2fr, 1fr))[
  #fa-icon(fill: primary) Content
][
  // Empty column for spacing
][
  #fa-icon(fill: primary) More content
]
```

### Quote Block
```typst
#quote()[
  #set text(15pt)
  Your quoted text here
]
```

### Ending Slide
```typst
#slide()[
  #align(center + horizon)[
    #set text(28pt)
    感谢大家的聆听!

    #v(2em)
    #set text(20pt)
    联系方式: your.email@example.com
  ]
]
```

## Important Typst/Touying Rules

### Critical Distinctions (from typst-author skill)
- **Arrays**: `(item1, item2)` (parentheses)
- **Dictionaries**: `(key: value, key2: value2)` (parentheses with colons)
- **Content blocks**: `[markup content]` (square brackets)
- **NO tuples**: Typst only has arrays

### Hash Usage
- Use `#` to start code expressions inside markup/content blocks
- Do NOT use `#` inside code contexts (argument lists, code blocks)
- Example: `#figure(image("file.png"))` (no `#` before `image`)

### Math Mode Subscripts with Function Calls
**CRITICAL**: When a subscript is followed by a function call, always add a space before the opening parenthesis:

```typst
// CORRECT ✓
$f_"name" (x, y)$
$r_"DIoU" (bold(G))$
$cal(L)_"PSFT" (theta)$

// WRONG ✗ - parenthesis becomes part of subscript!
$f_"name"(x, y)$
$r_"DIoU"(bold(G))$
```

Without the space, Typst treats the parentheses as part of the subscript notation, causing incorrect rendering.

### Styling Rules
- `set`: Configure default parameters (scoped to block/file)
- `show`: Transform/replace element output selectively
- Use `set` for common styling; `show` for selective changes

### Avoid Common Mistakes
- Don't call things "tuples" (use "arrays")
- Don't use `[]` for arrays (use `()`)
- Don't access array elements with `arr[0]` (use `arr.at(0)`)
- Don't omit `#` in markup blocks for function calls
- Don't use `#` inside code contexts
- Don't use LaTeX syntax (`\section`, `\begin{}`, etc.)
- **Math subscripts with functions**: Always add space before parentheses: `$f_"name" (x)$` not `$f_"name"(x)$`
- **Navigation bar size**: Keep ≤3 level-2 headings (`==`) per section to avoid oversized navigation

## Documentation References

### Touying (from touying-author skill)
- Read `docs/start.md` for basics
- Read `docs/multi-file.md` for multi-file projects
- Read `docs/layout.md` for slide-level configuration
- Read `docs/dynamic/simple.md` for pause/meanwhile
- Read `docs/themes/dewdrop.md` for Dewdrop theme specifics

### Typst
- Tutorial: `docs/tutorial/writing-in-typst.md`
- Reference: `docs/reference/**/*.md`
- Styling: `docs/reference/styling.md`
- Math: `docs/reference/math/`

## Troubleshooting

### Font Warnings
If "unknown font family" warnings appear, remove font specification to use system defaults. Font warnings don't prevent compilation.

### Package Not Found
Verify exact package name and version on Typst Universe. Check for typos in `@preview/package:version` syntax.

### Layout Issues
- If content overflows, use `#pagebreak(weak: true)` or adjust font size
- For image sizing, use percentage widths: `image("file.png", width: 80%)`
- For multi-column balance, adjust `composer` ratios: `(1fr, 2fr)` gives 1:2 ratio

### Animation Issues
- `#pause` only works in main slide flow, not inside deep nesting
- For complex animations, use callback-style slides with `repeat` parameter
- Avoid `#pause` inside `context` blocks

## Example: Creating a Research Presentation

```typst
#import "@preview/touying:0.6.1": *
#import themes.dewdrop: *
#import "@preview/numbly:0.1.0": numbly
#import "@preview/fontawesome:0.6.0": *

#show ref: it => text(purple.darken(30%), it)

#let primary = rgb("#024e99")

// ... (include new-section-slide definition and theme setup) ...

#title-slide()

= Introduction
== Motivation
Current methods face challenges:

#pause
1. Computational cost
#pause
2. Limited scalability
#pause
3. Lack of interpretability

== Our Contribution
#slide(composer: (1fr, 1fr))[
  #fa-lightbulb(fill: primary) \ *Key Idea*

  We propose a novel approach that...
][
  #fa-rocket(fill: primary) \ *Results*

  - 3x faster
  - 15% accuracy improvement
]

= Methodology
== Architecture
#figure(
  image("architecture.png", width: 80%),
  caption: [Overview of our proposed method]
)

= Experiments
== Results on Benchmark Dataset

#let good(it) = text(fill: rgb("#008000"))[#it]
#let bad(it) = text(fill: rgb("#B00000"))[#it]
#let gray(it) = text(fill: rgb("#808080"))[#it]

#figure(
  caption: [Performance comparison on benchmark dataset],
  table(
    columns: 4,
    inset: 8pt,
    align: (left, center, center, center),
    stroke: none,

    table.hline(stroke: 1.5pt),
    table.header(
      [*Method*],
      [*Accuracy* \ (↑)],
      [*Speed* \ (↓)],
      [*Params*]
    ),
    table.hline(stroke: 0.5pt),

    [Baseline],
    [78.5% \ #gray[-]],
    [10s \ #gray[-]],
    [100M],

    [Ours],
    [*85.3%* \ #good[+6.8%]],
    [*0.2s* \ #good[-98%]],
    [*50M*],

    table.hline(stroke: 1.5pt),
  )
)

= Conclusion
#slide()[
  #align(center + horizon)[
    Thank you for your attention!

    Questions?
  ]
]
```

## Summary

This skill combines:
- **Lin's aesthetic preferences**: Dewdrop theme, specific fonts, purple accents, 16:9 format
- **Lin's structural patterns**: Custom section slides, multi-column layouts, progressive reveals
- **Lin's academic style**: FontAwesome icons, result tables, colored metrics, mathematical notation
- **Touying best practices**: Centralized config, heading-based slides, animation patterns
- **Typst fundamentals**: Correct syntax, styling rules, common pitfalls to avoid

When authoring presentations for Lin, always start with the quick-start template, follow the style guidelines, and leverage the common patterns documented here.
