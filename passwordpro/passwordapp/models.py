from django.db import models
from passlib.hash import pbkdf2_sha256

class Register(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)

    def verify_password(self,raw_password):
    	return pbkdf2_sha256.verify(raw_password,self.password)