from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
#home_page는 곧 작성하게 될 뷰 함수로 HTML을 반환한다. 
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        #resolve는 URL을 해석해서 일치하는 뷰 함수를 찾는다.
        #여기서는 '/'가 호출될 때 resolve를 실행해서 home_page라는 함수를 호출한다.
        self.assertEqual(found.func,home_page)
