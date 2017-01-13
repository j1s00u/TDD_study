from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
# unittest.TestCase를 상속해서 테스트를 클래스 형태로
    # setup,tearDown은 테스트 시작 전과 후 실행
    def setUp(self):
        binary = 'C:\\chromedriver_win32\\chromedriver.exe'
        self.browser = webdriver.Chrome(binary)
        self.browser.implicitly_wait(3)
        # 암묵적 대기 기능

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    # 테스트 메인 코드
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')
        # 강제적으로 테스트 실패를 발생시켜 에러 메시지 출력, 테스트의 끝을 의미

        # 그녀는 바로 작업을 추가하기로 한다

        # "공작깃털 사기"라고 텍스트 상자에 입력한다
        # (에디스의 취미는 날치 잡이용 그물을 만드는 것이다)

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 공작깃털 사기" 아이템이 추가된다.

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다
        # 에디스는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 그녀를 위한 특정 URL을 생성해 준다
        # 이때 URL에 대한 설명도 함꼐 제공된다

        # 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다

        # 만족하고 잠자리에 든다
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    #테스트 작성 시에 발생하는 불필요한 리소스 경고를 제거
