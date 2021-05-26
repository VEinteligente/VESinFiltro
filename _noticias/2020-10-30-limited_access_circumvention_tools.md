---
layout: post
title: "Limited access to circumvention tools in Venezuela"
#small:   ""
excerpt: "From blocked access DNS servers, to some circumvention tool's websites
being blocked. Venezuela's returning appetite to block censorship
circumvention tools."
permalink: /noticias/2020-10-30-limited_access_circumvention_tools/
date:   2020-10-30 12:00:00 -0400
categories: bloqueos
image: /res/post_img/2020-10-30-en.png
---
![](/res/post_img/2020-10-30-en.png)

Este reporte también está publicado [en español](https://vesinfiltro.com/noticias/Phishing_impulsado_por_gobierno_de_Venezuela/).
This report is also published [in spanish](https://vesinfiltro.com/noticias/Phishing_impulsado_por_gobierno_de_Venezuela/).

## Introduction

For many years, Venezuela has suffered website blockades, affecting everything from the media to initiatives in response to the COVID-19 pandemic. Additionally, the state-owned internet provider, CANTV, has implemented blocks to prevent the use of censorship circumvention tools. In 2018, we [denounced](https://twitter.com/vesinfiltro/status/1009596837911826432?s=20) and subsequently [documented](https://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/) the [blocking of Tor](https://vesinfiltro.com/noticias/CANTV_bloquea_Tor_2017-06-26/), an important network to navigate privately and evade censorship, in addition to registering other actions directed by the national executive power that violate the digital freedoms of Venezuelans.

The precarious conditions of internet freedoms in Venezuela have been
registered by different international organizations, including a [report from the Office of the United Nations High Commissioner for Human Rights](https://ohchr.org/EN/HRBodies/HRC/RegularSessions/Session41/Documents/A_HRC_41_18_SP.docx) and [*Freedom House*](https://freedomhouse.org/). In their latest report, [**Freedom on the net 2020**](https://freedomhouse.org/country/venezuela/freedom-net/2020), Freedom House has concluded that there is direct censorship of news portals and political content, therefore limiting its accessibility from the largest internet providers in the country, which implies a clear violation of users’ rights.

Circumvention tools to avoid censorship or governmental interference have become necessary, not only for users who seek to access news about the reality of Venezuela, but also for journalists looking to protect both their information and themselves and those surrounding them.

**This report gives an update on which circumvention tools are still
available for internet users in Venezuela considering all the major
internet providers in the country by October 2020.**

## Use of circumvention tools

Internet censorship circumvention is the use of various methods and tools to bypass [internet censorship](https://en.wikipedia.org/wiki/Internet_censorship), such as proxy servers, VPNs, Tor or anonymization techniques. These tools can also provide an extra layer of protection for people that handle sensible information like journalists, activists or political leaders.

In nations where the internet is being strongly censored and surveillanced, the use of circumvention tools have become essential. Venezuelans for many years have been using VPNs and changing their DNS in order to avoid government censorship and protect their digital
privacy. However, these practices can also be affected by the same restrictions that they try to bypass.

The [2018 report](https://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/) titled *“The State of Internet Censorship in Venezuela”* documented how the state-owned ISP, CANTV, blocked access to the Tor network and to it's publicly known [obfs3 and obfs4](https://gist.github.com/hellais/ec4915246641a9f96ff0c9539ba9fe1d) bridges sued to circumvent censorship to Tor itself. In 2019 VE sin Filtro alerted and documented the block of Tunnelbear and Windscribe; while also identifying the block of Opera's built-in "VPN" feature.

Just a few months ago, on August 28th 2020, [VeSinFiltro informed](https://vesinfiltro.com/noticias/2020-08-28-block-VPNs/) about a new wave of access restrictions by the major internet service providers in Venezuela. This time, the blockage affected Psiphon and Tunnelbear, both VPN services, and the web proxy Anonymouse, with the intention to stop the healthcare program for medical personnel promoted by the president of the National Assembly, Juan Guaidó, amidst the COVID-19 crisis.

## Current censorship of VPNs and circumvention tools

By April 5, 2020, after a fire in a key facility in Caracas that [took down almost half of their network](https://twitter.com/vesinfiltro/status/1246985092045639686), CANTV’s censorship to Tunnelbear, Windscribe and Opera's VPN feature ceased for most of its users, as well as many HTTP-based blocks (HTTP host and SNI filtering) that also became ineffective, as [reported on April 7 2020](https://vesinfiltro.com/noticias/2020-04-06-levantados_multiples_bloqueos_cantv).

However by 2020-08-20 three new DNS blocks were implemented on circumvention tools, of which two remain on all major ISPs, affecting access to their websites, but not limiting in-app functionality .

{:.table-responsive.thead-dark.table-striped}
| Website | URL | CANTV | Movistar | Digitel | Inter | Supercable
|--|--|--|--|--|--|--
| Tunnelbear | https://tunnelbear.com | Blocked   | DNS Block | Blocked   | DNS Block |  DNS Block
| Psiphon | https://psiphon.ca | Blocked   | DNS Block | Blocked   | DNS Block |  DNS Block

This new wave of DNS blocks came after the announcement of a plan created by Juan Guaidó and the National Assembly in order to give monetary aid to healthcare workers amidst the COVID-19 pandemic. The money was transferred through the platform AirTM, which was soon [blocked by all major ISPs](https://twitter.com/vesinfiltro/status/1296564174198276102?s=20), and for that reason many people started using VPNs to avoid censorship. Tunnelbear and Psiphon were the [most recommended tools by us](https://twitter.com/vesinfiltro/status/1296570595065331712), and [this video](https://youtu.be/iYQQTE1-Thk) about how to use a VPN went viral after the AirTm blockade.

No blocks preventing the functionality of VPN services and other circumvention tools once installed were identified by published date.

## Blocking and limiting of DNS servers

Limits to general use of DNS servers different to the ones provided by the ISPs were evidenced on two private ISPs. The state-owned ISP did not show any restrictions, although it's noteworthy how CANTV has repeatedly used DNS response injection even when the users were using a third-party DNS server during major state-sponsored [phishing campaigns](https://vesinfiltro.com/noticias/Phishing_by_Venezuelan_government_targets_activists/).

{:.table-responsive.thead-dark.table-striped.table-sm}
| Public DNS              | IP              | CANTV | movistar    | digitel   | inter | supercable |
|-------------------------|-----------------|-------|-------------|-----------|-------|------------|
| a.resolvers.level3.net. | 4.2.2.1         |       |             | Blocked   |       |            |
| b.resolvers.Level3.net. | 4.2.2.2         |       |             | Blocked   |       |            |
| c.resolvers.level3.net. | 4.2.2.3         |       |             | Blocked   |       |            |
| Cloudfare               | 1.1.1.1         |       | Inaccesible | Blocked   |       |            |
| Cloudfare               | 1.0.0.1         |       |             | Blocked   |       |            |
| cns1.cw.net.            | 141.1.1.1       |       |             | Blocked   |       |            |
| Comodo Secure DNS       | 8.26.56.26      |       |             | Blocked   |       |            |
| Comodo Secure DNS       | 8.20.247.20     |       |             | Blocked   |       |            |
| DNS Advantage           | 156.154.70.1    |       |             | Blocked   |       |            |
| DNS Advantage           | 156.154.71.1    |       |             | Blocked   |       |            |
| dns-fra.de.ignite.net.  | 195.182.110.132 |       |             | Blocked   |       |            |
| dns-muc.de.ignite.net.  | 62.134.11.4     |       |             | Blocked   |       |            |
| dns1.nyc.dns-roots.net. | 208.78.24.238   |       |             | Blocked   |       |            |
| Dyn                     | 216.146.35.35   |       |             | Blocked   |       |            |
| Dyn                     | 216.146.36.36   |       |             | Blocked   |       |            |
| Google DNS              | 8.8.8.8         |       |             |           |       |            |
| Google DNS              | 8.8.4.4         |       |             | Blocked   |       |            |
| Open DNS                | 208.67.222.222  |       |             | Blocked   |       |            |
| Open DNS                | 208.67.222.220  |       |             | Blocked   |       |            |
| Quad 9                  | 9.9.9.9         |       |             | Blocked   |       |            |
| Quad 9                  | 149.112.112.112 |       |             | Blocked   |       |            |
| Yandex                  | 77.88.8.8       |       |             | Blocked   |       |            |
| Yandex                  | 77.88.8.1       |       |             | Blocked   |       |            |
| Yandex Family           | 77.88.8.7       |       |             | Blocked   |       |            |
| Yandex Family           | 77.88.8.3       |       |             | Blocked   |       |            |
| Yandex safe             | 77.88.8.88      |       |             | Blocked   |       |            |
| Yandex safe             | 77.88.8.2       |       |             | Blocked   |       |            |
| cns2.cw.net             | 195.27.1.1      |       |             | Blocked   |       |            |
| uneeda.telstra.net      | 139.130.4.4     |       |             | Blocked   |       |            |

### Digitel

Our tests covered a list of 30 DNS servers, all of which were blocked by Digitel, with the exception of the most well-known one, 8.8.8.8, Google's Public DNS server.

Digitel blocked any UDP or TCP connection on port 53, regardless of their content or application-layer protocol. Requests to these servers from other ports worked when available, with the exception of connections to Google's 8.8.8.8 that weren’t blocked at all.

**We can conclude that, with the exception of the server 8.8.8.8 by Google, all other standard DNS services are blocked for Digitel users.**

Movistar
---
In the case of Movistar, 1.1.1.1, the main public DNS server of Cloudflare and APNIC, is inaccessible. Given that the rest of the most popular DNS, including Google's 8.8.8.8, do not present censorship, it is very likely that this is not a case of censorship but rather an internal operations conflict with the IP address 1.1.1.1 by Movistar.

The Cloudflare 1.0.0.1 alternate DNS server is fully functional as well as the Cloudfare’s mobile app called "1.1.1.1".

CANTV, Inter y Supercable
---
All tested DNS servers work on CANTV, Inter and Supercable.

## Recomendations

We recommend Venezuelan internet users to have at least one VPN installed and tested on personal devices such as cell phones and computers, even if it’s not planned to use them immediately.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iYQQTE1-Thk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The VPN we recommend the most is Psiphon, but Tunnelbear is also a good option that is very easy to use. To download them from Venezuela you can use the following alternative links that until the date of publication have not been blocked:

**Psiphon:**

-   [psiphon3.com](http://psiphon3.com/es/download.html)

-   [Android: Play Store](https://play.google.com/store/apps/details?id=com.psiphon3.subscription)

-   [iOS: Apple App Store](https://apps.apple.com/us/app/psiphon/id1276263909?ls=1)

-   Proxy: [https://58685.info](https://58685.info/)

-   E-mail: get@psiphon3.com

**Tunnelbear:**

-   [Android: Play Store](https://play.google.com/store/apps/details?id=com.tunnelbear.android)

-   [iOS: Apple App Store](https://geo.itunes.apple.com/app/tunnelbear-vpn-unblock-websites/id564842283?mt=8&at=1010l9nk)

-   [tuneloso.com](http://tuneloso.com/)

We recommend using a trusted VPN, especially when accessing websites with political content or participating in online activities that may be in conflict with the ruling party in Venezuela. Additionally, a VPN allows you to access blocked websites and media.

It is not a bad idea to change DNS servers, as long as you are aware that this does not help you bypass all the blocks in Venezuela or protect you from sophisticated DNS manipulations that the Government of Venezuela has used against its citizens. There are many public CNS options, among them the most recognized are: 8.8.8.8 and 8.8.8.4 (Google); 1.1.1.1 and 1.0.0.1 (Cloudflare and APNIC); or 9.9.9.9 and 149.112.112.112 (Quad 9). To know how to change the DNS of your computer or mobile device, you can check [this link](https://vesinfiltro.com/bloqueos/dns/).

## Methods

All tests were performed in the months of September and October, from the following ISPs: CANTV (AS8048), Movistar (AS6306), Digitel
(AS264731), Inter (AS21826) and Supercable (AS22313). CANTV is known to share key infrastructure and behave the same from other censorship testing as their mobile subsidiary, Movilnet (AS27889).

### Checking for blocked tools

For all tools, a new install of the application was performed on a mobile phone connected for each ISP, and the functionality was tested performing the most common use case using the default app or tool settings. If the tool required a logged-in user, the user performed the login process connected to the ISP being tested at the moment without any circumvention techniques in place.

For Tor in particular, OONI's [Vanilla Tor](https://ooni.torproject.org/nettest/vanilla-tor/) test and [Tor Bridge Reachability](https://ooni.torproject.org/nettest/tor-bridge-reachability/) tests were performed.

The following tools were tested on all ISPs:

-   Opera browser’s built-in “VPN”

-   Lantern

-   Tor

-   Tunnelbear

-   Psiphon

-   Windscribe VPN

-   hotspotshield

-   Intra

-   Outline

-   Open VPN

-   Hyde My Ass

-   1.1.1.1 app (DoT / DoH)

-   1.1.1.1 app (1.1.1.1 + Warp)

### Blocked websites

The list of websites was tested using OONI's [Web Connectivity](https://ooni.torproject.org/nettest/web-connectivity/) test, as well as manual testing for any URL that produced anomalous OONI test results.

The following URLS were tested

- Opera browser’s built-in “VPN” https://www.opera.com

-   Lantern https://getlantern.org

-   Tor https://www.torproject.org

-   Tor https://bridges.torproject.org

-   Tunnelbear http://tunnelbear.com

-   Tunnelbear http://tuneloso.com

-   Psiphon http://psiphon.ca

-   Psiphon http://psiphon3.com

-   Windscribe VPN https://windscribe.com

-   hotspotshield https://www.hotspotshield.com

-   Intra http://getintra.org

-   Outline http://getoutline.org

-   Guardster.com

-   multiproxy.org

-   Open VPN openVPN.net

-   proxy.org

-   Ultrasurf ultrasurf.us

-   Hyde My Ass https://www.hidemyass.com/

-   get2ip geti2p.net

-   Pure VPN purevpn.com

### Checking for blocked DNS servers

For testing access to standard DNS queries we attempted to query
multiple well-known domains to the following list of DNS servers programmatically, and evaluating upon failure to obtain answers at the tested ISPs, these tests were repeated multiple times on different dates.

DNS over TLS and DNS over HTTPS was also tested using command line tools.

-   Each ISP's DNS server (generally private)

-   a.resolvers.level3.net. 4.2.2.1

-   b.resolvers.Level3.net. 4.2.2.2

-   c.resolvers.level3.net. 4.2.2.3

-   Cloudfare 1.1.1.1

-   Cloudfare 1.0.0.1

-   cns1.cw.net. 141.1.1.1

-   Comodo Secure DNS 8.26.56.26

-   Comodo Secure DNS 8.20.247.20

-   DNS Advantage 156.154.70.1

-   DNS Advantage 156.154.71.1

-   dns-fra.de.ignite.net. 195.182.110.132

-   dns-muc.de.ignite.net. 62.134.11.4

-   dns1.nyc.dns-roots.net. 208.78.24.238

-   Dyn 216.146.35.35

-   Dyn 216.146.36.36

-   Google DNS 8.8.8.8

-   Google DNS 8.8.4.4

-   Open DNS 208.67.222.222

-   Open DNS 208.67.222.220

-   Quad 9 9.9.9.9

-   Quad 9 149.112.112.112

-   Yandex 77.88.8.8

-   Yandex 77.88.8.1

-   Yandex Family 77.88.8.7

-   Yandex Family 77.88.8.3

-   Yandex safe 77.88.8.88

-   Yandex safe 77.88.8.2

-   cns2.cw.net 195.27.1.1

-   uneeda.telstra.net 139.130.4.4

-   Two test servers, IPs not published.

#### Blocking by Digitel
The block by digitel was identified as a block of any UDP or TCP packages on port 53, regardless of their content or application-layer protocol. This was tested using tools to send different kinds of requests on different ports, including ICPM packages to the DNS servers and attempting the same requests on our test servers.

We could confirm that DNS requests on different ports worked, and that UDP and TCP packets on port 53 are being blocked by the ISP.
