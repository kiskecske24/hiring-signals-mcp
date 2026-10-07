# Job Market Data skill

Ask your AI agent about the job market for a role, skill or city. Searches Germany's federal job board (Bundesagentur für Arbeit), Sweden's Platsbanken and a daily-updated database of tech and startup jobs from Greenhouse, Lever, Ashby, Workable, Recruitee and Personio career pages worldwide.

Example prompts:
- "How many data engineer jobs were posted in Berlin in the last 14 days, and who is hiring?"
- "Find remote product manager jobs in Europe posted this week, with salary ranges."
- "Which employers in Stockholm are hiring nurses right now?"

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/job-market-data/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/arbeitsagentur-jobs-scraper,Kadi_Bence/sweden-jobs-scraper,Kadi_Bence/ats-jobs-feed`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http job-market-data "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Also listed
Official MCP Registry: `io.github.kiskecske24/job-market-data` (also Smithery and Glama).

## Costs
The tools run on your Apify account and bill per saved job (fractions of a cent; default 20 jobs per search, so a typical question costs well under one cent). Apify's free plan includes monthly credit.

## Works well with
The Hiring Signals skill (one company's openings from its own career site).

## Privacy
Only public job postings. No personal data; contact details in job descriptions are stripped.

## Custom versions
Need other countries' job boards, a daily new-jobs feed or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
