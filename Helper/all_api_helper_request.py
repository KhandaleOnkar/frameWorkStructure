import requests

class Wrapper:
    '''this class resp to define all the requests http method
   get_api : arg:api
           : return resp

   post_api : arg:api,payload(json)
            : return resp

    put_api : arg:api,payload(json)
            : return resp

    patch_api : arg:api,payload(json)
            : return resp
    del_api : arg:api
            : return resp
   '''

    def get_api(self,api):
        return requests.get(api)

    def post_api(self,api,payload):
        return requests.post(api,payload)

    def put_api(self,api,payload):
        return requests.put(api,payload)

    def patch_api(self,api,payload):
        return requests.patch(api,payload)

    def delete_api(self,api):
        return requests.delete(api)