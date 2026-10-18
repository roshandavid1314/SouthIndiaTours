# South India Tours — a local guide in Kerala

A responsive, contact-only website for Dennis Anthony, a Kerala-based tour guide covering all of South India. Six destinations: Kochi, Kumarakom, Alleppey, Munnar, Thekkady and Kovalam. Each has a static page with scenery, history, highlights, visiting notes and a four-photo gallery. The homepage focuses on tour coverage, destination cards and contact details. Personal introductions and the personal photo journal are on the About page. No bookings, payments or submission forms.

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

The generator replaces the homepage destination collection and the generated pages in `destinations/`. It does not add a duplicate destination photo journal. Other homepage content remains editable in `index.html`. Photo dialogs support keyboard activation, Escape to close and focus return to the opening button.

## Photography and content

24 destination photos are stored in `assets/destinations/`, sized to a maximum of 1600 pixels and compressed as JPEG. Source URLs and captions are recorded in `assets/destinations/sources.json`; copies were retrieved from the public `salihkm0/kerala-tourism` repository. Original photographer and reuse-license information was not supplied by that collection; establish that information or replace with the guide’s approved images before public launch. Additional original homepage photos are from Unsplash (photo-1602216056096-3b40cc0c9944 and photo-1593693397690-362cb9666fc2). Fonts use Google Fonts with system fallbacks.

Destination descriptions are original summaries. Background-reading links are included on each page. The original reference itinerary covers Kochi, Kumarakom and Alleppey: https://www.intersighttours.com/packages/jet-to-kerala/stunning-backwaters-of-kerala. Munnar, Thekkady and Kovalam expand the collection at the user’s request. Current access, activity availability and guide coverage should be confirmed locally.

## About Binu and transport

`about.html` is a standalone guide page, linked from the homepage and every destination. It includes an introductory biography, 18 user-supplied photographs, a personal photo journal and three vehicle sections: Toyota MPV, touring minibus and Tata passenger van. Seating capacities, model variants and equipment have not been assumed. Vehicle images and interiors can be enlarged using the shared photo dialog.

Contact name: Dennis Anthony; local name: Binu. WhatsApp: https://wa.me/919447134447. Phone link: tel:+919447134447. These details appear on the homepage and About page; clicking WhatsApp opens a conversation without automatically sending a message. No email address has been supplied.

The user-supplied photographs are in `assets/guide/` and `assets/transport/`. Their original archive filenames and dimensions are recorded in `assets/guide/sources.json`. Web copies preserve the photos’ content, use JPEG compression and omit original metadata. Original ZIP archives remain separate from the site.

Binu can expand the short introduction with his personal background, languages and experience later.

Coverage: Kerala, Tamil Nadu, Karnataka, Andhra Pradesh and Telangana. The six destination detail pages remain featured Kerala highlights; homepage and guide introductions promote South India-wide tours.
