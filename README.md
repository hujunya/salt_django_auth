Salt Django Auth
========================
Django project for salt external authentication

Salt doc: [SALT.AUTH.DJANGO](https://docs.saltstack.com/en/latest/ref/auth/all/salt.auth.django.html)

Installation
------------
Deploy this project on the salt master server.

I made some changes in `salt-2016.11` to let django auth can work. you can see [fix_django_auth](https://github.com/hujunya/salt/tree/fix_django_auth).

#### Download
```bash
mkdir -p /opt/projects/
git clone https://github.com/hujunya/salt_django_auth.git /opt/projects/salt_django_auth
```

#### Config Project And Migrate
Add this into `/opt/projects/configs/server.conf`:
```
[global]
env = dev
```
You can config `env = test` or `env = prod`.

Config `SECRET_KEY` and `DATABASES` in `salt_django_auth\settings\dev.py`.

Then install requirements and migrate db:
```bash
cd /opt/projects/salt_django_auth/
pip install -r requirements.txt

python makemigrations
python manage.py migrate
python manage.py collectstatic -c --noinput
```

#### Config Salt

Add this into `/etc/salt/master.d/auth.conf`：
```
django_auth_path: /opt/projects/salt_django_auth/
django_auth_settings: salt_django_auth.settings

external_auth:
  django:
    ^model: django_auth.models.SaltExternalAuthModel
```
Then restart the salt master:
```bash
service salt-master restart
```

#### Config uWSGI and Nginx

```bash
yum -y install nginx uwsgi uwsgi-plugin-python

cp /opt/projects/salt_django_auth/deploy/uwsgi/salt_django_auth.ini /etc/uwsgi.d/
mkdir -p /var/log/uwsgi/
touch /var/log/uwsgi/salt_django_auth.log
sysctl net.core.somaxconn=1024
/usr/sbin/uwsgi /etc/uwsgi.d/salt_django_auth.ini

cp /opt/projects/salt_django_auth/deploy/nginx/salt_django_auth.conf /etc/nginx/conf.d/
service nginx start
```

Add this into `/etc/rc.d/rc.local`:
```bash
/usr/sbin/uwsgi /etc/uwsgi.d/salt_django_auth.ini
```

Then you can access `http://<your_server_ip_or_domainname>:8080/`.

#### Config Permissions

See [SALT.AUTH.DJANGO](https://docs.saltstack.com/en/latest/ref/auth/all/salt.auth.django.html).

If the master is master of master, because mofm can not list minions, the configuration of `minion_or_fn_matcher` will not work.
