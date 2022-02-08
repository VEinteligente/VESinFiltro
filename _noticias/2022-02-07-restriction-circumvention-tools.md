---

layout: post
title:  "Report: Restriction to circumvention tools in Venezuela"
small:   "Restriction to circumvention tools in Venezuela"
excerpt: "Restriction to circumvention tools in Venezuela"
permalink: /noticias/2022-02-07-restriction-circumvention-tools/
date:   2022-02-07 18:20:00 -0400
categories: bloqueos
image: /res/post_img/2022-02-07/2022-02-07.png
---

![](/res/post_img/2022-02-07/2022-02-07.png)

## Importance of circumvention tools in the Venezuelan context

Venezuelans have been suffering from increasing levels of internet censorship for more than 15 years, with increasing limits on the tools used to circumvent it. Access to information and news, as well as their right of association, are curtailed by internet blocks against websites and platforms. Journalists, politicians, human rights defenders, activists and many other actors among the civil society are constantly being censored due to the government's attempts to limit free speech online in a context where independent media in radio is scarce and censored, and practically nonexistent in printed press and TV.

The censorship is implemented by all major Internet Service Providers (ISP), normally under orders from the telecoms regulator CONATEL. However, the most extensive and sophisticated blocking is performed by the state-owned ISP, CANTV, the government has successfully blocked access to information using different techniques, from DNS blocks to SNI Filtering and DNS response injection, which was used in state-sponsored phishing attacks.

Just a few days ago [VE sin Filtro reported new blocks to four news organizations](https://vesinfiltro.com/noticias/2022-02-01-bloqueo-Noticias/) that affected users in six different ISPs on top of [35 News sites being already blocked](https://vesinfiltro.com/noticias/2021-election-blocks/) during a recent election. The limitations of human rights in the Venezuelan digital space are documented in the  [Freedom on the Net 2021](https://freedomhouse.org/country/venezuela/freedom-net/2021) report, from Freedom House. 


## Current censorship of VPNs and circumvention tools

In order to have access to reliable information and avoid surveillance, Venezuelan citizens need to use different circumvention tools and strategies. The most effective has been the use of VPN services that allowed them to hide their identity and overcome internet blocks, despite attempts to limit them.

Changing the DNS servers used by a device is also a common technique, but it doesn't work for many blocked sites, particularly on the state-owned CANTV.


### TunnelBear

The block against TunnelBear continues on all major ISPs in Venezuela. It's main website, tunnelbear.com, has experienced DNS blocks in addition to HTTP/HTTPS simultaneously by CANTV (AS8048) since 2019. The rest of ISPs in the country started a DNS block on August 20th, 2020. 

TunnelBear can be downloaded from the app stores on both iOS and Android, the block mostly affects users wanting to know more and those trying to download it to their PC. The software can be downloaded on alternative URLs.

![](/res/post_img/2022-02-07/2022-02-07-tb.png)

While these blocks don’t affect the VPN functionality itself, for a period of time in 2021 they prevented the registration of new users once the app was installed on the device, a required step to use the VPN. This was fixed after TunnelBear was made aware of this. Currently the blocks do affect TunnelBear users trying to change their passwords since that system relies on the accessibility to tunnelbear.com in order to work properly.


### Psiphon

Psiphon’s main website, psiphon.ca, remains blocked by all major ISPs. In the state-owned CANTV the site is affected by an HTTP/HTTPS + DNS block, while in the rest of the ISPs is only affected by a DNS block. The site has been blocked in Venezuela since August 2020, after increased attention around blocks at the time and awareness campaigns.

These blocks don’t affect the VPN functionality in any way, nor does it compromise the normal user experience of Psiphon.


![](/res/post_img/2022-02-07/2022-02-07-ps.png)



### IKEv2 VPN Protocol

VPNs use different protocols to protect and anonymize an internet connection, one of them being IKEv2, which is built into many popular VPN providers such as Windscribe, Proton VPN, NordVPN, among others. During most —if not all— of 2021, users of CANTV couldn’t establish connections with any VPN service using the IKEv2 protocol, but by February 2022 this block was lifted. Incidentally, IKEv2 is now very rarely, if ever, the default protocol of VPN applications


### Anonymouse.org

Anonymouse is a web proxy that can be used to circumvent censorship, however we strongly discourage its use, as it's an unencrypted web proxy that poses important privacy and security risks. It was previously blocked in the state owned CANTV, but it's currently only blocked by some private providers.

<div class="table-responsive">
  <table class="blocklist">
    <thead>
      <tr>
        <th>Website</th>
        <th>CANTV</th>
        <th>Inter</th>
        <th>NetUno</th>
        <th>Supercable</th>
        <th>Movistar</th>
        <th>Digitel</th>
      </tr>
    </thead>
    <tbody>
        <tr>
        <td>psiphon.ca</td>
        <td class="block">DNS+HTTP/HTTPS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
      </tr>
        <tr>
        <td>tunnelbear.com</td>
        <td class="block">DNS+HTTP/HTTPS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
      </tr>
        <tr>
        <td>anonymouse.org</td>
        <td class="accesible">Accessible</td>
        <td class="accesible">Accessible</td>
        <td class="block">DNS Block</td>
        <td class="block">DNS Block</td>
        <td class="block">HTTPS block</td>
        <td class="block">DNS Block</td>
      </tr>
</table>

## Tor blocking

Tor is a well-known tool that provides a high level of anonymity to internet traffic and circumvents internet censorship.  We noticed an increase in the number of inaccessible bridges and directory authority relays from CANTV, similar but less effective than what happened almost four years ago. 

This means that there is currently an active effort to block Tor connections in Venezuela, but it's not very effective. According to the measurements gathered in the past few months, between 70% to 80% of Tor directory authorities are blocked at any given time in AS8048. In practice, Tor connections are successfully established most of the time, but it may take longer

The Venezuelan government has blocked Tor on CANTV in the past. In 2018 VE sin Filtro and OONI reported the blocking of Tor connections including many obfs3 and obfs4 public bridges, specially those that the Tor Browser has built-in by default. That time the block was much more effective, preventing users from connecting to the Tor network from CANTV most of the time.

This censorship against Tor operates using a TCP block to these known IPs or IP:Port pairs, similarly to what happened in 2018. Many publicly known bridges that were not built-in have been blocked.


## Blocking and limiting of DNS servers

We monitor the behavior of different DNS servers on all the major ISPs, since changing to a trusted DNS server can mitigate the majority of blocks that internet users in Venezuela are constantly experiencing. The results that we obtained remain the same as what we shared in [our last report](https://vesinfiltro.com/noticias/2020-10-30-limited_access_circumvention_tools/) regarding this topic.


<table>
  <tr>
   <td>Public DNS
   </td>
   <td>IP
   </td>
   <td>CANTV
   </td>
   <td>movistar
   </td>
   <td>digitel
   </td>
   <td>inter
   </td>
   <td>supercable
   </td>
   <td>NetUno
   </td>
  </tr>
  <tr>
   <td><a href="http://a.resolvers.level3.net/">a.resolvers.level3.net</a><span style="text-decoration:underline;">.</span>
   </td>
   <td>4.2.2.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://b.resolvers.level3.net/">b.resolvers.Level3.net</a>
   </td>
   <td>4.2.2.2
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://c.resolvers.level3.net/">c.resolvers.level3.net</a>
   </td>
   <td>4.2.2.3
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Cloudfare</strong>
   </td>
   <td>1.1.1.1
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Cloudfare</strong>
   </td>
   <td>1.0.0.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://cns1.cw.net/">cns1.cw.net</a>
   </td>
   <td>141.1.1.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Comodo Secure DNS</strong>
   </td>
   <td>8.26.56.26
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Comodo Secure DNS</strong>
   </td>
   <td>8.20.247.20
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>DNS Advantage</strong>
   </td>
   <td>156.154.70.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>DNS Advantage</strong>
   </td>
   <td>156.154.71.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://dns-fra.de.ignite.net/">dns-fra.de.ignite.net</a>
   </td>
   <td>195.182.110.132
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://dns-muc.de.ignite.net/">dns-muc.de.ignite.net</a>
   </td>
   <td>62.134.11.4
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>dns1.nyc.dns-roots.net.</strong>
   </td>
   <td>208.78.24.238
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Dyn</strong>
   </td>
   <td>216.146.35.35
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Dyn</strong>
   </td>
   <td>216.146.36.36
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Google DNS</strong>
   </td>
   <td>8.8.8.8
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Google DNS</strong>
   </td>
   <td>8.8.4.4
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Open DNS</strong>
   </td>
   <td>208.67.222.222
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Open DNS</strong>
   </td>
   <td>208.67.222.220
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Quad 9</strong>
   </td>
   <td>9.9.9.9
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Quad 9</strong>
   </td>
   <td>149.112.112.112
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex</strong>
   </td>
   <td>77.88.8.8
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex</strong>
   </td>
   <td>77.88.8.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex Family</strong>
   </td>
   <td>77.88.8.7
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex Family</strong>
   </td>
   <td>77.88.8.3
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex safe</strong>
   </td>
   <td>77.88.8.88
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><strong>Yandex safe</strong>
   </td>
   <td>77.88.8.2
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://cns2.cw.net/">cns2.cw.net</a>
   </td>
   <td>195.27.1.1
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
  <tr>
   <td><a href="http://uneeda.telstra.net/">uneeda.telstra.net</a>
   </td>
   <td>139.130.4.4
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>No
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
   <td>Si
   </td>
  </tr>
</table>


### Digitel

Our tests covered a list of 30 DNS servers, all of which were blocked by Digitel, with the exception of the most well-known one, 8.8.8.8, Google’s Public DNS server.

Digitel blocked any UDP or TCP traffic on port 53, regardless of their content or application-layer protocol. Requests to these servers from other ports worked when available, with the exception of connections to Google’s 8.8.8.8 that weren’t blocked at all.

We can conclude that, with the exception of the server 8.8.8.8 by Google, and DNS servers used internally, all other standard DNS services are blocked to Digitel users.


### Movistar

In the case of Movistar, 1.1.1.1, the main public DNS server of Cloudflare and APNIC, is inaccessible. Given that the rest of the most popular DNS, including Google’s 8.8.8.8, do not present censorship, it is very likely that this is not a case of censorship but rather an internal operations conflict with the IP address 1.1.1.1 by Movistar.

The Cloudflare 1.0.0.1 alternate DNS server is fully functional as well as the Cloudflare's mobile app called “1.1.1.1”.


### CANTV

While no blocking of public DNS servers was observed, VE sin Filtro has documented two separate instances of DNS response injection by CANTV in 2019 and 2020. In those instances it was used to impersonate third party servers and forge a response pointing politically sensitive domains to malicious servers, as part of a state-sponsored phoning campaign. This demonstrates interest and the capacity to interfere with DNS requests performed to any server on the internet. Future DNS manipulation or blocking of external DNS resolvers should be considered a significant risk for CANTV users.


### DoH and DoT

Considering the above, the use of DNS over TLS (DoT) and DNS over HTTPS (DoH) are recomendable when possible for added privacy and security, in addition to selecting an external DNS of your choice. On all ISPs DoT and DoH worked, with the exception of address 1.1.1.1 on Movistar that was unreachable for any kind of traffic.


<table>
  <tr>
   <td>
   </td>
   <td>CANTV
   </td>
   <td>Movistar
   </td>
   <td>Digitel
   </td>
   <td>Inter
   </td>
   <td>NetUno
   </td>
   <td>Supercable
   </td>
  </tr>
  <tr>
   <td>DoT
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked, except 1.1.1.1
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
  </tr>
  <tr>
   <td>DoH
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked, except 1.1.1.1
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
   <td>Not blocked
   </td>
  </tr>
</table>



## Methods

The assessment of blocked websites was performed by analyzing OONI web connectivity  network measurements produced periodically from multiple vantage points as well as other ad-hoc tests.

Tor blocking was analyzed using OONI Tor measurements produced periodically from different vantage points, tests provided by The Tor Project and ad-hoc tests.

The operation of different tools and apps was verified by running the apps on different days, from different vantage points using different configurations and manually evaluating any problems.


## Recommendations

We recommend Venezuelan internet users to have at least one VPN installed and tested on personal devices such as cell phones and computers, even if it’s not planned to use them immediately.

The VPN we recommend the most is Psiphon, but Tunnelbear is also a good option that is very easy to use. To download them from Venezuela you can use the following alternative links that until the date of publication have not been blocked:

**Psiphon:**

 - psiphon3.com
   
  - Android: Play Store
   
   - iOS: Apple App Store
   
   - Proxy: https://58685.info
   
   - E-mail: get@psiphon3.com

**Tunnelbear:**

- Android: Play Store

- iOS: Apple App Store

- tuneloso.com

We recommend using a trusted VPN, especially when accessing websites with political content or participating in online activities that may be in conflict with the ruling party in Venezuela. Additionally, a VPN allows you to access blocked websites and media.

If you use Tor in Venezuela  it's advisable to note down a list of additional bridges that are possibly not blocked, to configure in Tor browser and to familiarize with how to use Pluggable Transports in Tor Browser.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iYQQTE1-Thk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<blockquote class="twitter-tweet" data-dnt="true"><p lang="es" dir="ltr">Estas son nuestras recomendaciones para evadir <a href="https://twitter.com/hashtag/bloqueos?src=hash&amp;ref_src=twsrc%5Etfw">#bloqueos</a> en <a href="https://twitter.com/hashtag/internetVE?src=hash&amp;ref_src=twsrc%5Etfw">#internetVE</a>:<br><br>Aunque la página de <a href="https://twitter.com/PsiphonEsp?ref_src=twsrc%5Etfw">@PsiphonEsp</a> y <a href="https://twitter.com/theTunnelBear?ref_src=twsrc%5Etfw">@theTunnelBear</a> estén bloqueadas en <a href="https://twitter.com/hashtag/CANTV?src=hash&amp;ref_src=twsrc%5Etfw">#CANTV</a>, estos siguen siendo nuestros VPN recomendados.<br><br>🧵Más info en este hilo: <a href="https://t.co/SFmRM00olQ">pic.twitter.com/SFmRM00olQ</a></p>&mdash; VE sin Filtro (@vesinfiltro) <a href="https://twitter.com/vesinfiltro/status/1377385735666421761?ref_src=twsrc%5Etfw">March 31, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

It is not a bad idea to change DNS servers, as long as you are aware that this does not help you bypass all the blocks in Venezuela or protect you from sophisticated DNS manipulations that the Government of Venezuela has used against its citizens. There are many public CNS options, among them the most recognized are: 8.8.8.8 and 8.8.8.4 (Google); 1.1.1.1 and 1.0.0.1 (Cloudflare and APNIC); or 9.9.9.9 and 149.112.112.112 (Quad 9). To know how to change the DNS of your computer or mobile device, you can check [this link](https://vesinfiltro.com/bloqueos/dns/).
