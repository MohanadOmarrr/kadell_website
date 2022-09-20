"""
ASGI config for kadell_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
>>>>>>> f7b29f26523cd6f744a4ebfbf26661858e117ab9
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kadell_website.settings')

application = get_asgi_application()
<<<<<<< HEAD
=======

>>>>>>> f7b29f26523cd6f744a4ebfbf26661858e117ab9
