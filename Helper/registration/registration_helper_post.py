try:
    def get_api_information(self, api, expected_status=None, expected_resp=None, expected_time=None):
        resp = super().get_api(api)
        if expected_status:
            if resp.status_code == StatusCode.OK:
                return True
            else:
                return False
        elif expected_resp:
            data = json.loads(resp.content)
            return data
        elif expected_time:
            return resp.elapsed.total_seconds()
except Exception as e:
    print(str(e))