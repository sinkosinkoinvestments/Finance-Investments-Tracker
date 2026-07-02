# Data Model

## Purpose

This document defines the preferred source data model for Finance Investments Tracker.

The goal is to make investment scenarios editable through YAML files and reproducible through deterministic calculations.

## Scenario file pattern

Each scenario should be stored as a YAML file under `/scenarios`.

Example:

```text
/scenarios/base.yml
/scenarios/cooroy-1-8m.yml
/scenarios/high-etf-contributions.yml
```

## Top-level scenario structure

```yaml
scenario:
  id: cooroy-1-8m
  name: Cooroy $1.8M investment property
  start_date: 2026-01-01
  target_date: 2043-12-31
  currency: AUD

family:
  adults:
    - id: adult_1
      age_at_start: 43
      income:
        salary: 200000
    - id: adult_2
      age_at_start: 44
      income:
        salary: 300000
  dependants:
    - id: child_1
      age_at_start: 7

goals:
  target_annual_net_income: 350000
  target_age: 60

assumptions:
  inflation_rate: 0.03
  property_growth_rate: 0.03
  equity_growth_rate: 0.07
  super_growth_rate: 0.07
  bond_growth_rate: 0.06
  interest_rate: 0.06
```

## Asset types

### Primary property

```yaml
primary_property:
  name: Wishart home
  type: primary_residence
  value: 1700000
  growth_rate: 0.03
  loans:
    - id: wishart_home_loan
      balance: 560000
      interest_rate: 0.06
      repayment_amount: 2100
      repayment_frequency: fortnightly
      deductible: false
```

### Investment property

```yaml
investment_properties:
  - id: cooroy
    name: Cooroy acreage investment property
    value: 1800000
    purchase_date: 2026-12-31
    growth_rate: 0.03
    rent:
      amount: 900
      frequency: weekly
      annual_growth_rate: 0.03
    expenses:
      annual_amount: 25000
      annual_growth_rate: 0.03
    features:
      dual_dwelling: true
      family_member_rent_free: true
    loans:
      - id: cooroy_loan
        balance: 1440000
        interest_rate: 0.06
        loan_type: interest_only
        deductible: true
      - id: wishart_equity_split
        balance: 260000
        interest_rate: 0.06
        loan_type: interest_only
        deductible: true
```

### Superannuation

```yaml
superannuation:
  accounts:
    - id: adult_1_super
      owner: adult_1
      balance: 400000
      growth_rate: 0.07
      contributions:
        - type: employer_sg
          amount: 23000
          frequency: annual
        - type: salary_sacrifice
          amount: 8000
          frequency: annual
    - id: adult_2_super
      owner: adult_2
      balance: 400000
      growth_rate: 0.07
      contributions:
        - type: employer_sg
          amount: 30000
          frequency: annual
```

### Cash savings

```yaml
cash:
  accounts:
    - id: emergency_buffer
      name: Emergency buffer
      balance: 0
      target_balance: 150000
      interest_rate: 0.04
    - id: cooroy_deposit_savings
      name: Cooroy deposit savings
      balance: 0
      target_balance: 150000
      target_date: 2026-12-31
```

### ETFs

```yaml
etfs:
  portfolio:
    id: global_etf_portfolio
    strategy: 60/20/20 global equities
    holdings:
      - ticker: VTS
        allocation: 0.60
        balance: 0
        expected_return: 0.07
      - ticker: NDQ
        allocation: 0.20
        balance: 0
        expected_return: 0.07
      - ticker: VGS
        allocation: 0.20
        balance: 0
        expected_return: 0.07
    contributions:
      - amount: 1000
        frequency: monthly
```

### Investment bond

```yaml
investment_bond:
  provider: Genlife
  balance: 200000
  plan_year: 4
  target_plan_year: 10
  growth_rate: 0.06
  contributions:
    - amount: 3000
      frequency: monthly
```

### Income

```yaml
income:
  salary:
    - owner: adult_1
      amount: 200000
      frequency: annual
    - owner: adult_2
      amount: 300000
      frequency: annual
  investment_income:
    - source: cooroy_rent
      linked_asset: cooroy
      amount: 900
      frequency: weekly
```

### Expenses

```yaml
expenses:
  living_costs:
    annual_amount: 150000
    annual_growth_rate: 0.03
```

## Contribution model

Every contribution should support:

```yaml
amount: 1000
frequency: monthly
start_date: 2026-01-01
end_date: null
linked_asset: global_etf_portfolio
```

Supported frequencies:

- weekly
- fortnightly
- monthly
- quarterly
- annual
- one_off

## Forecast output model

The forecast engine should produce yearly rows like:

```yaml
- year: 2026
  age_adult_1: 43
  age_adult_2: 44
  total_assets: 0
  total_debt: 0
  net_worth: 0
  investable_assets: 0
  annual_income: 0
  annual_expenses: 0
  annual_surplus: 0
  goal_progress_percent: 0
```

## Validation rules

- Scenario IDs must be unique.
- Contributions must have supported frequencies.
- Dates must be valid ISO dates.
- Asset balances must be numeric.
- Allocation percentages should sum to 1.0 where applicable.
- Loan records must state whether interest is deductible.
- Forecast assumptions must be visible and editable.
