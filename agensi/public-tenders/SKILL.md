---
name: public-tenders
description: Find European public procurement opportunities and contract awards from TED (Tenders Electronic Daily, the EU's official tenders journal) by keyword, CPV code, buyer country, region, estimated value, publication date and submission deadline. Use when the user looks for open calls for tenders they can still bid on, public-sector sales leads, government contracts in a country or sector, who won a public contract and for how much, what a public buyer has purchased, or wants a list of recent EU tenders with deadlines and values.
---

# Public tenders: EU calls for tenders and contract awards from TED

The `public-tenders` MCP server gives you one tool. It reads the official TED API (the EU's public procurement journal, about 1,000 new notices per working day from EU/EEA countries plus Switzerland, the Western Balkans, Türkiye, Ukraine, Moldova and Georgia), so results are the official notices.

## If the tools are not available yet

If you cannot see the `ted-tenders-scraper` tool, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes: a Smithery login plus a free Apify account):

- Server URL: `https://public-tenders--bence-kadi.run.tools` (hosted on Smithery: https://smithery.ai/servers/bence-kadi/public-tenders)
- Listed in the official MCP Registry as `io.github.kiskecske24/public-tenders` (also on Smithery/Glama), so registry-aware clients can install it by name.
- Transport: Streamable HTTP. Auth: OAuth. The agent opens a Smithery login; Smithery then asks the user to connect their free Apify account (apify.com), where the scrapers run.
- Claude Code: `claude mcp add --transport http public-tenders "<server URL>"`, then `/mcp` > public-tenders > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `public-tenders` with the URL above.

Then stop and wait; do not try to scrape tender portals another way.

Tool names can carry a client prefix (for example `mcp__public-tenders__kadi_bence--ted-tenders-scraper`); match on the part after the prefix.

| Tool | Source | Limit field (default 20) |
|---|---|---|
| `kadi_bence--ted-tenders-scraper` | TED (ted.europa.eu): EU-wide above-threshold notices | `maxResults` |

Coverage: TED publishes tenders above the EU value thresholds. Small national tenders, US federal contracts (SAM.gov) and UK tenders after 2020 (Find a Tender) are not in TED; say so when the user asks for them.

## Build the search

- `keywords`: short terms searched in the full notice text, any EU language; several entries mean OR. Notices are mostly in the buyer's language, so add local words (`["software", "Software", "logiciel", "informatica"]`).
- `countries`: buyer country as ISO codes (`["DE", "FR"]`). `nutsCodes` narrows to a region (`DE2` Bavaria, `FR10` Paris area).
- `cpvCodes`: CPV categories; sub-categories are included (`72000000` IT services, `45000000` construction, `79000000` business services, `33000000` medical equipment). A CPV code is more precise than a keyword.
- `noticeTypes`: `["contract_notice"]` for open calls the user can still bid on; `["contract_award"]` for winners and awarded values; `prior_information` for planned purchases.
- Dates: `publishedWithinDays` (for example 7) for recent notices; `deadlineAfter` (`"today"` or `"+14 days"`) to keep only tenders still open for bids; `publishedFrom` / `publishedTo` (YYYY-MM-DD) for a fixed period.
- `minEstimatedValue` / `maxEstimatedValue` (notice currency, mostly EUR) and `buyerName` (words in the authority's name) narrow further.

For "open tenders I can bid on" use `noticeTypes: ["contract_notice"]` plus `deadlineAfter: "today"`.

## Keep runs small and cheap

Each saved notice is a paid event on the user's Apify account (fractions of a cent per notice; see the Actor's Store page for the current price). The default of 20 notices is enough to answer most questions.

- Narrow with `countries`, `cpvCodes`, `noticeTypes` and a date filter instead of raising `maxResults`.
- Raise the limit only when the user wants a full list or counts. Before a run that could return more than about 500 notices, say how many notices it may save and ask the user to confirm. Setting `maxResults` to `0` means no limit.
- Without any keyword, country, CPV or date filter the search matches every notice ever published; always set at least one filter.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields` (for example `publicationDate,title,noticeType,buyerName,buyerCountry,mainCpvLabel,estimatedValue,currency,deadline,url`) to page through them. If the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

One item per notice: `publicationNumber`, `title`, `noticeType`, `contractNature`, `buyerName`, `buyerCountry`, `buyerCity`, `mainCpv`, `mainCpvLabel`, `cpvCodes`, `estimatedValue`, `currency`, `deadline`, `procedureType`, `placeOfPerformanceNuts`, `lotsCount`, `url` (TED page), `pdfUrl`. Award notices also fill `winners`, `awardedValue` and `awardedCurrency`. `description` holds the notice summary text.

## Answer the question

Summarise for the user, do not dump raw rows:

- Count of notices returned, and say if the list was capped by `maxResults`.
- For open calls: sort by `deadline`, flag those closing within 7 days, and give buyer, country, CPV label and estimated value.
- For awards: who won (`winners`), for how much (`awardedValue`), and which buyers buy most.
- Link the 3-5 most relevant notices by `url`. Titles are often in the buyer's language; translate them briefly.

## Don't

- Don't use this tool to find, profile or contact individual people. Notices are official publications about public buyers and contracts.
- Don't present an estimated value or deadline as certain when the field is empty; say it was not published.
- Don't run the same search again in one conversation; reuse the dataset with `get-dataset-items`.
