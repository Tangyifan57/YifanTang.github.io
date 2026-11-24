---
layout: page
title: Publications
permalink: /publications/
---

# Publications

Research articles in electrode materials, interfacial chemistry, and alkali-ion compensation. See also my [Google Scholar profile]({{ site.owner.scholar }}).

## Peer-Reviewed Articles

{% include publication-list.html %}

## Manuscript Under Review

{% for paper in site.data.publications %}
{% if paper.status == 'under-review' %}
<div class="manuscript">
<strong>{{ paper.title }}</strong><br>
{{ paper.authors | escape | replace: 'Y. Tang', '<strong>Y. Tang</strong>' }}<br>
<em>{{ paper.journal }}</em> · {{ paper.year }} · <span class="review-label">Under review</span>
</div>
{% endif %}
{% endfor %}

<p class="author-note">Manuscript status follows the CV supplied on 24 November 2026. This section is separate from peer-reviewed publications.</p>
