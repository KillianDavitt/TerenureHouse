# TerenureHouse
A repo for the Terenure House website

python3 + flask

## Objectives 1.0
- Jobs Interface
- Add new job
- Add name to job
- Data stored in sqlite3 with sqlalchemy
- Updating jobs using ajax
- No auth

## Deployment
To deploy:

```bash
git clone https://www.github.com/KillianDavitt/TerenureHouse.git
cd TerenureHouse

./install.sh

sudo cp ./deploy/terenure.service /etc/systemd/system/terenure.service

sudo systemctl enable terenure.service

sudo cp ./deploy/terenure /etc/nginx/sites-enabled/terenure

sudo systemctl restart nginx

sudo systemctl start terenure
```
