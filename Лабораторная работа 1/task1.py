from typing import Union
import doctest

class QuestionList:
    """
    Документация на класс.
    Класс описывает модель списка вопросов к экзамену.
    """

    def __init__(self, question_amount: int, question_learnt: int):
        """
        Инициализация экземпляра класса.

        :param question_amount: Количество вопросов, которые нужно выучить.
        :param question_learnt: Количество выученных вопросов.

        Пример:
        >>> question_list = QuestionList(100, 0)  # Инициализация экземпляра класса
        """
        if not isinstance(question_amount, int):
            raise TypeError("Количество вопросов должно быть целым числом (тип int)")
        if not question_amount > 0:
            raise ValueError("Количество вопросов должно быть положительным числом")
        self.question_amount = question_amount

        if not isinstance(question_learnt, int):
            raise TypeError("Количество выученных вопросов должно быть целым числом (тип int)")
        if question_learnt < 0:
            raise ValueError("Количество выученных вопросов должно быть положительным числом")
        if question_learnt > question_amount:
            raise ValueError("Количество выученных вопросов не может быть больше количества вопросов")
        self.question_learnt = question_learnt

    def add_learnt_questions(self, added_learnt_questions: int) -> None:
        """
        Увеличение числа выученных вопросов.

        :param added_learnt_questions: Количество добавленных выученных вопросов.
        :raises TypeError: Если количество вопросов не является целым числом.
        :raises ValueError: Если суммарное число выученных вопросов превышает общее количество вопросов.
        """
        if not isinstance(added_learnt_questions, int):
            raise TypeError("Количество добавленных вопросов должно быть целым числом (тип int)")
        if self.question_learnt + added_learnt_questions > self.question_amount:
            raise ValueError("Суммарное число выученных вопросов превышает общее количество вопросов")
        self.question_learnt += added_learnt_questions

    def is_ready(self) -> bool:
        """
        Проверка, все ли вопросы выучены.

        :return: Возвращает True, если все вопросы выучены, иначе False.
        """
        return self.question_learnt == self.question_amount

    def percentage_learnt(self) -> float:
        """
        Определяет процент выученных вопросов от общего числа вопросов.

        :return: Возвращает процент выученных вопросов.
        """
        return (self.question_learnt / self.question_amount) * 100


class FlashDisk:
    """
    Документация на класс.
    Класс описывает модель накопителя.
    """

    def __init__(self, capacity_memory: Union[int, float], free_memory: Union[int, float], service_life: int):
        """
        Инициализация экземпляра класса.

        :param capacity_memory: Объем памяти накопителя в ГБ.
        :param free_memory: Свободный объем памяти в ГБ.
        :param service_life: Гарантийный срок службы накопителя в месяцах.

        Пример:
        >>> flash_disk = FlashDisk(100, 100, 12)  # Инициализация экземпляра класса
        """
        if not isinstance(capacity_memory, (int, float)):
            raise TypeError("Объём памяти должен быть числом (тип int или float)")
        if not capacity_memory > 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.capacity_memory = capacity_memory

        if not isinstance(free_memory, (int, float)):
            raise TypeError("Свободный объём памяти должен быть числом (тип int или float)")
        if free_memory < 0:
            raise ValueError("Свободный объем памяти должен быть положительным числом или 0")
        if free_memory > capacity_memory:
            raise ValueError("Свободный объем памяти не может быть больше объема памяти накопителя")
        self.free_memory = free_memory

        if not isinstance(service_life, int):
            raise TypeError("Гарантийный срок службы должен быть целым числом (тип int)")
        if not service_life > 0:
            raise ValueError("Гарантийный срок службы должен быть положительным числом")
        self.service_life = service_life

    def add_file(self, add_file: Union[int, float]) -> None:
        """
        Добавление файла на накопитель.

        :param add_file: Размер файла для добавления.
        :raises TypeError: Если размер файла не является числом (тип int или float).
        :raises ValueError: Если размер файла превышает свободный объём памяти.
        """
        if not isinstance(add_file, (int, float)):
            raise TypeError("Размер файла должен быть числом (тип int или float)")
        if add_file > self.free_memory:
            raise ValueError("Размер файла превышает свободный объём памяти")
        self.free_memory -= add_file

    def how_many(self, file_weight: Union[int, float]) -> int:
        """
        Определяет, сколько файлов заданного размера можно записать на накопитель.

        :param file_weight: Размер файла для записи.
        :return: Возвращает целое количество файлов, которые можно записать в свободную память.
        :raises TypeError: Если размер файла не является числом (тип int или float).
        """
        if not isinstance(file_weight, (int, float)):
            raise TypeError("Размер файла должен быть числом (тип int или float)")
        return int(self.free_memory // file_weight)


class Concrete:
    """
    Документация на класс.
    Класс основной модели бетона.
    """

    def __init__(self, cement_strength: int, cement_water_proportion: float):
        """
        Инициализация экземпляра класса.

        :param cement_strength: Марка цемента по прочности.
        :param cement_water_proportion: Цементно-водное соотношение.

        Пример:
        >>> concrete = Concrete(300, 2.5)  # Инициализация экземпляра класса
        """
        if not isinstance(cement_strength, int):
            raise TypeError("Марка цемента должна быть целым числом (тип int)")
        if not cement_strength > 0:
            raise ValueError("Марка цемента должна быть положительным числом")
        self.cement_strength = cement_strength

        if not isinstance(cement_water_proportion, float):
            raise TypeError("Цементно-водное соотношение должно быть вещественным числом (тип float)")
        if not cement_water_proportion > 0:
            raise ValueError("Цементно-водное соотношение должно быть положительным числом")
        self.cement_water_proportion = cement_water_proportion

    def stamp(self, aggregate_type: float) -> int:
        """
        Определение нормы бетона по прочности.

        :param aggregate_type: Коэффициент, характеризующий количество и качество заполнителей.
        :return: Возвращает норму бетона по прочности.
        :raises TypeError: Если коэффициент заполнителя имеет неверный тип.
        """
        if not isinstance(aggregate_type, float):
            raise TypeError("Коэффициент заполнителя должен быть вещественным числом (тип float)")
        # Логика расчета нормы бетона по прочности
        return int(self.cement_strength * aggregate_type)

    def strength_n(self, day_hardening: int) -> float:
        """
        Определение прочности бетона на данный день твердения.

        :param day_hardening: День твердения.
        :return: Возвращает прочность бетона.
        :raises TypeError: Если день твердения имеет неверный тип.
        :raises ValueError: Если день твердения больше 28.
        """
        if not isinstance(day_hardening, int):
            raise TypeError("День твердения должен быть целым числом (тип int)")
        if day_hardening > 28:
            raise ValueError("День твердения не может быть больше 28")
        # Логика расчета прочности бетона
        return self.cement_strength * (day_hardening / 28)


if __name__ == "__main__":
    # Проверка работоспособности экземпляров класса с помощью doctest
    doctest.testmod()