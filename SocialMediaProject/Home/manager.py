from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
  def create_user(self, email, name, user_name, mobile ,term_conditions, profile_image=None ,address=None,pin_code=None, password=None, password2=None,**kwargs):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          user_name=user_name,
          mobile=mobile,
          term_conditions=term_conditions,
          profile_image=profile_image,
          address=address,
          pin_code=pin_code,
          
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, user_name, mobile ,term_conditions, profile_image=None ,address=None, pin_code=None, password=None,**kwargs):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email=self.normalize_email(email),
          password=password,
          name=name,
          user_name=user_name,
          mobile=mobile,
          term_conditions=term_conditions,
          profile_image=profile_image,
          address=address,
          pin_code=pin_code,
        #   is_staff=is_staff,

      )
      user.is_superuser = True
    #   user.is_staff=True
      user.is_admin = True
      user.save(using=self._db)
      return user