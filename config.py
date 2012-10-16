import os
basedir	= os.path.abspath(os.path.dirname(__file__))
dbdir	= basedir + '/db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(dbdir, 'db_repoitory')

CSRF_ENABLED = True
SECRET_KEY = '(@\xbeq\x96\x82\xda\x86t\x91\xa0\x16M\xd8a\x1c\xdf\x98\xb5*h#\xc30'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]