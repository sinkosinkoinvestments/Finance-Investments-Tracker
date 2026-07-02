# ATO and Tax Data Strategy

## Purpose

The tracker should support tax-related assumptions and, where practical, pull or snapshot authoritative tax reference data.

The goal is not to automate tax advice. The goal is to keep forecast assumptions aligned with current reference settings where possible.

## Tax assumptions to track

The app should support assumptions for:

- Australian resident income tax rates
- Medicare levy
- Superannuation concessional contribution caps
- Non-concessional contribution caps
- Division 293 threshold assumptions
- Capital gains tax assumptions
- Rental property income and expense assumptions
- Deductible and non-deductible loan interest treatment
- Negative gearing treatment
- Depreciation and capital works assumptions, where manually entered

## ATO data approach

ATO data should be handled carefully because not every useful value is available through a clean public API.

Recommended approach:

```text
ATO / official source
  -> manual or automated reference snapshot
  -> tax assumptions file
  -> forecast engine
```

## Source-of-truth principle

The app should not depend on live ATO lookups at calculation time.

Instead:

1. Keep editable tax assumptions in YAML.
2. Store dated tax reference snapshots.
3. Record the source URL and retrieval date.
4. Allow manual override.
5. Display a warning when tax assumptions are stale.

## Suggested files

```text
/data/tax/
├── tax-rates-2026.yml
├── super-caps-2026.yml
├── rental-property-rules-2026.yml
└── cgt-assumptions-2026.yml
```

## Example tax rates snapshot

```yaml
source:
  authority: Australian Taxation Office
  url: https://www.ato.gov.au/
  retrieved_at: 2026-01-31
  notes: Manual snapshot. Verify before relying on outputs.

australian_resident_income_tax:
  financial_year: 2026
  medicare_levy: 0.02
  brackets:
    - min: 0
      max: 18200
      rate: 0
    - min: 18201
      max: 45000
      rate: 0.16
    - min: 45001
      max: 135000
      rate: 0.30
    - min: 135001
      max: 190000
      rate: 0.37
    - min: 190001
      max: null
      rate: 0.45
```

## Negative gearing assumptions

The model should represent negative gearing as an assumption, not as a hard-coded fact.

Suggested fields:

```yaml
negative_gearing:
  enabled: true
  applies_to:
    - investment_property_interest
    - eligible_property_expenses
  loss_offset_against_salary_income: true
  grandfathering_notes: null
  source_url: null
  verified_at: null
```

This makes it easier to model possible future policy changes.

## Rental property deductions

The app should track rental assumptions separately:

- Gross rent
- Property expenses
- Interest linked to investment loans
- Deductible percentage
- Private-use percentage
- Depreciation estimate
- Capital works estimate
- Accountant-adjusted values

## Implementation recommendation

For MVP:

1. Use manually maintained tax YAML files.
2. Display all tax assumptions in the dashboard.
3. Add stale-data warnings.
4. Allow manual updates through the input GUI.

For later versions:

1. Add scheduled checks for official source changes where feasible.
2. Use a serverless worker or GitHub Action to fetch/cache public reference pages or datasets.
3. Keep the final calculation based on committed snapshots, not live calls.

## Important limitation

Tax rules change and can be complex. The app should clearly state that tax calculations are planning estimates and should be reviewed by a qualified accountant or adviser before decisions are made.
