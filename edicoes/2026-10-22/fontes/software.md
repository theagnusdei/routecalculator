# PHP patches released for two critical RCEs

- Editoria: Software (`software`)
- Fonte: LWN.net — https://lwn.net/Articles/1102014/
- Autor: [Posted October
- Publicado: 2026-10-21T13:53:18+00:00
- Score: 5.48
- Imagem: imagens/software-php-patches-released-for-two-critical-rc.jpg | crédito: U.S. Space Force photo by Senior Airman Ryan Quijas / Wikimedia Commons | licença: Wikimedia Commons — Public domain

## Outras coberturas
- nenhuma

## Texto extraído

PHP patches released for two critical RCEs
The PHP project has published PHP versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35 to address two critical vulnerabilities that could allow unauthenticated remote code execution.
Who is at risk: all PHP installations serving web requests,
including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We
consider the risk highest for mod_php, with a demonstrated exploit where an
unauthenticated request can trigger the attack before any application code
runs.
The vulnerabilities:
- RCE via OOM corruption, CVE-2026-109618 (GHSA-w8hw-w9fx-j79w): out-of-memory handling can interrupt PHP while internal request data is only partially initialized. Request cleanup may then treat the invalid data as valid.
- RCE via stale global state, CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp): request-owned internal state can survive after its backing memory has been freed. A later request handled by the same worker may use that stale state before normal initialization resets it.
PHP versions older than 8.1 will not receive updates from the project, though the project has provided some patches for PHP 7.4, PHP 8.0, and PHP 8.1 to assist in creating backports. According to the announcement, Linux distributions and vendors received patches in advance, so updated packages should be coming soon.
