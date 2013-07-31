from behave import *
import urllib2


@given('the {fn} file')
def step_impl(context, fn):
    context.fn = fn


@when('we read the file')
def step_impl(context):
    with file(context.fn) as f:
        fields = [line.strip('* \n') for line in f.readlines()
                  if line.startswith('* ')]
    context.fields = dict(f.split(':') for f in fields)


@then("we see the student's {key}")
def step_impl(context, key):
    pass


@then("the student's {key}")
def step_impl(context, key):
    d = context.fields
    assert key in d, key
    assert len(d[key].strip())


@then('not my default information')
def step_impl(context):
    d = context.fields
    assert 'Peter Parente' != d['Name'].strip()
    assert 'parente@cs.unc.edu' != d['Email'].strip()
    assert 'parente' != d['GitHub Username'].strip()
    assert 'peter_parente' != d['BitBucket Username'].strip()

@then('we find the {field} on {site}')
def step_impl(context, field, site):
    username = context.fields[field].strip()
    c = urllib2.urlopen('http://%s/%s' % (site, username))
    print c.getcode()
    c.close()
