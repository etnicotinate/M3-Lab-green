---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

Our M3-Lab (Multiscale Modeling and Machine Learning Lab) led by Prof. Wang Shuo is located at the School of Materials Science and engineering at the Eastern Institute of Technology, Ningbo (EIT), Ningbo City, Zhejiang Province, China. We are on the F2 of Chemistry Materials Building.

{%
  include button.html
  type="email"
  text="shuowang@eitech.edu.cn"
  link="shuowang@eitech.edu.cn"
%}
{%
  include button.html
  type="address"
  text="Jiaochuan Street, 2911 Haijiang Avenue, Zhenhai District, Ningbo City (315200)"
  tooltip="宁波市镇海区蛟川街道 海江大道2911号，邮编315200"
  link="https://surl.amap.com/12T9xuyS0oQ"
%}
<!-- 宁波市镇海区蛟川街道 海江大道2911号 邮政编码 315200 -->
<!-- {%
  include button.html
  type="phone"
  text="(86) \*\*\*-\*\*\*"
  link="+86-\*\*\*-\*\*\*-\*\*\*\*"
%} -->

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/EIT/EIT_1.jpg"
  caption="EIT Campus"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/EIT/EIT_2.jpg"
  caption="EIT Campus"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col2 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% capture col3 %}
Lorem ipsum dolor sit amet  
consectetur adipiscing elit  
sed do eiusmod tempor
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
