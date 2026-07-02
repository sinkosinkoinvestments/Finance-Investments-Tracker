# Calculation Engine

## Purpose

The calculation engine is the core of the Finance Investments Tracker.

It should convert scenario inputs into deterministic financial forecasts that can be reviewed, tested, and reproduced.

## Primary goal

Given a scenario file, the engine should answer:

- What is the current position?
- What happens each year between start date and target date?
- Are goals on track?
- Which assumptions drive the outcome?
- How do alternative scenarios compare?

## Design principle

The calculation engine must be independent from the dashboard UI.

```text
Scenario YAML
  -> parse
  -> validate
  -> normalise
  -> calculate
  -> forecast output
  -> dashboard rendering
```

The dashboard should display calculated outputs, not perform financial calculations directly.

## Inputs

The engine should consume normalised scenario data including:

- Family profile
- Income
- Expenses
- Properties
- Loans
- Superannuation
- ETFs
- Investment bond
- Cash accounts
- Contributions
- Tax assumptions
- Market assumptions
- Goals
- Portfolio allocation targets
- Financial health configuration

## Outputs

The engine should produce:

- Yearly forecast rows
- Current-position summary
- Net worth forecast
- Cashflow forecast
- Asset balances
- Debt balances
- Income forecast
- Expense forecast
- Contribution forecast
- Goal progress
- Portfolio allocation
- Financial health score
- Recommendation inputs

## Forecast period

Initial implementation should use yearly periods.

Future versions may add monthly forecasting, but yearly forecasts are simpler and sufficient for long-range strategy modelling.

## Core modules

### 1. Scenario parser

Responsibilities:

- Load scenario YAML or JSON.
- Convert source values into internal types.
- Apply defaults.
- Preserve scenario metadata.

### 2. Scenario validator

Responsibilities:

- Validate required fields.
- Validate numeric values.
- Validate supported contribution frequencies.
- Validate dates.
- Validate portfolio allocations.
- Validate loan deductibility fields.
- Return warnings and errors.

### 3. Normalisation module

Responsibilities:

- Convert weekly, fortnightly, monthly, quarterly, and annual values into annual equivalents.
- Convert one-off events into dated forecast events.
- Standardise asset, liability, income, and expense records.

### 4. Contribution engine

Responsibilities:

- Apply recurring contributions.
- Apply one-off contributions.
- Route contributions to the correct asset or liability.
- Support scheduled changes over time.

### 5. Asset engine

Responsibilities:

- Project asset values.
- Apply growth assumptions.
- Apply contributions and withdrawals.
- Support different asset types.

Asset types:

- Property
- Superannuation
- ETF portfolio
- Investment bond
- Cash
- Other investments

### 6. Liability engine

Responsibilities:

- Project loan balances.
- Apply interest assumptions.
- Apply repayments.
- Track deductible and non-deductible debt separately.
- Estimate payoff dates.

### 7. Cashflow engine

Responsibilities:

- Calculate income.
- Calculate expenses.
- Calculate contributions.
- Calculate loan repayments.
- Calculate annual surplus or deficit.

### 8. Tax engine

Responsibilities:

- Estimate income tax.
- Apply Medicare levy assumptions.
- Apply rental property deductions.
- Model negative gearing assumptions.
- Apply super contribution cap assumptions.

MVP tax calculations should be simple and clearly labelled as estimates.

### 9. Goal engine

Responsibilities:

- Compare forecast results against scenario goals.
- Calculate goal progress.
- Identify shortfalls.
- Identify surplus capacity.

### 10. Portfolio allocation engine

Responsibilities:

- Calculate current allocation.
- Calculate investable allocation.
- Compare allocation against scenario target.
- Identify overweight and underweight categories.

### 11. Financial health score engine

Responsibilities:

- Calculate category scores.
- Calculate overall score.
- Generate strengths and risks.
- Provide inputs to the recommendation engine.

## Forecast row structure

Example yearly output:

```yaml
- year: 2026
  age:
    adult_1: 43
    adult_2: 44
  assets:
    total: 0
    property: 0
    superannuation: 0
    etfs: 0
    investment_bond: 0
    cash: 0
  liabilities:
    total: 0
    deductible: 0
    non_deductible: 0
  net_worth: 0
  cashflow:
    income: 0
    expenses: 0
    tax_estimate: 0
    contributions: 0
    loan_repayments: 0
    surplus: 0
  goals:
    target_income_progress: 0
    on_track: true
  allocation:
    current: {}
    target_gap: {}
  health_score:
    score: 0
    label: null
```

## Calculation assumptions

All assumptions should be visible and traceable.

Examples:

- Growth rates
- Inflation rates
- Interest rates
- Tax rates
- Contribution caps
- Target allocations
- Rental growth assumptions

## Testing expectations

The engine should have tests for:

- Frequency conversion
- Compound growth
- Loan interest and repayment calculations
- Contribution application
- Scenario validation
- Goal progress
- Financial health score

## MVP scope

The first implementation should support:

- One base scenario
- Yearly forecast rows
- Property values
- Loan balances
- Superannuation balances
- ETF balances
- Investment bond balances
- Cash savings
- Annual income and expenses
- Basic tax estimate
- Goal progress

## Deferred scope

Defer until after MVP:

- Monthly forecasting
- Monte Carlo simulation
- Direct bank feeds
- Live broker data
- Complex tax optimisation
- Automated advice generation
