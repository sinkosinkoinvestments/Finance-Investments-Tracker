# Financial Health Score

## Purpose

The dashboard should calculate a simple Financial Health Score for each scenario.

The score should help summarise whether the family is financially resilient and on track to meet its goals.

The score should not replace the detailed forecast. It should act as a quick signal that highlights strengths, risks, and areas needing attention.

## Score range

```text
0 to 100
```

Suggested labels:

- 90–100: Excellent
- 75–89: Strong
- 60–74: Moderate
- 40–59: Needs attention
- 0–39: High risk

## Core scoring categories

### 1. Goal progress

Measures whether the scenario is on track to meet the target goal by the target date.

Inputs:

- Target annual net income
- Target net worth
- Target investable assets
- Forecast annual income at target date
- Forecast net worth at target date

Suggested weighting: 25 percent

### 2. Cash buffer resilience

Measures whether liquid cash and offset balances are sufficient for emergencies and holding costs.

Inputs:

- Cash savings
- Offset balances
- Monthly expenses
- Monthly loan commitments
- Target buffer months

Suggested weighting: 20 percent

### 3. Debt sustainability

Measures whether debt is manageable relative to income, assets, and time horizon.

Inputs:

- Total debt
- Deductible debt
- Non-deductible debt
- Loan-to-value ratio
- Debt repayments
- Interest rate stress test

Suggested weighting: 20 percent

### 4. Liquidity and flexibility

Measures whether enough wealth is accessible outside illiquid assets.

Inputs:

- Cash
- ETFs
- Investment bond liquidity
- Property equity
- Superannuation preservation rules

Suggested weighting: 15 percent

### 5. Diversification

Measures whether assets are too concentrated in one asset class.

Inputs:

- Property exposure
- Superannuation exposure
- ETF exposure
- Cash exposure
- Investment bond exposure

Suggested weighting: 10 percent

### 6. Contribution discipline

Measures whether planned contributions are consistent with the scenario goal.

Inputs:

- Super contributions
- ETF contributions
- Investment bond contributions
- Cash buffer contributions
- Debt reduction or offset contributions

Suggested weighting: 10 percent

## Example output

```yaml
financial_health_score:
  score: 82
  label: Strong
  strengths:
    - Strong superannuation base
    - Investment goal remains achievable under base assumptions
    - Diversified income sources at target date
  risks:
    - Cash buffer below preferred target
    - High property concentration
    - Interest rate sensitivity remains material
  recommended_actions:
    - Build emergency buffer before increasing ETF contributions
    - Maintain separate loan splits for deductible and non-deductible debt
    - Review assumptions annually
```

## Dashboard display

The dashboard should show:

- Overall score
- Category scores
- Strengths
- Risks
- Recommended actions
- Scenario comparison

Example UI cards:

```text
Financial Health Score: 82 / 100
Status: Strong

Strengths
- Goal is broadly on track
- Strong superannuation base
- Diversified future income sources

Needs attention
- Cash buffer below target
- High property concentration
- Sensitive to higher rates
```

## Scenario comparison

The score should be calculated for every scenario so the dashboard can compare:

- Base plan
- Higher ETF contributions
- Higher super contributions
- Conservative debt reduction
- Higher interest rate scenario
- Lower return scenario

## MVP scoring rules

For MVP, use transparent rule-based scoring.

Example:

- If forecast income at target date is at or above goal, goal progress score is high.
- If cash buffer covers target months of expenses, cash buffer score is high.
- If LVR is below a chosen threshold, debt score is stronger.
- If one asset class dominates the portfolio, diversification score is reduced.
- If regular contributions are active and aligned with target strategy, contribution score improves.

## Configuration

The score should be configurable per scenario.

Example:

```yaml
financial_health:
  enabled: true
  target_buffer_months: 6
  max_preferred_lvr: 0.70
  max_single_asset_class_exposure: 0.65
  weights:
    goal_progress: 0.25
    cash_buffer: 0.20
    debt_sustainability: 0.20
    liquidity: 0.15
    diversification: 0.10
    contribution_discipline: 0.10
```

## Important caveat

The score is a planning signal only. It should not be presented as financial advice or a guarantee of outcomes.

All scores should display the assumptions used and allow the user to inspect the underlying calculations.
