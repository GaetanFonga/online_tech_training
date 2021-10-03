from xmlrpc import client

url = 'https://gaetanfonga-online-tech-training-14-0-dev-academy-3331986.dev.odoo.com'
db = 'gaetanfonga-online-tech-training-14-0-dev-academy-3331986'
username = 'admin'
password = 'Admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password, 'academy.session', 'check_access_rights',
                                ['write', {'raise_exception': False}])

print(model_access)

courses = models.execute_kw(db, uid, password, 'academy.course', 'search_read',
                           [[['level', 'in', ['intermediate', 'beginner']]]])

print(courses)

course = models.execute_kw(db, uid, password, 'academy.course', 'search',
                          [[['name', '=', 'Accounting 200']]])

print(course)

session_fields = models.execute_kw(db, uid, password, 'academy.session', 'fields_get', [], {'attribute': ['string', 'type', 'required']})

print(session_fields)

new_session = models.execute(db, uid, password, 'academy.session', 'create',
                            [
                                {
                                    'course_id': course[0],
                                    'state': 'open',
                                    'duration': 5,
                                }
                            ])
print(new_ession)