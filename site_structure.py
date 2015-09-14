from pages import Page, Pages
import loremipsum
from random import random

def random_image(width, height=None):
  if not height:
    height=width
  scale = random() + 1
  height = int(height*scale)
  width = int(width*scale)
  
  return "http://lorempixel.com/%s/%s" % (width, height)
  

pages = Pages([
  Page('About', 'demo.html', context={'image': random_image(590,288)}),
  Page('Page Layouts', 'layouts/overview.html', children=[
    Page('Subsection with navigation', 'layouts/subnav.html'),
    Page('Subsection without navigation', 'layouts/subnonav.html'),
    Page('Subsection without right column', 'layouts/subnocol.html'),
  ]),
  Page('Core Elements', children=[
    Page('Typography', 'core_elements/typography.html'),
    Page('Links and Buttons', 'core_elements/links_and_buttons.html'),
    Page('Forms', 'core_elements/forms.html'),
    Page('Lists', 'core_elements/lists.html'),
  ]),
  Page('In Page Components', children=[
    Page('Navigation', children=[
      Page('Tabs', 'components/inpage/navigation/tabs.html'),
      Page('Pills', 'components/inpage/navigation/pills.html'),
      Page('Pagination', 'components/inpage/navigation/pagination.html'),
      Page('Search', 'components/inpage/navigation/search.html'),
    ]),
    Page('Content', children=[
      Page('Tables', 'components/inpage/content/tables.html'),
      Page('Alerts', 'components/inpage/content/alerts.html'),
      Page('Date/Time Picker', 'components/inpage/content/datetimepicker.html'),
    ]),
    Page('Teasers', 'components/teasers/examples.html'),
  ]),
])

front_page = Page(
  'Home',
  'layouts/frontpage_example.html',
  context={
    'CAROUSEL': [
      (random_image(885, 432), '/', ' '.join(loremipsum.get_sentences(1))),
      (random_image(885, 432), '/', ' '.join(loremipsum.get_sentences(2))),
      (random_image(885, 432), None, ' '.join(loremipsum.get_sentences(1))),
    ]
  },
  front_page=True,
)