---
layout: page
title: Beyond Research
permalink: /life/
description: "A few moments from life beyond the lab."
---

# Beyond Research

A few moments beyond the lab.

<div class="life-gallery">
{% for photo in site.data.life %}
<figure class="life-photo{% if photo.wide %} life-photo--wide{% endif %}">
  <a href="{{ photo.image | relative_url }}" target="_blank" rel="noopener" aria-label="Open photo: {{ photo.caption }}"><img src="{{ photo.image | relative_url }}" alt="{{ photo.alt }}" width="{{ photo.width }}" height="{{ photo.height }}" loading="lazy"></a>
  <figcaption>{{ photo.caption }}</figcaption>
</figure>
{% endfor %}
</div>
