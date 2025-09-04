import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    
# 10 testes

def test_question_has_default_points():
    question = Question(title='Default points question')
    assert question.points == 1

def test_question_can_have_multiple_choices():
    question = Question(title='What is 2+2?')
    question.add_choice('3', False)
    question.add_choice('4', True)
    assert len(question.choices) == 2
    assert any(c.is_correct for c in question.choices)

def test_choice_text_cannot_be_empty():
    question = Question(title='Pick an option')
    with pytest.raises(Exception):
        question.add_choice('', True)

def test_points_must_be_within_valid_range():
    with pytest.raises(Exception):
        Question(title='Negative points', points=-1)
    with pytest.raises(Exception):
        Question(title='Too many points', points=101)

def test_questions_have_unique_ids():
    q1 = Question(title='Question 1')
    q2 = Question(title='Question 2')
    assert q1.id != q2.id

def test_choice_ids_increment_correctly():
    question = Question(title='Increment test')
    c1 = question.add_choice('Option A')
    c2 = question.add_choice('Option B')
    assert c2.id == c1.id + 1

def test_remove_choice_by_id_removes_correctly():
    question = Question(title='Remove choice test')
    choice = question.add_choice('Option A')
    question.remove_choice_by_id(choice.id)
    assert len(question.choices) == 0

def test_set_correct_choices_marks_only_selected():
    question = Question(title='Set correct test')
    c1 = question.add_choice('Option A')
    c2 = question.add_choice('Option B')
    question.set_correct_choices([c1.id])
    assert c1.is_correct
    assert not c2.is_correct

def test_correct_selected_choices_respects_max_selections():
    question = Question(title='Max selection test', max_selections=1)
    c1 = question.add_choice('Option A', True)
    c2 = question.add_choice('Option B', True)
    with pytest.raises(Exception):
        question.correct_selected_choices([c1.id, c2.id])

def test_remove_all_choices_clears_all():
    question = Question(title='Clear all choices test')
    question.add_choice('Option A')
    question.add_choice('Option B')
    question.remove_all_choices()
    assert len(question.choices) == 0

