# songlyrics-finder

A Python GUI Program To Find Lyrics Of A Song

## Python Modules Required
* tkinter -: For user interface
* lyricsgenius -: For extracting song lyrics from [genius](https://genius.com/)
* pillow -: For using jpeg image in background

## How To Install These Modules?
Open **powershell** or **command prompt(cmd)** in your computer.
We only need to install *lyricsgenius* and *pillow* module. Tkinter is a built-in module in python.

Type in **powershell** or **command prompt(cmd)**:
```bash
 * pip install lyricsgenius
```
```bash
 * pip install pillow
```

## Creating an account on [genius](https://genius.com/)
*We are required to create an account on genius in order to use their api key for extarcting song lyrics*

### Steps:
* Go to [Sign-Up/Log-In Page](https://genius.com/signup_or_login). If you already have an account, log in to your account else sign up to create an account. After this you will be re-routed back to home page. Scroll down to footer of this page and click on *Developers*.
* Once you are on "Developers" page click on "*CREATE AN API CLIENT*" (Google Chrome). You will be prompted to a page like this:
![rsz_imp](https://user-images.githubusercontent.com/60878349/110454113-e191d480-80ec-11eb-83f5-f9952fa69011.png)
* You just need to fill *APP NAME* and *APP WEBSITE URL* column. Write the name of your app in *APP NAME* and you can put your github address in *APP WEBSITE URL*. Click on *Save* and you will be taken to credentials page.
* On credentials page click on **GENERATE ACCESS TOKEN**. Copy this generated token and paste it in your file where the code is like this-
genius = lg.Genius('<Put your generated token here>', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
                    
                        
