# Positive Product-Narrative and Diagram-Legibility Implementation

**Date:** 29 August 2026  
**Governing brief:** `guidance/POSITIVE_PRODUCT_NARRATIVE_AND_DIAGRAM_LEGIBILITY_PLAN.md`  
**Status:** Source implementation and PDF visual validation complete; empirical expansion and independent review remain the next workstream

## Narrative changes

The first manuscript-wide audit found 168 occurrences of defensive constructions represented by `not`, `does not`, `cannot`, `must not`, `never` and `no`. The first implementation pass reduced that count to 22.

The remaining instances are concentrated in places where a negative boundary carries real meaning:

- technical distinctions such as observation confidence versus hazard probability;
- permission tables defining actions SCRI may support and actions owned elsewhere;
- pilot stop conditions;
- sparse-evidence and model-failure scenarios;
- explicit synthetic or review status.

Product prose now follows this order:

1. capability;
2. user and practical outcome;
3. operating mechanism;
4. trade-off or failure scenario;
5. firm restriction where consequential.

Representative changes include:

- Part 1 now describes how six physical adapters create one financial product interface.
- Part 2 gives YOLO, segmentation, source fusion and crowd reporting defined positive roles.
- Part 3 describes baselines as operational benchmarks and challengers as evidence-led improvements.
- Part 4 leads with the policy and financial transformation rather than distribution caveats.
- Part 5 frames continuous catastrophe underwriting around a stable customer promise and distinct decision clocks.
- Part 6 describes governance as the mechanism that turns shared evidence into accountable decisions.

## Diagram changes

The Mermaid production defaults now use:

- 22 px source typography, increased from 18 px;
- increased node spacing and rank spacing;
- 2x rendering scale at 2,800 px width;
- a larger default maximum figure height;
- full-width page-oriented layouts for wide diagrams, with landscape support available where future figures genuinely require it.

Figure 5.2, Figure 6.3, Figure 6.5 and Figure B.1 were rebuilt as compact full-width product panels. Figure 5.2 now reads left to right across one flood morning. Figure 6.3 presents the nine stages as three substantial phases—Foundation, Models and Product—with evidence gates between them. Figure 6.5 turns independent review into a readable evidence-and-disposition loop. Figure B.1 presents the whole system through three large architectural components. Long chains elsewhere use portrait or square layouts when those forms improve label size.

## Acceptance test

The revised PDF must pass all of the following at 100% view:

- every node and edge label is comfortably readable on a 13-15 inch display;
- major sequence and systems diagrams use the page rather than occupying a narrow strip;
- portrait figures remain within page margins;
- any future landscape pages rotate correctly and preserve headers/footers where appropriate;
- no figure overlaps prose or captions;
- figure numbering and contents links remain consistent;
- all pages render without clipping, missing glyphs or duplicate captions.

The PDF is released only after every page has been rendered and inspected, with full-size checks of each Mermaid figure page.

## Accepted PDF build

- Output: `output/pdf/SCRI_Positive_Product_Narrative_Edition.pdf`
- Format: 65 pages, US Letter, PDF 1.7
- Author metadata: Nevil Maloba
- SHA-256: `8295219F2D9DDF12FEB6CF83D058BF92237B9A17CDD4E42D7ECBF13CCCDBDF4F`
- Rendering QA: 65 of 65 pages rendered with Poppler at 110 dpi and inspected through six contact sheets
- Full-size QA: product journey, implementation stages, independent-review loop and canonical architecture inspected at normal page scale
- Reference QA: 37 of 37 numbered entries contain explicit HTTPS source locations; all six bibliography sections were inspected at full size for clean wrapping
- Result: no clipping, overlap, missing glyphs or duplicate captions observed; the redesigned diagrams use the page width and remain readable without zoom-dependent inspection
- Production enhancement: tagged-PDF accessibility remains the next format improvement
