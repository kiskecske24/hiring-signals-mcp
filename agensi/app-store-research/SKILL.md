---
name: app-store-research
description: Research iPhone and iPad apps on the Apple App Store - top free and paid charts by category and country (169 countries), app details (rating, rating count, price, version, release notes, size, genre), every app of a developer, and user reviews. Use when the user asks which apps top a chart, how an app ranks in a country or category, compares competing apps, wants an app's rating, price or update history, lists a developer's apps, wants recent App Store reviews or complaints about an app, or does app market or ASO research.
---

# App Store research: charts, apps, developers and reviews

The `app-store-research` MCP server gives you one tool. It reads Apple's public App Store data (charts, app pages and reviews) country by country, so prices, ratings, ranks and reviews are what users in that country see.

## If the tools are not available yet

If you cannot see the `app-store-scraper` tool, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/app-store-scraper`
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http app-store-research "<server URL>"`, then `/mcp` > app-store-research > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `app-store-research` with the URL above.

Then stop and wait; do not try to scrape the App Store another way.

Tool names can carry a client prefix (for example `mcp__app-store-research__kadi_bence--app-store-scraper`); match on the part after the prefix.

| Tool | What it reads | Limit fields |
|---|---|---|
| `kadi_bence--app-store-scraper` | Apple App Store (iPhone / iPad): top charts, app details, developer portfolios, reviews | `maxResults` (app rows, default 20), `maxChartPositions` (default 20), `maxReviewsPerApp` (default 5, max 20) |

This skill covers Apple's App Store only, not Google Play. Download numbers and revenue are not public on the App Store; say so instead of estimating.

## Build the input

Use one or more of these sources in a run:

- Specific apps: `appIds` with App Store URLs (`https://apps.apple.com/us/app/notes/id1110145109`), numeric IDs (`1110145109`) or bundle IDs (`com.spotify.client`). If the user gives only an app name, look up its App Store URL first or run the overall chart for its category.
- A developer's apps: `developerIds` with developer page URLs or IDs.
- Charts: `charts` (`top-free`, `top-paid`), `chartCategories` (for example `Games`, `Finance`, `Health & Fitness`; empty = all apps), `platform` (`iphone` or `ipad`), `maxChartPositions` (how deep: top 10, top 50...).
- `countries`: 2-letter codes (`["us"]` default, `["gb", "de"]`). Every app, developer and chart is read in each country, so each extra country multiplies the rows.
- Reviews: `includeReviews: true` and `maxReviewsPerApp` (Apple shows up to 20 per app and country on the public page). For a daily review feed, `onlyNewReviews: true` with a `monitorName`.

## Keep runs small and cheap

Each app row and each review is a paid event on the user's Apify account (fractions of a cent; reviews are about ten times cheaper than apps; see the Actor's Store page for the current price).

- Rows = apps (or chart positions) x countries. Keep `maxChartPositions` at 10-20 and use one country unless the user compares countries.
- Before a run that could return more than about 500 rows, say how many rows it may save and ask the user to confirm. `maxResults: 0` means no limit.
- Turn on reviews only when the user asks about reviews, complaints or sentiment.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields`. If the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

Rows have a `type`:

- App rows: `appId`, `name`, `developer`, `bundleId`, `price`, `formattedPrice`, `isFree`, `rating`, `ratingCount`, `ratingCurrentVersion`, `ratingHistogram`, `primaryGenre`, `genres`, `version`, `currentVersionReleaseDate`, `releaseDate`, `releaseNotes`, `sizeMb`, `contentRating`, `languages`, `country`, `url`, and for charts `chartType`, `chartCategory`, `chartPosition`. Useful `fields`: `type,chartPosition,name,developer,rating,ratingCount,formattedPrice,primaryGenre,version,currentVersionReleaseDate,country,url`.
- Review rows (`type` = review): `appId`, `appName`, `rating`, `title`, `text`, `date`, `version`, `country`. Useful `fields`: `type,appName,rating,title,text,date,version`.

## Answer the question

Summarise for the user, do not dump raw rows:

- Charts: a ranked table (position, app, developer, rating and rating count, price); point out new or unusual entries.
- Comparisons: one row per app with rating, rating count, price, last update and size; say which is rated highest and which is updated most often.
- Reviews: the average stars of the returned reviews, the 3-5 most common complaints and praises with one short quote each, and whether they concern the current version.
- Link apps by `url`. Say which country the data is for.

## Don't

- Don't use this tool to identify or profile individual reviewers. Report review content, not reviewer identities.
- Don't present review samples as complete: Apple's public page shows at most 20 reviews per app and country.
- Don't run the same apps again in one conversation; reuse the dataset with `get-dataset-items`.
