# Hiring Signals skill

Ask your AI agent which roles a company is hiring for, where, and how fast. Reads live openings straight from the company's own career site (Workday, Greenhouse, Lever, Ashby, Workable, Recruitee, Personio).

Example prompts:
- "What is NVIDIA hiring for in Germany right now?"
- "Compare open engineering roles at Stripe, Ramp and Notion. Which team is growing fastest?"
- "Which of these 20 accounts opened data-engineering roles in the last 14 days?"

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/hiring-signals/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http hiring-signals "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Also listed
Official MCP Registry: `io.github.kiskecske24/hiring-signals` (also Smithery and Glama).

## Costs
The scrapers run on your Apify account and bill per saved job (fractions of a cent; default 20 jobs per company, so a typical question costs well under one cent). Apify's free plan includes monthly credit.

## Privacy
Only public job postings. No personal data; contact details in job descriptions are stripped by default.

## Custom versions
Need other career sites, a weekly feed or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
