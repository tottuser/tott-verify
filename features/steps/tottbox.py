from behave import *
import os
import subprocess


@given('the {folder} folder')
def step_impl(context, folder):
    context.folder = folder
    assert os.path.isdir(folder)


@when('we list its contents')
def step_impl(context):
    context.files = os.listdir(context.folder)


@then('we see the {fn}')
def step_impl(context, fn):
    assert fn in context.files


@given('we execute {cmd}')
def step_impl(context, cmd):
    context.output = subprocess.check_output([cmd])


@when('we check the assigned ips')
def step_impl(context):
    lines = context.output.split('\n')
    context.addrs = [line.strip() for line in lines if line.strip().startswith('inet addr')]


@then('we see a 192.168.x.x address')
def step_impl(context):
    print context.addrs
    assert any(['192.168' in ip for ip in context.addrs])