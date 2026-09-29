---
permalink: /
author_profile: true
stylesheets:
  - /assets/css/home.css
redirect_from:
  - /about/
  - /about.html
---
{% assign home = site.data.homepage %}
<div id="about">
  <h1 class="main-heading">Hi there! Welcome to my Homepage!</h1>
  {% if site.profile_draft %}<p class="draft-notice">Profile in preparation · 个人资料待补充</p>{% endif %}
  {{ home.intro | markdownify }}
  {% if home.research_interests.size > 0 %}<p><strong>Research interests:</strong> {{ home.research_interests | join: ' · ' | escape }}</p>{% endif %}
  {% if home.cv != '' %}<p><a href="{{ home.cv | relative_url }}">Download my CV</a></p>{% endif %}
</div>

{% if home.news.size > 0 %}
<h2 id="news">News</h2>
<div class="news-box"><ul class="news-list">
  {% for item in home.news %}<li><span class="news-date">{{ item.date | escape }}</span> {{ item.text | markdownify }}</li>{% else %}<li class="empty-copy">Updates coming soon.</li>{% endfor %}
</ul></div>
{% endif %}

<h2 id="experience">Experience</h2>
<div class="experience-container">
  {% for item in home.experience %}
  <div class="experience-card">
    {% if item.logo %}<img src="{{ item.logo | relative_url }}" alt="{{ item.institution | escape }}" class="experience-logo" loading="lazy">{% endif %}
    <div class="experience-info"><strong>{{ item.institution | escape }}</strong><br><em>{{ item.date | escape }}</em><br>{{ item.role | escape }}<div class="experience-description">{{ item.description | markdownify }}</div></div>
  </div>
  {% else %}<div class="experience-card empty-copy">Education and research experience will be added here.</div>{% endfor %}
</div>

{% if home.publications.size > 0 %}
<h2 id="publications">Publications</h2>
<div class="pub-button-container" role="group" aria-label="Publication filter">
  <button type="button" class="pub-button active" aria-pressed="true" data-filter="selected">Selected publications</button>
  <button type="button" class="pub-button" aria-pressed="false" data-filter="all">All publications</button>
</div>
<div class="publication-list">
  {% for item in home.publications %}
  <article class="publication-card" data-selected="{{ item.selected }}">
    {% if item.image %}<img class="publication-image" src="{{ item.image | relative_url }}" alt="{{ item.title | escape }}" loading="lazy">{% endif %}
    <div class="publication-details"><h3>{{ item.title | escape }}</h3><div class="publication-authors">{{ item.authors | escape }}</div><p>{{ item.description | escape }}</p><strong class="publication-venue">{{ item.venue | escape }}</strong>
    <div class="publication-links">{% if item.paper %}<a href="{{ item.paper | escape }}">[Paper]</a>{% endif %} {% if item.code %}<a href="{{ item.code | escape }}">[Code]</a>{% endif %} {% if item.project %}<a href="{{ item.project | escape }}">[Project]</a>{% endif %}</div></div>
  </article>{% endfor %}
</div>
<p class="empty-copy" id="no-selected-publications" hidden>No selected publications yet. Choose “All publications” to see the full list.</p>
{% endif %}

{% if home.projects.size > 0 %}
<h2 id="projects">Projects</h2>
{% for item in home.projects %}
<article class="project-card"><div class="project-details"><h3>{% if item.url %}<a href="{{ item.url | escape }}">{{ item.title | escape }}</a>{% else %}{{ item.title | escape }}{% endif %}</h3>{{ item.description | markdownify }}</div></article>
{% endfor %}
{% endif %}

{% for section in home %}{% if section[0] == 'awards' or section[0] == 'services' or section[0] == 'talks' %}{% if section[1].size > 0 %}
<h2 id="{{ section[0] }}">{{ section[0] | capitalize }}</h2><ul>{% for item in section[1] %}<li>{{ item | markdownify }}</li>{% endfor %}</ul>
{% endif %}{% endif %}{% endfor %}
<script src="{{ '/assets/js/homepage.js' | relative_url }}" defer></script>
