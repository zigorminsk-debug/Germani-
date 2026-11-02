# Германия ближе

Небольшой статический сайт на HTML5 с интерактивной картой Германии. На карте используется HTML `<map>`: Берлин выделен круглой областью (`circle`), Дрезден и Франкфурт-на-Майне — многоугольниками (`poly`). Размеры областей автоматически подстраиваются под ширину карты. Те же страницы городов доступны по ссылкам в карточках.

## Запуск

Откройте `index.html` в браузере или запустите локальный сервер, например `python3 -m http.server 8000`. Сборка и зависимости не требуются.

## GitHub Actions и просмотр

Workflow `.github/workflows/pages.yml` проверяет сайт и сохраняет готовые файлы в артефакте **germany-site**. В сводке запуска также есть ссылка на просмотр через сторонний сервис raw.githack.com; он может показать страницу подтверждения. Это временный просмотр, а не GitHub Pages, и его доступность зависит от стороннего сервиса. Ссылка привязана к конкретному коммиту.

Если включить **Settings → Pages → Build and deployment → GitHub Actions**, тот же workflow дополнительно опубликует сайт на GitHub Pages. При включённой защите окружения `github-pages` публикация может требовать подтверждения. Workflow запускается при отправке изменений в `main` или рабочую ветку и вручную.

## Источники

- Контуры федеральных земель: [Click That Hood](https://github.com/codeforgermany/click_that_hood/blob/main/public/data/germany.geojson).
- Фотографии: [Берлин — Pexels](https://www.pexels.com/search/brandenburg%20gate/), [Дрезден — Free Walking Tour](https://freewalkingtour.com/dresden/dresden-old-town-germany/), [Франкфурт — Pexels](https://pexels.com/photo/frankfurt-skyscrapers-behind-river-in-winter-20101875).
