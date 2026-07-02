# Input GUI Design

## Purpose

The app should include a browser-based input screen so scenario assumptions can be edited without manually changing YAML files.

The GUI should make it easier to update assets, loans, income, contributions, assumptions, and goals, while still allowing the underlying scenario files to remain transparent and version-controlled.

## Design principle

The GUI is an editor for scenario inputs. It should not hide assumptions or make irreversible changes.

Recommended flow:

```text
Edit inputs in browser
  -> validate fields
  -> preview forecast
  -> export scenario YAML or JSON
```

For the first version, the GUI can export a file rather than writing directly to GitHub.

## Input sections

The GUI should include these sections:

1. Family profile
2. Income
3. Properties
4. Loans
5. Superannuation
6. ETFs and investments
7. Investment bond
8. Cash and savings buffers
9. Expenses
10. Goals
11. Assumptions
12. Scenarios

## Key fields

The input editor should support:

- Asset names and balances
- Loan balances, rates, repayment types, and frequencies
- Contribution amounts and frequencies
- Target dates and target goals
- ETF tickers and target allocations
- Property values, rent, expenses, and growth assumptions
- Tax and inflation assumptions
- Scenario notes

## Validation rules

The GUI should check that:

- Required fields are present.
- Numeric values are valid.
- Dates are valid.
- ETF allocations add to 100 percent.
- Contribution frequencies are supported.
- Loans have clear deductible or non-deductible treatment.
- Target date is after the scenario start date.

## MVP recommendation

Build the first version as a client-side editor that:

- Loads a scenario file.
- Displays editable form fields.
- Runs a preview forecast.
- Exports updated YAML or JSON.

Do not add direct GitHub writes, databases, or account sync until the local editor works reliably.

## Future enhancements

- Save drafts in browser local storage.
- Compare an edited scenario with the base scenario.
- Import CSV files.
- Pre-fill market assumptions from data snapshots.
- Add secure GitHub commit support later if needed.
