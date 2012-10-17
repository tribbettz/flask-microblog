import os

# path to project and database directories
basedir	= os.path.abspath(os.path.dirname(__file__))
dbdir	= basedir + '/db'

# database and migration repository locations
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(dbdir, 'db_repoitory')

# cross site request forgery prevention enabled
CSRF_ENABLED = True
SECRET_KEY = '(@\xbeq\x96\x82\xda\x86t\x91\xa0\x16M\xd8a\x1c\xdf\x98\xb5*h#\xc30'

# dictionary of OpenID providers as options for logon
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# mail server settings
MAIL_SERVER		= 'localhost'
MAIL_PORT		= 3000
MAIL_USERNAME	= None
MAIL_PASSWORD	= None

# administrator list
ADMINS = ['tribbettz.dev@gmail.com']

# pagination settings
POSTS_PER_PAGE = 3