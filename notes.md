


The __init__.py file makes Python treat directories containing it as modules.

1. The models are the data descriptor of our application, in many cases related to the database model. How each model is defined will heavily depend on the library you use to connect to your database.

2. The routes are the URIs to our application, where we define our resources and actions.

3. The schemas are the definitions for inputs and outputs of our API, what parameters are allowed, what information we will output. They correlate to our resources, but they are not necessarily the same as our models.

4. The services are modules that define application logic or interact with other services or the db layer. Routes should be as simple as possible and delegate all logic to the services.


https://auth0.com/blog/best-practices-for-flask-api-development/

https://levelup.gitconnected.com/structuring-a-large-production-flask-application-7a0066a65447

https://medium.com/@arslanaut/minimal-flask-application-using-mvc-design-pattern-842845cef703