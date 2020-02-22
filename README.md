# Captcha-Attack-RadCaptcha

Plain captcha cracking using object detection. The testing scripts only works for a demo website that generates pages but the model can be used and trained to do targetted attack
on any website.

## Requirements:
virtualenv (sudo pip install virtualenv)

python2

## Run:

### Step 1: Setup and Activate virtual environment
source env/bin/activate

Install tensorflow: sudo pip install tensorflow

### Step 2: Run the script
python2 attack.py

### Step3: Configure RadCaptcha
The browser will automatically open so configure the complexity of captcha manually

### Step4: Autofill captcha
Press any key on the terminal and the captcha will appear in the text box on the website. This can be repeated continuously.

### Step 5: Exit
Press Ctrl-C (or send a keyboard interrupt) to exit the attack script.
