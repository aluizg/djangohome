# djangohome
Projeto base com melhorias de segurança, SSO, CRUD e customizaçao no seção Admin

# Atualização do gitignore
Adicione as seguintes linhas ao seu arquivo `.gitignore` para evitar o versionamento de arquivos
- relacionados a ambientes virtuais e arquivos compilados:
```
.idea/
.vscode/
```

## Pacotes a serem instalados
Para executar este projeto, você precisará instalar os seguintes pacotes Python:
- Django
- Social-Auth-App-Django
- Bootstrap5

```commandline
pip install django social-auth-app-django django-bootstrap5
```

## Criando o Projeto Django e Aplicação
Para criar um novo projeto Django, execute o seguinte comando no terminal:
```commandline
django-admin startproject djangohome .
```

Em seguida, crie uma nova aplicação dentro do projeto:
```commandline
django-admin startapp core
```

## Configurações de Segurança no Django

Por padrão o Django vem com várias configurações de segurança, mas é importante garantir que algumas delas estejam corretamente configuradas no arquivo `settings.py` do seu projeto.

Principais recursos de segurança do Django:
+ Cross-Site Scripting (XSS) Protection
+ Cross-Site Request Forgery (CSRF) Protection
+ SQL Injection Protection
+ Suporte para HTTPS e TLS
+ Armaenamento Seguro de Senhas

No arquivo `settings.py`, certifique-se de que as seguintes configurações estejam definidas:

```python
# Habilitar proteção contra XSS
SECURE_BROWSER_XSS_FILTER = True

# Habilitar proteção contra CSRF
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Habilitar HTTPS
SECURE_SSL_REDIRECT = not DEBUG

# Configurar HSTS
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configurar armazenamento seguro de senhas
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Configurar Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://stackpath.bootstrapcdn.com')
CSP_SCRIPT_SRC = ("'self'", 'https://code.jquery.com')

# Adicionar middleware de segurança
MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    ...
]

# Configurar cabeçalhos de segurança adicionais
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'

# Configurar políticas de cookies
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Configurar políticas de redirecionamento
SECURE_REDIRECT_EXEMPT = []

# Configurar políticas de autenticação
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Configurar X-Frame-Options para prevenir clickjacking
X_FRAME_OPTIONS = 'DENY'

```

## Configuração do Bootstrap5
No arquivo `settings.py`, adicione `'django_bootstrap5'` à lista de `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_bootstrap5',
    ...
]
```

## Configuração do Social Auth para SSO
No arquivo `settings.py`, adicione as seguintes configurações para habilitar o Social Auth:
```python
INSTALLED_APPS = [
    ...
    'social_django',
    ...
]
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
MIDDLEWARE = [
    ...
    'social_django.middleware.SocialAuthExceptionMiddleware',
    ...
]
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                ...
            ],
        },
    },
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'sua-chave-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'seu-segredo-client'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
```

## Formatação de valores numerico no settings.py
No arquivo `settings.py`, adicione a seguinte configuração para formatação de valores numéricos:
```python
INSTALLED_APPS = [
    ...
    'django.contrib.humanize',
    ...
]
```

## Configuracao para não criar novo usuario ao logar via SSO
No arquivo `settings.py`, adicione a seguinte configuração para evitar a criação automática de novos usuários ao fazer login via SSO:
```python
SOCIAL_RAISE_EXCEPTIONS = False
````

## Definição do diretorio de templates
No arquivo `settings.py`, defina o diretório de templates para a aplicação:
```python
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],
        ...
    },
]
``` 

## Outras definições no settings.py
No arquivo `settings.py`, adicione as seguintes definições adicionais:
```python
# Definir idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# definicao de arquivos staticos
# Atencao projetos anteriores o apontamento da variavel STATIC_URL estava incompleto
STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Modificação da Rota do Admin
Alteração da rota padrão do admin para melhorar a segurança no arquivo `urls.py`:
```python
urlpatterns = [
path('controle/', admin.site.urls),
...
]
```

## Criar o arquivo de requirements.txt
Para facilitar a instalação das dependências do projeto, crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:
```commandline
pip freeze > requirements.txt
```

## Personalização do Django Admin
Para personalizar a interface do Django Admin, você pode criar um arquivo `admin.py` dentro da sua aplicação `core` e registrar seus modelos personalizados.

## URL para CDN do Bootstrap5
Você pode usar a seguinte URL para incluir o Bootstrap5 via CDN em seus templates HTML:
```html
<!--Bootstrap icons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<!--Bootstrap CSS and JS-->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
```

## CRUD utilizando Class-Based Views
Para implementar operações CRUD (Create, Read, Update, Delete) utilizando Class-Based Views no Django, você pode seguir o exemplo abaixo:

