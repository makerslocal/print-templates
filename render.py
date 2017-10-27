#!/usr/bin/env python
from __future__ import print_function
import jinja2
t = jinja2.Template("Hello {{name}}!")
print(t.render(name="Test"))
