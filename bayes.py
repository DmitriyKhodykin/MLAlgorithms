# -*- coding: utf-8 -*-
# python 3.7


def bayes_test_proba(proba_sick: float, proba_test: float) -> float:
    """Возвращает вероятность того, что если у человека положительный
    тест на заболевание, то он действительно болен
    
    proba_sick - доля болеющих заболеванием по популяции
    proba_test - точность теста (например, 0.98)
    """
    
    # Доля позитивных тестов у здоровых
    positive_health = (1 - proba_sick) * (1 - proba_test)
    # Доля позитивных тестов у заболевших
    positive_sick = proba_sick * proba_test
    # Всего позитивных срабатываний теста
    positive = positive_health + positive_sick
    # Результирующая вероятность
    proba = positive_sick * proba_sick / positive
    
    return round(proba * 100, 1)

if __name__ == "__main__":
    proba_sick = 0.5
    proba_test = 0.4
    proba_covid = bayes_test_proba(proba_sick, proba_test)
    print(f'Тест COVID положительный, вероятность болезни: {proba_covid} %')
