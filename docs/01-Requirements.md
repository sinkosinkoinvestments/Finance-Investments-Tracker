# Requirements

## Purpose

Finance Investments Tracker is a web-based dashboard for tracking and forecasting a family's investment position over time.

The system should help answer:

- What is the family's current net worth?
- How are assets, debt, contributions, and income changing over time?
- Are current investment plans on track to meet the target goal by the target date?
- How do different investment, debt, contribution, and property scenarios compare?

## Primary context

The initial planning context is based on a family investment strategy with:

- Two adults and one child.
- Primary residence in Wishart, Queensland.
- Target acquisition of an investment property on acreage at Cooroy.
- Superannuation balances for each adult.
- Investment bond contributions.
- ETF investing using individual ETF allocations.
- A long-term goal of retirement/investment income by a defined target date.

The dashboard must be configurable so the above context is data-driven rather than hard-coded.

## Core tracked inputs

Prefer storing source inputs in YAML files so scenarios are transparent, version-controlled, and easy for Codex or humans to edit.

The system should track:

1. Primary property
2. Investment property
3. Superannuation accounts
4. Cash savings
5. ETFs, with each ETF tracked individually
6. Investment bond
7. Regular contributions to all assets, with different frequencies
8. Primary job income
9. Investment income
10. Investment goal and target date
11. Multiple scenarios for comparison

## Core workflows

### 1. View current position

The user should be able to see:

- Total assets
- Total debts
- Net worth
- Investable assets
- Property equity
- Cash buffer
- Current income and expenses

### 2. Forecast future position

The user should be able to forecast:

- Asset balances by year
- Debt balances by year
- Contributions by asset class
- Projected income by target date
- Net worth at target date
- Whether the investment goal is on track

### 3. Compare scenarios

The user should be able to compare scenarios such as:

- Base case
- Higher ETF contributions
- Higher super contributions
- Conservative debt reduction
- Different investment property prices
- Different interest rate assumptions
- Different rent and investment income assumptions

### 4. Track contributions

The system should support contributions with different frequencies, including:

- Weekly
- Fortnightly
- Monthly
- Quarterly
- Annually
- One-off

### 5. Track investment goals

Each scenario should support a target goal such as:

- Target annual net income
- Target retirement date
- Target net worth
- Target investable asset base
- Target property debt level

## Required dashboard pages

Initial dashboard pages should include:

- Overview
- Assets
- Debt
- Cashflow
- Forecast
- Scenarios
- Contributions
- Goals
- Assumptions

## Non-functional requirements

- Static-site friendly where possible.
- Suitable for GitHub Pages or Cloudflare Pages.
- Mobile-friendly layout.
- Source YAML files should be human-readable.
- No secrets or private API keys in the frontend.
- Calculations should be explainable and auditable.
- Scenario results should be reproducible from committed source data.

## Out of scope for MVP

- Bank feed integrations.
- Broker integrations.
- Automatic live market pricing.
- Tax advice automation.
- Personal financial advice recommendations.
- Authentication beyond deployment-level access controls.

## Important caveat

This dashboard is a planning and tracking tool. It should not present outputs as personal financial advice. Forecasts should clearly show assumptions, limitations, and sensitivity to interest rates, income, returns, tax, and contribution changes.
