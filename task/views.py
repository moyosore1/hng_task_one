from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def endpoint_task(request):
    context = {
        "slackUsername": "Moyo",
        "backend": True,
        "age": 21,
        "bio": "A backend engineer!"
    }
    response =  Response(context)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response



