'''
import requests

website = "https://jsonplaceholder.typicode.com/"

def username(username):
    response = requests.get("https://jsonplaceholder.typicode.com/users", params={'username': username})
    return response.json()[0]['id']

def post(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={'userId': user_id})
    return response.json()

def comments(post_id):
    response = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': post_id})
    return response.json()

name = input()
for i in post(username(name)):
    for j in comments(i['id']):
        print(j['email'])
'''

'''
def create_topic(topic_name):
    return {'topic_name':topic_name, 'users_id':[], 'posts':[]}

def subscribe(user_id, topic):
    if user_id not in topic['users_id']:
        topic['users_id'].append(user_id)

def post_feed(topic, feed_id):
    topic['posts'].append(feed_id)
    for us in topic['users_id']:
        print(f"пользователь {users[us]} получил новость {feed_id}")

def users_dict(n):
    users = {}
    for i in range(1, n+1):
        users[i] = 'User%s' % i
    return users

users = users_dict(10)
topic_1 = create_topic('topic_1')
topic_2 = create_topic('topic_2')
topic_3 = create_topic('topic_3')
topic_4 = create_topic('topic_4')

subscribe(1, topic_1)
subscribe(1, topic_2)
subscribe(2, topic_3)
subscribe(4, topic_1)
subscribe(5, topic_2)
subscribe(6, topic_1)
subscribe(5, topic_3)

post_feed(topic_1, 'Новый пост')

'''
