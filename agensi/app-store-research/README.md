# App Store Research skill

Ask your AI agent about iPhone and iPad apps on the Apple App Store: top free and paid charts by category and country, app details (rating, price, version, release notes, size), a developer's full app list, and recent user reviews.

Example prompts:
- "What are the top 20 free Finance apps in the US and the UK right now?"
- "Compare Headspace, Calm and Balance: rating, number of ratings, price and last update."
- "What do users complain about in the latest App Store reviews of our app?"

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/app-store-research/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/app-store-scraper`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http app-store-research "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Costs
The tool runs on your Apify account and bills per app row and per review (fractions of a cent; reviews are about ten times cheaper). A top-20 chart costs about two cents. Apify's free plan includes monthly credit.

## Coverage
Apple App Store, iPhone and iPad, 169 countries. Not included: Google Play, download numbers and revenue (Apple does not publish them).

## Privacy
Only public App Store data. Reviewer identities are not used for profiling.

## Custom versions
Need a daily chart or review feed, Google Play, or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
