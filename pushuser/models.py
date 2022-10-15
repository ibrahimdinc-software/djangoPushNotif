from django.db import models

from ownwebpush import send_user_notification

# Create your models here.


class PushMessageModel(models.Model):
    addTime = models.DateTimeField(verbose_name="Add Time", auto_created=True)
    detail = models.CharField(verbose_name="Detail (Only Admin)", max_length=130, default="Varsayılan AÇıklama", blank=True, null=True)
    title = models.CharField(verbose_name="Title", max_length=130)
    description = models.TextField(verbose_name="Description", max_length=300)
    icon = models.CharField(verbose_name="Icon", blank=True, null=True, max_length=500)
    url = models.CharField(verbose_name="URL", max_length=255, blank=True,null=True)

    def __str__(self) -> str:
        return self.detail

    def getPayload(self):
        return {
            'head': self.title, 
            'body': self.description,
            'icon': self.icon,
            'url': self.url
        }

class PushUserModel(models.Model):
    identifier = models.CharField(verbose_name="Identifier", unique=True, max_length=255)

    def __str__(self) -> str:
        return self.identifier


class PushGroupModel(models.Model):
    name = models.CharField(verbose_name="Group Name", max_length=255)

    def __str__(self) -> str:
        return self.name



class UserGroupModel(models.Model):
    pushUser = models.ForeignKey(verbose_name="Push User", to=PushUserModel, on_delete=models.CASCADE)
    pushGroup = models.ForeignKey(verbose_name="Push Group", to=PushGroupModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pushGroup) + ' / ' + str(self.pushUser)


class PushToGroupModel(models.Model):
    sendDate = models.DateTimeField(verbose_name="Add Date", blank=True, null=True)
    pushGroup = models.ForeignKey(verbose_name="Push Group", to=PushGroupModel, on_delete=models.CASCADE)
    pushMessage = models.ForeignKey(verbose_name="Push Message", to=PushMessageModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pushGroup) + " grubuna gönderilen " + self.pushMessage.detail

    def sendNotif(self):
        users = [i.pushUser for i in self.pushGroup.usergroupmodel_set.all()]
        for user in users:
            payload = self.pushMessage.getPayload()
            send_user_notification(user=user, payload=payload, ttl=1000)
