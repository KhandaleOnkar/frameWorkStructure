
class StatusCode:
    CONTINUE=100
    SWITCH=101
    OK=200
    CREATED=201
    ACCEPTED=202
    NOCONTENT=204
    BADREQUEST=400
    UNAUTHORIZESD=401
    NOTFOUND=404
    id_in_respo=[i for i in range(7,13)]

get_apis_dict={"get_users":"https://reqres.in/api/users?page=2",
           "get_single_user":"https://reqres.in/api/users/2",
           "get_single_user_not_found":"https://reqres.in/api/users/23",
           "list_resources":"https://reqres.in/api/unknown",
           "single_resource":"https://reqres.in/api/unknown/2",
           "resource_not_found":"https://reqres.in/api/unknown/23",
           "delay_api":"https://reqres.in/api/users?delay=3"
}

post_apis_dict={
    "post_create":"https://reqres.in/api/users"
}