from celery import shared_task
from .process_zipcode import download_data
import json
from process_model import create_model

# this decorator is all that's needed to tell celery this is a worker task
@shared_task(bind=True)
def do_work(self, list_of_work, radius=5):
    task_id = self.request.id
    print("Task ID - "+str(task_id))
    try:
        download_url = []
        for work_item in list_of_work:
            print("Extracting ZipCode - {}; and its type is - {}".format(work_item, type(work_item)))
            temp = download_data(work_item, radius)
            if temp:
                download_url.append()
            else:
                pass
        filename = f"Result.csv"
        result = {"status_code": 200,
                  "location": download_url,
                  "filename": filename}
        json_result = json.dumps(result)
        create_model(task_id=task_id, result=json_result)
    except Exception as e:
        print(e.args)
        result = {"status_code": 500,
                  "error_message": str(e.args)}
        json_result = json.dumps(result)
        create_model(task_id=task_id, result=json_result)
    return task_id
