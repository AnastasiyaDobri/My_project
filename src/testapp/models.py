from django.db import models
import datetime

class Parsing(models.Model):
    ip=models.TextField(
        verbose_name="ip",
        null=True,
        blank=True
    )
    date=models.TextField(
        verbose_name="time",
        null=True,
        blank=True
    )

    browser=models.TextField(
        verbose_name="browser",
        null=True,
        blank=True
    ) 

    def __str__(self):
        return self.ip


def creating():
    tf=open('apache_logs.txt','r')
    k=0
    users = dict(u_ip=0, u_date=0, u_browser=0)
    total=dict()
    tf.seek(0)   
    lin=tf.readlines()
    z=len(lin)
    for k in range(0,z): 
       a=lin[k]
       l1=a.find('[')+1
       l2=a.find(':')
       tn=(a[l1:l2])
       users['u_date']=datetime.datetime.strptime(tn,"%d/%B/%Y")
       users['u_ip']=a[0:11]
       a2=a[::-1]
       n1='Mozilla'
       n2='Safari'
       n3='Firefox'
       n4='Chrome'
       if a2.find(n4[::-1])>0:
          users['u_browser']=n4
       if a2.find(n3[::-1])>0:
          users['u_browser']=n3
       if a2.find(n2[::-1])>0:
          users['u_browser']=n2
       if a2.find(n1[::-1])>0:
          users['u_browser']=n1
       total[k]=users
       k=k+1
    return total

total=creating()
for k in range (0,100000):
    a=str(total[k]['u_ip'])
    b=str(total[k]['u_date'])
    c=str(total[k]['u_browser'])
    parsing=Parsing(ip=a,date=b,browser=c)
    parsing.save()



