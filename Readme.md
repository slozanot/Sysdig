#Testing https://app.sysdigcloud.com/

#Installation
Just create a new folder with this project. Assert that you have the correct chromedriver for your chrome version
By default, this project contains chromedriver for chrome v92.
#How to run
Just open this project in any Python valid IDE and run main method.

#How works
This project open a new chrome browser window, and load app.sysdigcloud.com page.
After page loaded, tries to enter with invalid credentials, and wait for expected error message.
Also, checks that link to external services are correctly added by checking href attribute.
As a typical functional test, everything is agrouped in a same main function. All tests are like one functional test (As a feature in BDD)
#Expected result
When tests finishes, an output folder must be created. There, you can fast check if there is any error inside output/error folder.
If no screenshot exists, it means test work fine.
To find all correct screenshots, go to output/screenshot folder


#Things to improve
I would want to make a better project structure, with differents files for locators and data, but not enought time to do it.
Also, include other libraries as Behave to execute different scenarios would be fantastic.
As I dont have any other data or requirements to test, I can't test much more this page.
I use libraries as Behave and Toolium, but I've never used just selenium with python like this. For that, probably there are a lot of thins to improve here