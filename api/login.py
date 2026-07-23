import json


def handler(request):
    body = json.loads(request.body)

    username = body.get("username")
    password = body.get("password")

    correct_username = "admin"
    correct_password = "password"

    if username == correct_username and password == correct_password:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True
            })
        }

    return {
        "statusCode": 401,
        "body": json.dumps({
            "success": False,
            "message": "Invalid username or password"
        })
    }
