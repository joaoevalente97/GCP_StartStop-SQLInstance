# This file uses the Cloud SQL API to turn on a Cloud SQL instance.
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)
project = '<Nome_Projeto_GCP>'  # Nome do Projeto.


def hello_world(self, request):

   instance = '<Nome_Instancia>'  # Nome da Instancia SQL.
   request = service.instances().get(project=project, instance=instance)
   response = request.execute()
   j = response["settings"]
   settingsVersion = int(j["settingsVersion"])

   dbinstancebody = {
      "settings": {
         "settingsVersion": settingsVersion,
         "tier": "db-n1-standard-2", # Tier = tipo de maquina.
         "databaseFlags":
         [
            {
               "name": "default_time_zone",
               "value": "-03:00"
            },
            {
               "name": "event_scheduler",
               "value": "on"
            },
            {
               "name": "innodb_file_per_table",
               "value": "on"
            },
            {
               "name": "max_allowed_packet",
               "value": "1073741824"
            },
            {
               "name": "sql-mode",
               "value": "TRADITIONAL"
            },
            {
               "name": "wait_timeout",
               "value": "1800"
            },
            {
               "name": "lower_case_table_names",
               "value": "1"
            }
         ],
         "activationPolicy": "Always" # Always = liga, Never = desliga.
      }
   }

   request = service.instances().update(
      project=project,
      instance=instance,
      body=dbinstancebody)
   response = request.execute()