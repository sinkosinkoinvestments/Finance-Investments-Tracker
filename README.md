# Financial Strategy Automated Tracker

This repository contains an automated system to track financial projections, ETF prices, and interest rates using Google Sheets, GitHub Actions, and Looker Studio for mobile dashboarding.

## Phase 1: Database & Automation Setup
1. Upload `Financial_Strategy_Model.xlsx` to Google Drive and convert to a Google Sheet.
2. Get the `SHEET_ID` from the Google Sheet URL (the long string of characters between `/d/` and `/edit`).
3. Create a Google Cloud Service account and generate a JSON credential key.
4. Share your Google Sheet with the Service Account email address.
5. In this GitHub repository, go to **Settings > Secrets and variables > Actions**.
6. Add two New Repository Secrets:
   - `GOOGLE_CREDENTIALS`: Paste the entire content of your JSON key file.
   - `SHEET_ID`: Paste your Google Sheet ID.
7. The automation will now run daily at midnight UTC, updating ETF values and RBA rates.

## Phase 2: Looker Studio Dashboard Setup
1. Go to [Looker Studio](https://datastudio.google.com) and create a "Blank Report".
2. Add data to report: Select **Google Sheets**, authenticate, and choose your `Financial_Strategy_Model` sheet. Select the **Projections** tab.
3. Build your Desktop view using the time-series charts (e.g., Net Worth over Time, Loan Balances decreasing).

## Phase 3: Mobile Layout Configuration (Free Version)
Since Looker Studio Pro is required for the native mobile app, use this workaround to create a perfect mobile web-app experience:
1. In Looker Studio, go to **Page > New Page** and rename it to "Mobile View".
2. With the "Mobile View" page selected, go to the right sidebar: **Theme and Layout > Layout**.
3. Under Canvas Size, change it to **Custom**. Set Width to `400 px` and Height to `1200 px` (or higher if you have more charts).
4. Build your mobile dashboard by stacking your charts vertically. Keep font sizes large (14pt+).
5. Click **View** in the top right, and copy the URL specifically while on the "Mobile View" page.
6. Send this URL to your phone. Open it in Safari or Chrome, tap the share icon, and select **"Add to Home Screen"**. 
7. You now have an app-like icon on your phone that opens directly to a perfectly scaled, auto-updating financial dashboard.
