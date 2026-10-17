# South India Tours — a local guide in South Kerala

A responsive, contact-only static website framework for a local tour guide. Includes a local-guide introduction, regional destination highlights, editorial travel content and a contact section. No booking, payment or inquiry forms are included.

## Run

```sh
cd /workspace/SouthIndiaTours
python3 -m http.server 8000 --bind 0.0.0.0
```

No dependencies or build step are required. JavaScript only updates the footer year.

## Content to finish

- Add the guide’s real name, biography and portrait.
- Destinations are based on the reference itinerary: Cochin (Kochi), Kumarakom and Alleppey (Alappuzha), including Vembanad Lake, the bird sanctuary and backwaters. Reference text was accessed successfully; it has not been copied.
- Add real phone, WhatsApp and email contact links when supplied. No contact details have been invented.
- Replace the illustrated coast card with an approved destination photo if desired.
- Review photography and permissions before launch. Kerala photographs are stored locally in assets, sourced from Unsplash (photo-1602216056096-3b40cc0c9944 and photo-1593693397690-362cb9666fc2). The Kochi card uses a decorative coastal illustration rather than a location photograph. Fonts are served by Google Fonts with system fallbacks.

Reference: https://www.intersighttours.com/packages/jet-to-kerala/stunning-backwaters-of-kerala
