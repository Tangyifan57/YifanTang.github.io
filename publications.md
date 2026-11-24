---
layout: page
title: Publications
permalink: /publications/
---

# Publications

Research articles in battery materials, electrode interfaces, electrochemical energy storage, and electrocatalysis. See also [Google Scholar]({{ site.owner.scholar }}) and [ResearchGate]({{ site.owner.researchgate }}).

## Peer-Reviewed Articles

{% assign published_articles = site.data.publications | where: 'status', 'published' %}
<p class="publication-summary">{{ published_articles.size }} published journal articles. First-author, co-first-author, and co-author contributions are identified below.</p>

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
