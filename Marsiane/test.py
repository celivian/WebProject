from requests import get, post, delete

print('-------------------------------------------')
print('Проверка получения')
print(get('http://127.0.0.1:8080/api/jobs').json())
print(get('http://127.0.0.1:8080/api/jobs/1').json())
print(get('http://127.0.0.1:8080/api/jobs/213123').json())
print(get('http://127.0.0.1:8080/api/jobs/efwefwe').json())
print('-------------------------------------------')
print('Проверка добавления')
print(post('http://127.0.0.1:8080/api/jobs', json={}).json())
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1, }).json())
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1,
                                                   'job': 'Посдаить дерево',
                                                   'work_size': 9,
                                                   'collaborators': '1, 2, 5',
                                                   'is_finished': True}).json())
print('-------------------------------------------')
print('Проверка удаления')
print(get('http://127.0.0.1:8080/api/jobs').json())
print(delete('http://127.0.0.1:8080/api/jobs/12').json())
print(delete('http://127.0.0.1:8080/api/jobs/12').json())
print(delete('http://127.0.0.1:8080/api/jobs/2342').json())
print(delete('http://127.0.0.1:8080/api/jobs/efefe').json())
print(get('http://127.0.0.1:8080/api/jobs').json())  # проверка что работа пропала
print('-------------------------------------------')
print('Проверка редактирования')
print(get('http://127.0.0.1:8080/api/jobs/13').json())
print(post('http://127.0.0.1:8080/api/jobs/13', json={}).json())
print(post('http://127.0.0.1:8080/api/jobs/13', json={'team_leader': 1, }).json())
print(post('http://127.0.0.1:8080/api/jobs/123123', json={'team_leader': 1,
                                                          'job': 'Сломать дерево1111',
                                                          'work_size': 1,
                                                          'collaborators': '1, 2, 5, 1, 4, 8',
                                                          'is_finished': False}).json())
print(post('http://127.0.0.1:8080/api/jobs/13', json={'team_leader': 1,
                                                      'job': 'Сломать дерево1111',
                                                      'work_size': 1,
                                                      'collaborators': '1, 2, 5, 1, 4, 8',
                                                      'is_finished': False}).json())
print(get('http://127.0.0.1:8080/api/jobs/13').json())  # проверка что работа изменилась
