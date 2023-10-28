from django.db import models


class UpperCaseCharField(models.CharField):
    def to_python(self, value):
        val = super().to_python(value)
        if isinstance(value, str):
            return val.upper()
        return val

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)
