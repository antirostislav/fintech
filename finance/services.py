from models import *


def get_expenses(user_uid: int) -> list[Expense]:
    """
    Получить список расходов пользователя по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :return: Список расходов пользователя
    :rtype: list[Expense]
    """
    pass


def add_expense(user_uid: int, expense_title: str, expense_datetime: str, expense_value: int) -> bool:
    """
    Добавить расход пользователю по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :param expense_title: Название расхода
    :type expense_title: str
    :param expense_datetime: Дата-время расхода
    :type expense_datetime: str
    :param expense_value: Размер расхода
    :type expense_value: int
    :return: Успешность выполнения
    :rtype bool
    """
    pass


def edit_expense(expense_uid: int, expense_title: str, expense_datetime: str, expense_value: int) -> bool:
    """
    Редактировать расход по его уникальному идентификатору

    :param expense_uid: Уникальный идентификатор расхода
    :type expense_uid: int
    :param expense_title: Название расхода
    :type expense_title: str
    :param expense_datetime: Дата-время расхода
    :type expense_datetime: str
    :param expense_value: Размер расхода
    :type expense_value: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass


def del_expense(expense_uid: int) -> bool:
    """
    Удалить расход

    :param expense_uid: Уникальный идентификатор расхода
    :type expense_uid: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass


def get_incomes(user_uid: int) -> list[Income]:
    """
    Получить список доходов пользователя по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :return: Список доходов пользователя
    :rtype: list[Income]
    """
    pass


def add_income(user_uid: int, income_title: str, income_datetime: str, income_value: int) -> bool:
    """
    Добавить доход пользователю по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :param income_title: Название дохода
    :type income_title: str
    :param income_datetime: Дата-время дохода
    :type income_datetime: str
    :param income_value: Размер дохода
    :type income_value: int
    :return: Успешность выполнения операции
    :rtype bool
    """
    pass


def edit_income(income_uid: int, income_title: str, income_datetime: str, income_value: int) -> bool:
    """
    Редактировать доход по его уникальному идентификатору

    :param income_uid: Уникальный идентификатор доход
    :type income_uid: int
    :param income_title: Название расхода
    :type income_title: str
    :param income_datetime: Дата-время расхода
    :type income_datetime: str
    :param income_value: Размер расхода
    :type income_value: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass


def del_income(income_uid: int) -> bool:
    """
    Удалить доход его уникальному идентификатору

    :param income_uid: Уникальный идентификатор дохода
    :type income_uid: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass


def get_goals(user_uid: int) -> list[Goal]:
    """
    Получить список целей пользователя по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :return: Список целей пользователя
    :rtype: list[Goal]
    """
    pass


def add_goal(user_uid: int, goal_title: str, goal_datetime: str, goal_value: int) -> bool:
    """
    Добавить цель пользователю по его уникальному идентификатору

    :param user_uid: Уникальный идентификатор пользователя
    :type user_uid: int
    :param goal_title: Название цели
    :type goal_title: str
    :param goal_datetime: Дата-время цели
    :type goal_datetime: str
    :param goal_value: Размер цели
    :type goal_value: int
    :return: Успешность выполнения операции
    :rtype bool
    """
    pass


def edit_goal(goal_uid: int, goal_title: str, goal_datetime: str, goal_value: int) -> bool:
    """
    Редактировать расход по его уникальному идентификатору

    :param goal_uid: Уникальный идентификатор цели
    :type goal_uid: int
    :param goal_title: Название цели
    :type goal_title: str
    :param goal_datetime: Дата-время цели
    :type goal_datetime: str
    :param goal_value: Размер цели
    :type goal_value: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass


def del_goal(goal_uid: int) -> bool:
    """
    Удалить цель по её уникальному идентификатору

    :param goal_uid: Уникальный идентификатор цели
    :type goal_uid: int
    :return: Успешность выполнения операции
    :rtype: bool
    """
    pass
