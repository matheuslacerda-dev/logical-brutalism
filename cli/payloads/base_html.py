"""
LOGICAL BRUTALISM :: PAYLOAD :: DJANGO BASE TEMPLATE
The root HTML template for Django projects under LB governance.
Includes Alpine.js (CDN), HTMX (django-htmx), Iosevka typography,
and the Logical Brutalism Core CSS matrix.
"""

BASE_HTML = r"""{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Logical Brutalism{% endblock %} :: Engineering Instance</title>

  <!-- Absolute Typography :: Iosevka Family -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;600;700&family=Iosevka:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Alpine.js :: Parasitic Reactivity Layer -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

  <!-- HTMX :: Server-Driven UI Engine (django-htmx integration) -->
  <script src="https://unpkg.com/htmx.org@1.9.12"></script>

  <!-- Logical Brutalism :: Core Visual Matrix -->
  <link rel="stylesheet" href="{% static 'css/logical-brutalism.css' %}">

  <!-- Tailwind :: Compiled Structural Output -->
  <link rel="stylesheet" href="{% static 'css/output.css' %}">

  {% block extra_head %}{% endblock %}
</head>
<body class="bg-lb-void text-lb-text font-struct"
      hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>

  {% block content %}{% endblock %}

  {% block extra_js %}{% endblock %}
</body>
</html>
"""
