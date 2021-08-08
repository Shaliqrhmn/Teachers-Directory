from import_export import resources
from login .models import Teacher

class fileResources(resources.ModelResource):
    class meta:
        model = Teacher