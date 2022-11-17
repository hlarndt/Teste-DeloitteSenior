### **ALUNOS API (Python & Django + DRF & Swagger)**

**PARA INSTALAR USE:**
1. $ python3 -m venv venv
2. $ source venv/bin/activate
   
Verificar se a virtualenv está funcional
(no inicio da linha de comando deve ter (env))

3. (env) $ pip install -r requirements.txt
4. (env) $ python manage.py migrate && python manage.py runserver 0.0.0.0:8888
----------------------------------------------------

**OU:**

$ docker-compose up --build

----------------------------------------------------

**TO EXECUTE TEST CASES:**
(env) $ python manage.py test

----------------------------------------------------

**ENDPOINTS OF APP:**
1. http://0.0.0.0:8888/docs/ - swagger API
2. http://0.0.0.0:8888/alunos/ - Django REST Framework API de Alunos 
3. http://0.0.0.0:8888/openapi/ - geração automática OPENAPI YAML JSONSchema
