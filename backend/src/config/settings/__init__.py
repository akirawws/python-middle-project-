# инициализация файлов 
# редактирование файла с определенным окржением для разработки продакшена и тестирования 

# cat > src/config/settings/__init__.py << 'EOF'

import os 
# определяем окружение 
environment = os.environ.get("DJANGO_ENV", "development")

if environment == "production":
    from .production import * 
elif environment == "testing":
    from .testing import * 
else: 
    from .development import *  