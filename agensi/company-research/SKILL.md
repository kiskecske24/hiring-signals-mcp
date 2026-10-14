---
name: company-research
description: Research a company's website and domain - detect its tech stack (CMS, ecommerce platform, analytics and marketing tags, JavaScript framework, CDN, hosting, web server, payment providers, live chat), capture screenshots or PDFs of its pages, look up domain WHOIS / RDAP data (age, registrar, expiry, DNS, e-mail provider, SPF / DMARC) and run an SEO audit (0-100 score per page, broken links, fix hints). Use when the user asks what a company's or competitor's website is built with, whether a site uses Shopify / WordPress / HubSpot / a given tool, wants to qualify a list of prospect websites by technology, compare the stacks of several companies, needs a screenshot (desktop or mobile, full page or above the fold) or PDF of a web page, asks how old a domain is, when it expires, who the registrar is or which e-mail provider a company uses, or wants an SEO check, broken-link scan or technical audit of a site.
---

# Company research: tech stack, screenshots, domain WHOIS and SEO audit

The `company-research` MCP server gives you four tools. All work on any public website or domain the user names: one reads the live HTML to detect technologies, one renders pages in a real browser and saves an image or PDF, one looks up the domain in the official registries (RDAP / WHOIS) and DNS, and one crawls the site for an SEO audit.

## If the tools are not available yet

If you cannot see the `tech-stack-detector` / `website-screenshot` / `domain-whois-lookup` / `seo-site-audit` tools, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot,Kadi_Bence/domain-whois-lookup,Kadi_Bence/seo-site-audit`
- Also listed in the official MCP Registry as `io.github.kiskecske24/company-research` (also on Smithery/Glama). If an installed server shows only two of the four tools, re-add it with the URL above.
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http company-research "<server URL>"`, then `/mcp` > company-research > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `company-research` with the URL above.

Then stop and wait; do not try to fingerprint or screenshot sites another way.

Tool names can carry a client prefix (for example `mcp__company-research__kadi_bence--tech-stack-detector`); match on the part after the prefix.

| Tool | What it does | Input / limit |
|---|---|---|
| `kadi_bence--tech-stack-detector` | 7,600+ technology fingerprints: CMS, ecommerce, analytics, tag managers, marketing automation, advertising, framework, CDN, hosting, server, payment processors, live chat | `urls` (list of URLs or domains); one charge per website. `maxPagesPerSite` (default 1, max 10) |
| `kadi_bence--website-screenshot` | Screenshot (PNG, JPEG, WebP) or PDF of a page, desktop / laptop / tablet / mobile | `urls` (list, required); one charge per screenshot |
| `kadi_bence--domain-whois-lookup` | Official RDAP / WHOIS for 1,100+ TLDs: registered or not, registrar, created / updated / expiry dates, domain age, nameservers, status, DNSSEC; plus DNS (A, MX, NS, TXT), SPF, DMARC and e-mail provider | `domains` (list of domains, URLs or e-mail addresses); one charge per domain. `includeDns` (default on) |
| `kadi_bence--seo-site-audit` | Crawls a site and scores every page 0-100: title, meta description, H1, canonical, indexability, redirects, broken links, missing alt texts, structured data, response time, with fix hints | `startUrls` (required); one charge per page audited. `maxPages` (default 20) |

## Pick the tool

1. "What is X built with / does X use Y / which of these sites run Z" means `tech-stack-detector`. Pass bare domains (`stripe.com`); `https://` is added automatically.
2. "Show me / capture / screenshot / PDF of a page" means `website-screenshot`. Pass full page URLs when the user means a specific page (`https://stripe.com/pricing`).
3. "How old is this domain / when does it expire / who is the registrar / which e-mail provider / is SPF or DMARC set up / is this domain registered" means `domain-whois-lookup`. Pass bare domains; URLs and e-mail addresses are reduced to the domain automatically.
4. "SEO audit / broken links / why is this page not indexed / check titles and meta descriptions" means `seo-site-audit`. Pass the homepage (or a section start URL) as `startUrls: [{"url": "https://example.com/"}]`.
5. For a "quick look at a company's website" run the tech stack on the homepage and the WHOIS lookup on the domain (both cheap); add a screenshot or SEO audit only if the user wants them.

This skill does not cover funding rounds, company registries or people. Say so instead of guessing.

## Keep runs small and cheap

Each website analysed, screenshot, domain looked up and page audited is a paid event on the user's Apify account (fractions of a cent each; see the Actor's Store page for the current price). The tech stack and screenshot tools have no result limit: the cost is the number of URLs you pass.

- Tech stack: keep `maxPagesPerSite` at 1 (homepage). Use 2-3 only when the user asks about tools that live on inner pages (checkout, pricing, blog); the price per website stays the same. Use `onlyCategories` (for example `["CMS", "Ecommerce", "Analytics"]`) to answer a narrow question; sites with nothing in those categories are not charged.
- Screenshots: default to `"format": "jpeg"` and `"fullPage": false` (above the fold) unless the user wants the whole page; use `"device": "mobile"` for a mobile view, `"format": "pdf"` for a printable copy.
- WHOIS: `maxResults` caps a long list (use 10-20 to test first). Leave `includeDns` on; it is included in the price.
- SEO audit: keep `maxPages` at 20 for a first look; raise it (100-500) only when the user wants the whole site, and use `includeUrlGlobs` (for example `["/blog/*"]`) to audit one section. `maxDepth: 0` audits only the start URL(s). You pay only for pages audited successfully; link checks are free.
- Before a run with more than about 50 URLs, domains or pages, say how many URLs it will process and ask the user to confirm.
- Failed sites (blocked, timed out, no technology found) are listed with an `error` and not charged.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields` to keep the response small. If the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

- Tech stack (one item per website): `url`, `finalUrl`, `title`, `technologyCount`, `technologyNames`, and one list per category: `cms`, `ecommerce`, `analytics`, `tagManagers`, `marketingAutomation`, `advertising`, `framework`, `cdn`, `hosting`, `server`, `paymentProcessors`, `liveChat`, `programmingLanguages`. `technologies` holds `name`, `version`, `confidence` and `categories` per technology. Useful `fields`: `url,title,cms,ecommerce,analytics,framework,cdn,hosting,marketingAutomation,paymentProcessors,technologyCount`.
- WHOIS (one item per domain): `domain`, `registered`, `availability`, `registrar`, `createdDate`, `updatedDate`, `expiresDate`, `domainAgeDays`, `daysUntilExpiry`, `status`, `nameservers`, `dnssec`, `registrantOrganization`, `registrantCountry` (only when the registry publishes them), `mxRecords`, `hasSpf`, `hasDmarc`, `dmarcPolicy`, `emailProvider`, `error`. Useful `fields`: `domain,registered,registrar,createdDate,expiresDate,domainAgeDays,daysUntilExpiry,nameservers,emailProvider,hasSpf,hasDmarc,dmarcPolicy,error`.
- SEO audit (one item per page): `url`, `status`, `seoScore` (0-100), `issues`, `fixes`, `issueCount`, `errorCount`, `warningCount`, `indexable`, `title`, `titleLength`, `metaDescription`, `metaDescriptionLength`, `h1`, `h1Count`, `canonical`, `metaRobots`, `redirectChain`, `brokenLinks`, `brokenLinkCount`, `imagesMissingAlt`, `structuredDataTypes`, `wordCount`, `responseTimeMs`, `depth`. Useful `fields`: `url,status,seoScore,issueCount,issues,fixes,brokenLinkCount,indexable,title`.
- Screenshot (one item per URL): `url`, `title`, `screenshotUrl` (a public link to the image or PDF), `format`, `device`, `width`, `height`, `bytes`, `truncated`, `error`. Useful `fields`: `url,title,screenshotUrl,width,height,error`.

## Answer the question

Summarise for the user, do not dump raw rows:

- Tech stack: lead with the answer to the question (for example "Yes, Shopify Plus"), then a short grouped list: platform (CMS / ecommerce / framework), marketing and analytics, infrastructure (CDN, hosting). For several sites, a compact comparison table.
- Mention when a detection has low `confidence` or when a site failed (`error`), and that tools loaded only after login or consent are not visible.
- WHOIS: answer the question directly ("registered in 2011, 14 years old, renews in March 2027 via MarkMonitor"); for several domains, a compact table. Say when a registry hides a date or the registrant, and flag domains that expire within 30 days or have no SPF / DMARC.
- SEO audit: give the average and lowest `seoScore`, the most common issues across pages ranked by how many pages they affect, every broken link with the page it was found on, and the 3-5 most valuable fixes from `fixes`. Do not list every page unless asked.
- Screenshots: give the `screenshotUrl` link(s) (or show the image if the client can render it) and note if the page was `truncated`.

## Don't

- Don't use these tools to find, profile or contact individual people. They read only public pages and registry data; no personal data is collected (registrant names, e-mails and phone numbers of individuals are not returned).
- Don't screenshot pages behind a login or pages the user is not allowed to capture; `website-screenshot` respects robots.txt by default (`respectRobotsTxt`), keep it on.
- Don't run an SEO audit with a high `maxPages` on a site the user does not own or manage without saying it crawls the whole site; keep `maxConcurrency` low (2-5) for small sites. The crawler respects robots.txt.
- Don't run the same site again in one conversation; reuse the dataset with `get-dataset-items`.
