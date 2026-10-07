# Agensi skills: end-to-end MCP test results

Date: 2026-10-08 (runs started 2026-10-07 22:52 UTC). Server: Apify hosted MCP (`apify-mcp-server` 0.17.3), Streamable HTTP, `Authorization: Bearer <owner Apify token>`.
Sequence per skill: `initialize` -> `notifications/initialized` -> `tools/list` -> one `tools/call` per Actor -> run and dataset checked via the Apify API.

Cost columns: "Platform usage" is what the owner account actually paid (compute + storage; the owner is not charged its own pay-per-event prices). "PPE price" is what a regular user would pay for the same call (charged events x Store price, incl. `apify-actor-start` at $0.00005 per GB of run memory).

## Store visibility check (Apify API `isPublic`, 2026-10-08)

| Actor | Public | Used |
|---|---|---|
| tech-stack-detector | yes | company-research |
| website-screenshot | yes | company-research |
| domain-whois-lookup | no (publish queue) | dropped |
| seo-site-audit | no (publish queue) | dropped |
| sec-form-d-funding | no (publish queue) | dropped |
| us-new-business-filings | no (publish queue) | dropped |
| ted-tenders-scraper | yes | public-tenders |
| sam-gov-scraper | no (publish queue) | dropped |
| gov-tenders-scraper (folder gov-tenders-uk-au-ca) | no (publish queue) | dropped |
| arbeitsagentur-jobs-scraper | yes | job-market-data |
| sweden-jobs-scraper | yes | job-market-data |
| ats-jobs-feed | yes | job-market-data |
| remote-jobs-scraper | no (publish queue) | dropped |
| eures-jobs-scraper | no (publish queue) | dropped |

Private Actors would work for the owner's token but fail for every other user, so they are not in the MCP URLs. Add them to the `tools=` list and the SKILL.md tables once the publish queue has made them public.

## tools/list

| Skill | MCP URL | Tools returned |
|---|---|---|
| company-research | `https://mcp.apify.com/?tools=Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot` | `kadi_bence--tech-stack-detector`, `kadi_bence--website-screenshot`, `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, `abort-actor-run` |
| public-tenders | `https://mcp.apify.com/?tools=Kadi_Bence/ted-tenders-scraper` | `kadi_bence--ted-tenders-scraper`, `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, `abort-actor-run` |
| job-market-data | `https://mcp.apify.com/?tools=Kadi_Bence/arbeitsagentur-jobs-scraper,Kadi_Bence/sweden-jobs-scraper,Kadi_Bence/ats-jobs-feed` | `kadi_bence--arbeitsagentur-jobs-scraper`, `kadi_bence--sweden-jobs-scraper`, `kadi_bence--ats-jobs-feed`, `get-actor-run`, `get-dataset-items`, `get-key-value-store-record`, `abort-actor-run` |

All `kadi_bence--...` names match the SKILL.md tables exactly. Each Actor tool also exposes `waitSecs`.

## tools/call (one tiny real run per Actor)

| Skill | Tool | Input | Status | Items | Charged events | Platform usage | PPE price | Time |
|---|---|---|---|---|---|---|---|---|
| company-research | tech-stack-detector | `urls: ["apify.com"]` | SUCCEEDED | 1 | site 1, start 4 | $0.00130 | $0.00170 | 11 s |
| company-research | website-screenshot | `urls: ["https://example.com"], format: jpeg, fullPage: false` | SUCCEEDED | 1 | screenshot 1, start 4 | $0.00405 | $0.00270 | 19 s |
| public-tenders | ted-tenders-scraper | `keywords: ["software"], countries: ["DE"], noticeTypes: ["contract_notice"], publishedWithinDays: 14, maxResults: 2` | SUCCEEDED | 2 | notice 2, start 1 | $0.00038 | $0.00305 | 9 s |
| job-market-data | arbeitsagentur-jobs-scraper | `keywords: ["Data Engineer"], location: "Berlin", maxResults: 2` | SUCCEEDED | 2 | job 2, start 1 | $0.00037 | $0.00155 | 9 s |
| job-market-data | sweden-jobs-scraper | `keywords: ["data engineer"], maxResults: 2` | SUCCEEDED | 2 | job 2, start 1 | $0.00053 | $0.00165 | 11 s |
| job-market-data | ats-jobs-feed | `keywords: ["data engineer"], timeRange: "7d", maxItems: 2` | SUCCEEDED | 2 (of 7 matching) | job 2, start 4 | $0.00117 | $0.00320 | 9 s |
| **Total** | | | 6/6 SUCCEEDED | 10 | | **$0.0078** | **$0.0139** | |

Also tested: `get-dataset-items` (`datasetId`, `limit`, `fields`) on the screenshot dataset returned the projected item; `screenshotUrl` is a signed public link.

## Fields confirmed in the datasets (documented in SKILL.md)

- tech-stack-detector: `url`, `domain`, `finalUrl`, `status`, `error`, `title`, `technologyCount`, `technologyNames`, `technologies` (`name`, `version`, `confidence`, `categories`), `cms`, `ecommerce`, `analytics`, `cdn`, `framework`, `server`, `paymentProcessors`, `hosting`, `tagManagers`, `marketingAutomation`, `advertising`, `liveChat`, `programmingLanguages`, `pagesAnalyzed`. Sample: apify.com = 19 technologies (Next.js, React, CloudFront, AWS, GTM, HubSpot...).
- website-screenshot: `url`, `finalUrl`, `status`, `title`, `screenshotUrl`, `key`, `format`, `device`, `fullPage`, `width`, `height`, `bytes`, `truncated`, `error`. Sample: example.com 1920x1080 JPEG, 64 KB.
- ted-tenders-scraper: `publicationNumber`, `title`, `noticeType`, `contractNature`, `buyerName`, `buyerCountry`, `buyerCity`, `mainCpv`, `mainCpvLabel`, `cpvCodes`, `estimatedValue`, `currency`, `awardedValue`, `winners`, `publicationDate`, `deadline`, `procedureType`, `placeOfPerformanceNuts`, `lotsCount`, `url`, `pdfUrl`, `description`. Sample: Kommunale Unfallversicherung Bayern laptops tender, EUR 302,645, 3 lots.
- arbeitsagentur-jobs-scraper: `title`, `occupation`, `employer`, `city`, `postalCode`, `region`, `postedDate`, `workingTime`, `contractType`, `homeOffice`, `salaryMin`, `salaryMax`, `salaryText`, `url`. Values in German board terms (`VOLLZEIT`, `UNBEFRISTET`).
- sweden-jobs-scraper: `title`, `employer`, `occupation`, `city`, `region`, `postedDate`, `deadline`, `employmentType`, `workMode`, `remote`, `salaryText`, `openPositions`, `url`.
- ats-jobs-feed: `title`, `company`, `companyDomain`, `ats`, `location`, `country`, `countryCode`, `remote`, `workMode`, `department`, `employmentType`, `postedAt`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `url`. Sample: Solace Health Data Engineer, remote US, USD 130-175k.

## Corrections made to SKILL.md from the test

- The hosted server's Actor tools return a run summary (status, item count, `datasetId`, field list), not the dataset rows. All three SKILL.md files tell the agent to call `get-dataset-items` next. (The older hiring-signals SKILL.md says the tool "returns the first items"; with server 0.17.3 it returns the summary only.)
- `get-actor-run` takes `runId` and `waitSecs` (max 45); documented as such.
- Limit fields as exposed by the tools: TED `maxResults`, Arbeitsagentur `maxResults`, Sweden `maxResults`, ATS Jobs Feed `maxItems`; tech stack and screenshots have no limit field (one charge per URL in `urls`).
