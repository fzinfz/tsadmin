# Execute:
# ./manage.py shell < ./scripts/init_data_post.shell.py

from connection.models import Post
from django.core.exceptions import ObjectDoesNotExist
import requests

url_post_body_2 = "https://raw.githubusercontent.com/wiki/fzinfz/tsadmin/template_shadowsocks.md"

# when updating, only title/slug/body will be modified by default
data = [
    {
        'id': 1,
        'data': {
            'title': "欢迎",
            'slug': "welcome",
            'body': "### 请[登录](/accounts/login/)",
            'public': True
        }
    },
    {
        'id': 2,
        'data': {
            'title': "使用说明",
            'slug': "instruction",
            'body': requests.get(url_post_body_2).content,
            'public': False
        }
    }
]

defaults = {
    "status": "PUBLISHED",
    "list": True,
    "topped": True
}

for d in data:
    if d['id'] == 2:
        print("adding/updating post 2 from: " + url_post_body_2)

    try:
        p = Post.objects.get(id=d['id'])
        print('updating post %s: %s' % (str(p.id), p.slug), end=" ==> ")
        p.title = d['data']['title']
        p.slug = d['data']['slug']
        p.body = d['data']['body']
        print(p.slug)
        p.save()
    except ObjectDoesNotExist:
        print('adding post %s: %s' % (str(d['id']), d['data']['title']), end=" ==> ")
        Post.objects.create(id=d['id'], **d['data'], **defaults)
