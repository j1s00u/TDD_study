from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
#home_page는 곧 작성하게 될 뷰 함수로 HTML을 반환한다.
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        #resolve는 URL을 해석해서 일치하는 뷰 함수를 찾는다.
        #여기서는 '/'가 호출될 때 resolve를 실행해서 home_page라는 함수를 호출한다.
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        #HttpRequest 객체를 생성해서 사용자가 어떤 요청을 브라우저에게 보내는지 확인한다.
        response = home_page(request)
        #home_page뷰에 전달해서 응답을 취득한다. 응답 내용이 특정 속성을 가지고 있는지 확인한다.
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
