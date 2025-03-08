from django.contrib.auth.models import BaseUserManager


class userManager(BaseUserManager):
    
    def create_user(self, email,username=None, password=None):
        if not email:
            raise ValueError('User must have an email')
        user = self.create(username=username,email=email)
        user.set_password(password)
        user.save()
        return user 