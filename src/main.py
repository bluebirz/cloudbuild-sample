import functions_framework
import flask
from pprint import pprint


@functions_framework.http
# def sum_list(req: flask.Request):
#     """
#     Expect JSON payload when action is 'POST'
#     Example:
#     ```json
#         {
#             "data": [1,2,3,10,20,30]
#         }
#     ```
#     """
#     if req.method == "POST":
#         data = req.get_json()["data"]
#         return f"Sum of {data} equals {sum(data)}"
#     else:
#         return ""
def hello_http(req):
    return "Hello World"
