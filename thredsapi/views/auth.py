from rest_framework.decorators import api_view
from rest_framework.response import Response
from thredsapi.models.threds_user import ThredsUser


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    threds_user = ThredsUser.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if threds_user is not None:
        data = {
            'id': threds_user.id,
            'uid': threds_user.uid,
            'first_name': threds_user.first_name,
            'last_name': threds_user.last_name,
            'username': threds_user.username,
            'address': threds_user.address,
            'image_url': threds_user.image_url
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the rareapi_user table
    threds_user = ThredsUser.objects.create(
        uid=request.data['uid'],
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        address = request.data["address"],
        image_url = request.data["imageUrl"],
        username = request.data["username"],
    )

    # Return the user info to the client
    data = {
            'id': threds_user.id,
            'uid': threds_user.uid,
            'first_name': threds_user.first_name,
            'last_name': threds_user.last_name,
            'address': threds_user.address,
            'image_url': threds_user.image_url,
            'username': threds_user.username
    }
    return Response(data)
