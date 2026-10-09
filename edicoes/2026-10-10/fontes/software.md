# Shopify Upgrades Checkout Blocks to Polaris Web Components, Cutting Bundle Sizes up to 85%

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/shopify-web-components/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Daniel Curtis
- Publicado: 2026-10-09T15:01:00+00:00
- Score: 5.064
- Imagem: imagens/software-shopify-upgrades-checkout-blocks-to-pola.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Shopify has detailed how it rebuilt its Checkout Blocks app, moving five high-traffic checkout UI extensions from React and the legacy Remote UI bridge to remote-dom with Preact and Polaris web components. The extensions, which render on roughly a third of all customized checkouts, were rewritten in TypeScript and moved from API version 2025-07 to 2026-01, part of a wider effort to shift Shopify's entire UI extension surface onto framework-agnostic components. The change is not optional: from October 1, 2026, app deployments will be blocked if they include extension versions earlier than 2026-01.
Transferred bundle sizes fell between 40 percent and 85 percent across the extension family, with the payment-icons extension shrinking by 84.4 percent. Extension Load Time dropped around 8 percent at the median and 7 percent at the 90th percentile, weighted by checkout volume. Much of that was driven by a hard 64KB gzip budget that the 2026-01 remote-dom CLI enforces per extension, down from bundles that were previously around 100KB to 112KB gzipped.
Switching from React to Preact removed react-reconciler and saved roughly 89KB on its own. The team replaced liquidjs (about 73KB) with an in-house Liquid parser nicknamed "droplet" at 13KB gzipped, validated against a 42,000 line parity corpus drawn from real merchant configurations. dayjs was swapped for a small custom date utility, while markdown-to-jsx was kept and aliased onto Preact rather than replaced.
For developers starting their own migration, Shopify points to its upgrade guides and AI toolkit and has published migration guides for Checkout and Customer Account extensions. In practice, most legacy Polaris React elements become framework-agnostic s-* custom elements loaded from Shopify's CDN.
The broader move to Preact and framework-agnostic web components first landed with the API 2025-10 release in late 2025, and the early reception was largely positive. The development platform Gadget called the direction "a great update", noting Preact delivers a React-like experience at a fraction of the runtime, and on Hacker News developers welcomed Shopify shipping components without the Shadow DOM, though some cautioned that web components are "not a panacea" and will not replace framework component systems.
A year on, as the 2026-01 version became the mandatory path, sentiment has been more mixed: one developer argued on the Shopify forums in April 2026 that shipping an unversioned CDN script with no way to pin a version is "a nightmare for stability," a complaint still active in the community through mid-2026, while a Reddit thread faulted the new components as "incomplete," citing gaps such as the missing Index Table that Polaris React offered.
Shopify is a commerce platform that powers millions of online stores, and Checkout Blocks is one of its apps for customising the checkout experience without writing code. Polaris is Shopify's open source design system, and its newer web components are framework-agnostic custom elements that render the same UI regardless of the framework a developer reaches for.
