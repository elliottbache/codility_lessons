{{ fullname }}
{{ underline }}

.. automodule:: {{ fullname }}
   :members:
   :undoc-members:
   :show-inheritance:

{% if modules %}
Submodules
----------

.. autosummary::
   :toctree:
   :recursive:

{# Filter out tests subpackages/modules #}
{% for item in modules if ".tests." not in item and not item.endswith(".tests") %}
   {{ item }}
{% endfor %}
{% endif %}
