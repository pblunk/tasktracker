import pytest
from django.urls import reverse, resolve
from base.views import (
    TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView,
    CustomLoginView, RegisterPage)
from django.contrib.auth.views import (LogoutView)



@pytest.mark.urls('base.urls')
def test_login_url():
    assert reverse('login') == '/login/'
    assert resolve('/login/').view_name == 'login'
    assert resolve('/login/').func.view_class == CustomLoginView

@pytest.mark.urls('base.urls')
def test_logout_url():
    assert reverse('logout') == '/logout/'
    assert resolve('/logout/').view_name == 'logout'
    assert resolve('/logout/').func.view_class == LogoutView

@pytest.mark.urls('base.urls')
def test_register_url():
    assert reverse('register') == '/register/'
    assert resolve('/register/').view_name == 'register'
    assert resolve('/register/').func.view_class == RegisterPage

@pytest.mark.urls('base.urls')
def test_tasks_url():
    assert reverse('tasks') == '/'
    assert resolve('/').view_name == 'tasks'
    assert resolve('/').func.view_class == TaskList

@pytest.mark.urls('base.urls')
def test_task_detail_url():
    assert reverse('task', args=[1]) == '/task/1/'
    assert resolve('/task/1/').view_name == 'task'
    assert resolve('/task/1/').func.view_class == TaskDetail

@pytest.mark.urls('base.urls')
def test_task_create_url():
    assert reverse('task-create') == '/task-create/'
    assert resolve('/task-create/').view_name == 'task-create'
    assert resolve('/task-create/').func.view_class == TaskCreate

@pytest.mark.urls('base.urls')
def test_task_update_url():
    assert reverse('task-update', args=[1]) == '/task-update/1/'
    assert resolve('/task-update/1/').view_name == 'task-update'
    assert resolve('/task-update/1/').func.view_class == TaskUpdate

@pytest.mark.urls('base.urls')
def test_task_delete_url():
    assert reverse('task-delete', args=[1]) == '/task-delete/1/'
    assert resolve('/task-delete/1/').view_name == 'task-delete'
    assert resolve('/task-delete/1/').func.view_class == DeleteView
