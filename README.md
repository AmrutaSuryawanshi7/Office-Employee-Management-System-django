# Office Employee Management System

> ### Show All Commands
> django-admin

> ### To Run A Project 
> 1. Create a project
> 2. `cd` till manage.py file on VS terminal `(Ex. "cd office_emp_proj")`
> 3. Run `python manage.py runserver`
> 4. Open http://127.0.0.1:8000/ in browser

> ### Steps To Develop A Django Project
>> ### Step 1: Create a project
>> `django-admin startproject office_emp_proj`
> 
>> ### Step2: Create app (emp_app) to handle all employee's
>> 1. `python manage.py startapp emp_app` 
>> 2. Add app(emp_app) in "office_emp_proj\settings.py" > INSTALLED_APPS ('emp_app',)
>> 3. Include app url in "office_emp_proj\urls.py"
>> 
>> ![alt text](screenshots/proj_urls.png "Description goes here")
>> 5. Create urls.py file for app(emp_app), then import views & add function/view
>> 
>> ![alt text](screenshots/emp_app_urls.png "Description goes here")
>> 6. Create function/view (index) in "emp_app\views.py" (So that function can route)
>> 7. Create template folder in app & add your templates (Ex. index.html)
>> 8. Then render the template in function/view (file: "emp_app\views.py")
>> 
>> ![alt text](screenshots/emp_app_urls.png "Description goes here")
>> 9. Run the project
>>> **Summary:** 
>>> 1. When Django server is started, `manage.py` file searches for `settings.py` file which contains information of all the applications, databases and path to the main urls config.
>>> 2. Django first determines and loads the requested `module/app urls` then check each URL pattern in apps `urls.py` file.
>>> 3. Django then imports and calls the given `view` from `views.py` file.
>>> 4. In case none of the URLs match the requested URL, Django invokes an error-handling view.
>>> 5. If URL maps, a view is called that interacts with `model and template`, it renders a `template`.
>>> 6. Django sends a `template` as a response to the user.
>>> 
>>> ![alt text](screenshots/MVT_architecture.png "Description goes here")
>
>> ### Step3: Create model
>> 1. Create tables in `models.py` file
>> 
>> ![alt text](screenshots/emp_app_models.png "Description goes here")
>> 2. Create migration file inside the migration folder:
>> <br>`python manage.py makemigrations`
>> 3. After creating a migration, to reflect changes in the database permanently execute migrate command:
>> <br>`python manage.py migrate`
>>
>>> **_Other commands for migrations:_**
>>> ![alt text](screenshots/other_migrate_commands.png "Description goes here")
>> 