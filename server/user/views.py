from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .serializers import UserCreateSerializer, UserLoginSerializer
from .models import User

# IsAuthenticated 설정이 되어있기 때문에 인증이 필요없는 api이므로 permission설정을 따로 부여
@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        serializers = UserCreateSerializer(data=request.data)
        if not serializers.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_400_BAD_REQUEST)
        
        # email 중복 검사
        if User.objects.filter(email=serializers.validated_data['email']).first() is None:
            serializers.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializers = UserLoginSerializer(data=request.data)

        if not serializers.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializers.validated_data['email'] == 'None':
            return Response({"message": "fail"}, status=status.HTTP_409_CONFLICT)

        response = {
            'message' : 'ok',
            'token': serializers.data['token']
        }

        return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def validateJWT(request):
    if request.method == 'GET':
        try:
            token = request.META['HTTP_AUTHORIZATION']
            data = {'token' : token.split()[1]}
            user = VerifyJSONWebTokenSerializer().validate(data)
        except KeyError as e:
            return Response({"message" : "fail"}, status=status.HTTP_409_CONFLICT)
        return Response({"message": "ok"}, status=status.HTTP_200_OK)
        # token = request.META['HTTP_AUTHORIZATION']
        # data = {'token' : token.split()[1]}
        # validData = VerifyJSONWebTokenSerializer().validate(data)
        # print(validData)