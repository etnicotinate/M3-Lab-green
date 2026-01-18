---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

Our team consists of members from Eastern Institute of Technology. Find out more about EIT [here](https://www.eitech.edu.cn/en/).

## Principal Investigator

{% include list.html
   data="members"
   component="portrait"
   filter="role == 'pi'"
%}

## Faculty

{% include list.html
   data="members"
   component="portrait"
   filter="role == 'faculty'"
%}

## Research Fellow

{% include list.html
   data="members"
   component="portrait"
   filter="role == 'postdoc'"
%}

## Students

{% include list.html
   data="members"
   component="portrait"
   filter="role == 'phd' or role == 'undergrad' or role == 'assistant'"
%}

## Visiting People

{% include list.html
   data="members"
   component="portrait"
   filter="role == 'visiting'"
%}

{% include section.html dark=true %}

We work with a wide range of outstanding groups from around the world, and we're always on the lookout for new and unique perspectives. We want to push the frontier of computatipnal materials science and AI for science, creating new breakthroughs in the field of all-solid-state batteries.

{% include button.html icon="fa-solid fa-handshake-angle" text="Join the Team" link="jobs" style="button" %}

{% include section.html %}

## Alumni

{% include list.html
   data="members"
   component="portrait"
   style="small"
   filter="role == 'alumni'"
%}

{% include section.html background="images/background.jpg" dark=true %}

## Gallery

Our team thrives on collaboration across disciplines and institutions, bringing together innovative ideas and diverse perspectives to tackle the challenges of xxx. Whether you’re interested in joining us or learning more about our research, we encourage you to explore the exciting work we’re doing.

{% include section.html %}

{% capture content %}

{% include figure.html image="team/photos/dinner.jpg" %}
{% include figure.html image="team/photos/teachers-day.png" %}
{% include figure.html image="team/photos/group-meeting.jpg" %}
{% include figure.html image="team/photos/teachers.jpg" %}
{% include figure.html image="team/photos/conference.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}