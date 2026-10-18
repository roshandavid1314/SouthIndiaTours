"""Render six static destination pages and the homepage collection from local content."""
from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parent.parent
places=json.loads((root/'destinations.json').read_text())
assert len(places)==6,'The site must feature exactly six destinations.'
def e(value):return html.escape(str(value),quote=True)
def image(photo,prefix='',lazy=True):
 return f'<img src="{prefix}{e(photo["file"])}" alt="{e(photo["caption"])}" width="{photo["width"]}" height="{photo["height"]}" {"loading=\"lazy\"" if lazy else "fetchpriority=\"high\""} decoding="async">'
def card(p,prefix=''):
 return f'<a class="destination" href="{prefix}destinations/{p["slug"]}.html">{image(p["photos"][0],prefix)}<div><small>{e(p["tag"])}</small><h3>{e(p["name"])} <span aria-hidden="true">→</span></h3><p>{e(p["summary"])}</p><span class="card-link">Discover {e(p["name"])} <span aria-hidden="true">→</span></span></div></a>'
section='<section class="destinations" id="destinations"><div class="section-top"><div><p class="eyebrow">START IN KERALA. EXPLORE ALL OF SOUTH INDIA.</p><h2>Find your kind of <em>somewhere.</em></h2></div><span class="muted">Six featured Kerala destinations. Tours across South India.</span></div><div class="destination-grid">'+''.join(card(p) for p in places)+'</div><p class="destination-note">Take a closer look at each place — its stories, scenery and everyday wonders. These six Kerala highlights are a starting point. Contact Dennis to explore routes across South India.</p></section>'
home=(root/'index.html').read_text()
home=re.sub(r'<section class="destinations".*?</section>',section,home,count=1,flags=re.S)
home=re.sub(r'<section class="photo-journal".*?</section>','',home,flags=re.S)
(root/'index.html').write_text(home)
for i,p in enumerate(places):
 others=[x for x in places if x['slug']!=p['slug']][:3]
 gallery=''.join(f'<figure class="gallery-item"><button class="photo-open" type="button" data-photo="../{e(photo["file"])}" data-caption="{e(photo["caption"])}" aria-label="Enlarge photograph: {e(photo["caption"])}">{image(photo,"../")}<span class="enlarge" aria-hidden="true">+</span></button><figcaption><span>0{j+1}</span>{e(photo["caption"])}</figcaption></figure>' for j,photo in enumerate(p['photos']))
 highlights=''.join(f'<article><span class="eyebrow">0{j+1}</span><h3>{e(title)}</h3><p>{e(text)}</p></article>' for j,(title,text) in enumerate(p['highlights']))
 next_place=places[(i+1)%len(places)]
 page=f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{e(p['summary'])} Discover {e(p['name'])}’s history, scenery and highlights with South India Tours."><title>{e(p['name'])} — Places & Stories | South India Tours</title><link rel="stylesheet" href="../style.css"></head>
<body class="destination-page"><header><a class="logo" href="../index.html">south india<span>SOUTH INDIA, WITH A LOCAL</span></a><nav aria-label="Main navigation"><a href="../index.html#destinations">All destinations</a><a href="../about.html">About me</a><a href="#gallery">Photo journal</a></nav><a class="nav-button" href="../index.html#contact">Say hello →</a></header><main>
<div class="breadcrumbs"><a href="../index.html">Home</a><span>/</span><a href="../index.html#destinations">Destinations</a><span>/</span><span aria-current="page">{e(p['name'])}</span></div>
<section class="place-hero">{image(p['photos'][0],'../',False)}<div class="shade"></div><div class="place-hero-copy"><p class="eyebrow">KERALA FIELD NOTES · 0{i+1} / 06</p><h1>{e(p['name'])}</h1><p class="place-tagline">{e(p['intro'])}</p><span class="place-label">{e(p['tag'])}</span></div><a href="#gallery" class="hero-gallery">See the photo journal ↓</a></section>
<section class="place-overview"><div><p class="eyebrow">{e(p['also']).upper()}</p><h2>Get to know<br><em>{e(p['name'])}.</em></h2></div><div><p class="place-lead">{e(p['summary'])}</p><p>{e(p['look'])}</p></div></section>
<section class="place-history"><figure>{image(p['photos'][1],'../')}<figcaption>{e(p['photos'][1]['caption'])}</figcaption></figure><div><p class="eyebrow">THE STORIES BENEATH THE SCENERY</p><h2>A little <em>history.</em></h2><p>{e(p['history'])}</p><a class="text-link" href="{e(p['source'])}" target="_blank" rel="noopener noreferrer">More background on {e(p['name'])} →</a></div></section>
<section class="place-highlights"><div class="section-top"><div><p class="eyebrow">LOOK A LITTLE CLOSER</p><h2>What makes it <em>special.</em></h2></div><span class="muted">Places to notice. Stories to ask about.</span></div><div class="highlight-grid">{highlights}</div></section>
<section class="place-gallery" id="gallery"><div class="section-top"><div><p class="eyebrow">A FEW FRAMES FROM {e(p['name']).upper()}</p><h2>The view from <em>here.</em></h2></div><span class="muted">Select a photograph to take a closer look.</span></div><div class="gallery-grid">{gallery}</div></section>
<section class="field-notes"><div><p class="eyebrow">BEFORE YOU GO</p><h2>A few local<br><em>considerations.</em></h2></div><article><h3>Weather & seasons</h3><p>{e(p['season'])}</p></article><article><h3>Travel thoughtfully</h3><p>{e(p['tip'])}</p></article></section>
<section class="place-contact"><p class="eyebrow">CURIOUS ABOUT {e(p['name']).upper()}?</p><h2>Start with a <em>conversation.</em></h2><p>Ask your local guide about the places that interest you.</p><a class="button" href="../index.html#contact">Contact your guide <span>→</span></a></section>
<section class="more-places"><div class="section-top"><div><p class="eyebrow">THERE’S MORE TO DISCOVER</p><h2>Keep <em>wandering.</em></h2></div><a class="text-link" href="../index.html#destinations">All six destinations →</a></div><div class="destination-grid">{''.join(card(x,'../') for x in others)}</div><a class="next-place" href="{next_place['slug']}.html">Next field note <span>{e(next_place['name'])} →</span></a></section>
</main><footer><a class="logo" href="../index.html">south india<span>SOUTH INDIA, WITH A LOCAL</span></a><p>South India. A local perspective.</p><span>© <span id="year"></span> South India Tours</span><a href="#">Back to top ↑</a></footer>
<dialog class="photo-dialog" aria-label="Expanded destination photograph"><button class="photo-close" type="button" aria-label="Close photograph">Close ×</button><img alt=""><p></p></dialog><script src="../app.js"></script></body></html>'''
 (root/'destinations'/f'{p["slug"]}.html').write_text(page)
print('Built six destination pages and homepage cards.')
