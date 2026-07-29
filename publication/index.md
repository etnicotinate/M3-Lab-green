---
title: Publication
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}Publication

<style>
  .publication-intro {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin: 8px 0 14px;
  }

  .publication-legend {
    margin: 0;
    line-height: 1.35;
  }

  .publication-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }

  .publication-actions .button {
    margin: 0;
  }
</style>

<div class="publication-intro">
  <p class="publication-legend">
    <strong>#: group members, *: corresponding author, †: co-first author</strong>
  </p>

  <div class="publication-actions">
    {% include button.html
      icon="fa-brands fa-google"
      text="More on Google Scholar"
      link="https://scholar.google.com/citations?user=DN3xCtoAAAAJ&hl=en"
    %}

    {% include button.html
      icon="fa-brands fa-orcid"
      text="More on ORCID"
      link="https://orcid.org/0000-0002-7907-9676"
    %}
  </div>
</div>

## All

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %}

<!-- 
## Highlighted

{% include citation.html lookup="Open collaborative writing with Manubot" style="rich" %}

{% include section.html %} -->
