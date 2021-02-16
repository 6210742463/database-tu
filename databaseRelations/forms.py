from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    doSomething = forms.ModelMultipleChoiceField(
            label = 'ทำอะไรบ้าง',
            queryset = DoSomething.objects.all(),
            widget = forms.CheckboxSelectMultiple,
            required = True) 
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'title' : 'คำนำหน้า',
            'firstName' : 'ชื่อจริง',
            'lastName' : 'นามสกุล',
            'email' : 'อีเมล',
            'tel_1' : 'เบอร์โทรศัพท์ 1',
            'tel_2' : 'เบอร์โทรศัพท์ 2',
            'tel_3' : 'เบอร์โทรศัพท์ 3',
            'county' : 'จังหวัด',
            'addess' : 'ที่อยู่',
            'faculty' : 'หน่วยงาน/คณะ',
            'status' : 'สถานะภาพ',
            'doSomething' : 'ทำอะไรบ้าง',
            'birthday' : 'วันเกิด',
            'idAddess' : 'เลขที่ไปรษณีย์',
        }
        

