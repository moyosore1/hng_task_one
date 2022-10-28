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
    return Response(context)



