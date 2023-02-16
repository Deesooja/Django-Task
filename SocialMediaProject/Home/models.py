from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from Home.manager import CustomUserManager
# from cloudinary.models import CloudinaryField
from cloudinary.models import CloudinaryField

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  user_name = models.CharField(max_length=200,unique=True)
  mobile=models.CharField(max_length=12,unique=True)
  term_conditions = models.BooleanField()
  profile_image=CloudinaryField(null=True, blank=True)
  address=models.CharField(max_length=200,null=True)
  pin_code=models.CharField(max_length=200,null=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff=models.BooleanField(default=False)
  is_superuser=models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','mobile','user_name','term_conditions',]

  def __str__(self):
      return self.email
#   def __str__(self):
#         return f"({self.email})"

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class Friend(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="friends")
    friend=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FriendRequest(models.Model):
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="send_by")
    resiver=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    action=models.BooleanField(default=False)
    accept=models.BooleanField(default=False)
    atempt=models.IntegerField(default=1)
    blocked=models.BooleanField(default=False)
    cancel_by_sender=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image=CloudinaryField('image')
    text=models.CharField(max_length=500)
    for_all=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    action=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)