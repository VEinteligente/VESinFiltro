---
layout: post
title: "Phishing attack targeting Instagram users"
small:   "Phishing attack targeting Instagram users"
excerpt: "Maliciuos domain network is targeting Instagram users in a phishing campaign"
permalink: /noticias/2021-02-03/
date:   2021-02-03 17:10:00 -0400
categories: phishing
image:
---

At VESinFiltro we have identified a network of domains used to phish Instagram credentials after we provided assistance to one of their victims.

The person or group running this campaign seems to not be politically motivated and is just seeking profit from the compromised accounts.  

# Observed MO

1.  The attackers send instagram direct messages, pretending to be an official Instagram support to an account they deem as valuable.
    
2.  They offer the possibility of validating the account (i.e. the blue tick) after filling a linked online form
    
3.  The form requests instagram username and password to begin, in addition to a phone number and other details. It is hosted online under a domain name that's constructed to look as official, mimics the branding and look and feel of the brand.
    
4.  The attackers take control of the account changing the password, recovery email and at least in some cases changing the account name.
    
5.  The attackers contact the victim demanding payment to return the account on the provided details.

Other options, it's possible that depending on the judgment of the attackers, that some accounts might be sold instead of demanding ransom. Our review found that they also trick other users with bogus copyright messages.

# Domains and IPs used

The URL received was hosted on the IP **35.225.60.105** along with multiple other phishing domains, and later was moved to the IP **34.76.11.139**. The phishing domains could be classified into two categories: fake copyright claims and false Instagram verification (blue checkmark). The other domains that were hosted on the server are either inactive, not showing any information or seemingly irrelevant to the phishing websites.

 IP 35.225.60.105 domain list:

| Domain                      |               Status           |
|-----------------------------------------|--------------------------|
| lnstagramhelpbusinessverified.com       | Active                   |
| pandesmidestek.com                      | Active on domain parking |
| lnstagramverify-tick.com                | Active                   |
| pandemimdestek.com                      | Active on domain parking |
| sosyalyardimm.com                       | Inactive                 |
| copyrightaccounthelp.com                | Inactive                 |
| copyrightaccounthelp.com                | Inactive                 |
| lnstagram-copyrights-helpcenter.com     | Inactive                 |
| ig-copyrightbusiness.com                | Inactive                 |
| lnstagram-verifiedaccount.com           | Inactive                 |
| helpbluetick.net                        | Inactive                 |
| helpaccountcopyright.com                | Inactive                 |
| servicecopyrighthelp.com                | Inactive                 |
| destekpandemis.com                      | Inactive                 |
| 105.60.225.35.bc.googleusercontent.com  | Inactive                 |
| lnstagram-helpscopyright-team.com       | Inactive                 |
| lnstagram-copyright-helpscenter.com     | Inactive                 |
| lnstagram-accountverify.com             | Inactive                 |
| cranky-perlman.35-225-60-105.plesk.page | Inactive                 |
| lnstagram-verify-tick.com               | Inactive                 |
| lnstagramverify-support.com             | Inactive                 |
| lnstagram-accountverification.com       | Inactive                 |
| lnstagramverifysupport.com              | Inactive                 |
| lnstagram-verifyform.com                | Inactive                 |
| ig-verifiedbadgesform.gq                | Inactive                 |
| lnstagramserviceverify.com              | Inactive                 |
| lnstagramverifyservice.com              | Inactive                 |
| lnstagramverifybusiness.com             | Inactive                 |
| ig-bluetick.com                         | Inactive                 |
| lnstagramcontactverified.com            | Inactive                 |
| ig-verifiedform.gq                      | Inactive                 |

The two active domains related to a fake Instagram verification scheme are lnstagramverify-tick.com and lnstagramhelpbusinessverified.com. These two websites are identical and their HTML code is the same. **Note the use of an L in place of an i in domain names, as it looks as an uppercase i**.

Although there are many other domains whose names indicate malicious intent, all of them were already unreachable by the time of the start of this investigation. There are also two domains, pandesmidestek.com and pandemimdestek.com,  which are reachable but without any content in their websites whatsoever. It’s important to note that these domains are also related to the Turkish language, as the words *“pandemi destek”* can be translated to “pandemic support”.

Some domains, but not all, had been identified for their use in phishing, leading the attacker(s) to migrate some domains that are still active to the IP **34.76.11.139**. Both IPs from google cloud services.

 IP 34.76.11.139 domain list:

| Domain                                                   | Status   |
|----------------------------------------------------------|----------|
| lnstagramhelpbusinessverified.com                        | Active   |
| copyrightaccountbusinesshelp.com                         | Active   |
| lnstagramverify-tick.com                                 | Active   |
| servicehelpcopyright.com                                 | Active   |
| cranky-murdock.34-76-11-139.plesk.page                   | Active   |
| freska-api-elasticsearch02.freska-staging.aivencloud.com | Active   |
| 34-76-11-139.plesk.page                                  | Inactive |
| 39.11.76.34.bc.googleusercontent.com                     | Inactive |

![](/res/post_img/2021-02-03/img_0.png)  ![](/res/post_img/2021-02-03/img_1.png)
WaybackMachine snapshots:
[/web/20210121175308/https://lnstagramhelpbusinessverified.com/](https://web.archive.org/web/20210121175308/https://lnstagramhelpbusinessverified.com/)

[web/20210121180220/https://lnstagramhelpbusinessverified.com/form/](https://web.archive.org/web/20210121180220/https://lnstagramhelpbusinessverified.com/form/)

**The URLs of the phishing pages are not the root of their domains, but located at /form**, such as lnstagramverify-tick.com **/form** and lnstagramhelpbusinessverified.com **/form**. The site shows a form in which the victim is asked to introduce their Instagram user and its password. If the person targeted by the phishing campaign fills this information and submits it, then it'll be received by the attackers who later on will try to steal the account.

The other type of phishing is executed by tricking the victim into believing he got a copyright strike on their Instagram account. The website related to this is servicehelpcopyright.com and like the previous case it also has a form in which the victim is supposed to fill their private information.



![](/res/post_img/2021-02-03/img_2.png)
![](/res/post_img/2021-02-03/img_3.png)

![](/res/post_img/2021-02-03/img_4.png)

WaybackMachine snapshots:
[http://web.archive.org/web/20210202035043/https://servicehelpcopyright.com/](http://web.archive.org/web/20210202035043/https://servicehelpcopyright.com/)

[http://web.archive.org/web/20210130233853/https://servicehelpcopyright.com/form/](http://web.archive.org/web/20210130233853/https://servicehelpcopyright.com/form/)

Not only is the Instagram username and password are solicited, but also an email and its password. It's also worth mentioning that the attackers ask to *"not put 2 factors in two days after confirming your account here"*, in an attempt to dissuade the victims of using 2FA.

As it can be seen on the screenshots, web pages share the same structure and some assets. The base URL looks like a destination used for testing purposes and it has some text written in Turkish. For example, alongside the word *“deneme”* in the center on the screen there is also a button that points to an email address called denemedene@gmail.com, which can be translated to “test” or “experiment”.

While researching this case we found the probable origin of the source code in a Turkish hacker forum, the description of the PHP documents and user comments match the phishing sites found, the username also matches an attribution comment in the HTML code.

# Recommendations
For the users who want to visit this site or any other with sensitive information, we recommend taking these basic security measures:

1.  Get the link or address using trusted sources. In this case: directly from the official Whatsapp or Facebook bots.
    
2.  Use a trusted VPN if there are any reasons to believe that the traffic could be monitored or manipulated, this applies to this case.
    
3.  Make sure that the link begins with HTTPS.
    
4.  Be suspicious and desist from using a website if the browser gives you a security warning.
    
5.  If the website address doesn’t match exactly with the domain that you know, consider the site as a false one and avoid any other type of interaction: mywebsite.co, mywwebsite.com and mywebsite.net can be controlled by completely different people.
