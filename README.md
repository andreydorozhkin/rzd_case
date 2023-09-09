#  Автоматизация процесса разработки способов размещения грузов
Кейсодержатель: ОАО "Российские Железные Дороги"

## Тизер
Мы представляем веб–сервис для автоматизации задач разработки способов размещения и крепления грузов. Наш веб-сервис производит расчет общего центра тяжести, расчет сил, действующих на груз, подбирает реквизит крепления и подготавливает расчетно-пояснительную записку. Наш сервис будет полезен как инженерам, так и руководителем.
Стек решения: Python, FastAPI, NumPy-STL, JavaScript, Vue.js
Уникальностью нашего решения является проработанная микросервисная архитектура, позволяющая легко масштабироваться и расширять систему.
Наша реализация построена через подход с построением 3D модели и последующей генерацией чертежа с созданием проекций на плоскость, что дает возможность последующего редактирования.

## Презентация решения
https://docs.google.com/presentation/d/1GA78EY8Knx7nznW8L4ydVd94qzt8hUuQsbd-AWdUeVQ/edit?usp=sharing

## Cтек технологий
Стек решения: Python, FastAPI, NumPy-STL, JavaScript, Vue.js

![JavaScript](https://github.com/andreydorozhkin/rzd_case/raw/main/docs/logos/js.png?raw=true)
![Vue.js](https://github.com/andreydorozhkin/rzd_case/raw/main/docs/logos/vue.png?raw=true)
![Python](https://github.com/andreydorozhkin/rzd_case/raw/main/docs/logos/python.png?raw=true)
![NumPy](https://github.com/andreydorozhkin/rzd_case/raw/main/docs/logos/numpy.png?raw=true)
![FastApi](https://github.com/andreydorozhkin/rzd_case/blob/main/docs/logos/fastapi.svg?raw=true)

## Ссылка на архитектуру решения
https://excalidraw.com/#room=4e0bb11019a21afe4f85,9fjpkKHFctWsAtTBkCnIWw

## Как запустить проект?
1. Склонировать проект
2. Необходимо чтобы был установлен docker (https://docs.docker.com/engine/install/)
3. Запустить проект командой ``docker compose up``
4. Сервис будет доступен по адресу http://localhost:80
5. Документация бекенда (swagger) доступна по адресу http://localhost:80/docs 