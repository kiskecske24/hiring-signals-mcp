"""Renders 4 listing screenshots per skill (1280x800) from real lookups run on 2026-10-07/08. Uses headless Chrome."""
import html, os, subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:\Users\utente\AppData\Local\Temp\claude\C--Users-utente-projects-personal\9bf10001-3c6b-4092-99de-b7457b78faa7\scratchpad"
CSS = """body{margin:0;background:#0f172a;font-family:Segoe UI,Arial,sans-serif;color:#e2e8f0}
.wrap{width:1180px;margin:34px auto}
.hdr{display:flex;align-items:center;gap:16px;margin-bottom:20px}.hdr img{width:56px;height:56px;border-radius:12px}
.hdr h1{font-size:26px;margin:0}.hdr p{margin:2px 0 0;color:#94a3b8;font-size:15px}
.user{background:#1e293b;border-radius:14px;padding:13px 18px;margin-left:200px;font-size:17px;border:1px solid #334155}.user b{color:#93c5fd}
.agent{background:#111827;border:1px solid #334155;border-radius:14px;padding:16px 22px;margin-top:14px;font-size:15.5px}
.agent h2{font-size:18px;margin:12px 0 8px;color:#f8fafc}.agent h2:first-of-type{margin-top:4px}
.tool{display:inline-block;background:#064e3b;color:#6ee7b7;border-radius:8px;padding:3px 10px;font-size:13px;margin-bottom:8px}
table{border-collapse:collapse;width:100%;margin:6px 0 4px}th,td{border-bottom:1px solid #334155;padding:7px 9px;text-align:left;vertical-align:top}th{color:#94a3b8;font-weight:600;font-size:14px}
.note{color:#94a3b8;font-size:14px;margin-top:8px}ul{margin:6px 0 0 18px;padding:0}li{margin:4px 0}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.card{background:#111827;border:1px solid #334155;border-radius:14px;padding:16px 20px}
.card h3{margin:0 0 8px;font-size:17px;color:#f8fafc}code{background:#1e293b;border-radius:6px;padding:2px 6px;font-size:13.5px;color:#fde68a}
.pill{display:inline-block;background:#1e3a8a;color:#bfdbfe;border-radius:999px;padding:2px 10px;font-size:13px;margin:2px 4px 2px 0}
.phone{float:right;margin:0 0 0 18px}.phone img{height:440px;border-radius:22px;border:6px solid #334155}"""


def esc(s):
    return html.escape(str(s))


def table(head, rows):
    h = "".join(f"<th>{esc(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><tr>{h}</tr>{b}</table>"


def frame(slug, title, sub, inner):
    icon = "file:///" + os.path.join(HERE, "..", "icons", f"{slug}.png").replace(os.sep, "/")
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='wrap'>"
            f"<div class='hdr'><img src='{icon}'><div><h1>{esc(title)}</h1><p>{esc(sub)}</p></div></div>{inner}</div></body></html>")


def chat(prompt, tool, body):
    return f"<div class='user'><b>You:</b> {esc(prompt)}</div><div class='agent'><span class='tool'>&#10003; {esc(tool)}</span>{body}</div>"


def howto(server, tools, ask, cost):
    url = f"https://mcp.apify.com/?tools={server}"
    return ("<div class='grid'>"
            f"<div class='card'><h3>1. Connect once (about 3 minutes)</h3><ul><li>Free Apify account</li><li>Add the MCP server:<br><code>{esc(url)}</code></li>"
            "<li>Log in with Apify (OAuth) or paste an API token</li><li>Works in Claude Code, Cursor, VS Code Copilot, Codex CLI, Gemini CLI and more</li></ul></div>"
            f"<div class='card'><h3>2. Ask in plain English</h3><ul>{''.join(f'<li>{esc(a)}</li>' for a in ask)}</ul></div>"
            f"<div class='card'><h3>Tools the skill uses</h3>{''.join(f'<span class=pill>{esc(t)}</span>' for t in tools)}<div class='note'>The skill tells the agent which tool fits, keeps runs small and summarises results instead of dumping rows.</div></div>"
            f"<div class='card'><h3>Cost and privacy</h3><ul><li>{esc(cost)}</li><li>Apify's free plan includes monthly credit</li><li>Public data only, no personal data</li></ul></div>"
            "</div>")


P = {}
HS = ("hiring-signals", "Hiring Signals", "Live job openings from company career sites, inside your AI agent")
P["hiring-signals-1"] = frame(*HS, chat("What is Stripe hiring for right now? Group by team and location, newest first.", "ats-jobs-scraper · 25 jobs · 7 s · ~$0.003",
    "<h2>Stripe: 25 open roles (Greenhouse, live)</h2>" + table(["Team", "Openings"], [["Radar (fraud ML) – Engineering", "2"], ["Account Executives – EMEA", "2"], ["Security Infrastructure", "1"], ["Technical Account Management – EMEA", "1"], ["Privy (crypto) – Sales & Marketing", "1"]]) +
    "<h2>Newest postings</h2>" + table(["Role", "Location", "Posted"], [["Software Engineer, Internal Identity", "–", "2026-10-07"], ["Machine Learning Engineer, Radar", "Seattle", "2026-10-07"], ["Head of Technical Account Management, EMEA", "Dublin", "2026-10-07"], ["Sales Development Representative (Spanish)", "Chicago", "2026-10-07"]]) +
    "<div class='note'>Signal: investing in fraud ML and EMEA go-to-market. Dublin leads with 5 roles; 3 of 25 remote.</div>"))
P["hiring-signals-2"] = frame(*HS, chat("Compare hiring at Ramp, Notion and Databricks: which teams are growing, remote share, salaries?", "ats-jobs-scraper · 3 companies · 120 jobs (40 each)",
    "<h2>Top teams by company (sample of 40 openings each)</h2>" + table(["", "Ramp", "Notion", "Databricks"], [["#1 team", "Sales (13)", "Engineering (7)", "Field Engineering (15)"], ["#2 team", "Engineering (8)", "People / Finance / Sales (6 each)", "Marketing (3)"], ["Remote roles", "2 of 40", "0 of 40", "16 of 40"], ["Salary range published", "40 of 40", "29 of 40", "24 of 40"]]) +
    "<h2>What it means</h2><ul><li><b>Ramp</b> is in a sales push; every posting shows pay (pay-transparency states).</li><li><b>Notion</b> hires on-site only, spread across functions.</li><li><b>Databricks</b> is scaling customer-facing field engineering, often remote.</li></ul>"))
P["hiring-signals-3"] = frame(*HS, chat("What is NVIDIA hiring for in Germany? Newest first.", "workday-jobs-scraper · NVIDIA (Workday) · 20 jobs",
    "<h2>NVIDIA, Germany filter: 20 openings returned</h2>" + table(["Location", "Openings"], [["Munich", "8"], ["Germany, remote", "5"], ["Berlin", "2"], ["Zurich / Swiss remote (nearby)", "3"]]) +
    "<h2>Newest postings</h2>" + table(["Role", "Location", "Posted"], [["Senior Solutions Architect, DevOps", "Munich", "2026-10-07"], ["Project Technical Delivery Manager", "Germany, remote", "2026-10-07"], ["Senior System Software Integration Engineer – ADAS", "Munich", "2026-10-06"], ["Senior Solution Architect, MLOps – AI Factory", "Germany, remote", "2026-10-05"]]) +
    "<div class='note'>Large enterprises usually run Workday; the skill picks the right tool automatically.</div>"))
P["hiring-signals-4"] = frame(*HS, howto("Kadi_Bence/workday-jobs-scraper,Kadi_Bence/ats-jobs-scraper", ["Workday Jobs Scraper", "Greenhouse · Lever · Ashby · Workable · Recruitee · Personio"],
    ["What is Salesforce hiring for in London?", "Which of my 20 target accounts opened data roles this month?", "Remote design jobs posted this week at Figma and Canva"], "Fractions of a cent per job; default 20 jobs per company"))

CR = ("company-research", "Company Research", "Website tech stack (7,600+ technologies) and screenshots")
P["company-research-1"] = frame(*CR, chat("What are linear.app, notion.so and basecamp.com built with?", "tech-stack-detector · 3 sites · ~10 s each",
    "<h2>Stack by site</h2>" + table(["", "linear.app", "notion.so", "basecamp.com"], [["Technologies", "16", "15", "6"], ["CMS", "Sanity", "Contentful", "–"], ["Framework", "Next.js, React", "Next.js, React", "Stimulus (Hotwire)"], ["CDN", "Cloudflare, Google Cloud CDN", "Cloudflare", "Cloudflare"], ["Hosting", "Google Cloud", "Vercel", "–"], ["Marketing / ads", "LinkedIn Insight Tag", "LinkedIn Ads, Insight Tag", "Mailchimp"]]) +
    "<h2>Takeaways</h2><ul><li>Headless CMS is the norm for product-led SaaS sites (Sanity, Contentful).</li><li>Basecamp runs a lean Rails/Hotwire stack with almost no third-party tags.</li></ul>"))
P["company-research-2"] = frame(*CR, chat("Which of these prospects use HubSpot or WordPress: hubspot.com, vercel.com, wordpress.org, zalando.de?", "tech-stack-detector · 4 sites",
    "<h2>Prospect check</h2>" + table(["Site", "Technologies", "CMS", "Marketing automation", "Analytics", "Framework / CDN"], [["hubspot.com", "9", "HubSpot CMS Hub", "HubSpot", "Cloudflare Insights, LinkedIn", "Cloudflare"], ["vercel.com", "12", "–", "–", "Sift, LinkedIn Insight", "Next.js, React · S3"], ["wordpress.org", "13", "WordPress (Block + Site Editor)", "–", "–", "–"], ["zalando.de", "–", "blocked (HTTP 403)", "–", "–", "not charged"]]) +
    "<div class='note'>Matches: HubSpot → hubspot.com · WordPress → wordpress.org. Sites that block bots are reported clearly and are free.</div>"))
shot = "file:///" + os.path.join(SCRATCH, "cr_shot.png").replace(os.sep, "/")
P["company-research-3"] = frame(*CR, chat("Show me Linear's pricing page on mobile.", "website-screenshot · mobile · PNG · 1.9 s",
    f"<div class='phone'><img src='{shot}'></div><h2>linear.app/pricing (mobile, live capture)</h2><ul><li>Real browser render, 412&times;915 viewport at 2&times; (824&times;1830 px)</li><li>Cookie banners and ads hidden automatically</li><li>Formats: PNG, JPEG, WebP or PDF; viewport or full page</li><li>Devices: desktop, laptop, tablet, mobile</li><li>Returns a public link to the image, ready to share</li></ul>"
    "<h2>Good for</h2><ul><li>Competitor pricing and landing-page snapshots</li><li>Visual QA across devices</li><li>Archiving pages as PDF for reports</li></ul>"))
P["company-research-4"] = frame(*CR, howto("Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot", ["Tech Stack Detector", "Website Screenshot"],
    ["What is this competitor's site built with?", "Which of these 50 prospects run Shopify?", "Screenshot their pricing page on desktop and mobile"], "Fractions of a cent per website or screenshot; failed sites are free"))

PT = ("public-tenders", "Public Tenders (EU TED)", "Open EU public tenders and contract awards, searchable by your agent")
P["public-tenders-1"] = frame(*PT, chat("Open software development tenders published on TED this week, sorted by deadline.", "ted-tenders-scraper · 8 notices · ~10 s",
    "<h2>8 open tenders (6 shown)</h2>" + table(["Deadline", "Country", "Buyer", "Tender", "Est. value"], [["05 Nov", "PT", "Imprensa Nacional-Casa da Moeda", "Back-office system support & maintenance", "€816,220"], ["06 Nov", "IE", "Skillnet Ireland", "Website optimisation, hosting & support", "€215,000"], ["06 Nov", "FI", "University of Helsinki", "AI-assisted invoice coding solution", "–"], ["09 Nov", "LV", "State transport company", "Public & freight transport management system", "€4,050,298"], ["09 Nov", "SE", "Telge Inköp (Södertälje)", "Building-permit case management system", "SEK 4,000,000"], ["18 Nov", "CH", "High Court of Zurich", "Intranet renewal for courts & notaries", "–"]]) +
    "<div class='note'>Largest: Latvian transport system (€4.05M). Each row links to the official TED notice.</div>"))
P["public-tenders-2"] = frame(*PT, chat("Who won cleaning-services contracts from Spanish public buyers in the last 60 days, and for how much?", "ted-tenders-scraper · contract awards · ES · 8 notices",
    "<h2>Recent contract awards: cleaning services, Spain</h2>" + table(["Date", "Buyer", "Winner", "Value"], [["07 Oct", "Distrito de Hortaleza (Madrid)", "Lacera Servicios y Mantenimiento", "€4,506,512"], ["08 Oct", "Ayto. Vegas del Genil", "Orthem Servicios y Actuaciones Ambientales", "€2,748,662"], ["06 Oct", "ASEPEYO", "Ilunion Lavanderías", "€1,378,434"], ["08 Oct", "Ayto. Manzanares el Real", "Ascan Servicios Urbanos", "€929,824"], ["06 Oct", "Universidad Miguel Hernández", "Eulen", "€502,927"], ["08 Oct", "TGSS Burgos", "ITMA", "€314,618"]]) +
    "<div class='note'>Use awards to see who usually wins, at what price, and which buyers purchase what you sell.</div>"))
P["public-tenders-3"] = frame(*PT, chat("Give me the details of the Latvian transport system tender.", "ted-tenders-scraper · 1 notice",
    "<h2>Unified public & freight transport management system (LV)</h2>" + table(["Field", "Value"], [["Notice", "696447-2026 (contract notice)"], ["Buyer", "Latvian state-owned company"], ["Estimated value", "€4,050,297.52"], ["Submission deadline", "2026-11-09"], ["Published", "2026-10-08"], ["Fields returned", "CPV codes, lots, procedure type, place of performance (NUTS), PDF + official link"]]) +
    "<div class='note'>Foreign-language titles are translated by the agent. Filters: keywords in any EU language, CPV, countries, value, dates.</div>"))
P["public-tenders-4"] = frame(*PT, howto("Kadi_Bence/ted-tenders-scraper", ["TED Tenders Scraper (EU / EEA + CH, Balkans, TR, UA, MD, GE)"],
    ["IT tenders in Germany above €500k closing in 30 days", "Open calls for CPV 72000000 this week", "Who won road-maintenance contracts in Austria this year?"], "Fractions of a cent per notice; default 20 per search"))

JM = ("job-market-data", "Job Market Data", "Live vacancies: Germany, Sweden and global tech jobs")
P["job-market-data-1"] = frame(*JM, chat("How many Data Engineer jobs are open in Berlin on the German job board? Top employers and newest.", "arbeitsagentur-jobs-scraper · 12 jobs · ~10 s",
    "<h2>Data Engineer · Berlin area · 12 vacancies (demo cap)</h2>" + table(["Employer", "Openings"], [["aconium GmbH", "2"], ["Siemens Energy", "1"], ["Smartbroker AG", "1"], ["Europace Ratenkredit", "1"], ["inovex", "1"]]) +
    "<h2>Newest postings</h2>" + table(["Posted", "Role", "Employer", "City"], [["01 Oct", "(Sr.) Data Engineer (m/f/d)", "Smartbroker AG", "Berlin"], ["10 Sep", "Data Engineer – Geodatenmanagement", "aconium GmbH", "Berlin"], ["03 Sep", "Data Engineer (home office)", "con terra", "Münster"]])))
P["job-market-data-2"] = frame(*JM, chat("Which employers in Stockholm are hiring nurses (sjuksköterska) right now?", "sweden-jobs-scraper · Platsbanken · 15 jobs",
    "<h2>Nurse vacancies, Stockholm: 15 returned</h2>" + table(["Employer", "Openings"], [["Region Stockholm", "10"], ["Capio Sverige", "1"], ["Familjeläkarna i Saltsjöbaden", "1"], ["Stiftelsen Kristofferskolan", "1"], ["Ideal BM / People by M", "2"]]) +
    "<h2>Newest postings</h2>" + table(["Posted", "Role", "Employer", "Apply by"], [["08 Oct", "Temporary nurses, urology clinic", "Region Stockholm", "27 Oct"], ["07 Oct", "Nurse, gynaecological cancer clinic (Solna)", "Region Stockholm", "21 Oct"], ["07 Oct", "Nurse, Endoscopy Centre, Södersjukhuset", "Region Stockholm", "29 Oct"], ["07 Oct", "School nurse", "Kristofferskolan", "06 Nov"]])))
P["job-market-data-3"] = frame(*JM, chat("Product manager roles posted this week in the global tech feed, with salary ranges.", "ats-jobs-feed · 15 jobs · Greenhouse / Lever / Ashby…",
    "<h2>Product manager roles, last 7 days (sample)</h2>" + table(["Role", "Company", "Location", "Salary"], [["Product Manager – Auth", "Supabase", "Remote, global", "–"], ["Senior Product Manager, Forward Deployed", "Anduril Industries", "Seattle / Washington DC / Costa Mesa", "$166k–220k"], ["AI Technical Product Manager (QVAC)", "Tether", "Remote", "–"]]) +
    "<div class='note'>Daily-updated database from six applicant tracking systems; salary shown whenever the posting states it. Pairs with Hiring Signals for single-company deep dives.</div>"))
P["job-market-data-4"] = frame(*JM, howto("Kadi_Bence/arbeitsagentur-jobs-scraper,Kadi_Bence/sweden-jobs-scraper,Kadi_Bence/ats-jobs-feed", ["Arbeitsagentur (Germany)", "Platsbanken (Sweden)", "ATS Jobs Feed (global tech)"],
    ["How many nurse jobs are open in Munich?", "Top employers hiring Java developers in Gothenburg", "Remote data roles with salary posted this week"], "Fractions of a cent per job; default 20 per search"))

for name, page in P.items():
    src = os.path.join(HERE, f"{name}.html")
    with open(src, "w", encoding="utf-8") as fh:
        fh.write(page)
    out = os.path.join(HERE, f"{name}.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    f"--screenshot={out}", "--window-size=1280,800", "file:///" + src.replace(os.sep, "/")], capture_output=True, timeout=60)
    print(name, os.path.exists(out))
