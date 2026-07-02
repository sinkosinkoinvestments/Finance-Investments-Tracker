# Forecast Confidence

## Purpose

Forecast confidence helps explain how much trust to place in a scenario forecast.

A forecast may look positive, but if many assumptions are stale, speculative, or manually estimated, the dashboard should make that visible.

## Goal

Every forecast should show:

- The assumptions used
- Where each assumption came from
- When it was last updated
- How confident the system is in the assumption
- Which assumptions most affect the result

## Confidence levels

Suggested labels:

- High
- Medium
- Low
- Unknown

## Assumption metadata

Each important assumption should support metadata.

Example:

```yaml
assumptions:
  equity_growth_rate:
    value: 0.07
    source: user_assumption
    confidence: medium
    updated_at: 2026-01-31
    notes: Long-term nominal return assumption.
  inflation_rate:
    value: 0.03
    source: official_snapshot
    confidence: high
    updated_at: 2026-01-31
  property_growth_rate:
    value: 0.03
    source: user_assumption
    confidence: medium
    updated_at: 2026-01-31
```

## Source types

Supported source types should include:

- user_assumption
- manual_snapshot
- official_snapshot
- api_snapshot
- adviser_confirmed
- accountant_confirmed
- historical_average
- unknown

## Confidence scoring

The app should calculate an overall forecast confidence score.

Suggested score range:

```text
0 to 100
```

Suggested labels:

- 80–100: High confidence
- 55–79: Medium confidence
- 0–54: Low confidence

## Confidence factors

### 1. Source quality

Higher confidence:

- Official snapshot
- Adviser or accountant confirmed
- Recent API snapshot

Lower confidence:

- User estimate
- Unknown source
- Old assumption

### 2. Freshness

Assumptions should lose confidence as they age.

Example stale thresholds:

- Tax assumptions: 12 months
- ETF prices: 30 days
- Interest rates: 90 days
- Property values: 12 months
- Living costs: 12 months

### 3. Sensitivity

High-impact assumptions should matter more.

Examples:

- Interest rate
- Salary income
- Property value
- Growth rates
- Living costs
- Contribution levels

### 4. Completeness

Missing metadata should reduce confidence.

## Example output

```yaml
forecast_confidence:
  score: 72
  label: Medium confidence
  key_drivers:
    - Interest rate assumption is current.
    - Tax assumptions are manually maintained.
    - Property growth assumption is a user estimate.
  stale_assumptions:
    - property_growth_rate
  missing_metadata:
    - investment_bond_growth_rate
```

## Dashboard display

The dashboard should show:

- Overall forecast confidence
- Assumption table
- Stale assumptions
- Unknown assumptions
- High-impact assumptions
- Recommended updates

Example:

```text
Forecast Confidence: 72 / 100
Status: Medium confidence

Needs review
- Property growth assumption is user-estimated.
- Investment bond growth assumption has no source metadata.
- Tax snapshot should be refreshed annually.
```

## MVP rules

For MVP, use simple deterministic rules:

- Assumptions with no source receive lower confidence.
- Assumptions older than their stale threshold are flagged.
- Official or adviser-confirmed sources receive higher confidence.
- High-impact assumptions are weighted more heavily.

## Integration with recommendations

Low-confidence assumptions should feed into the recommendation engine.

Example recommendations:

- Refresh ETF price snapshot.
- Review tax assumptions.
- Confirm loan interest rates.
- Update property valuation.

## Important caveat

Forecast confidence measures the quality and freshness of assumptions. It does not guarantee that the forecast will happen.

All forecasts remain estimates and should be reviewed regularly.
