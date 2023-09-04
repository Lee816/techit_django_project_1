from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class MyManager(BaseUserManager):
    # 일반 회원
    def create_user(self, phone, name, password=None):
        if not phone:
            raise ValueError('휴대폰번호를 입력해 주세요')
        if not name:
            raise ValueError('이름을 입력해 주세요')

        user = self.model(
            phone = phone,
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # 관리자 생성
    def create_superuser(self, phone, name, password):
        user = self.create_user(
            phone=phone,
            name=name,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    # 생성 클래스
    object = MyManager()
    
    # 사용할 필드
    phone = models.CharField(verbose_name='휴대폰번호',max_length=15,unique=True)
    name = models.CharField(verbose_name='이름',max_length=10)
    
    # 생성 날짜 필드
    created = models.DateTimeField(auto_now_add=True)
    
    # 권한 필드
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_admin
    
    # 로그인에 사용할 필드
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']
    
