#!/usr/bin/env python3
"""Build the independent bilingual Onitama introduction with real pack data."""
import argparse,html,json,shutil
from pathlib import Path
H=html.escape

def build(repo,out):
 cfg=json.loads((repo/'site/project.json').read_text());content=json.loads((repo/'site/content.json').read_text());out.mkdir(parents=True,exist_ok=True);media=out/'media';media.mkdir(exist_ok=True)
 for f in ['style.css','cards.js']:shutil.copy(repo/'site'/f,out/f)
 for src,dest in [('docs/readme/banner.png','banner.png'),('public/Onitama_Logo.svg.png','logo.png'),('docs/readme/assets/frankie.svg','signature.svg')]:shutil.copy(repo/src,media/dest)
 for name in ['board','move','packs','wind']:shutil.copy(repo/f'site/assets/{name}-current.png',media/f'{name}.png')
 normal=json.loads((repo/'public/pack/onitama_cards_normal.json').read_text())['cards'];samples=[next(x for x in normal if x['id']==id) for id in ['ox','crab','tiger']]
 counts={p:len(json.loads((repo/f'public/pack/onitama_cards_{p}.json').read_text())['cards']) for p in ['normal','senseis','promo','special','windway','dual']}
 packnames={'en':['Standard','Sensei’s Path','Promo','Special','Way of the Wind','Mimicry'],'zh':['标准包','大师之路','限定包','特殊包','风之道','摹形']}
 (out/'.nojekyll').touch()
 for lang,c in content.items():
  zh=lang=='zh';pre='../' if zh else './';dest=out/'zh' if zh else out;dest.mkdir(exist_ok=True)
  rows=lambda xs:''.join('<article><h3>'+H(a)+'</h3><p>'+H(b)+'</p></article>' for a,b in xs)
  gallery=''.join(f'<figure><a href="{pre}media/{n}.png"><img src="{pre}media/{n}.png" width="1468" height="1247" loading="lazy" alt="{H(caption)}"></a><figcaption>{H(caption)}</figcaption></figure>' for n,caption in zip(['board','move','packs','wind'],c['captions']))
  buttons=''.join(f'<button type="button" data-card="{i}" aria-pressed="{str(i==0).lower()}">{H(x["name"].get("zh" if zh else "en"))}</button>' for i,x in enumerate(samples))
  data=json.dumps({'cards':samples,'lang':lang,'center':c['center'],'destination':c['destination']},ensure_ascii=False).replace('<','\\u003c')
  packs=''.join(f'<div><dt>{H(name)}</dt><dd>{n} {"张" if zh else "cards"}</dd></div>' for name,n in zip(packnames[lang],counts.values()))
  page=f'''<!doctype html><html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Frankie Onitama | {H(c['headline'])}</title><meta name="description" content="{H(c['intro'])}"><meta name="theme-color" content="#faf8f2"><link rel="stylesheet" href="{pre}style.css"><link rel="canonical" href="{cfg['pages_url']+('zh/' if zh else '')}"><link rel="alternate" hreflang="en" href="{cfg['pages_url']}"><link rel="alternate" hreflang="zh-CN" href="{cfg['pages_url']}zh/"><meta property="og:type" content="website"><meta property="og:url" content="{cfg['pages_url']+('zh/' if zh else '')}"><meta property="og:title" content="Frankie Onitama"><meta property="og:description" content="{H(c['intro'])}"><meta property="og:image" content="{cfg['pages_url']}media/banner.png"></head><body><a class="skip" href="#main">{H(c['skip'])}</a>
<header class="shell"><a class="brand" href="{pre}"><img src="{pre}media/logo.png" alt="Onitama" width="140" height="52"></a><nav aria-label="{'页面导航' if zh else 'Page navigation'}"><a href="#rules">{c['nav'][0]}</a><a href="#use">{c['nav'][1]}</a><a href="#screens">{c['nav'][2]}</a><a href="{pre}" lang="en" {'aria-current="page"' if not zh else ''}>EN</a><a href="{pre}zh/" lang="zh-CN" {'aria-current="page"' if zh else ''}>中文</a></nav></header>
<main class="shell" id="main"><section class="hero"><div><h1>{H(c['headline'])}</h1><p class="lead">{H(c['intro'])}</p><a class="button" href="{cfg['app_url']}">{H(c['open'])} ↗</a></div><figure class="hero-screen"><img src="{pre}media/move.png" width="1468" height="1247" alt="{H(c['hero_alt'])}" fetchpriority="high"></figure></section>
<section class="section" id="rules"><h2>{H(c['concept_title'])}</h2><p class="lead narrow">{H(c['concept'])}</p><div class="rules">{rows(c['rules'])}</div></section>
<section class="section diagram"><div><h2>{H(c['sample_title'])}</h2><p>{H(c['sample_note'])}</p><div class="card-buttons">{buttons}</div><label for="perspective">{H(c['perspective'])}</label><select id="perspective"><option value="red">{H(c['red'])}</option><option value="blue">{H(c['blue'])}</option></select></div><div class="move-card"><h3 id="card-name">{H(samples[0]['name'].get('zh' if zh else 'en'))}</h3><div id="move-grid" class="move-grid" role="img" aria-label="{H(c['sample_title'])}"></div><p id="move-description" aria-live="polite"></p></div></section>
<section class="section"><h2>{H(c['win_title'])}</h2><div class="wins">{rows(c['wins'])}</div></section>
<section class="section"><h2>{H(c['packs_title'])}</h2><p class="lead narrow">{H(c['packs_intro'])}</p><dl class="pack-list">{packs}</dl><div class="variants">{rows(c['variants'])}</div><h3 class="ai-heading">{H(c['ai_title'])}</h3><p class="narrow">{H(c['ai'])}</p><p class="small narrow">{H(c['ai_note'])}</p></section>
<section id="use" class="section"><h2>{H(c['workflow_title'])}</h2><ol class="steps">{''.join('<li><h3>'+H(a)+'</h3><p>'+H(b)+'</p></li>' for a,b in c['steps'])}</ol></section>
<section id="screens" class="section"><h2>{H(c['gallery_title'])}</h2><div class="gallery">{gallery}</div></section>
<section id="start" class="section runtime"><div><h2>{H(c['run_title'])}</h2><p>{H(c['runtime'])}</p><h3>{H(c['research_title'])}</h3><p>{H(c['research'])}</p><p><a href="https://www.arcanewonders.com/eu/product/onitama/">{H(c['rules_link'])} ↗</a><br><a href="https://www.arcanewonders.com/eu/wp-content/uploads/sites/6/2024/06/Onitama_Way_of_the_Wind.pdf">{H(c['wind_link'])} ↗</a></p></div><div><h3>{H(c['local'])}</h3><pre><code>npm ci\nnpm run dev</code></pre><p class="small">{H(c['local_note'])}</p><a href="https://github.com/{cfg['repository']}/blob/main/site/GUIDE.md">{H(c['guide'])} ↗</a></div></section></main>
<footer class="shell"><img src="{pre}media/signature.svg" width="90" height="38" alt="Frankie"><span>{H(c['footer'])}</span><a href="https://github.com/{cfg['repository']}">{H(c['source'])} ↗</a></footer><script id="card-data" type="application/json">{data}</script><script src="{pre}cards.js" defer></script></body></html>'''
  (dest/'index.html').write_text(page)
 print(out)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='_site');a=ap.parse_args();build(Path(__file__).resolve().parents[1],Path(a.out).resolve())
