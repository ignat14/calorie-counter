from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db.models.signals import post_save 
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
	"""auth/login-related fields"""
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	PERMISSIONS = (
		('USER', 'USER'),
		('MANAGER', 'MANAGER'),
		('ADMIN', 'ADMIN'),
	)
	username = models.CharField(max_length=250, null=True, blank=True)
	email = models.EmailField(unique=True)
	permission = models.CharField(max_length=30, choices=PERMISSIONS)

	objects = UserManager()


class Profile(models.Model):
	"""non-auth-related/cosmetic fields"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	expected_calories_per_day = models.IntegerField(null=True, blank=True)
	full_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
	"""receiver to add a Profile for newly created users"""
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
	"""receiver to save the Profile for newly created users"""
	instance.profile.save()
