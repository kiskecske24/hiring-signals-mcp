# Agensi.io listings

Upload one zip per listing (folder at zip root). Shared for every listing:

- Pricing: Free
- Permissions: Network Access; needs access to Apify. Domains: apify.com, console.apify.com, mcp.apify.com
- Author contact: bence.kadi@gmail.com, https://apify.com/kadi_bence

---

## 1. hiring-signals.zip

**Listing name:** Hiring Signals: Live Job Openings by Company

**Tagline:** Ask which roles any company is hiring for, straight from its own career site.

**Long description:**
Hiring Signals lets your AI agent answer "what is this company hiring for?" with live data instead of guesses. It reads the public job feeds behind the company's own career site on Workday, Greenhouse, Lever, Ashby, Workable, Recruitee and Personio, so the openings are current and complete, not a stale copy from a job board.

Ask for one company or compare many. The agent picks the right source for each company, keeps runs small, and summarises the result: number of openings, teams and functions that are growing, locations and remote share, salary ranges where the posting states one, and how many roles were posted in the last week or month, with links to the most relevant postings.

Typical uses: sales and account-based marketing teams looking for buying signals (which target accounts just opened data or security roles), recruiters and agencies tracking target companies, investors and analysts watching team growth, and job seekers checking where a company is really hiring.

The skill connects to Apify's hosted MCP server and runs two published Apify Actors on your own free Apify account. You pay only fractions of a cent per job returned; a typical question costs well under one cent. Only public job postings are read, and contact details in descriptions are removed by default.

**Category:** Sales & Marketing (alt: Research & Data)

**Tags:** hiring signals, job openings, careers, workday, greenhouse, lever, sales intelligence, mcp

**Compatibility:** Requires a free Apify account and the hiring-signals MCP server (setup in README). Works with any MCP-capable agent.

**FAQ**
- Q: Which companies does it work for? A: Any company whose career site runs on Workday, Greenhouse, Lever, Ashby, Workable, Recruitee or Personio, which covers most large enterprises and most tech scale-ups. If a company uses another system, the agent tells you and asks for the careers page URL.
- Q: What does it cost? A: The skill is free. The scrapers run on your Apify account at fractions of a cent per job (default 20 jobs per company), and Apify's free plan includes monthly credit.
- Q: Does it collect personal data? A: No. It reads only public job postings and strips e-mail addresses and phone numbers from descriptions by default.

---

## 2. company-research.zip

**Listing name:** Company Research: Website Tech Stack & Screenshots

**Tagline:** See what any company's website is built with and capture it in one prompt.

**Long description:**
Company Research gives your AI agent two practical tools for looking into a company through its website. The first detects the site's technology stack with more than 7,600 fingerprints: CMS, ecommerce platform, analytics and tag managers, marketing automation, advertising pixels, JavaScript framework, CDN, hosting, web server, payment providers and live chat, with versions and confidence scores. The second renders any page in a real browser and returns a screenshot (PNG, JPEG or WebP) or a PDF, on desktop, laptop, tablet or mobile, with cookie banners and ads hidden.

Ask "what is this site built with?", "which of these 30 prospects run Shopify or WooCommerce?", "does this competitor use HubSpot?" or "show me their pricing page on mobile". The agent keeps runs small, answers the question first, groups technologies into platform, marketing and infrastructure, and links each screenshot.

Typical uses: agencies qualifying prospects before a pitch, sales teams enriching account lists by technology, product and marketing teams benchmarking competitors, and anyone who needs a quick visual record of a web page.

The skill connects to Apify's hosted MCP server and runs two published Apify Actors on your own free Apify account, billed at fractions of a cent per website or screenshot. Failed sites are not charged. Only public pages are read and robots.txt is respected.

**Category:** Research & Data (alt: Sales & Marketing)

**Tags:** tech stack, website analysis, competitor research, lead qualification, screenshot, wappalyzer alternative, company research, mcp

**Compatibility:** Requires a free Apify account and the company-research MCP server (setup in README). Works with any MCP-capable agent.

**FAQ**
- Q: How accurate is the tech stack detection? A: It matches the live HTML, headers, cookies and scripts against an open fingerprint database with 7,600+ technologies; each result has a confidence score. Tools that load only after login or cookie consent may not be visible.
- Q: What does it cost? A: The skill is free. Each website analysed or screenshot taken costs a fraction of a cent on your Apify account, failed sites are free, and Apify's free plan includes monthly credit.
- Q: Can it check domain age, SEO or funding? A: Not yet. This version covers tech stack and screenshots; more company data sources will be added as they are published.

---

## 3. public-tenders.zip

**Listing name:** Public Tenders: EU Procurement Search (TED)

**Tagline:** Find open EU public tenders and contract awards by keyword, CPV and deadline.

**Long description:**
Public Tenders lets your AI agent search TED (Tenders Electronic Daily), the official journal for public procurement in the European Union, which publishes about 1,000 new notices every working day. Ask in plain English and the agent turns your question into the right filters: keywords in any EU language, CPV categories, buyer countries and regions, estimated contract value, publication date and submission deadline.

Get open calls for tenders you can still bid on, sorted by deadline, with buyer, country, category, estimated value and a link to the official notice. Or look backwards at contract awards: who won, for how much, and which public buyers purchase what you sell. The agent translates foreign-language titles, flags tenders that close within a week, and keeps every search small so it costs fractions of a cent.

Typical uses: bid and tender managers building a daily shortlist, B2G sales teams finding public-sector buyers, consultants and analysts researching market size and competitors' wins, and small companies entering public procurement for the first time.

The skill connects to Apify's hosted MCP server and runs a published Apify Actor on your own free Apify account, billed per notice returned (default 20 per search). Coverage is the EU and EEA plus Switzerland, the Western Balkans, Türkiye, Ukraine, Moldova and Georgia, for notices above EU value thresholds.

**Category:** Business & Operations (alt: Sales & Marketing)

**Tags:** public tenders, procurement, TED, government contracts, CPV, bid management, B2G sales, mcp

**Compatibility:** Requires a free Apify account and the public-tenders MCP server (setup in README). Works with any MCP-capable agent.

**FAQ**
- Q: Which countries are covered? A: All EU and EEA countries plus Switzerland, the Western Balkans, Türkiye, Ukraine, Moldova and Georgia, as published on TED. Small national tenders below EU thresholds, US federal and post-2020 UK tenders are not included.
- Q: Can it show only tenders I can still bid on? A: Yes. Ask for open calls and the agent filters to contract notices whose submission deadline is today or later, sorted by deadline.
- Q: What does it cost? A: The skill is free. Each notice returned costs a fraction of a cent on your Apify account (default 20 per search), and Apify's free plan includes monthly credit.

---

## 4. job-market-data.zip

**Listing name:** Job Market Data: Vacancies by Keyword & Country

**Tagline:** Live job vacancies in Germany, Sweden and global tech, searchable by your agent.

**Long description:**
Job Market Data gives your AI agent live access to job vacancies across whole markets, not just one company. It searches Germany's federal job board (Bundesagentur für Arbeit Jobbörse, all sectors), Sweden's Platsbanken from Arbetsförmedlingen (all sectors, with an archive back to 2016), and a daily-updated database of tech and startup jobs from Greenhouse, Lever, Ashby, Workable, Recruitee and Personio career pages worldwide.

Ask how many data engineer jobs were posted in Berlin this month, which employers in Stockholm are hiring nurses, or where to find remote product manager roles in Europe with salary ranges. The agent chooses the right source, filters by keyword, city, country, remote, contract type and posting date, and summarises: number of jobs, top hiring employers, locations, remote share, salary ranges and recent postings, with links to the best matches.

Typical uses: recruiters and staffing agencies sizing a market, job seekers and career coaches, labour-market and salary research, job boards and newsletters, and sales teams spotting which employers are hiring for a skill.

The skill connects to Apify's hosted MCP server and runs three published Apify Actors on your own free Apify account, billed at fractions of a cent per job (default 20 per search). It pairs well with Hiring Signals, which covers a single company's openings.

**Category:** HR & Recruiting (alt: Research & Data)

**Tags:** job market, job search, vacancies, recruiting, labour market, germany jobs, sweden jobs, mcp

**Compatibility:** Requires a free Apify account and the job-market-data MCP server (setup in README). Works with any MCP-capable agent.

**FAQ**
- Q: Which countries are covered? A: Germany and Sweden fully (all sectors, from the national public job boards) and tech and startup jobs worldwide from six applicant tracking systems. Other national job boards are not included yet.
- Q: How is this different from Hiring Signals? A: Hiring Signals answers "what is this company hiring for?". Job Market Data answers "what jobs exist for this role or skill in this place?" across many employers. They work well together.
- Q: What does it cost? A: The skill is free. Each job returned costs a fraction of a cent on your Apify account (default 20 per search), and Apify's free plan includes monthly credit.
