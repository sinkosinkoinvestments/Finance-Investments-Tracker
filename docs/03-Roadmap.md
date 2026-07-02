# Roadmap

## Product direction

Finance Investments Tracker should evolve from a simple dashboard into a family wealth planning and forecasting platform.

The product should help compare scenarios, forecast progress toward financial goals, and explain the assumptions behind every projection.

## Priority 1: Planning foundation

Status: In progress

Deliverables:

- Requirements document
- Architecture document
- Data model document
- Roadmap
- Sprint plan
- Decision log
- Integration plan
- AI development guide

## Priority 2: Scenario and forecasting engine

Goal: Build the core engine that converts YAML scenario files into forecast outputs.

Deliverables:

- YAML scenario schema
- Scenario parser
- Scenario validator
- Contribution frequency normaliser
- Forecast engine
- Yearly projection output
- Basic unit tests

## Priority 3: Core dashboard

Goal: Build a readable dashboard that shows current position and future trajectory.

Initial pages:

- Overview
- Assets
- Debt
- Cashflow
- Forecast
- Scenarios
- Assumptions

## Priority 4: API data adapters

Goal: Add optional data feeds for market and macro inputs without making the dashboard dependent on paid APIs.

Planned adapter types:

- ETF price data
- ETF distribution/yield data
- Interest rate assumptions
- Inflation assumptions
- Exchange rates
- Property valuation assumptions

Important principle:

- API data should enrich scenarios, not replace the source YAML files.
- Scenario files remain the source of truth.
- API-sourced values should be cached or snapshotted for reproducibility.

## Priority 5: Scenario comparison

Goal: Allow side-by-side comparison of alternative futures.

Example scenarios:

- Base plan
- Cooroy $1.8M investment property
- Higher ETF contributions
- Higher super contributions
- Conservative debt reduction
- Higher interest rates
- Lower market returns
- Earlier or later retirement

## Priority 6: Reporting and exports

Goal: Generate reviewable outputs for annual planning.

Possible outputs:

- PDF strategy summary
- Annual position report
- Scenario comparison report
- Assumptions report
- CSV exports

## Priority 7: Private deployment

Preferred deployment path:

```text
GitHub
  -> Cloudflare Pages
  -> Cloudflare Access
  -> Private dashboard
```

## Paused or future work

- Bank feed integrations
- Open Banking connections
- Brokerage integrations
- Automatic super fund feeds
- Personal tax optimisation automation
- Adviser-grade compliance tooling
