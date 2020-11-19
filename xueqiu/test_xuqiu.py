from xueqiu.main_page import Main_page


class Testxuqiu:
    def test_main(self):
        Main_page().goto_market().goto_serach().serach()

    # def serach(self):
    #     self.main.goto_table().goto_serach().mark()
    # def teardown_class(self):
    #     self