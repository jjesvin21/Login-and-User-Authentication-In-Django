# Login-and-User-Authentication-In-Django
This is an Example for how to do User Login and authentication using simpleJWT and to do custom  user permissions.

<b> ROUTES </b>

1-> api/token/

POST | username,password | refresh token, acess token [ for login ]

2-> api/token/refresh/

POST | refresh tocken | refresh token, acess token

3 -> api/newuser/

POST | username,password,permission,first_name,last_name | [to create a new user]

4->api/hello/

GET -> returns hello if logined user have the permission to acess hello

