from pytest import mark

@mark.skip
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('Vizio')
])

@mark.skip
@mark.tv
def test_television_turns_on(tv_brand):
    print(f'{tv_brand} turns on as expected')

@mark.tv
def test_televison_turns_on2(tv_model):
    print(f'{tv_model} turns on as expected')

@mark.skip
@mark.tv
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')
