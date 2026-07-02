# Integrations

## Purpose

This document defines how Finance Investments Tracker should integrate with external data sources such as ETF prices, interest rates, inflation assumptions, and exchange rates.

## Integration principle

External APIs should enrich the dashboard, but they should not make forecasts non-reproducible.

The preferred pattern is:

```text
External API
  -> adapter
  -> normalised data snapshot
  -> scenario engine
  -> dashboard
```

Scenario YAML files should remain the primary source of truth. API data should either:

1. populate missing values,
2. update reference market data,
3. create dated snapshots, or
4. provide optional live display values.

## Recommended data-source categories

### ETF prices

Use cases:

- Current ETF market value
- Historical returns
- Portfolio valuation
- Allocation drift
- Scenario assumptions

Potential data options:

- Free or low-cost market data APIs
- Static CSV imports
- Manually maintained price snapshots
- Brokerage export files

Important caution:

- Some market-data services have licensing restrictions.
- Some unofficial finance endpoints can break without notice.
- The app should support manual fallback values.

### Interest rates

Use cases:

- Mortgage rate assumptions
- Sensitivity testing
- Scenario comparison
- Cash account return assumptions

Potential data options:

- Manual scenario values
- Public central bank statistics
- Lender-specific manually entered rates
- Cached reference-rate snapshots

### Inflation

Use cases:

- Living cost escalation
- Retirement income targets
- Property expenses
- School fees and lifestyle costs

Potential data options:

- Manual assumption in YAML
- Public statistics feeds
- Historical inflation snapshots

### Exchange rates

Use cases:

- International ETF exposure
- USD-denominated ETF values
- Foreign withholding tax assumptions

Potential data options:

- Free exchange-rate APIs
- Manual annual assumptions
- Snapshot files

### Property values

Use cases:

- Property growth assumptions
- Manual valuation updates
- Scenario comparison

Potential data options:

- Manual valuations
- Property dashboard exports
- Periodic valuation snapshots

## Adapter architecture

Each integration should use the same adapter pattern:

```text
fetch source data
  -> validate response
  -> normalise fields
  -> write snapshot
  -> expose to calculation engine
```

Suggested adapter interface:

```ts
interface MarketDataAdapter<TInput, TOutput> {
  id: string;
  sourceName: string;
  fetch(input: TInput): Promise<TOutput>;
  normalise(raw: unknown): TOutput;
  validate(output: TOutput): boolean;
}
```

## Snapshot-first design

Do not calculate long-range forecasts directly from live API calls.

Instead:

1. Fetch current data.
2. Save a dated snapshot.
3. Use the snapshot in forecasts.
4. Keep the scenario reproducible.

Example:

```text
/data/snapshots/market-prices/2026-01-31.yml
/data/snapshots/interest-rates/2026-01-31.yml
```

## Secrets and API keys

Do not expose paid API keys in client-side code.

If an integration requires a secret key, use one of these approaches:

1. Manual import instead of live API access.
2. GitHub Actions scheduled job storing generated static data.
3. Cloudflare Worker or serverless function.
4. Backend service later if required.

For MVP, avoid paid API dependencies.

## MVP integration plan

Start with manual and static-data-friendly integrations:

1. YAML assumptions
2. Manual price snapshots
3. CSV imports
4. Optional free public data feeds

Then add live API adapters only after the calculation engine and dashboard are stable.

## Recommended MVP snapshots

```text
/data/snapshots/
├── market-prices/
│   └── 2026-01-31.yml
├── interest-rates/
│   └── 2026-01-31.yml
├── inflation/
│   └── 2026-01-31.yml
└── exchange-rates/
    └── 2026-01-31.yml
```

## Future enhancements

- Scheduled data refresh via GitHub Actions.
- Cloudflare Worker for private API calls.
- Alert when API values differ materially from scenario assumptions.
- Historical charting of assumption changes.
- Data-source health checks.
