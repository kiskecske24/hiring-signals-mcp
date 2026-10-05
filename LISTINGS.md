# Directory listings: Hiring Signals

All listings point to the same server; nothing is hosted by us:

- MCP URL: `https://mcp.apify.com/?tools=Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper`
- Transport: Streamable HTTP
- Auth: OAuth (Apify login), or header `Authorization: Bearer <Apify API token>`
- Repo: https://github.com/kiskecske24/hiring-signals-mcp (must be public first)

Users pay Apify per saved job on their own Apify account; that is where the income comes from. None of these directories needs billing setup.

## 0. Before any listing: make the GitHub repo public

```bash
gh repo create kiskecske24/hiring-signals-mcp --public --source . --push
```

## 1. Claude plugin directory

- Where: https://claude.ai/directory/manage > Submit new > Plugin bundle
- Repo: `kiskecske24/hiring-signals-mcp`, branch `master`, plugin path `plugin`
- Name: Hiring Signals
- Short description: Live job openings from company career sites on Workday, Greenhouse, Lever, Ashby, Workable, Recruitee and Personio.
- Category: Sales / Research (whichever is closest)
- Validation: `claude plugin validate . --strict` passes locally.

## 2. Official MCP Registry

- Double-click `registry/PUBLISH_REGISTRY.cmd` (downloads the official `mcp-publisher` v1.8.1 from GitHub, logs in with GitHub, publishes `server.json`).
- Name: `io.github.kiskecske24/hiring-signals` (the GitHub login proves the namespace).
- Glama and some other directories import new registry entries automatically.

## 3. Smithery

- Where: https://smithery.ai/new > enter URL (log in with GitHub)
- URL: the MCP URL above
- Namespace / name: `@kiskecske24/hiring-signals`
- Auth: leave as OAuth (the server answers 401 with an OAuth challenge, which Smithery expects). No config schema needed.
- Display name: Hiring Signals
- Description: same as the Glama description below.

## 4. Glama

- Where: https://glama.ai/mcp/servers > Add MCP Server > **Connector** (remote URL; log in with GitHub)
- Name: Hiring Signals
- URL: the MCP URL above
- Description: Live job openings from company career sites. Two tools: Workday Jobs Scraper (any myworkdayjobs.com site) and Greenhouse, Lever & Ashby Jobs Scraper (also Workable, Recruitee, Personio). Returns title, company, locations, remote status, posted date, salary range and URL per job. Runs on your Apify account (OAuth or API token), pay per saved job.
- Test credentials: not needed if OAuth works; otherwise use a Glama-only Apify token you can revoke.
- `glama.json` in the repo lists the maintainer (kiskecske24), so you can claim the repo listing.

## 5. mcp.so

- Where: https://mcp.so/submit > tab **Remote Server** (free option; ignore the $39 fast-track)
- Name: Hiring Signals
- Repository URL: https://github.com/kiskecske24/hiring-signals-mcp
- Server URL: the MCP URL above
- Transport: Streamable HTTP
- Auth: OAuth or Bearer Apify API token
- Short description: Live job openings from Workday, Greenhouse, Lever, Ashby, Workable and Personio career sites.
- Tags: jobs, hiring, recruiting, sales intelligence, workday, greenhouse, apify
- Connection JSON:

```json
{
  "mcpServers": {
    "hiring-signals": {
      "type": "http",
      "url": "https://mcp.apify.com/?tools=Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper"
    }
  }
}
```

## Description to reuse anywhere (long)

Hiring Signals connects your AI assistant to the live career sites of any company. Ask "What is NVIDIA hiring for in Germany?" or "Which teams are Stripe and Ramp growing?" and get current openings with title, locations, remote / hybrid / onsite, posted date, salary range and a link to each posting. Two tools cover the main applicant systems: Workday (most large enterprises) and Greenhouse, Lever, Ashby, Workable, Recruitee and Personio (most startups and scale-ups, auto-detected). Each call returns up to 20 jobs per company by default, so lookups cost fractions of a cent on your Apify account. Public job data only, no personal data.
