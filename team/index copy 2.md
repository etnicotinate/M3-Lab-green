---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

Our team consists of members from Eastern Institute of Technology. Find out more about our research group [here](https://www.eitech.edu.cn/en/).

## Principal Investigator

{% include list.html data="members" component="portrait" filters="role: pi" %}

## Faculty

{% include list.html data="members" component="portrait" filters="role: faculty" %}

## Administration and Research Staff

{% include list.html data="members" component="portrait" filters="role: (coordinator|researcher|postdoc)" %}

## Students

{% include list.html data="members" component="portrait" filters="role: (phd|undergrad|assistant)" %}

## Affiliated and Visiting Students

{% include list.html data="members" component="portrait" filters="role: (summer|affiliated|visiting)" %}

{% include section.html dark=true %}

We work with a wide range of outstanding groups from around the world, and we're always on the lookout for new and unique perspectives. We want to push the frontier of computatipnal materials science and AI for science, creating new breakthroughs in the field of all-solid-state batteries.

{% include button.html icon="fa-solid fa-handshake-angle" text="Join the Team" link="jobs" style="button" %}

{% include section.html %}

<!-- {% include gallery.html %} -->

## Alumni

{% include list.html data="members" component="portrait" style="small" filters="role: alumni" %}

{% include section.html background="images/background.jpg" dark=true %}

Our team thrives on collaboration across disciplines and institutions, bringing together innovative ideas and diverse perspectives to tackle the challenges of xxx. Whether you’re interested in joining us or learning more about our research, we encourage you to explore the exciting work we’re doing.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/teachers-day.png" %}
{% include figure.html image="images/dinner.jpg" %}
{% include figure.html image="images/group-meeting.jpg" %}

{% endcapture %}



{% include grid.html style="square" content=content %}