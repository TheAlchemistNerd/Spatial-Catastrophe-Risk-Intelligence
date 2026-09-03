# Reference URL Audit

**Audit date:** 29 August 2026  
**Scope:** Numbered reference entries in the six substantive manuscripts  
**Result:** 37 of 37 reference entries contain an explicit `https://` source URL

## Coverage

| Manuscript | Reference entries | Entries with URLs | Missing URLs |
|---|---:|---:|---:|
| Part 1 - Kenya Multi-Hazard Intelligence Thesis | 11 | 11 | 0 |
| Part 2 - Crowd AI and Observation Architecture | 5 | 5 | 0 |
| Part 3 - Spatiotemporal Hazard-State Modelling | 6 | 6 | 0 |
| Part 4 - Actuarial Catastrophe Loss Intelligence | 5 | 5 | 0 |
| Part 5 - Insurance, Investment and Resilience Finance | 5 | 5 | 0 |
| Part 6 - Governance, Validation and Implementation | 5 | 5 | 0 |
| **Total** | **37** | **37** | **0** |

## URL treatment

- Official agency, regulator, legal and institutional sources retain their direct publication or landing-page URLs.
- Journal articles with DOIs now include the canonical `https://doi.org/` resolver as an explicit online source.
- Books now include a publisher or DOI landing page.
- Each newly added online location carries an access date.
- DOI text remains in the citation where it forms part of the bibliographic identity; the resolver URL makes the source directly accessible in Markdown and the compiled PDF.

## Repeatable audit rule

The audit counts lines beginning with an IEEE-style numeric reference marker and requires an HTTP or HTTPS URL on the same entry. A future build should return zero missing entries:

```powershell
$refs = Get-ChildItem manuscripts -Filter '*.md' |
  ForEach-Object { Select-String -LiteralPath $_.FullName -Pattern '^\[[0-9]+\]' }
$refs | Where-Object { $_.Line -notmatch 'https?://' }
```

URL presence establishes reference accessibility in the manuscript. Source authority, claim support, edition currency and legal applicability remain governed through the claim-and-evidence ledger and substantive review.
