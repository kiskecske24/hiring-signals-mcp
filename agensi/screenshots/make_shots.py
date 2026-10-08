import html, subprocess, os
CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CSS="""body{margin:0;background:#0f172a;font-family:Segoe UI,Arial,sans-serif;color:#e2e8f0}
.wrap{width:1180px;margin:40px auto}
.hdr{display:flex;align-items:center;gap:16px;margin-bottom:22px}.hdr img{width:56px;height:56px;border-radius:12px}
.hdr h1{font-size:26px;margin:0}.hdr p{margin:2px 0 0;color:#94a3b8;font-size:15px}
.user{background:#1e293b;border-radius:14px;padding:14px 18px;margin-left:220px;font-size:17px;border:1px solid #334155}
.user b{color:#93c5fd}
.agent{background:#111827;border:1px solid #334155;border-radius:14px;padding:18px 22px;margin-top:16px;font-size:15.5px}
.agent h2{font-size:18px;margin:14px 0 8px;color:#f8fafc}.agent h2:first-child{margin-top:0}
.tool{display:inline-block;background:#064e3b;color:#6ee7b7;border-radius:8px;padding:3px 10px;font-size:13px;margin-bottom:10px}
table{border-collapse:collapse;width:100%;margin:6px 0 4px}th,td{border-bottom:1px solid #334155;padding:7px 9px;text-align:left}th{color:#94a3b8;font-weight:600;font-size:14px}
.note{color:#94a3b8;font-size:14px;margin-top:6px}ul{margin:6px 0 0 18px;padding:0}li{margin:3px 0}"""
def table(head,rows): return "<table><tr>"+"".join(f"<th>{html.escape(h)}</th>" for h in head)+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)+"</table>"
def page(slug,title,sub,prompt,tool,body):
    icon=os.path.abspath(f"../icons/{slug}.png").replace("\\","/")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='wrap'><div class='hdr'><img src='file:///{icon}'><div><h1>{title}</h1><p>{sub}</p></div></div><div class='user'><b>You:</b> {html.escape(prompt)}</div><div class='agent'><span class='tool'>✓ {tool}</span>{body}</div></div></body></html>"
S={}
S["hiring-signals"]=page("hiring-signals","Hiring Signals","Live job openings from company career sites, inside your AI agent",
 "What is Stripe hiring for right now? Group by team and location, newest first.","ats-jobs-scraper · 25 jobs · 7 s · ~$0.003",
 "<h2>Stripe: 25 open roles (Greenhouse, live)</h2>"+table(["Team","Openings"],[["Radar (fraud ML) – Engineering","2"],["Account Executives – EMEA","2"],["Security Infrastructure","1"],["Technical Account Management – EMEA","1"],["Privy (crypto) – Sales & Marketing","1"]])+
 "<h2>Newest postings</h2>"+table(["Role","Location","Posted"],[["Software Engineer, Internal Identity","–","2026-10-07"],["Machine Learning Engineer, Radar","Seattle","2026-10-07"],["Head of Technical Account Management, EMEA","Dublin","2026-10-07"],["Sales Development Representative (Spanish)","Chicago","2026-10-07"]])+
 "<div class='note'>Signal: investing in fraud ML and EMEA go-to-market. Dublin leads with 5 roles; 3 of 25 remote.</div>")
S["company-research"]=page("company-research","Company Research","Website tech stack (7,600+ technologies) and screenshots",
 "What are linear.app, notion.so and basecamp.com built with?","tech-stack-detector · 3 sites · ~10 s each",
 "<h2>Stack by site</h2>"+table(["","linear.app","notion.so","basecamp.com"],[["Technologies","16","15","6"],["CMS","Sanity","Contentful","–"],["Framework","Next.js, React","Next.js, React","Stimulus (Hotwire)"],["CDN","Cloudflare, Google Cloud CDN","Cloudflare","Cloudflare"],["Hosting","Google Cloud","Vercel","–"],["Marketing / ads","LinkedIn Insight Tag","LinkedIn Ads, LinkedIn Insight","Mailchimp"]])+
 "<h2>Takeaways</h2><ul><li>Headless CMS is the norm for product-led SaaS sites (Sanity, Contentful).</li><li>LinkedIn is the paid channel Linear and Notion instrument.</li><li>Basecamp runs a lean Rails/Hotwire stack with almost no third-party tags.</li></ul>")
S["public-tenders"]=page("public-tenders","Public Tenders (EU TED)","Open EU public tenders and contract awards, searchable by your agent",
 "Open software development tenders published on TED this week, sorted by deadline.","ted-tenders-scraper · 8 notices · ~10 s",
 "<h2>8 open tenders (6 shown)</h2>"+table(["Deadline","Country","Buyer","Tender","Est. value"],[["05 Nov","PT","Imprensa Nacional-Casa da Moeda","Back-office system support & maintenance","€816,220"],["06 Nov","IE","Skillnet Ireland","Website optimisation, hosting & support","€215,000"],["06 Nov","FI","University of Helsinki","AI-assisted invoice coding solution","–"],["09 Nov","LV","State transport company","Public & freight transport management system","€4,050,298"],["09 Nov","SE","Telge Inköp (Södertälje)","Building-permit case management system","SEK 4,000,000"],["18 Nov","CH","High Court of Zurich","Intranet renewal for courts & notaries","–"]])+
 "<div class='note'>Largest: Latvian transport system (€4.05M). Each row links to the official TED notice.</div>")
S["job-market-data"]=page("job-market-data","Job Market Data","Live vacancies: Germany, Sweden and global tech jobs",
 "How many Data Engineer jobs are open in Berlin on the German job board? Top employers and newest.","arbeitsagentur-jobs-scraper · 12 jobs · ~10 s",
 "<h2>Data Engineer · Berlin area · 12 vacancies (demo cap)</h2>"+table(["Employer","Openings"],[["aconium GmbH","2"],["Siemens Energy","1"],["Smartbroker AG","1"],["Europace Ratenkredit","1"],["inovex","1"]])+
 "<h2>Newest postings</h2>"+table(["Posted","Role","Employer","City"],[["01 Oct","(Sr.) Data Engineer (m/f/d)","Smartbroker AG","Berlin"],["10 Sep","Data Engineer – Geodatenmanagement","aconium GmbH","Berlin"],["03 Sep","Data Engineer (home office)","con terra","Münster"],["29 Aug","Data Engineer – Fintech – remote","Europace Ratenkredit","Bremen"]])+
 "<div class='note'>Also searches Sweden (Platsbanken) and a global tech-jobs feed with salary ranges.</div>")
for slug,h in S.items():
    p=os.path.abspath(f"{slug}.html"); open(p,"w",encoding="utf-8").write(h)
    out=os.path.abspath(f"{slug}.png")
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",f"--screenshot={out}","--window-size=1280,800","file:///"+p.replace(os.sep,'/')],capture_output=True,timeout=60)
    print(slug, os.path.exists(out))
