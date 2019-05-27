import allure,pytest

class Test001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤")
    def test_001(self):
        print("--->test_001")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤")
    def test_002(self):
        allure.attach("用户名", "张三")
        allure.attach("密码", "123456")
        print("--->test_002")
        assert True