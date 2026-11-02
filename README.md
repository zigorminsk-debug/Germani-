# Германия ближе

Небольшой статический сайт на HTML5 с интерактивной картой Германии. На карте используется HTML `<map>`: Берлин выделен круглой областью (`circle`), Дрезден и Франкфурт-на-Майне — многоугольниками (`poly`). Размеры областей автоматически подстраиваются под ширину карты. Те же страницы городов доступны по ссылкам в карточках.

## Запуск

Откройте `index.html` в браузере или запустите локальный сервер, например `python3 -m http.server 8000`. Сборка и зависимости не требуются.

## Публикация

Workflow `.github/workflows/pages.yml` публикует сайт через GitHub Actions и GitHub Pages при отправке изменений в `main` или в рабочую ветку, а также вручную. В настройках репозитория **Settings → Pages → Build and deployment** необходимо выбрать источник **GitHub Actions**. При включённой защите окружения `github-pages` запуск может требовать подтверждения.

## Источники

- Контуры федеральных земель: [Click That Hood](https://github.com/codeforgermany/click_that_hood/blob/main/public/data/germany.geojson).
- Фотографии: [Берлин — Pexels](https://www.pexels.com/search/brandenburg%20gate/), [Дрезден — Free Walking Tour](https://freewalkingtour.com/dresden/dresden-old-town-germany/), [Франкфурт — Pexels](https://pexels.com/photo/frankfurt-skyscrapers-behind-river-in-winter-20101875).
