# Recommendation Engine

## Purpose

The recommendation engine should convert forecast results into useful planning prompts and action suggestions.

It should help the user understand what to review next, where the scenario is strong, and where assumptions or actions may need attention.

## Important caveat

The recommendation engine must not present outputs as personal financial advice.

Recommendations should be framed as planning prompts, scenario observations, or areas to review.

## Inputs

The recommendation engine should consume:

- Forecast outputs
- Goal progress results
- Cashflow results
- Portfolio allocation gaps
- Financial health score
- Assumption confidence score
- Scenario metadata
- Validation warnings

## Outputs

The engine should produce:

- Strengths
- Risks
- Suggested review items
- Scenario improvement ideas
- Contribution routing prompts
- Assumption warnings
- Goal shortfall explanations

Example output:

```yaml
recommendations:
  strengths:
    - Forecast income is above the target goal under base assumptions.
    - Superannuation remains a strong driver of retirement income.
  risks:
    - Cash buffer is below the preferred target.
    - Property exposure is high relative to liquid investments.
  review_items:
    - Review interest rate assumptions.
    - Confirm deductible loan split treatment with an accountant.
  possible_actions:
    - Build cash buffer before increasing ETF contributions.
    - Consider increasing ETF contributions once buffer target is met.
```

## Recommendation categories

### 1. Goal recommendations

Generated when:

- Target income is below goal.
- Target income is above goal.
- Net worth target is not met.
- Goal is sensitive to key assumptions.

Example prompts:

- Increase contributions or extend target date.
- Review target income assumption.
- Compare a lower-expense scenario.

### 2. Cashflow recommendations

Generated when:

- Annual surplus is low or negative.
- Expenses exceed assumptions.
- Contributions exceed sustainable surplus.
- Cash buffer is below target.

Example prompts:

- Build cash buffer first.
- Reduce discretionary contributions temporarily.
- Review living cost assumptions.

### 3. Debt recommendations

Generated when:

- LVR is above target.
- Non-deductible debt is high.
- Interest-rate stress test creates deficit.
- Loan payoff date is after target date.

Example prompts:

- Prioritise non-deductible offset.
- Review interest-rate sensitivity.
- Model a lower-debt scenario.

### 4. Portfolio recommendations

Generated when:

- Portfolio is heavily concentrated.
- ETF allocation is below target.
- Cash is below target.
- Property exposure is high.

Example prompts:

- Increase liquid investments when surplus allows.
- Review property concentration.
- Rebalance ETF contributions toward underweight holdings.

### 5. Tax assumption recommendations

Generated when:

- Tax assumptions are stale.
- Negative gearing assumptions are enabled but unverified.
- Super contribution caps are missing or stale.
- Deductible debt classification is missing.

Example prompts:

- Refresh tax snapshots.
- Confirm deductible interest treatment.
- Review super contribution caps annually.

### 6. Data quality recommendations

Generated when:

- Inputs are missing.
- Values are manually estimated.
- API snapshots are stale.
- Assumption confidence is low.

Example prompts:

- Update ETF price snapshot.
- Review market return assumptions.
- Add source metadata for property growth assumptions.

## Severity levels

Recommendations should use severity levels:

- info
- watch
- action
- urgent

Example:

```yaml
- severity: watch
  category: cashflow
  title: Cash buffer below target
  detail: The scenario shows only 3 months of buffer against a target of 6 months.
```

## MVP rules

Start with deterministic rules.

Example rules:

- If goal progress is below 90 percent, flag goal shortfall.
- If cash buffer months are below target, flag buffer risk.
- If total LVR is above configured maximum, flag debt risk.
- If a single asset class exceeds configured maximum exposure, flag concentration risk.
- If tax assumptions are older than 12 months, flag stale tax assumptions.
- If ETF allocation drift exceeds threshold, suggest contribution review.

## Dashboard presentation

Show recommendations in three groups:

1. Strengths
2. Needs attention
3. Suggested review items

Avoid overwhelming the user with too many items.

Suggested limits:

- Maximum 5 strengths
- Maximum 5 risks
- Maximum 5 suggested actions

## Future enhancements

- Compare recommendations across scenarios.
- Rank recommended scenarios by goal fit and risk.
- Generate annual review checklist.
- Allow user to dismiss or acknowledge recommendations.
- Track recommendation history over time.
