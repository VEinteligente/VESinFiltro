---
layout: post
title: Phishing by Venezuelan government puts activists and internet users at risk.
small: Phishing by Venezuelan government puts activists at risk.
excerpt: "Report: voluntariosxvenezuela.com, a site to register humanitarian aid volunteers, has suffered a state-sponsored phishing campaign empowered by DNS injection."
permalink: /noticias/Phishing_by_Venezuelan_government_targets_activists/
date:   2019-02-16 18:00:00 -0400
categories: bloqueos
image: /res/post_img/2019-02-15-report_en.png
author: "Andrés Azpúrua, Carlos Guerra, Jose Luis Rivas"
---

This report was originally [published in Spanish on 2019-02-15](https://vesinfiltro.com/noticias/Phishing_impulsado_por_gobierno_de_Venezuela/)

### Executive Summary

The website voluntariosxvenezuela.com, a portal associated with the Venezuelan opposition led by Juan Guaidó, was created to register volunteers interested in helping with the distribution of humanitarian aid. It has become a target of a phishing campaign led by those aligned with the Nicolás Maduro government.

On February 12, 2019 we detected that CANTV, the largest internet service provider in Venezuela owned by the government of Nicolás Maduro, was redirecting users visiting the website to another server hosting a visually identical malicious website which is not owned or controlled by the legitimate site administrators of voluntariosxvenezuela.com.

On the same day, interim President Juan Guaidó launched a massive campaign  encouraging people to register as volunteers. As a result, thanks to the scope and number of people mobilized through the campaign, and the percentage of Internet traffic that passes through CANTV networks, we estimate that tens of thousands of people submitted their data to the malicious cloned website.

We were able to verify that the redirection to the malicious website happened even when using DNS servers that were not CANTV servers (for example, when using Google’s 8.8.8.8 or Cloudflare/APNIC’s 1.1.1.1); traffic was actively monitored and CANTV gave falsified DNS responses to user requests. Our research also directly linked CONATEL, Venezuela’s regulatory institute for communications, with the registration of the false domain. In addition, our research also discovered multiple domains that are similar to social media sites and popular websites that could be used in future phishing campaigns (or have been used already) to collect user data.

These developments are worrying because they point to an increased sophistication in digital attacks linked to and originating from the government of Nicolás Maduro. This dramatically increases the need for both users and website administrators to take preventative measures to avoid falling into this type or similar phishing campaigns.

### Index


* [Context](#context)

* [Blocking and phishing of VoluntariosXVenezuela.com](#blocking-and-phishing-of-voluntariosxvenezuelacom)

    - [Spoofing, poisoning and DNS injection](#spoofing-poisoning-and-dns-injection)

    - [The Malicious Site](#the-malicious-site)

    - [What Users Saw and Experienced](#what-users-saw-and-experienced)

    - [Impact and current status](#impact-and-current-status)

* [Other phishing campaings](#other-phishing-campaigns)

    - [Server owners](#server-owners)

* [Conclusions](#conclusions)

* [Recomendations](#recommendations)


Context
=======

Venezuela has experienced a complex humanitarian crisis in recent years that has led millions of Venezuelans seeking refugee in other countries, even fleeing Venezuela by foot. [The UN estimates that more than 3 million Venezuelan refugees have fled the country] (https://www.unhcr.org/news/press/2018/11/5be4192b4/number-refugees-migrants-venezuela-reaches-3-million.html).

In addition, in January 2019 the world witnessed a Venezuelan presidential crisis - the legitimacy of Nicolás Maduro as President was questioned after Juan Guaidó was proclaimed the President of the National Assembly and Interim President of Venezuela  (http://es.wikipedia.org/wiki/Crisis_presidencial_de_Venezuela_de_2019).

The presidential crisis has triggered a wave of internet censorship that has been much more tactical, using tools such as SNI filtering. The first blocking occured with the
[blocking of Wikipedia](http://vesinfiltro.com/noticias/wikipedia_2019-01/) when various articles began referring to Juan Guaidó as President of Venezuela, and has focused on silencing public debates that are transmitted via streaming.  
[The blocking of streaming platforms](http://vesinfiltro.com/noticias/report-jan-2019/#blocking-of-instagram-twitter-and-youtube) is particularly important in the Venezuelan context where there is a near  
[complete censorship of traditional media](https://rsf.org/en/venezuela). We have reported multiple cases of blocking including the [blocking of Tor in
2018](http://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/), and entities like Freedom House classify [internet in Venezuela as not free.](http://freedomhouse.org/report/freedom-net/2018/venezuela).

In response to the humanitarian crisis, and in support of the interim government,
collection centers have been created in various countries to collect aid to ship to Venezuela, including in places like Colombia, Brazil, Chile, Argentina, Costa Rica, The United States, and the Netherlands among others. However, the Maduro government has impeded this humanitarian aid from entering the country.  As a result, the Venezuelan opposition led by Juan Guaidó organized a movement of volunteers to help with the logistics and distribution of this humanitarian aid using the website
[voluntariosxvenezuela.com] (https://voluntariosxvenezuela.com/) for coordination.


Blocking and phishing of VoluntariosXVenezuela.com
==============================================

We have identified and analyzed a sophisticated phishing campaign against Venezuelans that volunteered to help with the distribution of humanitarian aid through an initiative organized and lead by the Venezuelan opposition lead Juan Guaidó.

**This grave phishing campaign was at least in part driven by the state owned internet service provider (ISP) of Venezuela, CANTV, and its mobile subsidiary Movilnet ** Individuals using CANTV and Movilnet who tried to visit the website to register as volunteers at [voluntariosxvenezuela.com](https://voluntariosxvenezuela.com) where directed to a server hosting the malicious website voluntariovenezuela.com (without the s or x).

This malicious website used by the phishing campaign was visually identical to the real website, and was used to collect personal information from volunteers, who only submitted their data because they thought they were registering on the real website. The malicious website **obtained a massive amount of traffic from the CANTV/Movilnet net using sophisticated techniques of interception and DNS spoofing**

It is difficult to know exactly when the phishing campaign began, since it is
possible that the malicious website was put to use before DNS spoofing was used. We began [alerting people of the
phishing campaign] (https://twitter.com/andresAzp/status/1095420751979708417) in the early afternoon of February 12, letting them know that they should not submit personal data to the malicious website, as well as supporting victims who had already done so.

The malicious site was posted on Twitter [starting in the afternoon of February 11](https://twitter.com/search?f=tweets&vertical=default&q=voluntariovenezuela.com%20since%3A2019-02-11%20until%3A2019-02-12&src=typd&lang=en)
(Venezuela timezone, GMT-4), by various users promoting it. This [particular tweet stands out](https://twitter.com/Wil_Ardilax1/status/1095071269538721793)
([archived](https://web.archive.org/web/20190214143056/https:/twitter.com/Wil_Ardilax1/status/1095071269538721793),
[2](https://archive.fo/AGjvI)) by user @Wil\_Ardilax1, sent out at 5:25pm(GMT-4), and contains the URL of the malicious website [https://www.voluntariovenezuela.com/index.html\#como-puedo-ayudar](https://www.voluntariovenezuela.com/index.html#como-puedo-ayudar) - we suspect he probably copied the link directly from the website and pasted into his post. In addition, a [tweet](https://twitter.com/alerodriguez150/status/1095073021939847170)
([archived](https://web.archive.org/web/20190214143240/https:/twitter.com/alerodriguez150/status/1095073021939847170),
[2](https://archive.fo/E1cPd)) from February 11 at 5:32pm(GMT-4), responding to  @voluntariosxve, asks that people take care in writing the URL correctly, and then links to the malicious website.

From 10:30am(GMT-4) one of the first complaints consistent with DNS spoofing  of [voluntariosxvenezuela.com](https://voluntariosxvenezuela.com), is registered [on
Twitter](https://twitter.com/ZombVE/status/1095329455529091074)
([archived](https://web.archive.org/web/20190214145414/https:/twitter.com/ZombVE/status/1095329455529091074),
[2](https://archive.fo/YKtC6)), as well as other clear
[references](https://twitter.com/josraf/status/1095385577946599424)
([archived](https://web.archive.org/web/20190214145250/https:/twitter.com/josraf/status/1095385577946599424),
[2](https://archive.fo/hfqek)) to the incident appear later.

We can estimate that the phishing campaign began on February 11 at 5:25pm (GMT-4), and DNS spoofing began on February 12 around 10:30am.
Our measurements indicate that the phishing campaign was lifted between 2:30 am and 7:30 am February 13.

There is also an account on Twitter,
[@voluntariosvene](https://web.archive.org/web/20190214175249/https:/twitter.com/voluntariosvene), that is similar to the verified account [@voluntariosxve](https://twitter.com/voluntariosxve), that was promoting links to the site with unsafe HTTP connections, which facilitates users falling victim to the phishing campaign without receiving any warning or error messages from their browser that may trigger a user to be suspicious or cautious of the website.

On February 14, the phishing campaign was reactivated briefly between 5:00 to 5:55pm, the malicious site was online with a different IP and CANTV restarted DNS injection of any DNS request to send traffic to the malicious.

Spoofing, poisoning and DNS injection
----------------------------------------

Internet browsers use DNS servers (Domain Name System) to translate the name of a website, such as example.com, to an IP address that will be used to connect to the desired server. Essentially, this what allows you to use your web browser to find or “visit” web sites.  DNS spoofing is a family of techniques that allows for corrupt DNS data to be introduced, causing the server to return an incorrect result, such as the wrong IP address. As a result, the user cannot visit their desired website or is sent to another website that they did not request.  

On February 12 all outgoing DNS traffic was inspected and any request for the IP address associated with voluntariosxvenezuela.com was returned with the IP address of the malicious site,159.65.65.194, and clearly does not match the [range of
IPs of the real site] (https://securitytrails.com/domain/voluntariosxvenezuela.com/history/a)
 voluntariosxvenezuela.com, which is hosted at AWS.  Additionally, the IP address of the malicious site is also returned by the DNS servers of
CANTV. It is unknown if this IP was configured in the CANTV servers or if its caches (temporary memory) were \ "poisoned \" and were also affected by the  malicious DNS injection.

Sophisticated equipment was configured by the malicious actors to inspect all (or almost all) of the traffic to detect any DNS request on volunteersxvenezuela.com and then impersonate that server to give a fake response. This is called DNS injection.

  **DNS injection can be done to any DNS request to any server on the Internet, including trusted servers.**  We were able to observe this phenomena happening even when using servers external to CANTV, such as 8.8.8.8 from Google and 1.1.1.1 from Cloudflare. Even when we sent requests to non-existent DNS servers, the same fake IP address was returned.

We ran several tests to obtain the IP address of voluntariosxvenezuela.com and voluntariovenezuela.com with the CANTV DNS:
200.44.32.12. In every case, the response was 159.65.65.194

```
$ dig voluntariosxvenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47904
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 2427 IN A 159.65.65.194
;; Query time: 32 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Tue Feb 12 17:56:41 -04 2019
;; MSG SIZE rcvd: 70

$ dig voluntariovenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariovenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33913
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariovenezuela.com. IN A
;; ANSWER SECTION:

voluntariovenezuela.com. 126 IN A 159.65.65.194
;; Query time: 139 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Tue Feb 12 17:56:53 -04 2019
;; MSG SIZE rcvd: 68

```
Additionally, we repeatedly found that the returned IP continued to be inconsistent with the range of [authentic IPs of
voluntariosxvenezuela.com](https://securitytrails.com/domain/voluntariosxvenezuela.com/history/a)
when requests were sent to different CANTV DNS servers, 8.8.8.8 of Google, 1.1.1.1 of Cloudfare, and for IPs where no DNS server existed. The following is an example of these repeated tests:


```

$ dig voluntariosxvenezuela.com @8.8.8.8

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27141
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194
;; Query time: 31 msec
;; SERVER: 8.8.8.8\#53(8.8.8.8)
;; WHEN: Tue Feb 12 18:09:33 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @1.1.1.1

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65246
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194
;; Query time: 96 msec
;; SERVER: 1.1.1.1\#53(1.1.1.1)
;; WHEN: Tue Feb 12 18:09:40 -04 2019
;; MSG SIZE rcvd: 84

```

The same occurred with IPs with no DNS servers like 185.199.108.153. For example:
```

$ dig voluntariosxvenezuela.com @185.199.108.153

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com
@185.199.108.153
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65246
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194\
```

During a small window on February 14,  DNS spoofing including DNS injection was observed again, the behaviour was the same as before but with DNS queries pointing to 134.209.13.64 instead of the previous IP address.

```
dig voluntariosxvenezuela.com @1.1.1.1

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26833
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 178 msec
;; SERVER: 1.1.1.1\#53(1.1.1.1)
;; WHEN: Thu Feb 14 17:11:30 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @8.8.8.8

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55983
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 32 msec
;; SERVER: 8.8.8.8\#53(8.8.8.8)
;; WHEN: Thu Feb 14 17:11:36 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55331
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 1009 IN A 134.209.13.64
;; Query time: 57 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Thu Feb 14 17:11:40 -04 2019
;; MSG SIZE rcvd: 70

$ dig voluntariosxvenezuela.com @185.199.111.153

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com
@185.199.111.153
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57551
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 34 msec
;; SERVER: 185.199.111.153\#53(185.199.111.153)
;; WHEN: Thu Feb 14 17:12:24 -04 2019
;; MSG SIZE rcvd: 84

```


## The Malicious Site

The server with the IP of 159.65.65.194 was housed in [Digital
Ocean](https://www.shodan.io/host/159.65.65.194), according to what was observed in the configuration. [Domain DNS](https://securitytrails.com/domain/voluntariovenezuela.com/dns)
([archived](https://web.archive.org/web/20190215022940/https://securitytrails.com/domain/voluntariovenezuela.com/dns)) and responds to the domain of
voluntariovenezuela.com (without the s or x) in addition to
voluntariosxvenezuela.com. It has a SSL certificate for the fake domain
voluntariovenezuela.com and does not show a certificate for the real site.

The malicious server hosts a visually identical clone to the official site
VoluntariosXVenezuela.com, the clone is based on the html source code and and resources, like images.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/1.png)

Analysis of the HTML code that makes up each site shows scarce differences in the source code. We noted that [HTtrack](https://www.httrack.com) was used to download the original site thanks to these code comments:

```
<!\-- Mirrored from www.voluntariosxvenezuela.com/ by HTTrack Website
Copier/3.x \[XR&CO\'2014\], Mon, 11 Feb 2019 13:41:27 GMT \-->
```
Comment on www.voluntariovenezuela.com

```
<!\-- Mirrored from www.voluntariosxvenezuela.com/descargar-kit/ by
HTTrack Website Copier/3.x \[XR&CO\'2014\], Mon, 11 Feb 2019 13:41:34
GMT \-->
```
The comment on www.voluntariovenezuela.com/descargar-kit/  suggests the site was downloaded on February 11, 2019, one day before the discovery of the fake site.

The use of this tool suggests that the real site was not compromised, but rather had to be cloned from what's user accessible, so that it could be setup on another server. The original site doesn't have these lines of comments in its code.

The differences in code are minor, especially on the [initial HTML source
](https://www.diffchecker.com/7jJKq1oH) (without dynamic changes in the DOM, such as the registration form that loads afterwards). Appreciable differences are whitespace, comments by HTTrack, changes in some URLs so that the malicious site would work and look correctly and, the removal of a Facebook pixel tracking code and the different ways the form submits after it's loaded.

The registration forms for both are treated differently, sending the information to different locations. The malicious site sends the information to a PHP script on the same server called guardar.php.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/2.png)

Submission destination on the original site
(//system.voluntariosxvenezuela.com/venezuela/PublicForm?source=1&jquery=0&geo=4&publicFormGroupClass=col-md-6)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/3.png)

Submission destination on the malicious site (guardar.php)

In comparing the servers, they provided different error messages when trying to load non existing URLs on both sites, indicating that they are running different web server software. The responses had different formats.

The malicious site had a SSL certificate by Let's Encrypt for
[www.voluntariovenezuela.com](http://www.voluntariovenezuela.com)
elaborado en Feb 11 17:38:42 2019 GMT

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/4.png)

404 Error corresponding to voluntariosxvenezuela.com (real)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/5.png)

404 Error corresponding to voluntariovenezuela.com (malicious)

The server hosting the malicious site
[www.voluntariovenezuela.com](http://www.voluntariovenezuela.com)
had the IP address 159.65.65.194. During the brief appearance during of the phishing campaign on January 14, the same server or a different one hosting the malicious site with the same purpose, had the IP address 134.209.13.64.

After the lifting of the phishing campaign momentarily in the afternoon of February 13, the server responded to that domain [only
with] (http://web.archive.org/web/20190213223700/http://voluntariovenezuela.com/)
`{" status ":" ok "}`.



What Users Saw and Experienced
---------------------------------

When CANTV users used an insecure connection (HTTP) to navigated to the real domain Volunteersxvenezuela.com, the browser was redirected, taking users to the malicious site,  www.voluntariovenezuela.com Users had no indication that this had occurred, or that there was something wrong beyond the URL change.


If users used a secure connection (HTTPS) to navigate to the real domain, they were shown an alert letting them know of the inconsistencies of of navigating to the domain  
voluntariosxvenezuela.com with an SSL certificate that corresponded to the fake site.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/6.png)


Impact and current status
---------------------------

The attack began February 12, 2019 and it was reported until the morning of February 13. The start of the phishing attack coincided with the massive march lead by interim president Juan Guaidó for Youth Day.


We estimate that the DNS spoofing lasted from 10:30 am of February 12, 2019 to 4:00am of February 13, 2019.  On February 12, many users attempted to connect to the site after listening to a speech by Juan Guaidó during the march, and after many highly visible members of the opposition tweeted the link, both HTTP and HTTPS versions. Considering the number of CANTV users and the publicity the website received through various calls to action by Juan Guaido and opposition leaders, we can conservatively estimate that the number of individuals that fell victims to the phishing attack and provided their personal data to the malicious site is in the tens of thousands, and probably much higher than that.

In Venezuela, [political discrimination is common](https://www.derechos.org.ve/opinion/discriminacion-politica-en-venezuela)
against employees in the [public sector](http://elestimulo.com/blog/cidh-asegura-que-despidos-por-la-lista-tascon-violan-los-derechos-humanos/) and against individuals [recieving social welfare](https://www.derechos.org.ve/investigacion/los-clap-7-indicios-de-discriminacion-politica).


As a result, the phishing campaign has generated a reasonable amount of fear for individuals, many who are still unsure if they were victims or not. This incident has been compared to what is known as the [\"Tascón list\"](https://www.observatoriodeconflictos.org.ve/derechos-humanos/corte-idh-condena-uso-de-ista-tascon-para-violar-derechos-politicos), a list of individuals critical of the government that was created after these individuals took part in a political process, and were then subject to political discrimination. The government’s use of of this list for this purpose was [condemned by the Inter-American Court of Human Rights] (https://www.observatoriodeconflictos.org.ve/derechos-humanos/corte-idh-condena-uso-de-lista-tascon-para-violar-derechos-politicos).

The phishing campaign ended early on February 13, and re-started briefly again during the afternoon of February 14. It is unclear why the phishing campaign was suspended, but one reason may be because the attack was publicized, with technical evidence backing up the allegations . The cessation in DNS spoofing does not necessarily have to match the inaccessibility of the site, but in this incident they came hand in hand.

There could be many reasons for the inaccessibility of the malicious site, among them include administrators deactivated the site, denial of service attacks (DoS), users successfully complaining on social media about the attack on February 13, or or because the hosting provider disabled the site.

As of the publishing of this report, none of the websites involved in the phishing campaign resolve to any IP address.


Other Phishing Campaigns
==========================

### Domain and Server Owners

The server we analyzed did not have any information or clues as to who owned the site. What we did discover is that it was hosted by Digital Ocean.

Since the domain voluntariovenezuela.com had Whois privacy protection, we were unable to identify who or what company registered the domain. However, when researching other domains associated with the corresponding IP address, we discovered that it housed various fake sites that are malicious clones of popular social media sites and popular websites. All these additional domains end in .ve, which means they are approved and authorized by CONATEL, the telecommunications regulatory body of Venezuela.

These fakes sites did have public Whois register information, with the following person being listed as registrant:


Name: Frank Lopez

Email
[franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com)

Company: micompraventa

Address: Caracas, 1 VE

Phone Number: 0212-0212-5554545 (We assume its 0212-5554545)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/7.jpg)

Reply from Whois to gmail.web.ve, one of the new domains discovered.

Archive with truncated data for Whois of google.web.ve:
[https://archive.fo/BBnZf](https://archive.fo/BBnZf)\
\

Prior to reporting the site voluntariovenezuela.com, the email and phone number in the Whois information of all the discovered malicious domains matched. After publication of these domains on Twitter, the telephone number in the Whois was changed for almost all the websites from 0212-9090597 to to 212-5554545. Notably, the Whois for the website google.web.ve still has the phone number of 0212-9090597

The Domains found in the reverse lookup services for DNS or DNS history for the servers were:

-   m.facebook.co.ve

-   www.facebook.co.ve

-   static.facebook.co.ve

-   facebook.co.ve

-   ssl.gmail.web.ve

-   gmail.web.ve

-   www.gmail.web.ve

-   accounts.gmail.web.ve

-   linkedin.co.ve

-   www.linkedin.co.ve

-   account.live.web.ve

-   outlook.live.web.ve

-   live.web.ve

-   www.live.web.ve

-   login.live.web.ve

-   mobile.twitter.info.ve

-   api.twitter.info.ve

-   [abs.twitter.info.ve](https://securitytrails.com/domain/abs.twitter.info.ve/history/a)

-   twitter.info.ve

-   www.voluntariovenezuela.com

-   voluntariovenezuela.com

Results available in
[https://securitytrails.com/list/ip/159.65.65.194](https://securitytrails.com/list/ip/159.65.65.194)
for February 12, before the publication in social media about the relationship between them. This information is still available in the history of every domain in
[securitytrails](https://securitytrails.com/list/ip/159.65.65.194).


When we did a search using ReverseWhois for the email franklopezsystem@gmail.com we discovered that there were diverse domains under the root.ve that seem to point to similar social media networks.
(Archive of Reverse Whois:
[archivo](https://archive.fo/eZkhr)).

All the discovered domains had the same email and number in their Whois registrant information: [franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com)
y 0212 909 0597.\
\

On February 13, the DNS entries for these domains pointed to server:

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/8.jpg)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/9.png)

(Screenshots of the responses to dig:
[https://twitter.com/joseluisrivas/status/1095691955693150214](https://twitter.com/joseluisrivas/status/1095691955693150214)
and
[https://twitter.com/joseluisrivas/status/1095715963138387970](https://twitter.com/joseluisrivas/status/1095715963138387970))

When reviewing host 159.65.65.194 against shodan.io, we discovered that on February 8, 2018 a scan of ports was conducted, and port 80 had a redirection to twitter.web.ve for a phishing campaign.

(Screenshot:
[https://twitter.com/joseluisrivas/status/1095702783880245248](https://twitter.com/joseluisrivas/status/1095702783880245248)).

The discovered domains try to imitate popular and high traffic websites, and are made to look like legitimate domains. They potentially might have been in other phishing attacks. This is suggested in
[checkphish.ai](https://checkphish.ai/insights/url/1534412032063/33aabce69dc4ba807c062a746bf80289d82884907d3302d9620238421f85eb1d)
where we could observe in the history results that the domain accounts.gmail.web.ve housed a form that imitated a Google sign-in form.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/10.png)

Results in checkphish.ai for accounts.gmail.web.ve., shows a web capture identical to the authentic Gmail web capture.

With this evidence, there is a clear connection or link established between the operators of the phishing campaign against  voluntariosxvenezuela.com and the operators of other phishing campaigns associated with the fake websites we discovered.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/11.png)
![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/12.png)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/13.png)

### Attribution of the phishing campaigns

With the help of various security researchers, we tried to recuperate the password for Gmail account
[franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com), and found that the number associated with that email account was 0212 9090597.

We called this phone number at 11am on February 13, 2018, and the person who answered stated their name was Gabriel. When we asked if this number corresponded with a company or a family home, he stated that it did not. He then stated  \"This is CNTI\". (CNTI is the government’s national IT center, part of the Ministry of Popular Power for University Education, Science and Technology)

However, our previous research revealed that the phone number did not correspond with the ranges that are usually used by CNTI but rather with the ranges used by CONATEL. On the footer of the CONATEL website the two main numbers  listed are: 0212 909
0599 and 0212 909 0419 (the phone number registered in the malicious domain is 0212 909 0597 and is listed for password recovery on the email)
) (archive ofl
Conatel homepage:
[https://archive.fo/lCYho](https://archive.fo/lCYho))\
\

When searching in archive.org, we found more information pointing to the range of telephone numbers used with CONATEL: 0212-909.03.11,
0212-909.03.47, 0212-909.04.18
[https://web.archive.org/web/20141024115047/https://www.conatel.gob.ve/index.php/principal/contactos](https://web.archive.org/web/20141024115047/https://www.conatel.gob.ve/index.php/principal/contactos)

When we called the phone number in question in other occasions, we got an answering machine recording explaining that we had reached CONATEL.

We also found that this number has been referenced on the UNEFA Caracas website, a website for internships, on October 15, 2018. The phone number corresponded to Gabriel Porco for his internship in NIC.ve, in CONATEL. (The URL of the website has been preserved, as well as the contents in web archive services. However, we do not wish to publish them to protect the data of other people who are listed on the snapshot of the website).

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/14_b.png)

NIC.ve which administers the .ve top level domain (TLD), functions as a department of CONATEL (National Commission of Telecommunications, Venezuela's telecomunicaitons regulator). Gabriel Porco is currently in charge of NIC.ve. The number of that office is linked with the email.

The mechanism that NIC.ve has previously used to re-acquire domains has been done ad-hoc, where the owner is NIC VE and the associated email is in the format:
"[domainer4@nic.ve](mailto:domainer@nic.ve)".  This can be seen in the Whois of domains retrieved during censorship against media such as  ntn24.com.ve, vivoplay.com.ve, and vpitv.com.ve, among others.

To recap, when we called the number listed in the in the Whois of the malicious site various times, the person who picked up the phone stated that their name was Gabriel. After different elements covered by this report was published on Twitter and became viral, the phone number on the Whois registries was quickly changed to a  phone number that sends you to a voicemail at CONATEL (The administration of NIC.ve is located in the main CONATEL building in Caracas, NIC.ve functions as a department of CONATEL)
0212-5554545![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/15.png)

We suspect the email probably belongs to someone that works in his office, since that CONATEL number was associated with that email account and used for password recovery. Only someone working for NIC.ve could have made those changes so quickly - changes that for every other user take a long time because there is no automatic platform for nic.ve. Essentially, users must submit a request via a support ticketing system or email, and must wait a period of various weeks.

Conclusions
===========

This case is very worrying considering the the precedent in Venezuela of persecuting activists and political dissidents. Particularly troublesome is the creation of lists for the purpose of targeting citizens that may be critical of the government, a tactics that [has been used since at least since  2004](https://prodavinci.com/la-lista-tascon-y-la-persecucion-politica-a-proposito-de-la-sentencia-de-la-corte-interamericana/).

The current situation puts the privacy and safety of citizens at risk, as many shared personal, identifying data on the malicious site. Most importantly, if they previously have been victims of other digital attacks such as being redirected to malicious clones of popular social media sites or fake email sites, their account information could be used against them for retaliation. We conservatively estimate that the number of victims of the phishing attack of voluntariosxvenezuela.com is in the tens of thousands, and probably much more than that.

In this specific digital attack involving voluntariosxvenezuela.com we observed the joint use of 2 different techniques. The first is the configuration of a fake site with a similar domain that asked users to register as volunteers and submit their personal information, just like the real, authentic site. The second technique is the interception and alteration of the DNS requests, which was made through the most important ISP in the country, CANTV. This was done both with CANTV’s own servers as well as outside servers using package inspection as interception strategy. These requests were redirected to the cloned, malicious site.

Sufficient evidence was gathered in this case to demonstrate that it was not just an episode of blocking, but in fact an attack on the opposition designed by the administration of Nicolás Maduro with the purpose of collecting the personal data of citizens that are critical of their government. How this data will be used is still unknown. We have also evidence that, for the first time, connects individuals working in public institutions with a digital attack of this nature.

Recommendations
===============

### For Users

It is incredibly important to be certain of the correct URL or direction of the website you are visiting, and make sure that the connection is secure (HTTPS://).If your browser gives you an error message or alert that suggests the site is not secure, immediately disconnect from it.


You have to be extra careful of being directed to sites that are malicious clones of popular social media sites.


It is recommended individuals use a VPN or Tor.  This is because changing DNS servers on devices and routers is an insufficient way to mitigate these risks, since requests to trusted servers can be intercepted.


As an advanced measure of risk mitigation, the use of password managers may help users detect a domain as fake and thus help them avoid entering credentials on these sites.


For high risk users, it is advisable that they use USB security keys to login to services like Google or Facebook.


### For website administrators

- Make sure your websites have SLL/TLS certificates, and that they are managed and protected.  

-   Make sure all HTTP traffic is redirected to HTTPS using the configurations of your virtual servers, redirecting by .htaccess, and the inclusion of the HSTS header, etc.

-   Only share HTTPS links with the public, for example on social media, press releases etc.

-  Use DNSsec to minimize the chances of successful phishing attacks (targeted cheating)

- The following are recommendations specifically for incidents similar to
VoluntariosXVenezuela.com:

    - Clearly share alerts of any security incidents that you observe.

    - Educate your users on how to detect changes to URLs, how to use HTTPS, and seriously heed browser security warnings.

    - Have clear communications and operations protocols to respond to incidents

        - Make sure your users understand where and how you will communicate with them. By knowing how you will communicate with them post-registration, users can know if the information is official, and avoid being victimized.

        - If the malicious site's registrations weren't forwarded by it to the genuine site, as it seems to be the case: Offer a simple and clear email-based form on your website to help people identify if they were a victim of the phishing attack. For example, users could submit their email they registered with and receive a message sent to that email clarifying if they were registered during the phishing attack.

Authors:  
[Andrés Azpúrua](https://twitter.com/andresAzp),
[Carlos Guerra](https://twitter.com/cguerrave),
[Jose Luis Rivas](https://twitter.com/joseluisrivas)

![Cover image](/res/post_img/2019-02-15-report_en.png)
