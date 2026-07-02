# Portfolio Allocation Strategy

## Purpose

The dashboard should show both the family's current investment portfolio spread and the recommended target spread needed to support the financial goals.

This feature should help answer:

- How are assets currently allocated?
- How should assets ideally be allocated to reach the target goal?
- Which asset classes are overweight or underweight?
- How do contributions need to change to move toward the target allocation?
- How does the recommended allocation differ by scenario?

## Important caveat

The app should present allocation targets as planning assumptions, not personal financial advice.

Recommended spreads should be labelled as scenario targets and should be editable by the user.

## Allocation views

The dashboard should include at least three allocation views:

### 1. Current portfolio spread

Shows current allocation across:

- Primary property equity
- Investment property equity
- Superannuation
- ETFs
- Investment bond
- Cash savings
- Other assets

### 2. Investable portfolio spread

Shows allocation excluding personal-use assets such as the primary residence if desired.

Example categories:

- Superannuation
- ETFs
- Investment bond
- Cash
- Investment property equity

### 3. Recommended target spread

Shows the target allocation for the selected scenario and goal.

Example categories:

- Growth assets
- Defensive assets
- Property equity
- Superannuation
- Liquid investments outside super
- Cash buffer

## Recommended dashboard components

### Allocation summary cards

Display:

- Current allocation
- Target allocation
- Difference
- Status: underweight, on target, overweight

### Allocation chart

Display a visual comparison between:

- Current spread
- Target spread
- Projected spread at target date

### Contribution guidance

Show where new contributions are planned to go based on the scenario, such as:

- Superannuation
- ETFs
- Investment bond
- Offset account
- Cash buffer

### Goal-alignment view

Show whether the current spread supports the goal assumptions.

Example outputs:

- On track
- Needs higher liquid investment allocation
- Cash buffer below target
- Too much non-income-producing equity
- Debt reduction priority remains high

## Data model additions

Scenario files should support allocation targets.

Example:

```yaml
portfolio_strategy:
  name: Balanced growth to age 60
  target_date: 2043-12-31
  allocation_basis: investable_assets
  current_view_includes_primary_residence: false
  target_allocation:
    superannuation: 0.45
    etfs: 0.20
    investment_bond: 0.15
    investment_property_equity: 0.15
    cash: 0.05
  contribution_priority:
    - cash_buffer
    - superannuation
    - etfs
    - non_deductible_debt_offset
  notes: Target spread is an editable planning assumption.
```

## ETF portfolio spread

The app should also support detailed ETF allocation.

Example:

```yaml
etfs:
  target_allocation:
    VTS: 0.60
    NDQ: 0.20
    VGS: 0.20
```

The dashboard should show:

- Current ETF allocation
- Target ETF allocation
- Drift from target
- Suggested next contribution direction

## Scenario-based recommendations

Different scenarios may have different allocation targets.

Examples:

### Growth-focused scenario

- Higher ETF allocation
- Higher super growth allocation
- Lower cash beyond buffer

### Debt-reduction scenario

- Higher offset/cash allocation
- Lower ETF contributions
- Faster non-deductible debt reduction

### Retirement-readiness scenario

- Higher liquid assets outside property
- Stronger cash buffer
- Reduced debt exposure

## Forecast output additions

The forecast engine should output yearly allocation rows.

Example:

```yaml
- year: 2030
  allocation:
    superannuation: 0.38
    etfs: 0.08
    investment_bond: 0.14
    investment_property_equity: 0.20
    cash: 0.05
    primary_property_equity: 0.15
  target_gap:
    superannuation: 0.07
    etfs: 0.12
    investment_bond: 0.01
    cash: 0.00
```

## Recommendation logic

For MVP, recommended spread should be rule-based and transparent.

Possible rules:

- Maintain cash buffer before increasing growth contributions.
- Prioritise concessional super contributions where tax-efficient and within caps.
- Direct remaining surplus to ETF target allocation.
- Avoid reducing deductible investment debt ahead of non-deductible debt unless scenario specifies otherwise.
- Increase liquid investments if retirement income goal relies too heavily on property equity.

## Future enhancements

- Risk profile questionnaire.
- Monte Carlo-style sensitivity testing.
- Automatic allocation drift alerts.
- Suggested rebalance trades.
- Suggested contribution routing.
- Comparison of adviser-recommended allocation versus current allocation.
