# South India Tours — a local guide in Kerala

A responsive, contact-only website for a local tour guide. Six destinations: Kochi, Kumarakom, Alleppey, Munnar, Thekkady and Kovalam. Each has a static page with scenery, history, highlights, visiting notes and a four-photo gallery. The homepage includes destination cards and a photo journal. No bookings, payments or submission forms.

## Preview

From the repository directory:

```sh
python3 -m http.server 8000 --bind 0.0.0.0
```

In a GitHub Codespace, open port 8000 through the Ports panel. No package installation or build is needed to serve the committed HTML pages.

## Edit destination content

Edit `destinations.json`, then regenerate the six pages and homepage destination sections:

```sh
python3 scripts/build-destinations.py
```

The generator only replaces the homepage destination collection and photo journal, plus the generated pages in `destinations/`. Other homepage content remains editable in `index.html`. Photo dialogs support keyboard activation, Escape to close and focus return to the opening button.

## Photography and content

24 destination photos are stored in `assets/destinations/`, sized to a maximum of 1600 pixels and compressed as JPEG. Source URLs and captions are recorded in `assets/destinations/sources.json`; copies were retrieved from the public `salihkm0/kerala-tourism` repository. Original photographer and reuse-license information was not supplied by that collection; establish that information or replace with the guide’s approved images before public launch. Additional original homepage photos are from Unsplash (photo-1602216056096-3b40cc0c9944 and photo-1593693397690-362cb9666fc2). Fonts use Google Fonts with system fallbacks.

Destination descriptions are original summaries. Background-reading links are included on each page. The original reference itinerary covers Kochi, Kumarakom and Alleppey: https://www.intersighttours.com/packages/jet-to-kerala/stunning-backwaters-of-kerala. Munnar, Thekkady and Kovalam expand the collection at the user’s request. Current access, activity availability and guide coverage should be confirmed locally.

Still to add: the guide’s name, personal biography, portrait, phone, WhatsApp and email. Contact placeholders are explicit; no personal details have been invented.
