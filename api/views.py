from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import EmailSerializer
from datetime import datetime


class SendEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            body = serializer.validated_data['body']
            visitor_email = serializer.validated_data['email']
            website_url = request.headers.get(
                'Origin') or request.headers.get('Referer', 'Unknown')

            developer_email = request.user.email
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            email_subject = f"New sunmission from: {website_url}"
            email_body = f"""
You received a new submission from your form!

Website: {website_url}
Submitted at: {timestamp}
-------------------------------------------------------------

Visitor Email: {visitor_email}
Subject: {subject}
-------------------------------------------------------------

Message:
{body}

-------------------------------------------------------------
This is an automated message from your form email service.
"""

            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [developer_email],
                    fail_silently=False,
                )
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
