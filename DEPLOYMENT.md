
* Kindly navigate back to README.md with this link [⬅ Back to README](README.md)

Or back to TESTING.md with [⬅ Back to Testing](testing.md)



# Deployment

The site is deployed with [Heroku](https://www.heroku.com/) which is a cloud platform that lets developers create, deploy, monitor and manage apps.
The deployed site can be found [here](https://voyage-backend-e8a4f1be604a.herokuapp.com/).

* These steps assume that you have set up your settings.py, Procfile, Requirements.txt and got it all ready for the deployment process and you also have a Heroku account and are logged in. 


## Back-end deployment

1. Go to the Heroku app Dashboard.
2. Click the 'Settings' tab.
3. Click 'Reveal Config Vars' and add these Config Vars:
- (KEY)CLOUDINARY_URL: (VALUE) Copy the Cloudinary URL from your env.py file without quotation marks.
- (KEY)SECRET_KEY: (VALUE) Make up a completely new Secret Key that is NOT the same as the one in settings or env - there are many online Secret Key generators you can search for. 
- (KEY)DISABLE_COLLECTSTATIC: (VALUE)1
4. Click the 'Deploy' tab.
5. In the Deployment method section, click "Connect to GitHub".
6. Search for the repo you want to connect and click 'Connect'.
7. Scroll down and click "Deploy Branch" in the Manual deploy section.
8. Your app has been deployed! You can find it in "Open app".
