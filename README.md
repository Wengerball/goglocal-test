# goglocal-test

Custom User Model with API functionalities



## POST API for users to login

 Request - curl -X POST http://127.0.0.1:8008/api/details/login/ -d "username=qwerty&password=Shash@123" 

 Response - {"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMzY4NTExNywiaWF0IjoxNzAzNTk4NzE3LCJqdGkiOiIyNjQwYjk0ZDM4Yzc0MTQ2YTJhMTMzZDk4NjY2MjNkNiIsInVzZXJfaWQiOjN9.p4s6_S3uXOWdq1E--JhM7GKIFQWbzyjBqUCCRvz2XDk","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NDYyNzE3LCJpYXQiOjE3MDM1OTg3MTcsImp0aSI6ImQ2ZWNhMjQ0MmRhMDQ0ZTBhODRhY2Y4YTY5YjFmNWI4IiwidXNlcl9pZCI6M30.na1qBgjX_ktQDV8fx9cMOhBW40sP1YC6lPV3jP0VTEE"}%                                                                                                     

## GET API for users to retrieve information based on JWT Token
 
Request - curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NDYyNzE3LCJpYXQiOjE3MDM1OTg3MTcsImp0aSI6ImQ2ZWNhMjQ0MmRhMDQ0ZTBhODRhY2Y4YTY5YjFmNWI4IiwidXNlcl9pZCI6M30.na1qBgjX_ktQDV8fx9cMOhBW40sP1YC6lPV3jP0VTEE" http://localhost:8008/api/details/user/

Response - {"username":"qwerty","email":"q@gmail.com","first_name":"Qwe","last_name":"ty","pan_card_number":"QWERTUI1"}
