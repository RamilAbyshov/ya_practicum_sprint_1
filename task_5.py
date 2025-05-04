class TestCase:

    def __init__(self, steps={}, result=None):
        self.steps = steps
        self.result = result

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
         removed_step = self.steps.pop(step_number, None)
         if removed_step is None:
            print(f"Шаг {step_number} не найден.")

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        test_case_info = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(test_case_info)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 