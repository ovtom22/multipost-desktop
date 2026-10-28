# MultiPost website source

The repository root is the single deployable source for the MultiPost product website.

The `commercial-preview/` directory is a retained local design reference. It is ignored on purpose and must not be deployed, indexed, submitted to a platform review, or used as a second public website.

## Deployment source and scope

- The root pages are an English product and audit-preparation source for the Windows app.
- `oauth/index.html`, the legacy legal aliases, TikTok verification files, `CNAME`, `robots.txt`, and `sitemap.xml` remain in place so existing configured URLs are not silently removed.
- This source uses the existing GitHub Pages deployment and `multipost.ilgotic.com` hostname. Updating the content does not require a hosting or DNS change.
- Product and availability pages retain their existing `noindex, nofollow` setting. The canonical Privacy and Terms pages retain `index, follow`.

## October 28 content revision

The homepage, workflow, TikTok flow, availability, support and Privacy
pages now distinguish the actual TikTok Sandbox candidate from broader
MultiPost builds and the commercial release. The candidate is portable Windows
x64 build `0.1.0-review.20261026.3`; its real HTTPS broker and connection checks
are recorded in the application repository. The pages provide a free reviewer
access request through TIGO support, while making clear that package delivery
and permitted Sandbox access must be confirmed for each reviewer. One
creator-approved Only you test completed on October 28, with its saved receipt
and private posted result verified. The selected capability clarification,
end-to-end recording, review submission and TikTok approval remain pending.
No unverified package download URL is advertised.

The Privacy notice adds TikTok authorization/token processing, direct media
upload, separate review-profile storage and the limits of Disconnect and local
deletion. Google and YouTube direct-exchange and disconnect descriptions are
scoped to the legacy developer builds verified in source. The current TikTok
reviewer package excludes YouTube; this notice does not claim the commercial
YouTube architecture is the same as the legacy one. The policy is
dated October 28 and its local-only banner has been removed for publication.
If publication occurs on a different date, update that date before deploying.

Deployment uses reviewed root-site changes in this repository. Preserve `CNAME`, the OAuth
callback page, legal aliases and verification files, and let the existing
GitHub Pages configuration publish them. After publication, compare live HTTPS
responses with the committed content and verify the policy and access links.

## Local verification

Run the static checker from this directory:

```powershell
py -3 .\check_site.py
```

It checks local navigation and asset references in the deployable root, confirms the core pages have a viewport and heading, and rejects legacy architecture claims that conflict with the commercial source design.

## Before public launch or a TikTok submission

1. Retain the verified product hostname `multipost.ilgotic.com` and TikTok broker `auth.ilgotic.com`; recheck the exact owned URLs and selected portal revision before submission. Do not change the apex domain as part of this work.
2. Keep policy wording aligned with actual broker settings, provider processing and support retention. Confirm the public product identity and accessible reviewer build before submission.
3. Resolve the product-included TikTok capability question and demonstrate free reviewer delivery and permitted Sandbox target-account access.
4. Retain the receipt and verified final status from the consented private test completed on October 28, then record the actual flow. A private creator account and manually selected Only you audience remain required for unaudited tests.
5. Keep commercial release work separate. A signed installer, updates, commerce, media relay and product-session issuer are not prerequisites of TikTok's local-file Direct Post integration merely because they belong to the broader architecture.
