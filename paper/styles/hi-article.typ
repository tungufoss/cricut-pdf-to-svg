// HÍ colours for the PDF (Typst), matching the HTML article: blue headings and title,
// turquoise rules and callout accents. Palette from the HÍ theme tokens.
#let hi-blue = rgb("#10099F")
#let hi-turquoise = rgb("#2DD2C0")
#let hi-surface = rgb("#F5F5F5")

#show heading: set text(fill: hi-blue, weight: "semibold")
#show heading.where(level: 1): it => block(width: 100%, above: 1.6em, below: 0.9em, inset: (bottom: 4pt),
  stroke: (bottom: 1.5pt + hi-turquoise), it)
#show link: set text(fill: hi-blue)
#show quote: it => block(fill: hi-surface, inset: 10pt, stroke: (left: 3pt + hi-turquoise), width: 100%, it.body)
#show table: set par(justify: false)
#set table(stroke: (x, y) => if y == 0 { (bottom: 1pt + hi-blue) } else { (bottom: 0.4pt + rgb("#E8E8E8")) })

// Title block in Jost and HÍ blue (Quarto's default article template uses Linux Libertine).
#let article = article.with(heading-family: "Jost", heading-weight: "semibold", heading-color: hi-blue)
