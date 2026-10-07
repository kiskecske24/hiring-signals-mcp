---
name: company-research
description: Research a company's website - detect its tech stack (CMS, ecommerce platform, analytics and marketing tags, JavaScript framework, CDN, hosting, web server, payment providers, live chat) and capture screenshots or PDFs of its pages. Use when the user asks what a company's or competitor's website is built with, whether a site uses Shopify / WordPress / HubSpot / a given tool, wants to qualify a list of prospect websites by technology, compare the stacks of several companies, or needs a screenshot (desktop or mobile, full page or above the fold) or PDF of a web page.
---

# Company research: tech stack and screenshots of a company's website

The `company-research` MCP server gives you two tools. Both work on any public website the user names; one reads the live HTML to detect technologies, the other renders the page in a real browser and saves an image or PDF.

## If the tools are not available yet

If you cannot see the `tech-stack-detector` / `website-screenshot` tools, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot`
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http company-research "<server URL>"`, then `/mcp` > company-research > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `company-research` with the URL above.

Then stop and wait; do not try to fingerprint or screenshot sites another way.

Tool names can carry a client prefix (for example `mcp__company-research__kadi_bence--tech-stack-detector`); match on the part after the prefix.

| Tool | What it does | Input / limit |
|---|---|---|
| `kadi_bence--tech-stack-detector` | 7,600+ technology fingerprints: CMS, ecommerce, analytics, tag managers, marketing automation, advertising, framework, CDN, hosting, server, payment processors, live chat | `urls` (list of URLs or domains); one charge per website. `maxPagesPerSite` (default 1, max 10) |
| `kadi_bence--website-screenshot` | Screenshot (PNG, JPEG, WebP) or PDF of a page, desktop / laptop / tablet / mobile | `urls` (list, required); one charge per screenshot |

## Pick the tool

1. "What is X built with / does X use Y / which of these sites run Z" means `tech-stack-detector`. Pass bare domains (`stripe.com`); `https://` is added automatically.
2. "Show me / capture / screenshot / PDF of a page" means `website-screenshot`. Pass full page URLs when the user means a specific page (`https://stripe.com/pricing`).
3. For a "quick look at a company's website" run the tech stack on the homepage and, only if the user wants to see it, one screenshot.

This skill does not cover domain WHOIS, SEO audits, funding rounds or company registries. Say so instead of guessing.

## Keep runs small and cheap

Each website analysed and each screenshot is a paid event on the user's Apify account (fractions of a cent each; see the Actor's Store page for the current price). Neither tool has a result limit: the cost is the number of URLs you pass.

- Tech stack: keep `maxPagesPerSite` at 1 (homepage). Use 2-3 only when the user asks about tools that live on inner pages (checkout, pricing, blog); the price per website stays the same. Use `onlyCategories` (for example `["CMS", "Ecommerce", "Analytics"]`) to answer a narrow question; sites with nothing in those categories are not charged.
- Screenshots: default to `"format": "jpeg"` and `"fullPage": false` (above the fold) unless the user wants the whole page; use `"device": "mobile"` for a mobile view, `"format": "pdf"` for a printable copy.
- Before a run with more than about 50 URLs, say how many URLs it will process and ask the user to confirm.
- Failed sites (blocked, timed out, no technology found) are listed with an `error` and not charged.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields` to keep the response small. If the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

- Tech stack (one item per website): `url`, `finalUrl`, `title`, `technologyCount`, `technologyNames`, and one list per category: `cms`, `ecommerce`, `analytics`, `tagManagers`, `marketingAutomation`, `advertising`, `framework`, `cdn`, `hosting`, `server`, `paymentProcessors`, `liveChat`, `programmingLanguages`. `technologies` holds `name`, `version`, `confidence` and `categories` per technology. Useful `fields`: `url,title,cms,ecommerce,analytics,framework,cdn,hosting,marketingAutomation,paymentProcessors,technologyCount`.
- Screenshot (one item per URL): `url`, `title`, `screenshotUrl` (a public link to the image or PDF), `format`, `device`, `width`, `height`, `bytes`, `truncated`, `error`. Useful `fields`: `url,title,screenshotUrl,width,height,error`.

## Answer the question

Summarise for the user, do not dump raw rows:

- Tech stack: lead with the answer to the question (for example "Yes, Shopify Plus"), then a short grouped list: platform (CMS / ecommerce / framework), marketing and analytics, infrastructure (CDN, hosting). For several sites, a compact comparison table.
- Mention when a detection has low `confidence` or when a site failed (`error`), and that tools loaded only after login or consent are not visible.
- Screenshots: give the `screenshotUrl` link(s) (or show the image if the client can render it) and note if the page was `truncated`.

## Don't

- Don't use these tools to find, profile or contact individual people. They read only public pages; no personal data is collected.
- Don't screenshot pages behind a login or pages the user is not allowed to capture; `website-screenshot` respects robots.txt by default (`respectRobotsTxt`), keep it on.
- Don't run the same site again in one conversation; reuse the dataset with `get-dataset-items`.
