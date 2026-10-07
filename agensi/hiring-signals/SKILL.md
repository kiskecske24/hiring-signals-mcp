---
name: hiring-signals
description: Look up a company's current job openings (hiring signals) from its own career site on Workday, Greenhouse, Lever, Ashby, Workable, Recruitee or Personio. Use when the user asks which roles a company is hiring for, where it is hiring, whether it is growing a team, wants to compare hiring across companies, wants sales/recruiting intent signals (which accounts are hiring for X), or needs a list of open jobs with salary, location, remote status and posted date.
---

# Hiring signals: live job openings from company career sites

The `hiring-signals` MCP server gives you two tools. Both read the public job feeds that the company's own career site uses, so results are the company's live openings.

## If the tools are not available yet

If you cannot see the `workday-jobs-scraper` / `ats-jobs-scraper` tools, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper`
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http hiring-signals "<server URL>"`, then `/mcp` > hiring-signals > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `hiring-signals` with the URL above.

Then stop and wait; do not try to scrape career sites another way.

Tool names can carry a client prefix (for example `mcp__hiring-signals__kadi_bence--workday-jobs-scraper`); match on the part after the prefix.

| Tool | Career sites | Limit field (default 20) |
|---|---|---|
| `kadi_bence--workday-jobs-scraper` | Workday (`*.myworkdayjobs.com`, `*.myworkdaysite.com`) | `maxJobsPerSite` |
| `kadi_bence--ats-jobs-scraper` | Greenhouse, Lever, Ashby, Workable, Recruitee, Personio (auto-detected) | `maxJobsPerCompany` |

## Pick the tool

1. If the user gives a career-site URL, choose by its domain: `myworkdayjobs.com` / `myworkdaysite.com` means Workday; `greenhouse.io`, `lever.co`, `ashbyhq.com`, `workable.com`, `recruitee.com`, `personio.de` / `personio.com` mean the ATS tool.
2. If you only have a company name: large enterprises (Fortune 500, banks, retailers, pharma) mostly use Workday; startups and tech scale-ups mostly use Greenhouse, Lever or Ashby. Try the likelier tool first.
3. If a tool reports that the company was not found, try the other tool once. If both miss, tell the user the company probably uses another applicant system and ask for its careers page URL.

Pass company names in `companies` (a list). A domain such as `target.com` is more precise than a common word such as `Target`.

## Keep runs small and cheap

Each saved job is a paid event on the user's Apify account (fractions of a cent per job; see the Actor's Store page for the current price). The default of 20 jobs per company is enough to answer most questions.

- Narrow with filters instead of raising the limit:
  - Workday: `searchKeywords`, `titleIncludes`, `titleExcludes`, `countries`, `postedWithinDays`.
  - ATS tool: `titleIncludes`, `titleExcludes`, `locations`, `remoteOnly`, `postedWithinDays`.
- Raise the limit only when the user wants a full list or counts. Before a run that could return more than about 500 jobs, say how many jobs it may save and ask the user to confirm. Setting the limit to `0` means no limit.
- Leave `descriptionFormat` at its default unless the user needs the full job text.

## Read the results

The tool returns the first items of the run's dataset. When the run saved more items than you received, call `get-dataset-items` with the returned `datasetId`, using `limit`, `offset` and `fields` (for example `title,location,workMode,postedDate,salaryMin,salaryMax,url`) to page through them. If a run is still going when the tool returns, call `get-actor-run` with `waitSecs` and then read the dataset.

Both tools return one item per job with the same core fields: `title`, `company`, `location`, `workMode` (`remote` / `hybrid` / `onsite`), `postedDate`, `salaryMin`, `salaryMax`, `salaryCurrency`, `url`.

## Answer the question

Summarise for the user, do not dump raw rows:

- Count of openings returned, and say if the list was capped by the limit.
- Grouped by team or function (from titles), and by country or location.
- Remote share, salary ranges where the posting states one, and how many were posted in the last 7 or 30 days.
- Link the 3-5 most relevant postings by `url`.

## Don't

- Don't use these tools to find, profile or contact individual people. The job data contains no personal data, and contact details in descriptions are stripped by default (`stripContactInfo`).
- Don't run the same company again in one conversation; reuse the dataset with `get-dataset-items`.
