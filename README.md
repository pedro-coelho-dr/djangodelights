# Tapioca Delights

This is a simple Django web application designed for managing inventory and tracking reports for a Tapioca restaurant. This project serves as the capstone for Codecademy's [Build Python Web Apps with Django](https://www.codecademy.com/learn/paths/build-python-web-apps-with-django) Skill Path. 

## Docker

This application was used for University of Helsinki´s [DevOps with Docker](https://devopswithdocker.com/) course. 

GitHub Repo: [pedro-coelho-dr/devopswithdocker](https://github.com/pedro-coelho-dr/devopswithdocker)

Docker Hub Repo: [pedrocoelhodr/djangodelights](https://hub.docker.com/r/pedrocoelhodr/djangodelights)

```bash
docker run -p 8080:8080 pedrocoelhodr/djangodelights

User and password are: 'admin' and 'password'

## GitHub Actions + Azure

[djangodelights.azurewebsites.net](https://djangodelights.azurewebsites.net)

User and password are: 'devops' and 'docker24'

[Dockerfile](https://github.com/pedro-coelho-dr/djangodelights/blob/a6ac3ef4e40fc9b7cb5e380dbfc3630b587abc99/Dockerfile)
[Settings.py](https://github.com/pedro-coelho-dr/djangodelights/blob/prod/djangodelights/settings.py)
[GitHub Actions](https://github.com/pedro-coelho-dr/djangodelights/blob/prod/.github/workflows/prod_djangodelights.yml)
