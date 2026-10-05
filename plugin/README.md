# Hiring Signals: live job openings from company career sites

Ask Claude which roles a company is hiring for, where, and how fast. This plugin connects Claude to two Apify Actors through Apify's hosted MCP server and reads the company's own career site:

| Tool | Career sites covered |
|---|---|
| [Workday Jobs Scraper](https://apify.com/kadi_bence/workday-jobs-scraper) | Workday (`*.myworkdayjobs.com`) |
| [Greenhouse, Lever & Ashby Jobs Scraper](https://apify.com/kadi_bence/ats-jobs-scraper) | Greenhouse, Lever, Ashby, Workable, Recruitee, Personio |

Each job comes back with title, company, locations, remote / hybrid / onsite, posted date, salary range (when the posting states one) and a link to the live posting.

Example prompts:

- "What is NVIDIA hiring for in Germany right now?"
- "Compare open engineering roles at Stripe, Ramp and Notion. Which team is growing fastest?"
- "List remote data-science jobs posted in the last 7 days at Hugging Face and Databricks."

## Setup (about 3 minutes)

You need a free Apify account. The Actors run on your account and are billed per saved job (fractions of a cent each, see each Actor's Store page). Apify's free plan includes monthly credit that covers small lookups.

1. Create an account at [apify.com](https://console.apify.com/sign-up) (skip if you have one).
2. Install the plugin:
   - Claude Code: run `/plugin marketplace add kiskecske24/hiring-signals-mcp`, then `/plugin install hiring-signals@hiring-signals`.
   - Claude apps: install "Hiring Signals" from the plugin directory.
3. Connect Apify: in Claude Code run `/mcp`, select `hiring-signals`, choose **Authenticate** and approve the Apify login in your browser (OAuth; no token to copy).
4. Ask a question, for example "What is Salesforce hiring for in London?"

### Prefer an API token instead of OAuth?

Any MCP client can send your [Apify API token](https://console.apify.com/account/integrations) as the header `Authorization: Bearer <token>` instead of using OAuth (see below). The plugin itself never reads tokens or files from your machine.

## Use it from any MCP client

The same server works in Claude Desktop, Cursor, VS Code and other MCP clients:

- URL: `https://mcp.apify.com/?tools=Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper`
- Transport: Streamable HTTP
- Auth: OAuth, or the header `Authorization: Bearer <your Apify API token>`

## Costs and limits

- Each call returns at most 20 jobs per company unless you or Claude ask for more, so a typical question costs well under one cent.
- You pay Apify only for jobs saved, plus a tiny per-run start fee; there is no subscription for this plugin.
- Set a monthly usage limit in [Apify Console > Billing](https://console.apify.com/billing) if you want a hard cap.

## What's included

- `.mcp.json`: the Apify MCP server limited to the two Actors above (plus Apify's run and dataset helper tools).
- `skills/company-job-openings`: tells Claude which Actor fits which career site, how to keep runs small, and how to summarise results.

## Privacy and data

- The Actors read only public job postings that companies publish on their career sites. They collect no personal data and strip e-mail addresses and phone numbers from job descriptions by default.
- Requests go from Claude to Apify's MCP server (`mcp.apify.com`) and from there to the career sites. This plugin has no server of its own and no telemetry.
- Full privacy notice: [PRIVACY.md](https://github.com/kiskecske24/hiring-signals-mcp/blob/master/PRIVACY.md). Apify's privacy policy: <https://apify.com/privacy-policy>.

## Support

Open an issue in this repository, or on the Actor's Apify Store page (Issues tab).

## License

MIT
