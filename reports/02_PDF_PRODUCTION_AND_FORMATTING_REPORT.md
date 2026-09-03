# PDF Production and Formatting Report

**Project:** Spatial Catastrophe Risk Intelligence  
**Author:** Nevil Maloba  
**Output:** `output/pdf/Spatial_Catastrophe_Risk_Intelligence_White_Paper.pdf`

## Production objective

Create a reproducible white-paper PDF with the visual rhythm of the shared *Mwendo Pamoja Continuous Underwriting* reference while preserving the rewritten Markdown manuscripts.

## Production workflow

The PDF is generated through Pandoc and XeLaTeX. Mermaid source remains embedded in the Markdown manuscripts and is rendered during compilation by the local Lua filter.

The build incorporates:

- Pandoc manuscript assembly.
- A custom Lua structure filter for part and contents handling.
- A Mermaid Lua filter that invokes Mermaid CLI.
- XeLaTeX book typography.
- Custom metadata, front matter, headers, footers, colours, and part-opening pages.

## Final presentation

The compiled edition contains:

- A navy-and-gold cover inspired by the reference paper.
- Letter-sized pages.
- Georgia body typography and Arial headings.
- Six numbered part openers.
- A separate appendices division rather than a seventh substantive part.
- Two contents pages.
- Consistent running headers, footers, and pagination.
- Seventeen rendered Mermaid diagrams.
- PDF metadata identifying Nevil Maloba as author.

## Source preservation

The manuscript prose was preserved during the PDF production pass. Two malformed duplicate Mermaid fragments were removed from Part 1, and the second Part 1 figure was corrected from Figure 1.3 to Figure 1.2.

## Validation performed

- Confirmed a 47-page Letter PDF.
- Confirmed title and author metadata.
- Rendered and visually inspected the cover, contents, all part openers, representative body pages, diagrams, equations, references, and final appendix page.
- Confirmed that all seventeen Mermaid figures were rendered and that no raw Mermaid source remained in the PDF text layer.
- Confirmed that the final PDF contained no replacement-character rendering errors.

## Important limitation

The design is comparable to the reference, but the manuscript is materially shorter. The current six parts contain approximately 10,600 substantive words, compared with roughly 48,700 words in the reference. The visual treatment cannot substitute for additional evidence, narrative development, actuarial specification, or product detail.
