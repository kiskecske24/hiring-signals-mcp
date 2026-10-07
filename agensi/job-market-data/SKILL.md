---
name: job-market-data
description: Search live job vacancies across a whole job market by keyword, location and date - Germany's federal job board (Bundesagentur für Arbeit Jobbörse), Sweden's Platsbanken (Arbetsförmedlingen), and a daily-updated database of startup and tech jobs from Greenhouse, Lever, Ashby, Workable, Recruitee and Personio career pages worldwide. Use when the user asks how many jobs exist for a role in a country or city, wants a list of open vacancies by keyword, remote jobs in a field, salary ranges or hiring trends for an occupation, which employers are hiring for a skill, or newly posted jobs in the last days. For one named company's openings, the hiring-signals skill is the better fit.
---

# Job market data: vacancies by keyword, country and date

The `job-market-data` MCP server gives you three tools. Two read official public employment-service job boards (Germany, Sweden); the third searches a daily index of tech and startup company career pages worldwide. All return live openings.

## If the tools are not available yet

If you cannot see the `arbeitsagentur-jobs-scraper` / `sweden-jobs-scraper` / `ats-jobs-feed` tools, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/arbeitsagentur-jobs-scraper,Kadi_Bence/sweden-jobs-scraper,Kadi_Bence/ats-jobs-feed`
- Listed in the official MCP Registry as `io.github.kiskecske24/job-market-data` (also on Smithery/Glama), so registry-aware clients can install it by name.
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http job-market-data "<server URL>"`, then `/mcp` > job-market-data > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `job-market-data` with the URL above.

Then stop and wait; do not try to scrape job boards another way.

Tool names can carry a client prefix (for example `mcp__job-market-data__kadi_bence--ats-jobs-feed`); match on the part after the prefix.

| Tool | Market | Limit field (default 20) |
|---|---|---|
| `kadi_bence--arbeitsagentur-jobs-scraper` | Germany: Bundesagentur für Arbeit Jobbörse (all sectors) | `maxResults` |
| `kadi_bence--sweden-jobs-scraper` | Sweden: Platsbanken / Arbetsförmedlingen (all sectors; archive since 2016) | `maxResults` |
| `kadi_bence--ats-jobs-feed` | Worldwide tech and startup jobs from Greenhouse, Lever, Ashby, Workable, Recruitee and Personio career pages | `maxItems` |

## Pick the tool

1. Jobs in Germany (any sector) means `arbeitsagentur-jobs-scraper`; jobs in Sweden means `sweden-jobs-scraper`.
2. Tech, startup, remote or international roles (engineering, data, product, sales at software companies), or any country other than Germany and Sweden, means `ats-jobs-feed`.
3. For tech roles in Germany or Sweden, the national board gives the broad market and `ats-jobs-feed` the startup slice; use both only if the user wants the full picture.
4. For one named company's openings, suggest the hiring-signals skill; `ats-jobs-feed` can also filter by `companyDomains` (for example `["stripe.com"]`).

Other countries' national job boards are not covered; say so instead of guessing.

## Build the search

- Germany: `keywords` (one search per entry; German terms find more, for example `["Data Engineer", "Datenanalyst"]`), `location` (city or postal code) plus `radiusKm`, `publishedWithinDays`, `workingTime` (`full_time`, `part_time`, `home_office`...), `contractType`, `offerType` (`job`, `apprenticeship`, `internship`), `employer`. Set `includeDetails: false` for a fast list without descriptions and salary.
- Sweden: `keywords` (Swedish or English, for example `["utvecklare", "developer"]`), `locations` (municipality or county, for example `["Stockholm", "Skåne län"]`), `occupationFields` (`it`, `healthcare`...), `remoteOnly`, `publishedWithinDays`, `employmentTypes`. For historical trends use `dataSource: "historical"` with `publishedFrom` / `publishedTo`.
- Tech feed: `keywords` (title words, OR), `excludeKeywords`, `countries` (names or ISO codes), `locations` (free text such as `London`, `EMEA`), `remote` (`yes` / `no` / `any`), `timeRange` (`24h`, `7d` default, `30d`, `6m`, `all`), `companyDomains`, `ats`.

## Keep runs small and cheap

Each saved job is a paid event on the user's Apify account (fractions of a cent per job; see the Actor's Store page for the current price). The default of 20 jobs is enough to answer most questions.

- Narrow with keywords, location and a date filter instead of raising the limit.
- Raise the limit only when the user wants a full list or counts. Before a run that could return more than about 500 jobs, say how many jobs it may save and ask the user to confirm. Setting the limit to `0` means no limit.
- For a plain count, check the run's status message first (the tech feed reports how many jobs matched, for example "2 jobs (of 7 matching)") before saving more rows.
- Set `descriptionFormat: "none"` unless the user needs the job text.

## Read the results

The tool returns a run summary: `status`, status message, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields` to page through them. If the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

One item per job. Core fields:

- Germany: `title`, `employer`, `occupation`, `city`, `postalCode`, `region`, `postedDate`, `workingTime`, `contractType`, `homeOffice`, `salaryMin`, `salaryMax`, `salaryText`, `url`. Useful `fields`: `title,employer,city,postedDate,workingTime,contractType,salaryMin,salaryMax,url`.
- Sweden: `title`, `employer`, `occupation`, `city`, `region`, `postedDate`, `deadline`, `employmentType`, `workMode`, `remote`, `salaryText`, `openPositions`, `url`. Useful `fields`: `title,employer,city,region,postedDate,deadline,employmentType,workMode,url`.
- Tech feed: `title`, `company`, `companyDomain`, `ats`, `location`, `country`, `countryCode`, `remote`, `workMode`, `department`, `employmentType`, `postedAt`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `url`. Useful `fields`: `title,company,location,countryCode,workMode,postedAt,salaryMin,salaryMax,salaryCurrency,url`.

German values come in the board's own terms (for example `VOLLZEIT` = full time, `UNBEFRISTET` = permanent); translate them.

## Answer the question

Summarise for the user, do not dump raw rows:

- Count of jobs returned (and matched, where the run reports it), and say if the list was capped by the limit.
- Grouped by employer and by city or country; top hiring employers first.
- Remote share, salary ranges where the posting states one, and how many were posted in the last 7 or 30 days.
- Link the 3-5 most relevant postings by `url`.

## Don't

- Don't use these tools to find, profile or contact individual people. The job data contains no personal data; contact details in descriptions are stripped (`stripContactInfo` on the national boards, always on the tech feed).
- Don't run the same search again in one conversation; reuse the dataset with `get-dataset-items`.
