# six_hats

Step to use project.
Intall django & python above 3
Make virtualenv
Take clone
url for clone: git clone https://github.com/dkmca/six_hats.git

Use data base postgress or any data base need to change in settings as per the data base selection.

Enpoints for add/edit/delete/list

1. url:  http://127.0.0.1:8000/users/add_user/
2. Params: 
Method: POST
name:Dharmendra k
email:pa@malinator.com
address:address one1

response:
{
    "status": 200,
    "message": "User added successfully",
    "data": {
        "user_id": 10,
        "name": "Dharmendra k",
        "email": "pa@malinator.com"
    }
}

2. edit user: url:  http://127.0.0.1:8000/users/edit_user/
params: 
Method: POST
user_id:1
name:Dharmenra
email:paald20@yopmail.com
address:a123

response:
{
    "status": 200,
    "message": "User updated successfully",
    "data": {
        "user_id": 1,
        "name": "Dharmenra",
        "email": "paald20@yopmail.com"
    }
}

3. delete user:
URL:  http://127.0.0.1:8000/users/delete_user/
param: 
user_id:1
Method: DELETE
response: 
{
    "status": 200,
    "message": "User deleted successfully"
}

List user: url:  http://127.0.0.1:8000/users/list_user/
Method: GET
response:
{
    "count": 7,
    "next": null,
    "previous": "http://127.0.0.1:8000/users/list_user/",
    "results": [
        {
            "id": 9,
            "name": "Dharmendra k",
            "email": "paa@malinator.com",
            "address": "address one1"
        },
        {
            "id": 10,
            "name": "Dharmendra k",
            "email": "pa@malinator.com",
            "address": "address one1"
        }
    ]
}
