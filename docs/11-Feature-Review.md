# Feature Review

## Purpose

This document captures additional features identified from the financial strategy context and early product design discussions.

## Current required features

The core product should support:

- Scenario-based family wealth forecasting
- YAML-driven inputs
- GUI input editing
- Assets, liabilities, income, expenses, and goals
- ETF-by-ETF tracking
- Superannuation tracking
- Property and loan tracking
- Investment bond tracking
- Regular contribution schedules
- Scenario comparison
- API-backed market assumptions where appropriate

## Additional recommended features

### 1. Milestone tracker

Track key dates such as:

- Deposit target date
- Investment property purchase date
- Retirement target date
- Loan payoff dates
- Investment bond year 10 date
- Child education stages

### 2. Cash buffer and resilience view

Show whether the household has enough liquidity for:

- Emergency buffer
- Property holding costs
- Loan repayment stress
- Interest rate increases
- Income interruption

### 3. Tax assumptions panel

Show assumptions used for:

- Income tax brackets
- Medicare levy
- Super contribution caps
- Division 293 assumptions
- Rental property deductions
- Capital gains tax assumptions

### 4. Loan split and deductibility tracking

Track each loan split separately so deductible and non-deductible debt can be modelled clearly.

Useful fields:

- Split name
- Purpose
- Balance
- Interest rate
- Repayment type
- Deductible status
- Linked asset

### 5. Contribution planner

Track planned contributions into:

- Superannuation
- ETFs
- Investment bond
- Cash buffer
- Loan offset
- Debt reduction

### 6. Scenario sensitivity testing

Compare outcomes under changes to:

- Interest rates
- Investment returns
- Property growth
- Rent
- Living costs
- Contribution rates
- Retirement age

### 7. Forecast confidence labels

Label assumptions as:

- Manual
- API-sourced
- Historical average
- Conservative estimate
- Optimistic estimate
- Adviser/accountant confirmed

### 8. Annual review workflow

Support an annual review checklist:

- Update balances
- Update loan rates
- Update ETF prices
- Update super balances
- Update tax assumptions
- Review progress to goal
- Save a dated snapshot

### 9. Data snapshots

Keep dated snapshots of external assumptions so old forecasts remain explainable.

Examples:

- ETF price snapshot
- Interest rate snapshot
- Inflation snapshot
- Tax-rate snapshot
- Property valuation snapshot

### 10. Report export

Later versions should export:

- Scenario summary
- Annual review report
- Assumptions report
- Goal progress report

## Features to defer

Defer these until the core engine is reliable:

- Bank feeds
- Brokerage feeds
- Open Banking
- Automatic personal tax lodgement logic
- Adviser-grade compliance tooling
- Complex Monte Carlo simulation
- Direct financial product recommendations

## Product caution

The app should remain a planning and modelling tool. It should show assumptions and projections clearly, but avoid presenting outputs as personalised financial advice.
