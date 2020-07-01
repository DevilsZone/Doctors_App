from django.shortcuts import render
from django.views import View
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .background_task import do_work
from .models import AsyncResults
import json
# Create your views here.


class ReportView(views.APIView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @staticmethod
    def post(request, *args, **kwargs):
        file = request.FILES["file_csv"]
        file_data = file.read().decode("utf-8")
        lines = file_data.split("\n")
        task = do_work.delay(lines)
        response = {"task_id": task}
        return Response(response, status=status.HTTP_202_ACCEPTED)


class AsyncResultView(views.APIView):

    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get("task_id", None)
        print(task_id)
        try:
            async_result = AsyncResults.objects.get(task_id=task_id)
            load_body = json.loads(async_result.result)
            status_code = load_body.get("status_code", None)
            if status_code == 500:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            elif status_code == 200:
                return Response(status=status.HTTP_200_OK, data=load_body)
            else:
                return Response(status=status.HTTP_410_GONE)
        except Exception as e:
            print(e.args)
            return Response(status=status.HTTP_202_ACCEPTED)
