# django_Sort_SeeCoursesdetails_Auth

Functionality to sort numbers is implemented 
1. visit https://laxmipolam.cf
2. Click on "Sort Numbers" from left navigation
3. Give some input in text are in th comma separated or space separated form. This is a required field.
4. Select ascending or descending as other input. Default is Ascending order.
5 Click on 'Submit'. It is a POST request. You will see output in a panel.

Functionality to change summary and Registration Date is implemented (Database connected)
1. Click on login from left navigation
2. Give credentials as Username : "instructor" ; password : "ccassignment"
3. Click on My Courses. 'My courses' is based on person logged in.
4. Next select "CC" from the registered Lectures.
5. Click on any UUID of this form 'Id: 513ec55a-b71d-4788-b68c-262db77bda4c". 
6. A form will be dispalyed on with previously saved data of that lecture (What user clicks as input) through GET. It has two fields registration and summary.
7. Summary is not a required field. Date is a required field and Even past data can be selected. Any instructor can change summary,date of all the lectures. This is saved to data base and will be reflected when you see this lecture summary,date next time.
8. You will see a registration closing date. Which is 10 days after the  date as ouput.