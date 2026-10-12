# MultiPost website source

The repository root is the single deployable source for the MultiPost product website.

The `commercial-preview/` directory is a retained local design reference. It is ignored on purpose and must not be deployed, indexed, submitted to a platform review, or used as a second public website.

## Current local-only state

- The root pages are an English product and audit-preparation source for the Windows app.
- `oauth/index.html`, the legacy legal aliases, TikTok verification files, `CNAME`, `robots.txt`, and `sitemap.xml` remain in place so existing configured URLs are not silently removed.
- No DNS, hosting, public deployment, app-review portal, payment, installer distribution, or checkout is performed from this repository work.
- The root pages are marked `noindex, nofollow` until the release checklist is completed and a public launch is explicitly approved.

## Local verification

Run the static checker from this directory:

```powershell
py -3 .\check_site.py
```

It checks local navigation and asset references in the deployable root, confirms the core pages have a viewport and heading, and rejects legacy architecture claims that conflict with the commercial source design.

## Before public launch or a TikTok submission

1. Decide whether `ilgotic.com` or `multipost.ilgotic.com` is the public product URL, then configure and verify DNS, HTTPS, sitemap, OAuth redirects, and every configured platform URL.
2. Replace the pre-release privacy and terms text with legally reviewed production documents that name the operator, providers, retention rules, jurisdiction, support and commercial terms.
3. Deploy and externally test the HTTPS authorization broker, controlled media relay, and product-session issuer.
4. Build, sign, install, update, and roll back the Windows installer on clean systems.
5. Record the actual end-to-end product flow with the same domain and behavior shown in the platform review submission.
